import os
import functools

from ConfigParser import ConfigParser

# Use vagrant by default
DEFAULTS = {
    'driver': 'vagrant',
    'directory': '/vagrant',
    'use_sudo': False,
}


def find_config(fname='.rdo.conf', start=None):
    """Go up until you find an rdo config.
    """
    start = start or os.getcwd()
    config_file = os.path.join(start, fname)
    if os.path.isfile(config_file):
        return config_file

    parent, _ = os.path.split(start)
    if parent == start:
        raise Exception('Config file not found')

    return find_config(fname, parent)


def get_config(config_file='.rdo.conf'):
    fname = find_config(config_file)
    config = ConfigParser()
    config.read(fname)
    env = os.environ.get('RDO_ENV') or 'default'

    return dict(config.items(env))


if __name__ == '__main__':
    c = Config('example.conf')
    c.parse()
    print(c.get('driver'))
