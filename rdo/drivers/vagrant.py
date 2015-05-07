from rdo.drivers.base import BaseDriver


class VagrantDriver(BaseDriver):

    def command(self, cmd):
        prefix = 'vagrant ssh -c'.split()
        cmd = ' '.join(cmd)
        working_dir = self.config.get('directory')
        if working_dir:
            cmd = 'cd %s && %s' % (working_dir, cmd)
        return prefix + [cmd]
