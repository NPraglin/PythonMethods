import pyautogui

# return screen resolution
print(pyautogui.size())

# return mouse position
print(pyautogui.position())

# move mouse to x,y with optional duration
pyautogui.moveTo(1000,1000, duration=1.5)

# move mous relative to current location with optional duration
pyautogui.moveRel(10,10, duration=2.0)

# mouse click
# pyautogui.click()
# pyautogui.middleClick()
# pyautogui.doubleClick()

# you can combine drags to make a macro
# pyautogui.dragRel()
pyautogui.click()

# type with keyboard via python
pyautogui.typewrite('Hello world!')

# screen shotsHello world!Hello world!
pyautogui.screenshot('C:\\Users\\16616\\Pictures\\screenshotexample.png')