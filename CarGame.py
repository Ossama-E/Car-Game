# Libraries
import random
import pygame
from pygame.locals import *

# Set the desired frame rate in frames per second
frame_rate = 60

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Define the size of the screen
size = width, height = (800, 800)
# Width of the black road
road_w = int(width / 1.6)
# Width of the road marks
roadmark_w = int(width / 80)
# Define the right lane
right_lane = width / 2 + road_w / 4
# Define the left lane
left_lane = width / 2 - road_w / 4

speed = 20

pygame.init()
running = True

# Set the screen
screen = pygame.display.set_mode(size)

# Set the screen title
pygame.display.set_caption("The ultimate car game")

# Fill the screen with a green color
screen.fill((60, 220, 0))

# Update the display
pygame.display.update()

# Load the yellow car image
car = pygame.image.load("userCar.png")
# Get the rectangular area of the car image
car_loc = car.get_rect()
# Set the initial position of the car to the center of the right lane
car_loc.center = (right_lane, height * 0.8)

# Load the other car image
car2 = pygame.image.load("oppCar.png")
# Get the rectangular area of the other car image
car2_loc = car2.get_rect()
# Set the initial position of the other car to the center of the left lane
car2_loc.center = (left_lane, height * 0.2)

counter = 0
up = 50
while running:
    # Increment the counter
    counter += 1
    # If the counter has reached a certain value, increase the speed and reset the counter
    if counter == 340:
        speed += 0.25
        counter = 0
        print("Level up", speed)

    # Move the other car down the screen
    car2_loc[1] += speed
    # If the other car has reached the bottom of the screen, move it back to the top and randomly place it in either lane
    if car2_loc[1] > height:
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200
    # If the other car and the yellow car are in the same lane and the other car is close to the yellow car, print "oops" and break out of the loop
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 230:
        print("oops")
        break

    # Check for events
    for event in pygame.event.get():
        # If the event is to quit the game, set running to False
        if event.type == QUIT:
            running = False

        # If a key is pressed
        if event.type == KEYDOWN:
            # If the left or a key is pressed, move the yellow car to the left lane if it is not already there
            if event.key in [K_a, K_LEFT]:
                update_car_l = car_loc[0]
                update_car_l -= int(road_w / 2)
                if int(update_car_l) >= (width / 2 - road_w + roadmark_w * 2):
                    car_loc = car_loc.move([-int(road_w / 2), 0])
                else:
                    pass

            # If the right or d key is pressed, move the yellow car to the right lane if it is not already there
            if event.key in [K_d, K_RIGHT]:
                update_car_r = car_loc[0]
                update_car_r += int(road_w / 2)
                if update_car_r < road_w:
                    car_loc = car_loc.move([+int(road_w / 2), 0])

            # If the up or w key is pressed, move the yellow car up
            if event.key in [K_w, K_UP]:
                car_loc = car_loc.move([0, -20])
                # print(car_loc[1], car2_loc[1])
            # If the down or s key is pressed, move the yellow car down
            if event.key in [K_s, K_DOWN]:
                car_loc = car_loc.move([0, +20])
                print(car_loc[1])

        # Update the display
        pygame.display.update()

    # Redraw the screen
    screen = pygame.display.set_mode(size)
    # Set the screen title
    pygame.display.set_caption("The ultimate car game")
    # Fill the screen with a green color
    screen.fill((60, 220, 0))
    # Draw the road in dark grey
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))
    # Draw the yellow road marks
    pygame.draw.rect(
        screen, (255, 240, 60), (width / 2 - roadmark_w / 2, 0, roadmark_w, height)
    )
    # Draw white marks on the right side of the road
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height),
    )
    # Draw the yellow car on the screen
    screen.blit(car, car_loc)
    # Draw the other car on the screen
    screen.blit(car2, car2_loc)
    # Limit the frame rate to the value specified in frame_rate
    clock.tick(frame_rate)

# Quit pygame
pygame.quit()
