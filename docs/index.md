# dockerize_platypus
[![Build Status](https://travis-ci.org/WendelHime/dockerize_platypus.svg?branch=master)](https://travis-ci.org/WendelHime/dockerize_platypus) [![Coverage Status](https://coveralls.io/repos/github/WendelHime/dockerize_platypus/badge.svg?branch=master)](https://coveralls.io/github/WendelHime/dockerize_platypus?branch=master) [![Documentation Status](https://readthedocs.org/projects/dockerize-platypus/badge/?version=latest)](http://dockerize-platypus.readthedocs.io/en/latest/?badge=latest)

Dockerize `report_html_db.pl` result and upload for docker cloud

## Installing dependencies
Wendellor's package was made using Python3. So you will need to execute some commands:

```bash
sudo apt-get install git \
    python-dev\
    python-pip\
    python3-dev\
    python3-pip
```
Here you're installing:

| Package | Description |
| :-- | :-- |
| git | Version control system for tracking changes in computer files and coordinating work on those files among multiple people. In this case, for manage our repository |
| python-dev | Header files, a static library and development tools for building Python modules, extending the Python 2.7 interpreter or embedding Python 2.7 in applications.  |
| python-pip | pip is the Python 2.7 package installer. It integrates with virtualenv, doesn't do partial installs, can save package state for replaying, can install from non-egg sources, and can install from version control repositories.  |
| python3-dev | Header files, a static library and development tools for building Python modules, extending the Python 3 interpreter or embedding Python 3 in applications.  |
| python3-pip | pip is the Python 3 package installer. It integrates with virtualenv, doesn't do partial installs, can save package state for replaying, can install from non-egg sources, and can install from version control repositories.  |

*You'll need to install EGene2 platform and Docker*


## Install
You can install this project with the following command:

```zsh
sudo pip3 install git+https://github.com/WendelHime/dockerize_platypus.git
```

## Upgrade
Upgrade with the following command:

```zsh
sudo pip3 install --upgrade Dockerize-Platypus
```

## Uninstalling
Uninstall with the following command:

```zsh
sudo pip3 uninstall Dockerize-Platypus
```

## Running an example
Here we're going to execute `dockerize_platypus.py` and see how it works.

### Copy example files
Copy examples file after install:
```bash
cp -r /usr/share/dockerize_platypus/example example
cd example
```

If you haven't installed with sudo, please, clone this repository and access example files:

```bash
git clone https://github.com/WendelHime/dockerize_platypus.git
cd dockerize_platypus/example
```

### Preparing data EGene2
First of all, we need to build our database, I'll not explain how EGene2 works or the components inside the example configuration file, so please, take your time and read!

You're going to run something like:

```bash
bigou_m.pl -c evidence.conf -d minibct_db -u chadouser -p egene_chado -h localhost -o output_dir
```

After finish, take a look of `report_html_db.conf` and change paths, after that, you can execute this configuration, samething as above:

```bash
bigou_m.pl -c report_html_db.conf -d minibct_db -u chadouser -p egene_chado -h localhost -o output_dir
```

### Running dockerize_platypus
After `report_html_db.conf` finish, we can dockerize this result using:

```bash
dockerize_platypus.py Minibacteria output chadouser minibct_db egene_chado wendelhime
```

If didn't understant anything:
```bash
dockerize_platypus.py -h
usage: dockerize_platypus.py [-h] [-v] [--log LOG]
                             organism filepath dbuser dbname dbpass
                             docker_user

dockerize_platypus.py - dockerize report_html_db.pl result

positional arguments:
  organism       Organism name for docker tag
  filepath       Output filepath from report_html_db.pl
  dbuser         DB username
  dbname         DB name
  dbpass         DB password to be used on docker
  docker_user    Docker username

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  --log LOG      output filepath log

Creates a docker image based on report_html_db.pl, build it and push into
docker cloud
```


