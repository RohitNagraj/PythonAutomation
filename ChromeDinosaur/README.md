# Automated chrome dinosaur runner
A simple python script that uses python image library(PIL) and
pyautogui to make the dinosaur jump when an obstacle is in front of it.

# Logic
PIL grabs a small area infront of the dino and and its put in a numpy array
whose sum has a particular value when there is no obstacle in that area, and if
the value changes, the dino jumps.

# Limitations
This currently only works on Windows on a 1366x768 screen with the chrome tab in the
left half of the screen.
