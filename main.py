import numpy as np
import matplotlib.pyplot as plt
from pendulum.pendulum import Pendulum
from pendulum.simulation import run_simulation, calculate_action
from pendulum.animation import create_animation
from pendulum.plot import setup_plots

# We define here the simulation parameters
length = 1.0                  # Length of pendulum in meters
mass = 1.0                    # Mass of pendulum bob in kg
initial_angle = np.pi / 4     # Initial angle of 45 degrees
initial_conditions = [initial_angle, 0]
time_span = (0, 10)           # Time span for simulation in seconds
time_points = np.linspace(time_span[0], time_span[1], 1000)

# Initialize pendulum and run simulation
pendulum = Pendulum(length, mass, initial_angle)
solution = run_simulation(pendulum, initial_conditions, time_span, time_points)

# Calculate action integral
action = calculate_action(pendulum, solution, time_points)

# Get angles and setup plots
angles = solution.y[0]
fig, ax_anim, ax_plot, current_point = setup_plots(length, time_points, angles, action)

# Create and display animation
ani = create_animation(fig, ax_anim, angles, length, time_points, ax_plot, current_point)
plt.tight_layout()
plt.show()
