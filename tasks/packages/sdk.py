from tasks import snap, dotfiles, apt, files


def build(c):
    git(c)
    docker(c)


def git(c):

    GIT_CONFIG = files.resolve_path('~/.gitconfig')

    apt.install(c, 'git aspell-en')
    dotfiles.link(c, 'files/git/gitconfig', GIT_CONFIG, context=c.config.dot)


def docker(c):
    c.sudo(f'groupdel docker || true')
    c.sudo(f'addgroup --system docker')
    c.sudo(f'adduser {c.config.dot.user} docker')
    snap.install(c, 'docker')
