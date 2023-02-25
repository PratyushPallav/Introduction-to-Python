import pygame
import random

# We are defining the colour of the robot and the background colour using the RGB ratios.
blue = (0, 0, 255)
white = (255, 255, 255)
# We are defining the height and width of the play area as a rectangle of 800*600 and radius of the robot is defined 20.
width = 800
height = 600
radius = 20
speed = 2
# class Ball is created to keep track of the robot illustrating Brownian motion.
class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
# We have defined a function to create a robot according to the set parameters above.
def make_ball():
    """
    Function to make a new, random robot.
    """
    ball = Ball()
    # Starting position of the robot is (400,300) which is the centre of the area, as asked in the test.
    ball.x = 400
    ball.y = 300
    # Speed and direction of robot changes at the rate at which we have defined the speed above.
    ball.change_y = speed
    ball.change_x = speed
    return ball
# This function holds the mathematical logics of the motion of the robot.
def main():
# We initiate teh pygame module
    pygame.init()
# We set the height and width of the screen
    size = [width, height]
    screen = pygame.display.set_mode(size)
# We set the name of the output screen to be "Brownian Motion !"
    pygame.display.set_caption("Brownian Motion !")
# We run a loop until the user clicks the close button.
    done = False
# It is used to manage how fast the screen updates
    clock = pygame.time.Clock()
    ball_list = []
    ball = make_ball()
    ball_list.append(ball)
    while not done:
        # We are using KEYDOWN function from the pygame library, so that when we press SpaceBar(event number 32)
        # The "Brownian Motion 1" window shuts.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 32:
                    done = True

        # Logic
        for ball in ball_list:
            # We change the robot coordinates at the rate of the speed, which is defined above.
            ball.x += ball.change_x
            ball.y += ball.change_y

            # What will happen if the robot encounters a wall? The logic is written below...
            normal_vector = None
            if ball.y > height - radius: # When robot touches the upper wall; height - radius = 600 - 20 = 580
                ball.change_y = abs(ball.change_y)
                normal_vector = pygame.Vector2(0, -1)
            elif ball.y < radius: # When radius (20) of the robot is greater than the y-coordinate of the current place.
                ball.change_y = -abs(ball.change_y)
                normal_vector = pygame.Vector2(0, 1)
            elif ball.x > width - radius: # When the robot touches the side walls of the container.
                ball.change_x = abs(ball.change_x)
                normal_vector = pygame.Vector2(-1, 0)
            elif ball.x < radius:
                ball.change_x = -abs(ball.change_x)
                normal_vector = pygame.Vector2(1, 0)

            if normal_vector:
                normal_vector.rotate_ip(random.randint(-10, 10))
                move_vector = pygame.Vector2(ball.change_x, ball.change_y)
                reflect_vector = move_vector.reflect(normal_vector)
                ball.change_x = reflect_vector.x
                ball.change_y = reflect_vector.y

        # Displaying our parameters
        # we set the screen background
        screen.fill(white)

        # The robot is drawn in the form of a blue circle.
        for ball in ball_list:
            pygame.draw.circle(screen, blue, [round(ball.x), round(ball.y)], radius)
        # We limit to 60 frames per second
        clock.tick(60)

        # We update the screen with what we've drawn.
        pygame.display.flip()

    # Thus, we come to the end if the Brownian Motion of the robot.
    pygame.quit()


if __name__ == "__main__":
    main()