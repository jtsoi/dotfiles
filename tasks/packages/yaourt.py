from fabric.api import run
from fabtools import files


def install(pkg):
    run('yaourt -S --noconfirm --nocolor --needed {}'.format(pkg))
