from rocket import Rocket
from simulation import run_simulation

test_rocket = Rocket(
    name="Test Rocket" ,
    mass=18,
    length=2.3,
    thrust=450,
    diameter=0.102,
    drag_coefficient=0.65,
    burn_time=3.2,
    propellant_type="solid"
)

time_history,altitude_history, velocity_history, acceleration_history, impact_velocity = run_simulation(test_rocket)
print("Rocket Flight Summary")
print("----------------------")
print(f"Rocket Name:", test_rocket.name)
print(f"Flight Time: {time_history[-1]:.2f} s")
print(f"Maximum Altitude: {max(altitude_history):.2f} m")
print(f"Maximum Velocity: {max(velocity_history):.2f} m/s")
print(f"Maximum Acceleration: {max(acceleration_history):.2f} m/s^2")
print(f"Impact Velocity: {impact_velocity:.2f} m/s")

import matplotlib.pyplot as plt
plt.plot(time_history, altitude_history)
plt.title("Altitude vs Time")
plt.xlabel("Time(s)")
plt.ylabel("Altitude (m)")
plt.grid(True)
plt.show()

plt.plot(time_history, velocity_history)
plt.title("Velocity vs Time")
plt.xlabel("Time(s)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.show()

plt.plot(time_history, acceleration_history)
plt.title("Acceleration vs Time")
plt.xlabel("Time(s)")
plt.ylabel("Acceleration (m/s^2)")
plt.grid(True)
plt.show()