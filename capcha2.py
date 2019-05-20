import pyautogui, time, datetime, logging, os

logging.basicConfig(filename='capcha.log',level=logging.DEBUG)

def currentDateTime():
	'''Informathon about date time'''
	unix = int(time.time())
	now = str(datetime.datetime.fromtimestamp(
		unix).strftime('%d-%m-%y %H:%M:%S'))
	return now


def findingImage():
        data = {}
        images = os.listdir("img/")
        for image in images:
            res = image.split('.')
            key = int(res[0])
            data[res[0]] = str('img/') + image
        logging.info('Всі файли у папці img \n{}'.format(data))
        return data

numCapcha = 0
faildCapcha = 0
dateInfo = []
info = {}
data = findingImage()

logging.info('Завантаження програми \n{}'.format(currentDateTime()))

windowLocation = (670, 380, 330, 270) #Записати місцезнаходження вікна. Чим більш точно визначено вікно тим швидше буде працювати програма
enter = (828, 621) # Місцезнаходження клавіші ентер

while True:
    if pyautogui.locateOnScreen(data['title'], region=windowLocation, grayscale=True):
        for el in data:
            if pyautogui.locateOnScreen(data[el], region=windowLocation, grayscale=True):
                info[el] = pyautogui.locateCenterOnScreen(data[el], region=windowLocation, grayscale=True)
                logging.info('Знайдено цифру {0}'.format(info[el]))
                
        sortedInfo = sorted(info)
             
        if len(sortedInfo) >= 0 and len(sortedInfo) <= 3:
                pyautogui.alert('Недoстатня кількість цифр')
                break

        elif len(sortedInfo) != []:
            pyautogui.moveTo(info[sortedInfo[0]][0], info[sortedInfo[0]][1]) 	
        
        pyautogui.mouseDown()
        
        logging.info('Затиснута ліва клавіша миші {0}'.format(currentDateTime()))

        for key in sorted(info):
            pyautogui.moveTo(x=info[key][0], y=info[key][1])
            logging.info('Курсор рухається до точки {0}'.format(key))
            
        pyautogui.mouseUp()
        logging.info('Відпущена ліва клавіша миші')
        
        pyautogui.click(enter)
        logging.info('Натиснутий Enter')

        time.sleep(2)

        if pyautogui.locateOnScreen(data['title'], region=windowLocation, grayscale=True):
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

