from tasks.packages import yaourt


def install():
    yaourt.install(
        ' '.join([
            'unzip'
        ])
    )
