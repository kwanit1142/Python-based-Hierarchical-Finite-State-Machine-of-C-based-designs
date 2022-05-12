from state import ExitState
from transition import NormalTransition


class StateMachine(object):
    def __init__(self, name):
        self._name = name
        self._states = []
        self._events = []
        self._transitions = []
        self._initial_state = None
        self._current_state = None
        self._exit_callback = None
        self._exit_state = ExitState()
        self.add_state(self._exit_state)
        self._exited = True

    def start(self, data):
        if not self._initial_state:
            raise ValueError("initial state is not set")
        self._current_state = self._initial_state
        self._exited = False
        self._current_state.start(data)

    def stop(self, data):
        if not self._initial_state:
            raise ValueError("initial state is not set")
        if self._current_state is None:
            raise ValueError("state machine has not been started")
        self._current_state.stop(data)
        self._current_state = self._exit_state
        self._exited = True

    def add_state(self, state, initial_state=False):
        if state in self._states:
            raise ValueError("attempting to add same state twice")
        self._states.append(state)
        state.set_parent_sm(self)
        if not self._initial_state and initial_state:
            self._initial_state = state

    def add_event(self, event):
        self._events.append(event)

    def add_transition(self, src, dst, evt):
        transition = None
        if src in self._states and dst in self._states and evt in self._events:
            transition = NormalTransition(src, dst, evt)
            self._transitions.append(transition)
        return transition

    def trigger_event(self, evt, data=None, propagate=False):
        if not self._initial_state:
            raise ValueError("initial state is not set")

        if self._current_state is None:
            raise ValueError("state machine has not been started")

        if propagate and self._current_state.has_child_sm():
            self._current_state.child_sm.trigger_event(evt, data, propagate)
        else:
            for transition in self._transitions:
                if transition.source_state == self._current_state and transition.event == evt:
                    self._current_state = transition.destination_state

                    transition(data)
                    if isinstance(self._current_state, ExitState) and self._exit_callback and not self._exited:
                        self._exited = True
                        self._exit_callback(self._current_state, data)
                    
                    break

    @property
    def exit_state(self):
        return self._exit_state

    @property
    def current_state(self):
        return self._current_state

    @property
    def name(self):
        return self._name
