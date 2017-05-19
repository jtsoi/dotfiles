"""
How to configure TLP:
http://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html

TODO: Write a balancer script:
## http: // www.thinkwiki.org / wiki / Talk:Code / tp - bat - balance
"""
from os import path
from tasks import dotfiles
from tasks.packages import yaourt
from fabtools import files


TLP_CONFIG = path.abspath('/etc/default/tlp')
TLP_PACKAGES = [
    'linux49-tp_smapi',
    'linux49-acpi_call',
    'tlp',
    'tlp-rdw',
    'ethtool',
    'x86_energy_perf_policy',
]


def install():
    yaourt.install(' '.join(TLP_PACKAGES))
    #configure()


def configure():
    files.remove(TLP_CONFIG, use_sudo=True)
    files.upload_template(
        'files/tlp/tlp',
        TLP_CONFIG,
        use_sudo=True,
        mode='0644',
        chown=True,
        user='root'
    )
