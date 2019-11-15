from pathlib import Path


def is_thinkpad():
    file = Path('/sys/devices/virtual/dmi/id/product_family')
    if not file.exists():
        return False
    return file.read_text().strip().startswith('ThinkPad')
