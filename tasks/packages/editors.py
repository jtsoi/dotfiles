from tasks.packages import snap


def build(c):
    snap.install(c, 'pycharm-professional')
    snap.install(c, 'vscode')