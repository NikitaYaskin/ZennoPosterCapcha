import pyautogui

while True:
	info = {}
	if pyautogui.locateOnScreen('img/title.png'):
		if pyautogui.locateOnScreen('img/1.png'):
			info[1] = pyautogui.locateCenterOnScreen('img/1.png')
			print(info)
		if pyautogui.locateOnScreen('img/2.png'):
			info[2] = pyautogui.locateCenterOnScreen('img/2.png')
			print(info)
		if pyautogui.locateOnScreen('img/3.png'):
			info[3] = pyautogui.locateCenterOnScreen('img/3.png')
			print(info)
		if pyautogui.locateOnScreen('img/4.png'):
			info[4] = pyautogui.locateCenterOnScreen('img/4.png')
			print(info)
		if pyautogui.locateOnScreen('img/5.png'):
			info[5] = pyautogui.locateCenterOnScreen('img/5.png')
			print(info)
		if pyautogui.locateOnScreen('img/6.png'):
			info[6] = pyautogui.locateCenterOnScreen('img/6.png')
			print(info)
		if pyautogui.locateOnScreen('img/7.png'):
			info[7] = pyautogui.locateCenterOnScreen('img/7.png')
			print(info)
		if pyautogui.locateOnScreen('img/8.png'):
			info[8] = pyautogui.locateCenterOnScreen('img/8.png')
			print(info)
		if pyautogui.locateOnScreen('img/9.png'):
			info[9] = pyautogui.locateCenterOnScreen('img/9.png')
			print(info)

		sortedInfo = sorted(info)
		pyautogui.click(info[sortedInfo[0]][0],info[sortedInfo[0]][1],interval=1)
		print(info[sortedInfo[0]][0],info[sortedInfo[0]][1])
		print(pyautogui.position())

	for key in sorted(info):
		print(info[key][0],  info[key][1])
		pyautogui.dragRel(info[key][0],  info[key][1], 1, button='left')
		print(pyautogui.position())

	pyautogui.click(pyautogui.locateOnScreen('img/enter.png'))
