import os
import functools

from ConfigParser import ConfigParser

# Use vagrant by default
DEFAULTS = {
    'driver': 'vagrant',
    'directory': '/vagrant'
}


def get_config(config_file='.rdo.conf'):
    config = ConfigParser()
    config.read(config_file)
    env = os.environ.get('RDO_ENV') or 'default'
    try:
        return dict(config.items(env))
    except ConfigParser.NoSectionError:
        return DEFAULTS


if __name__ == '__main__':
    c = Config('example.conf')
    c.parse()
    print(c.get('driver'))
