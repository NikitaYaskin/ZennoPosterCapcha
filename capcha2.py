import pyautogui, time, datetime, logging

def currentDateTime():
	'''Informathon about date time'''
	unix = int(time.time())
	now = str(datetime.datetime.fromtimestamp(
		unix).strftime('%d-%m-%y %H:%M:%S'))
	return now

logging.basicConfig(filename='capcha.log',level=logging.DEBUG)
logging.info('Завантаження програми \n{}'.format(currentDateTime()))

numCapcha = 0
faildCapcha = 0
dateInfo = []

windowLocation = (670, 380, 330, 270) #Записати місцезнаходження вікна. Чим більш точно визначено вікно тим швидше буде працювати програма

while True:
    info = {}
    data = {1: 'img/1.png', 2: 'img/2.png', 3: 'img/3.png', 4: 'img/4.png',
            5: 'img/5.png', 6: 'img/6.png', 7: 'img/7.png', 8: 'img/8.png', 9: 'img/9.png'}

    if pyautogui.locateOnScreen('img/title.png', region=windowLocation, grayscale=True):
        for el in data:
            if pyautogui.locateOnScreen(data[el], region=windowLocation, grayscale=True):
                info[el] = pyautogui.locateCenterOnScreen(data[el], region=windowLocation, grayscale=True)
                logging.info('Знайдено цифру {0}'.format(info[el]))
                
        sortedInfo = sorted(info)
        
        if sortedInfo != []:
        	pyautogui.moveTo(info[sortedInfo[0]][0], info[sortedInfo[0]][1])

        pyautogui.mouseDown()
        
        logging.info('Затиснута ліва клавіша миші {0}'.format(currentDateTime()))

        for key in sorted(info):
            pyautogui.moveTo(x=info[key][0], y=info[key][1])
            logging.info('Курсор рухається до точки {0}'.format(key))
            
        pyautogui.mouseUp()
        logging.info('Відпущена ліва клавіша миші {0}'.format(currentDateTime()))
        
        pyautogui.click(828, 621) #click enter
        logging.info('Натиснутий Enter {0}'.format(currentDateTime()))

        time.sleep(3)

        if pyautogui.locateOnScreen('img/title.png', region=windowLocation, grayscale=True):
                faildCapcha += 1
                logging.warning('Капча {0} не введена'.format(faildCapcha))
                #faildCapchaName = 'faildCapcha/' + str(currentDateTime()) + '.png'
                #pyautogui.screenshot(faildCapchaName, region=windowLocation)
                continue
        else:
        	numCapcha += 1
        	logging.info('Натиснутий Enter. \nВведено {0} капч. {1}'.format(numCapcha,currentDateTime()))
        	time.sleep(60)
        	continue

'''	Перевірка на те чи є 4 елемента в словнику.
	Перевірка на те чи зник титул після введення капчі.+
	
'''
