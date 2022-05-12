class NormalTransition():
    def __init__(self, event, src, dst):
        self._event = event
        self._source_state = src
        self._destination_state = dst
        self._condition = None
        self._action = None

    def add_condition(self, callback):
        self._condition = callback

    def add_action(self, callback):
        self._action = callback

    def __call__(self, data):
        if not self._condition or self._condition(data):
            if self._action:
                self._action(data)
            self._from.stop(data)
            self._to.start(data)
    
    @property
    def event(self):
        return self._event

    @property
    def source_state(self):
        return self._source_state

    @property
    def destination_state(self):
        return self._destination_state





