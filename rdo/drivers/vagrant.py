from rdo.drivers.base import BaseDriver


class VagrantDriver(BaseDriver):

    def command(self, cmd):
        prefix = 'vagrant ssh -c'.split()
        cmd = ' '.join(cmd)
        cmd = self.use_sudo(cmd)
        cmd = self.working_dir(cmd)
        return prefix + [cmd]
