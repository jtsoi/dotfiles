from invoke import task

from tasks import apt, snap, files


@task
def signal(c):
    snap.install(c, 'signal')


@task
def slack(c):
    snap.install(c, 'slack', classic=True)


