from invoke import task

from tasks import dotfiles, files, local, apt


@task
def base(c):
    apt.install(c, 'curl')


@task
def snap(c):
    apt.install(c, 'snapd')


@task
def tldr(c):
    apt.install(c, 'tldr')


@task
def zsh(c):
    HOME = files.resolve_path('~/')

    PREZTO_DIR = files.resolve_path('~/.zprezto')
    PREZTO_SYMLINKS = [
        'zlogin',
        'zlogout',
        'zpreztorc',
        'zprofile',
        'zshenv',
    ]

    apt.install(c, 'zsh direnv fasd fonts-powerline')
    if not files.exists(c, PREZTO_DIR):
        c.run(f'git clone --recursive https://github.com/sorin-ionescu/prezto.git {PREZTO_DIR}')
        c.run(f'git clone --recurse-submodules https://github.com/belak/prezto-contrib {PREZTO_DIR}/contrib')

    with c.cd(str(PREZTO_DIR)):
        c.run('git pull && git submodule update --init --recursive')

    for link in PREZTO_SYMLINKS:
        target_path = HOME / f'.{link}'
        files.remove(c, target_path)
        files.symlink(c, PREZTO_DIR / 'runcoms' / link, target_path)

    c.run('chsh -s /usr/bin/zsh')


@task
def zsh_conf(c):
    BASH_ALIASES = files.resolve_path('~/.bash_aliases')
    PREZTO_CONFIG = files.resolve_path('~/.zpreztorc')
    ZSHRC = files.resolve_path('~/.zshrc')

    dotfiles.link(c, 'files/zsh/zshrc', ZSHRC)
    dotfiles.link(c, 'files/zsh/zpreztorc', PREZTO_CONFIG)
    dotfiles.link(c, 'files/zsh/bash_aliases', BASH_ALIASES)
    dotfiles.link(c, 'files/zsh/zshrcd/zshrcd.zsh', files.resolve_path('~/.zshrc.d/zshrcd.zsh'))


@task
def ssh(c):
    apt.install(c, 'keychain ssh-askpass')


@task
def ssh_conf(c):
    SSH_CONFIG = files.resolve_path('~/.ssh/config')

    files.directory(c, SSH_CONFIG.parent, mode=755)
    dotfiles.link(c, 'files/ssh/config', SSH_CONFIG)
    files.chmod(c, 600, SSH_CONFIG)

    for name, key in c.config.dot.ssh.key_files.items():
        private_key_path = files.resolve_path(f'~/.ssh/{name}')
        public_key_path = files.resolve_path(f'~/.ssh/{name}.pub')

        local.content(c, key['private'], private_key_path)
        files.chmod(c, 600, private_key_path)
        local.content(c, key['public'], public_key_path)
        files.chmod(c, 644, public_key_path)
