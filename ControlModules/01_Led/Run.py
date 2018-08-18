import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def Main():
	try:
		print("Movement Test Started...")
		while 1:
			#Prender Led
			time.sleep(3)
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc()
	finally:  
		GPIO.cleanup() 		

Main()