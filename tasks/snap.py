
def install(c, pkg, classic=True):
    cmd = f'snap install {pkg} {"--classic" if classic else ""}'
    c.sudo(cmd, pty=True)


def remove(c, pkg,):
    cmd = f'snap remove {pkg}'
    c.sudo(cmd)
