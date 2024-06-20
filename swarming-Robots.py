import random  
import math  
import threading  
import time  


class SwarmRobot:
    def __init__(self, robot_id, x, y):
        self.robot_id = robot_id  
        self.position = (x, y)  
        self.orientation = random.uniform(0, 2 * math.pi)  
        self.speed = 0.1 

    def move(self):
        new_x = self.position[0] + self.speed * math.cos(self.orientation)
        new_y = self.position[1] + self.speed * math.sin(self.orientation)
        self.position = (new_x, new_y)  # Update the robot's position

    def avoid_collision(self, robots):
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


if __name__ == '__main__':
    main()  
