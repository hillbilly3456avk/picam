import picamera
from time import sleep
import time
import datetime
import logging

from astral import LocationInfo
from astral.sun import sun

logging.basicConfig(filename="/home/pi/picam/webcamLogger.log", format='%(asctime)s: %(levelname)s: %(message)s', level=logging.WARNING)

localTime=time.localtime()

city = LocationInfo("Reichenbach", "Switzerland", "Europe/Zurich", 46.37, 7.41)
s = sun(city.observer, date=datetime.date.today())
logging.debug(f'Dawn:    {s["dawn"]}')
logging.debug(f'Sunrise: {s["sunrise"]}')
logging.debug(f'Noon:    {s["noon"]}')
logging.debug(f'Sunset:  {s["sunset"]}')
logging.debug(f'Dusk:    {s["dusk"]}')

if (localTime.tm_hour > s["dawn"].hour) and \
	(localTime.tm_hour < s["dusk"].hour):

	imageName=str(localTime.tm_year) + "-" + str(localTime.tm_mon) + "-" + str(localTime.tm_mday) + "_" \
		+ str(localTime.tm_hour) + ":" + str(localTime.tm_min) + "_WebCamFr34.jpeg"

	logging.info("we are between dusk and dawn")
	logging.info("taking a pic named: " + imageName)
	#create object for PiCamera class
	camera = picamera.PiCamera()
	#set resolution
	camera.resolution = (1024, 768)
	camera.brightness = 60
	#camera.start_preview()
	#add text on image
	#camera.annotate_text = 'Hi Pi User'
	#sleep(5)
	#store image
	camera.capture(imageName)
	#camera.stop_preview()
else:
	logging.warning("Es isch dunkel wi ire chue es git kes föteli")



