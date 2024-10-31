# Pendulum Simulation: Exploring the Principle of Least Action

This project simulates a pendulum's motion based on the principle of least action by calculating the Lagrangian mechanics involved in its swing. The simulation includes an animated pendulum swing alongside a dynamic graph of angle vs. time. We aim to demonstrate core physics concepts in an interactive, visual format.

## Features

- **Physics-based Simulation**: Uses Lagrangian mechanics to solve equations of motion for a realistic pendulum swing.
- **Real-Time Animation**: Visualizes the pendulum swing in real-time using `matplotlib` animation.
- **Action Integral Calculation**: Computes the action integral over the swing path based on kinetic and potential energy.
- **Modular Design**: Clean and organized code structure, with separate modules for pendulum mechanics, simulation setup, animation, and plotting.

## Project Structure

- `main.py`: Runs the simulation and coordinates components.
- `pendulum/pendulum.py`: Defines the `Pendulum` class and equations of motion.
- `pendulum/simulation.py`: Manages simulation execution and action integral calculation.
- `pendulum/animation.py`: Sets up the pendulum animation.
- `pendulum/plot.py`: Sets up the plot for angle vs. time visualization.

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/hregua/pendulum-simulation.git
   cd pendulum_simulation

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the simulation:
   ```bash
   python main.py

## Applications
This simulation project is ideal for:
- Visualizing fundamental physics concepts
- Exploring the principle of least action and Lagrangian mechanics
- Serving as an educational tool for students and physics enthusiasts
