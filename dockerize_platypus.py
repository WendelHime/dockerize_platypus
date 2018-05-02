#/usr/bin/python3
"""
Dockerize report_html_db.pl result.
Creates a docker image, build it, and push to docker cloud
"""
import os
import sys
import argparse
import subprocess
import docker
import logging


def create_image(organism, filepath, database, dbname, init_filepath):
    """Write docker image
    Args:
        organism: organism name
        filepath: output filepath from report_html_db
        database: database filepath
        dbname: db name
        init_filepath: init filepath sql
    Returns:
        Dockerfile content
    """
    image = "FROM wendelhime/platypus:latest\n"
    image += "RUN apt-get update && apt-get install -y postgresql\n"
    image += "RUN perl -pe 's/local\s*\w+\s*\w+\s*peer//g' /etc/postgresql/9.6/main/pg_hba.conf > pg_hba.conf\n"
    image += "RUN echo 'local\\tall\\t\\tall\\t\\t\\t\\t\\ttrust\\nhost\\tall\\t\\t\\tall\\t0.0.0.0/0\\t\\tmd5\\n' >> pg_hba.conf\n"
    image += "RUN cp pg_hba.conf /etc/postgresql/9.6/main\n"
    image += "COPY {} /root/init.sql\n".format(init_filepath)
    image += "COPY {} /root/{}.sql\n".format(database, organism)
    image += "RUN mkdir /root/{}\n".format(organism)
    image += "COPY {}/{}-Services /{}-Services\n".format(
            filepath,
            organism,
            organism)
    image += "COPY {}/{}-Website /{}-Website\n".format(
            filepath,
            organism,
            organism)
    entrypoint = generate_docker_entrypoint(dbname, organism)
    image += "COPY {} /usr/local/bin/{}\n".format(entrypoint, entrypoint)
    image += "RUN chmod +x /usr/local/bin/{}\n".format(entrypoint)
    image += "ENTRYPOINT [\"{}\"]\n".format(entrypoint)
    image += "CMD [\"-h\"]"
    return image


def generate_init(dbuser, dbpass, dbname):
    """Generate init SQL

    """
    content = "CREATE ROLE %s LOGIN SUPERUSER INHERIT CREATEDB;\n" % dbuser
    content += "ALTER USER %s WITH PASSWORD '%s';\n" % (dbuser, dbpass)
    content += "CREATE DATABASE %s;\n" % dbname
    content += "GRANT CONNECT ON DATABASE %s TO %s;" % (dbname, dbuser)
    return content


def dump_db(dbuser, dbname, filepath):
    """Generate postgrsql dump sql file
    Args:
        dbuser: User db
        dbname: DB name
        filepath: output filepath
    Returns:
        a string with filepath if exists
    """
    ps = subprocess.Popen(
            [
                'pg_dump',
                '-U',
                dbuser,
                '-Fp',
                dbname],
            stdout=subprocess.PIPE)
    std1, stderr = ps.communicate()
    with open(filepath, 'wb') as fh:
        fh.write(std1)
    if os.path.exists(filepath):
        return filepath
    
    return ''


def generate_docker_entrypoint(dbname, organism):
    """Generate docker entrypoint script
    Args:
        dbname: Database name
        organism: organism name
    Returns:
        filepath script
    """
    script = "#!/bin/bash\n"
    script += "/etc/init.d/postgresql start\n"
    script += "psql template1 -U postgres < /root/init.sql\n"
    script += "psql {} -U {} < /root/{}.sql\n".format(
            dbname,
            'chadouser',
            organism)
    script += "auxiliar.py $@\n"

    filepath = 'docker-entrypoint.sh'
    with open(filepath, 'w') as fh:
        fh.write(script)

    if os.path.exists(filepath):
        return filepath
    
    return ''


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="""dockerize_platypus.py - dockerize report_html_db.pl result""",
            epilog='Creates a docker image based on report_html_db.pl, build it and push into docker cloud')
    parser.add_argument('-v', '--version', action='version', version='%(progr)s 0.1')
    parser.add_argument('organism', type=str, help='Organism name for docker tag')
    parser.add_argument('filepath', type=str, help='Output filepath from report_html_db.pl')
    parser.add_argument('dbuser', type=str, help='DB username')
    parser.add_argument('dbname', type=str, help='DB name')
    parser.add_argument('dbpass', type=str, help='DB password to be used on docker')
    parser.add_argument('docker_user', type=str, help='Docker username')
    parser.add_argument('--log', type=str, help='output filepath log')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    logging.basicConfig(
        filename=args.log,
        format='%(asctime)s : %(levelname)s : %(message)s',
        level=logging.INFO)

    logging.info('Dumping %s database' % args.dbname)
    sql_dump = dump_db(
            args.dbuser,
            args.dbname,
            '{}.sql'.format(args.organism))

    logging.info('Creating basic SQL file')
    init = generate_init(args.dbuser, args.dbpass, args.dbname)
    with open('init.sql', 'w') as init_file:
        init_file.write(init)

    logging.info('Creating Dockerfile')
    content = create_image(
            args.organism,
            args.filepath,
            sql_dump,
            args.dbname,
            'init.sql')
    with open('Dockerfile', 'w') as dockerfile:
        dockerfile.write(content)
    
    client = docker.from_env()
    logging.info('Building image...')
    client.images.build(
            tag='{}/{}'.format(
                args.docker_user,
                args.organism.lower()),
            path='.')
    logging.info('Removing generated files...')
    os.remove(sql_dump)
    os.remove(init)
    os.remove(Dockerfile)
    logging.info('Finished!')
