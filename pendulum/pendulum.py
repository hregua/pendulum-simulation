import numpy as np

class Pendulum:
    def __init__(self, length, mass, initial_angle):
        self.length = length
        self.mass = mass
        self.initial_angle = initial_angle
        self.g = 9.81 # acceleration due to gravity (m/s^2)

    def equations_of_motion(self, t, y):
        theta, omega = y
        dydt = [omega, -(self.g / self.length) * np.sin(theta)]
        return dydt

    def kinetic_energy(self, omega):
        return 0.5 * self.mass * (self.length * omega) ** 2

    def potential_energy(self, theta):
        return self.mass * self.g * self.length * (1 - np.cos(theta))