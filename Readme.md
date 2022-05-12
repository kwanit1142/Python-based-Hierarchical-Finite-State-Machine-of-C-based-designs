## Hierarchal FSM

We have coded a hierarchical FSM using python classes based on a c based design

### Structure
- main.py : entry point for the project
- state.py : provides a utility class for STATE of fsm
- event.py : provides a utility class for EVENT in an fsm
- transition.py : provides a utility class for a TRANSITION in an fsm
- fsm.py : provides a utility class for defining an fsm

### Input Events
- When you run the main.py file, the user is prompted to enter a number from [0 - 3, -1] that corresponds to an event in the FSM.
- We are modelling a hierarchical fsm of tv control using either the tv buttons or a remote
- 0 : Decrease the channel using Tv button
- 1 : Increase the channel using Tv button
- 2 : Decrease the channel using remote button
- 3 : Increase the channel using remote button
- -1 : Turn Off the Tv