from invoke import task

from tasks import snap, dotfiles, apt, files


@task
def wireguard(c):
    apt.install(c, 'wireguard')


@task
def wireguard_conf(c):
    pass
