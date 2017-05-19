from tasks.packages import yaourt

FONTS = [
    '--force',
    'ttf-ms-fonts',
    'fonts-meta-base',
    'ttf-vista-fonts',
    'ttf-mac-fonts',
    'ttf-roboto-mono'
]


def install():
    yaourt.install(' '.join(FONTS))

