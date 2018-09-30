from tasks.packages import apt


def install(c, pkg, classic=True):
    cmd = f'snap install {pkg} {"--classic" if classic else ""}'
    c.sudo(cmd)


def remove(c, pkg,):
    cmd = f'snap remove {pkg}'
    c.sudo(cmd)


def build(c):
    apt.install(c, 'snapd')
