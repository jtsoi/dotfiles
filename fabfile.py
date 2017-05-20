from fabric.api import sudo, run, local, task, env

from tasks import vars
from tasks import sshd
from tasks import packages


@task
def local():
    vars.load_variables('local')


@task
def setup():
    with sshd.sshd():
        packages.install()
