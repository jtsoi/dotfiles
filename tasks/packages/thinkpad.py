"""
ATTENTION!
As this is a dkms package, you need to keep
correct version of linux-headers installed

How to configure TLP:
http://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html

Unfortunately new style ThinkPad laptops do not support force discharge. so there is no point in trying.
So no point in installing 
- tp_smapi
- tpacpi-bat


Consider installing thermald to limit CPU when using a lot of cpu

"""

from os import path
from tasks import dotfiles
from tasks.packages import yaourt
from fabtools import files


TLP_CONFIG = path.abspath('/etc/default/tlp')
TLP_PACKAGES = [
    'acpi_call-dkms',
    'tlp',
    'tlp-rdw',
    'ethtool',
    'x86_energy_perf_policy',
    'powertop',
    #'thermald'
]


def install():
    yaourt.install(' '.join(TLP_PACKAGES))
    configure()


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
