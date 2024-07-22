from .Simulation import simulation_control_actions
from .Controller import controller_control_actions

control_actions = []

control_actions.extend(simulation_control_actions)
control_actions.extend(controller_control_actions)
