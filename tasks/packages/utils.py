from invoke import task

from tasks import apt, snap


@task
def htop(c):
    snap.install(c, 'htop')

