import numpy as np
from matplotlib.animation import FuncAnimation

def create_animation(fig, ax, angles, length, time_points, ax_plot, current_point):
    x = length * np.sin(angles)
    y = -length * np.cos(angles)
    line, = ax.plot([], [], 'o-', lw=2)

    def update(frame):
        # Update pendulum position
        line.set_data([0, x[frame]], [0, y[frame]])
        # Update point on angle-time plot
        current_point.set_data([time_points[frame]], [angles[frame]])
        return line, current_point

    ani = FuncAnimation(fig, update, frames=len(time_points), blit=True, interval=20)
    return ani
