from ansible.plugins.callback.default import CallbackModule as CallbackModule_org


class CallbackModule(CallbackModule_org):
    def v2_runner_on_ok(self, result):
        super(CallbackModule, self).v2_runner_on_ok(result)
        self._display.display("Hello callback plugin!")
