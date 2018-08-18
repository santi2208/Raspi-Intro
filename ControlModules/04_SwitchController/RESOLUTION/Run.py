import sys
sys.path.append('../../../Services/UDPService/')
from UDPService import *
from SwitchRelayActions import *
from CommandConstants import GetActionName
from CommandConstants import GetGpioPort

class MainSwitchController(object):
	def __init__(self, udpService = None):
		if udpService:
			self.udpService = udpService
		else:	
			self.udpService = UDPService()

	def RunSwitchService(self, portNumber, host = None):
		try:	
			print("Switch Controller running...")
			while 1:
				# Receive UDP Params
				udpRawAction = self.udpService.ListenToPortOnce(portNumber, host)
				print(udpRawAction)
				actionName = udpRawAction.split('#')[0]
				switchName = udpRawAction.split('#')[1]
				functionName = GetActionName(actionName)
				gpioNumber = GetGpioPort(switchName)
				if(functionName is not None and gpioNumber is not None):
					gpioNumber = int(gpioNumber) 
					# Execute Action
					relayActions = SwitchRelayActions()
					getattr(relayActions,functionName)(gpioNumber)
					print functionName
		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			traceback.print_exc()
		finally:  
			GPIO.cleanup() 

if __name__ == '__main__':
	port = int(sys.argv[1])
	mainSwitchController = MainSwitchController()
	mainSwitchController.RunSwitchService(port, sys.argv[2] if len(sys.argv) > 1 else None)