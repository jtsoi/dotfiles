from invoke import task

from tasks import apt, snap, files


@task
def htop(c):
    snap.install(c, 'htop')


@task
def broot(c):
    files.curl_download(
        c,
        'https://dystroy.org/broot/download/x86_64-linux/broot',
        '/usr/local/bin/broot',
        sudo=True
    )
    c.sudo('chmod +x /usr/local/bin/broot', pty=True)
    c.run('broot --install', pty=True)


@task
def jq(c):
    apt.install(c, 'jq')