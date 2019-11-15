"""
ATTENTION!
As this is a dkms package, you need to keep
correct version of linux-headers installed

How to configure TLP:
http://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html

Consider installing thermald to limit CPU when using a lot of cpu
"""
from invoke import task

from tasks import apt


@task
def tlp(c):
    # https://wiki.archlinux.org/index.php/tp_smapi
    # apt.install(c, 'tp-smapi-dkms') # For older Thinkpads? https://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html
    apt.install(c, 'tlp tlp-rdw acpi-call-dkms smartmontools')

    tlp_lines = [
        "sed -i.bak 's|#START_CHARGE_THRESH_BAT1=75|START_CHARGE_THRESH_BAT1=80|g' /etc/default/tlp",
        "sed -i.bak 's|#START_CHARGE_THRESH_BAT0=75|START_CHARGE_THRESH_BAT0=80|g' /etc/default/tlp",
        "sed -i.bak 's|#STOP_CHARGE_THRESH_BAT1=80|STOP_CHARGE_THRESH_BAT1=89|g' /etc/default/tlp",
        "sed -i.bak 's|#STOP_CHARGE_THRESH_BAT0=80|STOP_CHARGE_THRESH_BAT0=89|g' /etc/default/tlp"
    ]
    for line in tlp_lines:
        c.sudo(line)


@task
def powertop(c):
    apt.install(c, 'powertop')
