#Weight Force equation
def weight_force(rocket, gravity):
    return -rocket.mass * gravity

#Drag Force Equation
def drag_force(rocket, velocity, air_density):
    drag_magnitude = 0.5 * rocket.drag_coefficient * air_density * velocity**2 * rocket.frontal_area()

    if velocity > 0:
        return -drag_magnitude
    elif velocity < 0:
        return +drag_magnitude
    else:
        return 0

#Thrust Force Equation
def thrust_force(rocket, current_time):
    if current_time < rocket.burn_time:
        return rocket.thrust
    else:
        return 0
