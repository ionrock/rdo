"""
The docker driver current assumes you'll use the following workflow:

 1. Start a container from some image
 2. Run commands in that container (using docker exec)

This will allow running commands that change the filesystem and have
them persist.
"""
import os

from subprocess import check_output, call
from rdo.drivers.base import BaseDriver


class Container(object):
    id_fname = '.rdo.docker.container_id'

    def __init__(self, image, directory):
        self.image = image
        self.directory = directory
        self._id = ''

    @property
    def id(self):
        if not self._id:
            try:
                self._id = open(self.id_fname).read().strip()
            except IOError:
                pass
        return self._id

    def is_running(self):
        for cid in check_output(['docker', 'ps', '-q']).split('\n'):
            if self.id and self.id.startswith(cid):
                return True
        return False

    def start_container(self):
        cmd = [
            'docker', 'run', '-it', '-d',
            '-v', '%s:%s' % (os.getcwd(), self.directory),
            self.image, 'bash'
        ]
        print('Starting conainer: %s' % (' '.join(cmd)))
        return check_output(cmd).strip()

    def start(self):
        """Idempotent function to start the container"""
        if not self.is_running():
            cid = self.start_container()
            with open(self.id_fname, 'w+') as fh:
                fh.write(cid)
        return self.id


class PersistentContainer(Container):

    def commit(self):
        cmd = ['docker', 'commit', self.id, self.image]
        call(cmd)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        if not traceback:
            self.commit()
            return True
        return False


class DockerDriver(BaseDriver):

    def command(self, cmd):
        # The command gets prefixed in the do method
        return cmd

        return prefix + cmd

    def do(self, cmd):
        prefix = ['docker', 'exec']
        container = PersistentContainer(
            self.config.get('name'),
            self.config.get('directory')
        )
        with container as c:
            prefix.append(c.id)
            super(DockerDriver, self).do(prefix + cmd)
