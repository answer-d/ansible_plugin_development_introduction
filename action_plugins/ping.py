from ansible.plugins.action import ActionBase
from ansible.utils.display import Display

display = Display()


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        display.display("action plugin `ping` : started")

        self._task.args = {"data": "action plugin test"}
        display.display("action plugin `ping` : update _task.args -> " + str(self._task.args))

        display.display("action plugin `ping` : exec module")
        result = self._execute_module()

        display.display("action plugin `ping` : finished")
        return result
