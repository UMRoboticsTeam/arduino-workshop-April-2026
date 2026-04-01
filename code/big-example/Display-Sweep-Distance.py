import serial, math, pygame, traceback

# Screen config
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
DISTANCE_SCALE = 7
FPS = 60


# Arduino communication config (MAY HAVE TO CHANGE PORT!)
ARDUINO_PORT = "COM3"
ARDUINO_BAUD = 115200
ARDUNIO_TIMEOUT = 0.01


def main():
    # Setup serial communication and initialize pygame for rendering
    arduino_serial = serial.Serial(port=ARDUINO_PORT, baudrate=ARDUINO_BAUD, timeout=ARDUNIO_TIMEOUT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # We store the dots in the format (x,y,timer) where timer controls the colour.
    # The index in the array is the angle, going from 0 to 180 inclusive
    dots = [(-1000, -1000, 0)] * 181

    # Main loop
    dt_ms = 0
    has_quit = False
    while not has_quit:
        # Just get pygame working
        if len(pygame.event.get(eventtype=pygame.QUIT)) != 0:
            has_quit = True  # User clicked X on window

        # Interesting stuff!
        # Read new dots from the arduino (may take some time)
        read_new_dots(arduino_serial, dots)
        # Draw all of the dots we have stored in the array.
        render_frame_and_update(screen, dots, dt_ms)

        # Wait for the next frame, and get the number of miliseconds it took.
        dt_ms = clock.tick(FPS)


def render_frame_and_update(screen, dots, dt):
    # Clear the screen
    screen.fill("white")

    # Draw a center point
    pygame.draw.circle(screen, "darkgreen", (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 6)

    # Draw all dots
    for i in range(len(dots)):
        x, y, timer = dots[i]

        colour = pygame.Color(min(timer // 2, 255), max(0, 255 - timer // 2), 0)
        pygame.draw.circle(screen, colour, (x, y), 2)

        # Update the timer for next time
        dots[i] = (x, y, timer + dt // 5)

    # Update the screen
    pygame.display.flip()


def read_new_dots(arduino_serial, dots):
    # The format we get from the arduino is "<angle>:<distance>" on each line repeated for every angle.

    # Read a limited number of lines (or else we will wait forever)
    lines = arduino_serial.readlines(5 * 10)
    for line in lines:
        if line != b"" and line.count(b":") == 1:
            # Parse the information, and overwrite the data we had previously.
            angle, distance = line.split(b":", 2)
            x = math.cos(math.radians(int(angle))) * DISTANCE_SCALE * int(distance) + SCREEN_WIDTH / 2
            y = -math.sin(math.radians(int(angle))) * DISTANCE_SCALE * int(distance) + SCREEN_HEIGHT / 2
            dots[int(angle)] = (x, y, 0)


if __name__ == "__main__":
    try:
        main()
        pygame.quit()
    except serial.SerialException as e:
        if e.errno == 2 and e.strerror.startswith("could not open port"):
            print(e.strerror)
            print()
            print("You should try:")
            print()
            print("           1. you will have to change to match the port you used to program the arduino")
            print("              (read-sweep.py line 11?)")
            print()
            print("       OR: 2. close the Ardunino 'serial monitor' tab, because if its open then this")
            print("              program won't be able to openthe serial port.")
        else:
            raise e  # pass along
