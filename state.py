class State(object):

    def __init__(self, name, child_sm=None):
        self._name = name
        self._entry_callbacks = []
        self._exit_callbacks = []
        self._child_state_machine = child_sm
        self._parent_state_machine = None

    def set_child_sm(self, child_sm):
        self._child_state_machine = child_sm

    def set_parent_sm(self, parent_sm):
        self._parent_state_machine = parent_sm

    def start(self, data):
        for callback in self._entry_callbacks:
            callback(data)
        if self._child_state_machine is not None:
            self._child_state_machine.start(data)

    def stop(self, data):
        for callback in self._exit_callbacks:
            callback(data)
        if self._child_state_machine is not None:
            self._child_state_machine.stop(data)

    def has_child_sm(self):
        return True if self._child_state_machine else False

    @property
    def name(self):
        return self._name

    @property
    def child_sm(self):
        return self._child_state_machine

    @property
    def parent_sm(self):
        return self._parent_state_machine


class ExitState(State):

    def __init__(self, status="Normal"):
        self._name = "ExitState"
        self._status = status
        super().__init__(self._status + self._name)
