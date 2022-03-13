import pyautogui, time

position = pyautogui.position()

kata = "HALOOOOOO"

for x in range(5):
    pyautogui.click(position.x, position.y)
    pyautogui.typewrite(kata)
    print(kata)
    time.sleep(0.5)
    pyautogui.typewrite(["enter"])
  
