

def install(c, pkg):
    cmd = f'apt-get -y install {pkg}'
    return c.sudo(cmd, pty=True)


def remove(c, pkg, purge=False):
    cmd = f'apt {"purge" if purge else "remove"} {pkg}'
    return c.sudo(cmd)


def update(c):
    return c.sudo('apt update')


def upgrade(c):
    return c.sudo('apt upgrade')


def add_ppa(c, ppa):
    return c.sudo(f'apt-add-repository {ppa} -y')
