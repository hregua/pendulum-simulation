import matplotlib.pyplot as plt

def setup_plots(length, time_points, angles, action):
    fig, (ax_anim, ax_plot) = plt.subplots(1, 2, figsize=(12, 6))

    # Setup pendulum animation plot
    ax_anim.set_xlim(-length - 0.5, length + 0.5)
    ax_anim.set_ylim(-length - 0.5, length + 0.5)
    ax_anim.set_aspect('equal')
    ax_anim.set_title("Pendulum Swing Animation")
    ax_anim.set_xlabel("X Position (m)")
    ax_anim.set_ylabel("Y Position (m)")
    ax_anim.grid(True)

    # Setup angle vs time plot
    ax_plot.plot(time_points, angles, label="Angle (radians)", color="blue")
    current_point, = ax_plot.plot([0], [angles[0]], 'ro')  
    ax_plot.set_title("Pendulum Angle Over Time")
    ax_plot.set_xlabel("Time (s)")
    ax_plot.set_ylabel("Angle (rad)")
    ax_plot.grid(True)
    ax_plot.legend()

    return fig, ax_anim, ax_plot, current_point