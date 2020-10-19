from invoke import task

from tasks import apt, snap, files


@task
def signal(c):
    apt.add_key(c, 'https://updates.signal.org/desktop/apt/keys.asc')
    apt.add_ppa(c, 'deb [arch=amd64] https://updates.signal.org/desktop/apt xenial main')
    apt.install(c, 'signal-desktop')


@task
def slack(c, slack_version='4.10.0'):
    files.wget_download(c, f'https://downloads.slack-edge.com/linux_releases/slack-desktop-{slack_version}-amd64.deb', '/tmp/slack-desktop.deb')
    c.sudo('apt install -y /tmp/slack-desktop.deb')

