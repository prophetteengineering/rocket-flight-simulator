# Rocket Class
# Represents a single rocket and stores its physical properties
class Rocket:
    def __init__(self, name, mass, length, thrust, diameter, drag_coefficient, burn_time, propellant_type):
        self.name = name
        self.mass = mass  # in kg
        self.length = length  # in meters
        self.thrust = thrust  # in Newtons
        self.diameter = diameter  # in meters
        self.drag_coefficient = drag_coefficient  # dimensionless
        self.burn_time = burn_time  # in seconds
        self.propellant_type = propellant_type  # e.g., "liquid", "solid"
        