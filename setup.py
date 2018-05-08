"""Setup script """
from setuptools import setup, find_packages


with open("requirements.txt") as f:
    REQUIREMENTS = f.read().split("\n")


with open("README.md", 'r') as f:
    DESCRIPTION = f.read()


setup(
    name='Dockerize-Platypus',
    version='0.01',
    description='Build a docker image using Report_HTML_DB results from EGene2',
    long_description=DESCRIPTION,
    license='GNU GPL',
    include_package_data=True,
    data_files=[
        ('share/dockerize_platypus/example', [ 'example/%s' % file for file in os.listdir('example') ])],
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    scripts=[
        'scripts/dockerize_platypus.py'],
    author='Wendel Hime Lino Castro',
    author_email='wendelhime@hotmail.com',
    url='https://github.com/WendelHime/dockerize_platypus.git',
    project_urls={
        "Travis CI": "https://travis-ci.org/WendelHime/dockerize_platypus",
        "Coveralls": "https://coveralls.io/github/WendelHime/dockerize_platypus?branch=master",
        "Documentation": "http://dockerize-platypus.readthedocs.io/en/latest/?badge=latest",
        "Source": "https://github.com/WendelHime/dockerize_platypus"
        },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools'
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
        ]
)
