from os import path
from fabric.api import env
from tasks import dotfiles
from tasks.packages import yaourt
from fabtools import files, require

BASHRC_CONFIG = path.abspath(path.expanduser('~/.extend.bashrc'))


def install():
    configure()


def configure():
    dotfiles.link('files/bash/extend.bashrc', BASHRC_CONFIG)
