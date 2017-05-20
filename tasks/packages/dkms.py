from tasks.packages import yaourt


LINUX_KERNEL = 'linux49'


def install():
    yaourt.install(LINUX_KERNEL + '-headers')
