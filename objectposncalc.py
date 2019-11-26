initial_position = float(input("Enter the object's initial position: "))
initial_velocity = float(input("Enter the object's initial velocity: "))
acceleration = float(input("Enter the object's acceleration: "))
time_elapsed = float(input("Enter the object's time elapsed: "))

final_position = initial_position + initial_velocity * time_elapsed + 0.5 * acceleration * time_elapsed ** 2


print("\nThe object's final position is", final_position)
