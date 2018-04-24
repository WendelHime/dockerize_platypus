#/usr/bin/python3
"""
Dockerize report_html_db.pl result.
Creates a docker image, build it, and push to docker cloud
"""
import sys
import argparse
# import docker


def create_image(organism, filepath, database):
    """Write docker image
    Args:
        organism: organism name
        filepath: output filepath from report_html_db
        database: database filepath
    Returns:
        Dockerfile content
    """
    image = "FROM wendelhime/platypus:latest\n"
    image += "RUN apt-get update && apt-get install postgresql-9.5\n"
    image += "COPY {}/{} /root/{}.sql\n".format(database, organism)
    image += "RUN mkdir /root/{}\n".format(organism)
    image += "COPY {}/{}-Services /root/{}\n".format(filepath, organism, organism)
    image += "COPY {}/{}-Website /root/{}\n".format(filepath, organism, organism)
    # image += "ENTRYPOINT"
    return image


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="""dockerize_platypus.py - dockerize report_html_db.pl result""",
            epilog='Creates a docker image based on report_html_db.pl, build it and push into docker cloud')
    parser.add_argument('-v', '--version', action='version', version='%(progr)s 0.1')
    parser.add_argument('organism', type=str, help='Organism name for docker tag')
    parser.add_argument('filepath', type=str, help='Output filepath from report_html_db.pl')
    parser.add_argument('database', type=str, help='Dump file from database. Use this command: pg_dump dbname > outfile.sql')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    content = create_image(args.organism, args.filepath, args.database)
    with open('Dockerfile', 'w') as dockerfile:
        dockerfile.write(content)
    
    # client = docker.from_env()
