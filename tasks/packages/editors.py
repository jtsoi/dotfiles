from tasks import apt, snap


def build(c):
    micro(c)
    pycharm(c)
    rubymine(c)
    sublime_merge(c)


def micro(c):
    # Or: curl https://getmic.ro | bash
    snap.install(c, 'micro', classic=True)


def pycharm(c):
    snap.install(c, 'pycharm-professional', classic=True)
    c.sudo('echo "fs.inotify.max_user_watches = 524288\n" | sudo tee /etc/sysctl.d/60-inotify-limits.conf', pty=True)
    c.sudo('sysctl -p --system')


def rubymine(c):
    snap.install(c, 'rubymine', classic=True)
    c.sudo('echo "fs.inotify.max_user_watches = 524288\n" | sudo tee /etc/sysctl.d/60-inotify-limits.conf', pty=True)
    c.sudo('sysctl -p --system')


def sublime_merge(c):
    c.sudo('wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -', pty=True)
    c.sudo('echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list', pty=True)
    apt.update(c)
    apt.install(c, 'sublime-merge')
