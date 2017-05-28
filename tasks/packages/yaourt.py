from fabric.api import run
from fabtools import files


def install(pkg):
    run('yaourt -S --noconfirm --nocolor --needed {}'.format(pkg))


def remove(pkg):
    run('yaourt -R --noconfirm --nocolor {}'.format(pkg))
