from tasks import snap, dotfiles, apt, files


def build(c):
    # git(c)
    # docker(c)
    # python(c)
    # ruby(c)
    # web(c)
    node(c)


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
    c.run(f'curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash', pty=True)
    dotfiles.link(c, 'files/zsh/zshrcd/pyenv.zsh', files.resolve_path('~/.zshrc.d/pyenv.zsh'))


def ruby(c, version='2.6.5'):
    apt.install(c, 'zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev')
    c.run(f'rm -rf ~/.rbenv', pty=True)
    c.run(f'git clone https://github.com/rbenv/rbenv.git ~/.rbenv', pty=True)
    c.run(f'cd ~/.rbenv && src/configure && make -C src', pty=True)

    c.run(f'git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build', pty=True)

    dotfiles.link(c, 'files/zsh/zshrcd/rbenv.zsh', files.resolve_path('~/.zshrc.d/rbenv.zsh'))

    c.run(f'rbenv install {version} && rbenv global {version} && rbenv rehash', pty=True)

    dotfiles.link(c, 'files/ruby/gemrc', files.resolve_path('~/.gemrc'))

    c.run(f'gem install bundler', pty=True)


def web(c):
    apt.install(c, 'apache2-utils')


def node(c):
    # Yarn & NPM included
    snap.install(c, 'node --channel=12/stable', classic=True)
