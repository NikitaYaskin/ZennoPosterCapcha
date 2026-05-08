import pyautogui, time, datetime, logging, os, pdb

logging.basicConfig(filename='capcha.log',level=logging.DEBUG)

def currentDateTime():
	'''Informathon about date time'''
	unix = int(time.time())
	now = str(datetime.datetime.fromtimestamp(
		unix).strftime('%d-%m-%y %H:%M:%S'))
	return now

def convertIfInteger(string):
        try:
                return int(string)
        except ValueError:
                return string

def leftOnlyDigits(digits):
        try:
                return int(digits)
        except ValueError:
                pass

def findingImage():
        data = {}
        images = os.listdir("img/")
        for image in images:
            res = image.split('.')
            key = convertIfInteger(res[0])
            data[key] = str('img/') + image
        logging.info('All files in the img folder\n{}'.format(data.values()))
        return data

def formatAllKeys(data):
        result = list()
        for item in data:
                if leftOnlyDigits(item) != None:
                        result.append(leftOnlyDigits(item))
        return result

numCapcha = 0
numFaildCapchas = 0
data = findingImage()
digitsOnScreen = formatAllKeys(data)

logging.info('Downloading the program\n {}'.format(currentDateTime()))

windowLocation = (670, 380, 330, 270) 
digitLocation = (691, 457, 300, 146) # Placing numbers in the window.
enter = (828, 621) # Location of the enter key

def faildCapcha(info):
        faildCapchaName = 'faildCapcha/'+ str(info) + '.png'
        pyautogui.screenshot(faildCapchaName, region=windowLocation)
        logging.warning('Captcha not entered {}'.format(currentDateTime()))

while True:
        dateInfo = []
        info = {}
        if pyautogui.locateOnScreen(data['title'], region=windowLocation, grayscale=True):
                for digit in digitsOnScreen:
                        if pyautogui.locateOnScreen(data[digit], region=digitLocation, grayscale=True):
                                info[digit] = pyautogui.locateCenterOnScreen(data[digit], region=digitLocation, grayscale=True)
                                logging.info('Number found {0}'.format(info[digit]))

                sortedInfo = sorted(info)

                if len(sortedInfo) >= 0 and len(sortedInfo) <= 3 or len(sortedInfo) > 4:
                        pyautogui.alert('Incorrect number of digits \n {}'.format(sortedInfo))
                        logging.warning('Incorrect number of digits')
                        logging.warning('{}'.format(sortedInfo))
                        faildCapcha(sortedInfo)
                        continue
                elif len(sortedInfo) != []:
                        pyautogui.moveTo(info[sortedInfo[0]][0], info[sortedInfo[0]][1])

                pyautogui.mouseDown()

                logging.info('Left mouse button pressed {0}'.format(currentDateTime()))

                for key in sorted(info):
                        pyautogui.moveTo(x=info[key][0], y=info[key][1])
                        logging.info('The cursor moves to the point {0}'.format(key))

                pyautogui.mouseUp()
                
                logging.info('Left mouse button released')
                
                capcha = 'success/' + str(datetime.date.today()) + ' ' + str(info.keys()) + '.png'
                pyautogui.screenshot(capcha, region=windowLocation)
                
                logging.info('Screenshot taken')
                
                pyautogui.click(enter)
                logging.info('Pressed Enter')
                time.sleep(1)

                if pyautogui.locateOnScreen(data['title'], region=windowLocation, grayscale=True):
                        faildCapcha(sortedInfo)
                        continue
                else:
                        numCapcha += 1
                        logging.info('Pressed Enter. \nEntered {0} captchas. {1}'.format(numCapcha, currentDateTime()))
                        time.sleep(30)
                        continue
