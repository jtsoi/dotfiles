from tasks import snap, dotfiles, apt, files


def build(c):
    #git(c)
    #docker(c)
    python(c)


def git(c):

    GIT_CONFIG = files.resolve_path('~/.gitconfig')

    apt.install(c, 'git aspell-en')
    dotfiles.link(c, 'files/git/gitconfig', GIT_CONFIG, context=c.config.dot)


def docker(c):
    c.sudo(f'groupdel docker || true')
    c.sudo(f'addgroup --system docker')
    c.sudo(f'adduser {c.config.dot.user} docker')
    snap.install(c, 'docker')


def python(c):
    # Custom RC Files
    c.run(f'curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash', pty=True)
    dotfiles.link(c, 'files/zsh/zshrcd/pyenv.zsh', files.resolve_path('~/.zshrc.d/pyenv.zsh'))


def web(c):
    apt.install(c, 'apache2-utils')