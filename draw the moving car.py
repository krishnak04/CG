import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Set up the car's initial position and plot limits
car_width = 2
car_height = 1
car_x = 0  # Starting position of the car on the x-axis
car_y = 0  # y-axis stays constant
ax.set_xlim(0, 10)  # Set x limits to allow movement
ax.set_ylim(-5, 5)  # Set y limits, which stay constant

# Draw the car (using a rectangle for the car body and circles for wheels)
car_body = plt.Rectangle((car_x, car_y - car_height / 2), car_width, car_height, color='blue')
wheel1 = plt.Circle((car_x + 0.5, car_y - car_height / 2 - 0.25), 0.25, color='black')
wheel2 = plt.Circle((car_x + 1.5, car_y - car_height / 2 - 0.25), 0.25, color='black')

# Draw the road (a simple rectangle representing the road)
road = plt.Rectangle((0, -2), 10, 1, color='gray', zorder=-1)
ax.add_patch(road)

# Add the car components to the plot
ax.add_patch(car_body)
ax.add_patch(wheel1)
ax.add_patch(wheel2)

# Function to update the car's position
def update(frame):
    global car_x

    # Update car's position (move it to the right)
    car_x += 0.1  # Move car by 0.1 units each frame
    
    # Update car body position
    car_body.set_x(car_x)
    
    # Update wheel positions
    wheel1.set_center((car_x + 0.5, car_y - car_height / 2 - 0.25))
    wheel2.set_center((car_x + 1.5, car_y - car_height / 2 - 0.25))

    # If the car moves off the screen, reset its position
    if car_x > 10:
        car_x = -2  # Reset car to starting position

    return car_body, wheel1, wheel2

# Set up the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show the plot
plt.show()
