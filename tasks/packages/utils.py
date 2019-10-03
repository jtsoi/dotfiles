from tasks import apt, snap


def build(c):
    snap.install(c, 'htop')

