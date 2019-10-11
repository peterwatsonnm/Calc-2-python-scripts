#script to clock in or out
#written by Peter Watson
import pyautogui
import time



print ('Enter 1 to clock in, 2 to clock out')
variable = input()
if variable == '1':
    #move to id number box
    pyautogui.moveTo(648, 373, duration=0.25)
    pyautogui.click()
    pyautogui.typewrite('108444')       #login number
    #click clock in
    pyautogui.moveTo(652,426, duration=0.25)
    pyautogui.click()
    #click confirm
    pyautogui.moveTo(1010, 739, duration=0.25)
    while (pyautogui.pixelMatchesColor(1010, 739, (51, 98, 161))) != True:
        time.sleep(.1)
    print('confirmed')
    pyautogui.click()
elif variable == '2':
    #move to id number box
    pyautogui.moveTo(648, 373, duration=0.25)
    pyautogui.click()
    pyautogui.typewrite('108444')       #login number
    #click clock in
    pyautogui.moveTo(841,425, duration=0.25)
    pyautogui.click()
    #click confirm
    pyautogui.moveTo(1010, 739, duration=0.25)
    while (pyautogui.pixelMatchesColor(1010, 739, (51, 98, 161))) != True:
        time.sleep(.1)
    print('confirmed')
    pyautogui.click()
else:
    print ('invalid input')
