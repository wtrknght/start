import requests
import keyboard
import time
keyboard.add_hotkey('esc', quit, args = ())
url = 'https://www.keepretro.com/products/miyoo-mini?variant=41343598985378'
while True:
	for i in range(12):
		for i in range(60):
			for i in range(60):
				time.sleep(1)
	r = requests.get(url)
	rr = r.text
	if "sold out" in rr:
		print('out of stock')
	else:
		print('check it')
