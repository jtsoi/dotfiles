from tasks import dotfiles
from tasks.packages import yaourt
from fabtools import files
from fabric.api import sudo, env


PACKAGES = [
    'aws-cli'
]


def install():
    yaourt.install(' '.join(PACKAGES))
    configure()


def configure():
    pass
