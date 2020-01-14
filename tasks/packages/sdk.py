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
def docker(c, docker_compose_version='1.25.0', dive_version='0.9.1'):
    # Install docker daemon
    apt.install(c, 'apt-transport-https ca-certificates curl gnupg-agent software-properties-common')
    c.sudo(f'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -', pty=True)
    apt.add_ppa(c, '"deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"')
    apt.install(c, 'docker-ce docker-ce-cli containerd.io')

    c.sudo('systemctl enable docker')

    # Install docker-compose
    files.curl_download(c, f'https://github.com/docker/compose/releases/download/{docker_compose_version}/docker-compose-$(uname -s)-$(uname -m)', '/usr/local/bin/docker-compose')
    c.sudo('chmod +x /usr/local/bin/docker-compose', pty=True)

    # Install dive to inspect images
    files.curl_download(c, f'https://github.com/wagoodman/dive/releases/download/v{dive_version}/dive_{dive_version}_linux_amd64.deb', '/tmp/dive.deb')
    apt.install(c, '/tmp/dive.deb')


@task
def docker_conf(c):
    # Ensure docker group
    c.sudo(f'groupdel docker || true')
    c.sudo(f'addgroup --system docker')
    c.sudo(f'usermod -aG docker {c.config.dot.user}')

    # Not needed really, but nice to have?
    dotfiles.link(c, 'files/sdk/docker/zshrcd/90-set-uid-gid-for-docker.zsh', files.resolve_path('~/.zshrc.d/90-set-uid-gid-for-docker.zsh'), jinja=False)

    # Set docker to use user namespacing
    c.sudo(f"""echo '{{"userns-remap": "{c.config.dot.user}"}}' | sudo tee /etc/docker/daemon.json""", pty=True)

    # add user to /etc/subuid & /etc/subgid
    user_name = c.config.dot.user
    user_id = c.run(f'id -u {user_name}').stdout.strip()
    expected_uid_line = f'{user_name}:{user_id}:1'
    c.sudo(f"grep -q '^{expected_uid_line}$' /etc/subuid || sudo sed -i.bak '1 i {expected_uid_line}' /etc/subuid")
    c.sudo(f"grep -q '^{expected_uid_line}$' /etc/subgid || sudo sed -i.bak '1 i {expected_uid_line}' /etc/subgid")

    # Restart docker to take effect
    c.sudo('systemctl restart docker')


@task
def python(c):
    c.sudo(f'pip3 install --upgrade pip setuptools wheel virtualenv', pty=True)


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

    # Gem home - probably not needed?
    # Doea not play nice with RubyMine
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
    # setup github packages access key
    dotfiles.link(c, 'files/sdk/ruby/gem/credentials', files.resolve_path('~/.gem/credentials'), jinja=True, context=c.config.dot)
    c.run('chmod 0600 ~/.gem/credentials', pty=True)


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


@task
def github_conf(c):
    # setup github packages access key
    dotfiles.link(c, 'files/sdk/github/zshrcd/91-github-packages-login.zsh',
                  files.resolve_path('~/.zshrc.d/91-github-packages-login.zsh'), jinja=True, context=c.config.dot)


@task
def ubuntu_multipass(c):
    # https://multipass.run/
    snap.install(c, 'multipass', classic=True)
    dotfiles.link(c, 'files/sdk/multipass/zshrcd/11-aliases-multipass.zsh',
                  files.resolve_path('~/.zshrc.d/11-aliases-multipass.zsh'), jinja=False, context=c.config.dot)
