#/usr/bin/python3
"""
Dockerize report_html_db.pl result.
Creates a docker image, build it, and push to docker cloud
"""
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            descriptions="""dockerize_platypus.py - dockerize report_html_db.pl result""",
            epilog='Creates a docker image based on report_html_db.pl, build it and push into docker cloud')
    parser.add_argument('-v', '--version', action='version', version='%(progr)s 0.1')
    parser.add_argument('organism', type=str, help='Organism name for docker tag')
    parser.add_argument('output_filepath', type=str, help='Output filepath from report_html_db.pl')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
