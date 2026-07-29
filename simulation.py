from constants import GRAVITY,SEA_LEVEL_AIR_DENSITY,TIME_STEP
from forces import ( weight_force, drag_force, thrust_force, net_force, acceleration)

def run_simulation(rocket):
    #Initial Conditions 
    time = 0.0
    altitude = 0.0
    velocity = 0.0
    impact_velocity = None
    launched = False
    #History
    time_history = []
    altitude_history = []
    velocity_history = []
    acceleration_history = []
    #Simulation Loop
    while not launched or altitude > 0:
        # Calculate thrust
        thrust = thrust_force(rocket , time)
        # Calculate weight
        weight = weight_force(rocket,GRAVITY)
        # Calculate drag
        drag = drag_force(rocket, velocity, SEA_LEVEL_AIR_DENSITY)
        #Calculate net
        net = net_force(thrust, weight, drag)
        #Calculate Acceleration
        xcel = acceleration(rocket, net)
        #Update velocity,altitude, and time
        velocity += xcel * TIME_STEP
        altitude += velocity * TIME_STEP
        time += TIME_STEP
        if launched and altitude <= 0:
            impact_velocity = velocity
            altitude = 0

            time_history.append(time)
            altitude_history.append(altitude)
            velocity_history.append(impact_velocity)
            acceleration_history.append(xcel)

            break

        time_history.append(time)
        altitude_history.append(altitude)
        velocity_history.append(velocity)
        acceleration_history.append(xcel)

        if altitude > 0:
            launched = True

    return (
        time_history,
        altitude_history,
        velocity_history,
        acceleration_history,
        impact_velocity,
    )
       