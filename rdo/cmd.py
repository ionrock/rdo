import sys

from rdo.config import get_config
from rdo.drivers import find_driver


def main():
    cmd = sys.argv[1:]
    config = get_config()
    driver = find_driver(config)
    driver.do(cmd)
