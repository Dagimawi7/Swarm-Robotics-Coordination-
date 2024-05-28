import random  # Import the random module for generating random numbers
import math  # Import the math module for mathematical functions
import threading  # Import the threading module for running concurrent threads
import time  # Import the time module for sleeping the threads

# Define a class for the swarm robot
class SwarmRobot:
    def __init__(self, robot_id, x, y):
        self.robot_id = robot_id  # Assign a unique ID to the robot
        self.position = (x, y)  # Set the initial position of the robot
        self.orientation = random.uniform(0, 2 * math.pi)  # Set a random initial orientation
        self.speed = 0.1  # Set the speed of the robot (units per second)

    def move(self):
        # Update position based on orientation and speed
        new_x = self.position[0] + self.speed * math.cos(self.orientation)
        new_y = self.position[1] + self.speed * math.sin(self.orientation)
        self.position = (new_x, new_y)  # Update the robot's position

    def avoid_collision(self, robots):
        # Check for nearby robots to avoid collisions
        for robot in robots:
            if robot.robot_id != self.robot_id:  # Skip self
                distance = self.calculate_distance(robot.position)
                if distance < 1.0:  # If another robot is too close
                    # Change direction to avoid collision
                    self.orientation = random.uniform(0, 2 * math.pi)
                    return True
        return False

    def calculate_distance(self, position):
        # Calculate the distance between the current position and another position
        return math.sqrt((self.position[0] - position[0])**2 + (self.position[1] - position[1])**2)

    def random_walk(self):
        # Change orientation randomly for random walk behavior
        self.orientation = random.uniform(0, 2 * math.pi)

    def run(self, robots):
        # Main loop for the robot's behavior
        while True:
            if not self.avoid_collision(robots):  # Check and avoid collisions
                self.move()  # Move the robot if no collision is detected
            time.sleep(0.1)  # Wait for a short period before the next update

# Main function to initialize and run the swarm
def main():
    # Initialize three robots with random starting positions
    robots = [SwarmRobot(i, random.uniform(0, 10), random.uniform(0, 10)) for i in range(3)]
    # Create and start a thread for each robot
    threads = [threading.Thread(target=robot.run, args=(robots,)) for robot in robots]

    for thread in threads:
        thread.start()  # Start each thread

    try:
        # Continuously print the positions of the robots
        while True:
            for robot in robots:
                print(f"Robot {robot.robot_id}: Position: {robot.position}")  # Print the robot's position
            time.sleep(1)  # Wait for 1 second before printing again
    except KeyboardInterrupt:
        # Handle keyboard interrupt to stop the simulation
        print("Simulation stopped.")

# Entry point of the script
if __name__ == '__main__':
    main()  # Run the main function
