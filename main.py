from rocket import Rocket

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

print(test_rocket.name)
print(test_rocket.mass)
print(test_rocket.frontal_area())
from forces import weight_force
weight = weight_force(test_rocket, 9.81)
print(weight)