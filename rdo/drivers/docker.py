from rdo.drivers.base import BaseDriver


class DockerDriver(BaseDriver):

    def command(self, cmd):
        action = 'run'
        if self.config.get('exec'):
            action = 'exec'

        prefix = ['docker', action, '-it', self.config.get('name')]
        return prefix + cmd
