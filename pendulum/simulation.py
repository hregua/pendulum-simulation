import numpy as np
from scipy.integrate import solve_ivp
from .pendulum import Pendulum

def run_simulation(pendulum, initial_conditions, time_span, time_points):
    solution = solve_ivp(
        pendulum.equations_of_motion,
        time_span,
        initial_conditions,
        t_eval=time_points,
        method="RK45"
    )
    return solution

def calculate_action(pendulum, solution, time_points):
    angles = solution.y[0]
    angular_velocities = solution.y[1]
    action = 0
    for i in range(1, len(time_points)):
        dt = time_points[i] - time_points[i - 1]
        kinetic = pendulum.kinetic_energy(angular_velocities[i])
        potential = pendulum.potential_energy(angles[i])
        lagrangian = kinetic - potential
        action += lagrangian * dt
    return action
