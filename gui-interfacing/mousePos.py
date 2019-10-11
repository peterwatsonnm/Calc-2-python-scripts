#script to display mouse cursor's current position and the color of the pixel
#used to write scripts for clicking things
import pyautogui
print('Press Ctrl-C to quit')
while True:
    x,y = pyautogui.position()
    #create an auto updating string with right justified values
    pixelColor = pyautogui.screenshot().getpixel((x, y))
    positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
    positionStr += ' RGB: ' +  (str(pixelColor[0]).rjust(3))
    positionStr += ', ' + (str(pixelColor[1]).rjust(3))
    positionStr += ', ' + (str(pixelColor[2]).rjust(3))
    print(positionStr, end='')     #need end='' character to not print endl character
    #delete previous line and print new line
    print('\b' * len(positionStr), end='', flush=True)
