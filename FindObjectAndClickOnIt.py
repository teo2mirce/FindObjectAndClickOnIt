import cv2
import numpy as np

#https://www.journaldev.com/15797/python-time-sleep
import time

#https://www.quora.com/How-can-we-take-screenshots-using-Python-in-Windows
import pyautogui

#https://stackoverflow.com/questions/6537481/python-making-a-beep-noise
import winsound
frequency = 4200  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second

while(1):
	time.sleep(1)

	
	# Take screenshot
	pic = pyautogui.screenshot()
	# Save the image
	pic.save('mario.png') 



	img_rgb = cv2.imread('mario.png')
	template = cv2.imread('mario_coin.png')
	template2 = cv2.imread('coin.png')
	
	
	w, h = template2.shape[:-1]
	res = cv2.matchTemplate(img_rgb, template2, cv2.TM_CCOEFF_NORMED)
	threshold = .7
	loc = np.where(res >= threshold)
	for pt in zip(*loc[::-1]):  # Switch collumns and rows
		#winsound.Beep(frequency, duration)
		print("macar special");
		cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
		#https://pyautogui.readthedocs.io/en/latest/mouse.html
		pyautogui.moveTo(pt[0]+np.random.randint(0,50), pt[1]+ np.random.randint(0,50),duration=0.4,tween=pyautogui.easeInOutQuad)
		for i in range(np.random.randint(35,45)):
			time.sleep(np.random.uniform(0.05,0.2))
			pyautogui.click()
		break
	
	
	w, h = template.shape[:-1]
	res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
	threshold = .5
	loc = np.where(res >= threshold)
	for pt in zip(*loc[::-1]):  # Switch collumns and rows
		#winsound.Beep(frequency, duration)
		print("macar");
		cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
		#https://pyautogui.readthedocs.io/en/latest/mouse.html
		pyautogui.moveTo(pt[0]-30+np.random.randint(0,20), pt[1]+100 - np.random.randint(0,20),duration=0.4,tween=pyautogui.easeInOutQuad)
		for i in range(np.random.randint(20,30)):
			time.sleep(np.random.uniform(0.05,0.2))
			pyautogui.click()
		#if np.random.randint(0,3)==0 : 
		if( True and img_rgb[680][1000][1] != img_rgb[680][1000][2]): #https://stackoverflow.com/questions/12187354/get-rgb-value-opencv-python
			pyautogui.moveTo(950+np.random.randint(0,200),625+np.random.randint(0,80),duration=0.4,tween=pyautogui.easeInOutQuad)
			pyautogui.click()
		break

	#cv2.imwrite('result.png', img_rgb)
