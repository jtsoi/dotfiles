from invoke import task

from tasks import apt, snap, files


@task
def kodi(c):
    apt.add_ppa(c, 'ppa:team-xbmc/ppa')
    apt.install(c, 'kodi')


@task
def spotify(c):
    snap.install(c, 'spotify')
