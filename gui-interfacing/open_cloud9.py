#script to automatically open AWS's Cloud9 IDE
#Written by Peter Watson
#works for screens of 1920x1080
import pyautogui
import time
import subprocess

print ('opening google chrome')
subprocess.Popen(['/usr/bin/google-chrome-stable'])
print('password must be autofilled')
time.sleep(2)
#move to web address bar
pyautogui.moveTo(413, 78, duration=0.25)
pyautogui.click()
pyautogui.typewrite('https://www.awseducate.com/signin/SiteLogin?ec=302&startURL=%2Fstudent%2Fs%2Fawssite%3Fsc_content%3DOther_ln_ot%26sc_outcome%3Dother%26sc_medium%3Dem_1218%26mkt_tok%3DeyJpIjoiWVdVNE5HTmhZbVUwWWpnMSIsInQiOiJcLzVlcXgwSTh6cHdrZUIzWGFzM2VpQ05xNmZ2QzZuN3hVMTdqTFJEMFlSY0VxOVBTZUZFSlVkWFFCM1RRSWZiOUh2ejVKZzEzYzU2NU1rR05zMXIzZk8xMVAwZzU4WUhyeSs5MGNBbVlyZkJETEVMeUw5Wjd4ZXF0TDhxendVb2IifQ%253D%253D%26sc_channel%3Dem%26sc_detail%3Dawseducatewelcomeemail1%26sc_country%3Dmult%26trk%3Dem_1218%26sc_campaign%3DGLOBAL_LN_aws-educate-welcome-series_20180312%26sc_geo%3Dmult')
pyautogui.press('enter')
time.sleep(5)

#move to login button
pyautogui.moveTo(857, 561, duration=0.25)
pyautogui.click()
#move to my classrooms button
time.sleep(5)
pyautogui.moveTo(709, 145, duration=0.25)
pyautogui.click()
#move to "go to classroom" button
time.sleep(2.5)
pyautogui.moveTo(1232, 603, duration=0.25)
pyautogui.click()
#move to "continue" button
time.sleep(.25)
pyautogui.moveTo(928, 523, duration=0.25)
pyautogui.click()
#move to aws console button
time.sleep(6.5)
pyautogui.moveTo(936, 448, duration=0.25)
pyautogui.click()
#move to search box, type in 'cloud9'
time.sleep(5.25)
pyautogui.moveTo(298, 406, duration=0.25)
pyautogui.click()
pyautogui.typewrite('cloud9')
time.sleep(.25)
pyautogui.moveTo(298, 441, duration=0.25)
pyautogui.click()
#open IDE button
time.sleep(3)
pyautogui.moveTo(786, 582, duration=0.25)
pyautogui.click()
