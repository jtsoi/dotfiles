from invoke import task

from tasks import snap, dotfiles, apt, files


@task
def aws(c):
    c.sudo('pip3 install awscli --upgrade --user')


@task
def aws_conf(c):
    dotfiles.link(c, 'files/aws/config', '~/.aws/config', context=c.config.dot)
    dotfiles.link(c, 'files/aws/credentials', '~/.aws/credentials', context=c.config.dot)


@task
def vagrant(c):
    apt.install(c, 'virtualbox vagrant')


@task
def docker(c):
    c.sudo(f'groupdel docker || true')
    c.sudo(f'addgroup --system docker')
    c.sudo(f'adduser {c.config.dot.user} docker')
    snap.install(c, 'docker')


@task
def python(c):
    c.sudo(f'pip3 install --upgrade pip setuptools wheel', pty=True)
    #c.run(f'curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash', pty=True)
    #dotfiles.link(c, 'files/zsh/zshrcd/pyenv.zsh', files.resolve_path('~/.zshrc.d/pyenv.zsh'))


@task
def ruby(c, version='2.6.5'):
    apt.install(c, 'zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev')
    c.run(f'rm -rf ~/.rbenv', pty=True)
    c.run(f'git clone https://github.com/rbenv/rbenv.git ~/.rbenv', pty=True)
    c.run(f'cd ~/.rbenv && src/configure && make -C src', pty=True)

    c.run(f'git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build', pty=True)

    dotfiles.link(c, 'files/zsh/zshrcd/rbenv.zsh', files.resolve_path('~/.zshrc.d/rbenv.zsh'))

    c.run(f'export PATH="$HOME/.rbenv/bin:$HOME/.rbenv/plugins/ruby-build/bin:$PATH" && rbenv install {version} && rbenv global {version} && rbenv rehash', pty=True)

    dotfiles.link(c, 'files/ruby/gemrc', files.resolve_path('~/.gemrc'))

    c.run(f'export PATH="$HOME/.rbenv/shims:$PATH" && gem install bundler', pty=True)


@task
def web(c):
    apt.install(c, 'apache2-utils')


@task
def node(c):
    # Yarn & NPM included
    snap.install(c, 'node --channel=12/stable', classic=True)
