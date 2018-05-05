# dockerize_platypus
[![Build Status](https://travis-ci.org/WendelHime/dockerize_platypus.svg?branch=master)](https://travis-ci.org/WendelHime/dockerize_platypus) [![Coverage Status](https://coveralls.io/repos/github/WendelHime/dockerize_platypus/badge.svg?branch=master)](https://coveralls.io/github/WendelHime/dockerize_platypus?branch=master) [![Documentation Status](https://readthedocs.org/projects/dockerize-platypus/badge/?version=latest)](http://dockerize-platypus.readthedocs.io/en/latest/?badge=latest)

Dockerize reposrt_html_db.pl result and upload for docker cloud

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

*You'll need to install EGene2 platform also*


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


