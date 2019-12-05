#!/usr/bin/env python3
import asyncio
import os
import pathlib

from aiorun import run

POLL_INTERVAL = 20
POWER_ROOT = pathlib.Path('/sys/class/power_supply')
AC_FILE = POWER_ROOT / 'AC' / 'uevent'
BAT0_FILE = POWER_ROOT / 'BAT0' / 'uevent'
BAT1_FILE = POWER_ROOT / 'BAT1' / 'uevent'


async def battery_loop():
    # Setup delegate
    print(os.getpid())
    while True:
        await update_battery_state()
        await asyncio.sleep(POLL_INTERVAL)


async def update_battery_state():
    print('Ping...')
    bat0_uevent_content = read_bat_uevent_file(BAT1_FILE)
    bat0_data = parse_uevent_file(bat0_uevent_content)
    print(bat0_data)


def read_bat_uevent_file(file_path):
    if file_path.exists():
        return file_path.read_text()
    return None


def parse_uevent_file(file_content):
    kv = dict()
    if file_content:
        for line in file_content.splitlines():
            key, _, value = line.partition('=')
            kv[key] = value
    return kv


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run(battery_loop())