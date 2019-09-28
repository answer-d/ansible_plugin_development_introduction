from ansible.utils.display import Display
from ansible.plugins.become import BecomeBase

display = Display()


class BecomeModule(BecomeBase):
    def build_become_command(self, cmd, shell):
        super(BecomeModule, self).build_become_command(cmd, shell)
        display.display("hello become plugin!")
        return self._build_success_command(cmd, shell)
