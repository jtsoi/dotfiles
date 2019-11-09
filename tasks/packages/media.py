from tasks import apt, snap, files


def build(c):
    kodi(c)


def kodi(c):
    apt.add_ppa(c, 'ppa:team-xbmc/ppa')
    apt.install(c, 'kodi')
