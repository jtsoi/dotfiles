from invoke import task

from tasks import apt, snap, files


@task
def sync_thing(c):
    # Maybe later
    c.sudo('curl -s https://syncthing.net/release-key.txt | sudo apt-key add -', pty=True)
    apt.add_ppa(c, '"deb https://apt.syncthing.net/ syncthing stable"')
    #apt.install(c, 'syncthing')
