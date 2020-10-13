from invoke import task

from tasks import apt, snap, files


@task
def signal(c):
    snap.install(c, 'signal')


@task
def slack(c, slack_version='4.10.0'):
    files.wget_download(c, f'https://downloads.slack-edge.com/linux_releases/slack-desktop-{slack_version}-amd64.deb', '/tmp/slack-desktop.deb')
    c.sudo('apt install -y /tmp/slack-desktop.deb')

