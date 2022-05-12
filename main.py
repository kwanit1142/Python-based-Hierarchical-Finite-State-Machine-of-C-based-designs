# Television Control FSM example

from event import Event
from fsm import StateMachine
from state import State

# states
IDLE = State('IDLE')
tv_on = State('TV_ON')
tv_off = State('TV_OFF')

last_channel = State('last_channel')
up_tv_chnl = State('up_tv_channel')
down_tv_chnl = State('down_tv_channel')

up_rmt_chnl = State('up_rmt_channel')
down_rmt_chnl = State('down_rmt_channel')

#  events
start_tv = Event('start_tv')
dec_tv_chnl = Event('dec_tv_chnl')
inc_tv_chnl = Event('inc_tv_chnl')

dec_rmt_chnl = Event('dec_rmt_chnl')
inc_rmt_chnl = Event('inc_rmt_chnl')

turn_off = Event('turn_off')

# Child FSM: Tv buttons

tv_fsm = StateMachine('tv_fsm')
tv_fsm.add_state(last_channel, True)
tv_fsm.add_state(up_tv_chnl)
tv_fsm.add_state(down_tv_chnl)
tv_fsm.add_event(dec_tv_chnl)
tv_fsm.add_event(inc_tv_chnl)
tv_fsm.add_event(turn_off)
tv_fsm.add_transition(last_channel, down_tv_chnl, dec_tv_chnl)
tv_fsm.add_transition(last_channel, up_tv_chnl, inc_tv_chnl)
tv_fsm.add_transition(down_tv_chnl, up_tv_chnl, inc_tv_chnl)
tv_fsm.add_transition(last_channel, up_tv_chnl, inc_tv_chnl)
tv_fsm.add_transition(up_tv_chnl, last_channel, turn_off)
tv_fsm.add_transition(down_tv_chnl, last_channel, turn_off)

# Child FSM: Remote control buttons

rmt_fsm = StateMachine('rmt_fsm')
rmt_fsm.add_state(last_channel, True)
rmt_fsm.add_state(up_rmt_chnl)
rmt_fsm.add_state(down_rmt_chnl)
rmt_fsm.add_event(dec_rmt_chnl)
rmt_fsm.add_event(inc_rmt_chnl)
rmt_fsm.add_event(turn_off)
rmt_fsm.add_transition(last_channel, down_rmt_chnl, dec_rmt_chnl)
rmt_fsm.add_transition(last_channel, up_rmt_chnl, inc_rmt_chnl)
rmt_fsm.add_transition(down_rmt_chnl, up_rmt_chnl, inc_rmt_chnl)
rmt_fsm.add_transition(last_channel, up_rmt_chnl, inc_rmt_chnl)
rmt_fsm.add_transition(up_rmt_chnl, last_channel, turn_off)
rmt_fsm.add_transition(down_rmt_chnl, last_channel, turn_off)

# Parent FSM

main_fsm = StateMachine('main_fsm')
main_fsm.add_state(IDLE, True)
main_fsm.add_state(tv_on)
main_fsm.add_state(tv_off)
main_fsm.add_event(start_tv)
main_fsm.add_event(turn_off)
main_fsm.add_transition(IDLE, tv_on, start_tv)
main_fsm.add_transition(tv_on, tv_off, turn_off)

# controller


def print_state():
    print(f"FSM state: Main={main_fsm.current_state.name} -> Tv_buttons={tv_fsm.current_state.name}, Remote_buttons={rmt_fsm.current_state.name}\n")

def run_event(n):
  if (n == -1):
    main_fsm.trigger_event(turn_off)
    tv_fsm.trigger_event(turn_off)
    rmt_fsm.trigger_event(turn_off)
    print('Event: Turn off')
    return

  if (n == 0):
    tv_fsm.trigger_event(dec_tv_chnl)
    print('Event: Decrease Tv Channel')
    return

  if (n == 1):
    tv_fsm.trigger_event(inc_tv_chnl)
    print('Event: Increase Tv Channel')
    return

  if (n == 2):
    rmt_fsm.trigger_event(dec_rmt_chnl)
    print('Event: Decrease Remote Channel')
    return

  if (n == 3):
    rmt_fsm.trigger_event(inc_rmt_chnl)
    print('Event: Increase Remote Channel')
    return

def main():
    n = 0
    print('Tv Remote Control FSM')
    main_fsm.start('start')
    tv_fsm.start('start')
    rmt_fsm.start('start')
    print_state()

    main_fsm.trigger_event(start_tv)
    print('Starting Tv')
    print_state()

    while n != -1:
        n = int(input('Action= '))
        run_event(n)
        print_state()

if __name__ == '__main__':
  main()