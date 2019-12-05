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
def gcloud(c):
    c.sudo('curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -', pty=True)
    apt.add_ppa(c, '"deb http://packages.cloud.google.com/apt cloud-sdk main"')
    apt.install(c, 'google-cloud-sdk')


@task
def gcloud_conf(c):
    dotfiles.link(c, 'files/sdk/gcloud/zshrcd/600_zsh_completion.zsh', files.resolve_path('~/.zshrc.d/600_zsh_completion.zsh'), jinja=False)


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
def ruby(c, ruby_install_version='0.7.0', chruby_version='0.3.9', gem_home_version='0.1.0'):
    # ruby-install
    apt.install(c, 'build-essential')

    files.curl_download(c,
                        f'https://github.com/postmodern/ruby-install/archive/v{ruby_install_version}.tar.gz',
                        f'/tmp/ruby-install-{ruby_install_version}.tar.gz')
    with c.cd('/tmp/'):
        c.run(f'tar -xzvf ruby-install-{ruby_install_version}.tar.gz')

    with c.cd(f'/tmp/ruby-install-{ruby_install_version}/'):
        c.run('sudo make install')

    # Chruby
    files.curl_download(c,
                        f'https://github.com/postmodern/chruby/archive/v{chruby_version}.tar.gz',
                        f'/tmp/chruby-{chruby_version}.tar.gz')
    with c.cd('/tmp/'):
        c.run(f'tar -xzvf chruby-{chruby_version}.tar.gz')

    with c.cd(f'/tmp/chruby-{chruby_version}/'):
        c.run('sudo make install')

    # Gem home
    files.curl_download(c,
                        f'https://github.com/postmodern/gem_home/archive/v{gem_home_version}.tar.gz',
                        f'/tmp/gem_home-{gem_home_version}.tar.gz')
    with c.cd('/tmp/'):
        c.run(f'tar -xzvf gem_home-{gem_home_version}.tar.gz')

    with c.cd(f'/tmp/gem_home-{gem_home_version}/'):
        c.run('sudo make install')


@task
def ruby_conf(c):
    dotfiles.link(c, 'files/zsh/zshrcd/chruby.zsh', files.resolve_path('~/.zshrc.d/chruby.zsh'))


@task
def web(c):
    apt.install(c, 'apache2-utils')


@task
def node(c):
    # Yarn & NPM included
    snap.install(c, 'node --channel=12/stable', classic=True)


@task
def dev_dns_conf(c):

    c.sudo("sed -i.bak 's/^#DNSStubListener=.*/DNSStubListener=no/g' /etc/systemd/resolved.conf")
    c.sudo('cp files/sdk/dev_dns/confd/00-enable-dnsmasq.conf /etc/NetworkManager/conf.d/00-enable-dnsmasq.conf')
    c.sudo('cp files/sdk/dev_dns/dnsmasqd/skovik.conf /etc/NetworkManager/dnsmasq.d/skovik.conf')

    c.sudo("mv /etc/resolv.conf /etc/resolv.conf.bak")
    c.sudo('systemctl restart systemd-resolved')
    c.sudo('systemctl restart NetworkManager')
