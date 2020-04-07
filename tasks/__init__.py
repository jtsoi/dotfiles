from os import environ

from invoke import Collection

from tasks import files, apt, snap, machine
from tasks.packages import (
    secrets,
    system,
    editors,
    desktop,
    browsers,
    messaging,
    sdk,
    code,
    media,
    thinkpad,
    utils,
    wireguard,
    prusa,
    regolith)


ns = Collection(

    system,
    regolith,
    browsers,
    messaging,
    editors,
    desktop,
    sdk,
    media,
    thinkpad,
    utils,
    wireguard,
    prusa,
    code
)

ns.add_task(secrets.pull_secrets)
ns.add_task(secrets.push_secrets)

ns.configure(dict(machine=dict(is_thinkpad=machine.is_thinkpad())))
