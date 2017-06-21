# Playing around with http requests and threads
# Requires https://github.com/kennethreitz/requests which can be installed with the following command: pip install requests
import requests
import multiprocessing
import threading
import time
import uuid

class Sensor:
	def __init__(self, url, httpMethod, headers, body, expectedStatusCode, maxResponsetime, testInterval):
		self.id = uuid.uuid4()
		self.url = url
		self.httpMethod = httpMethod
		self.headers = headers
		self.body = body
		self.expectedStatusCode = expectedStatusCode
		self.maxResponsetime = maxResponsetime
		self.testInterval = testInterval

class SensorResult:
	def __init__(self, sensorId, response):
		self.sensorId = sensorId
		self.response = response
		
class Monitor:
	def __init__(self):
		self._sensors = []
		manager = multiprocessing.Manager()
		self.resultsQueue = manager.Queue()
	
	def __timedelta_milliseconds(self, td):
		return td.days*86400000 + td.seconds*1000 + td.microseconds/1000

	def __testSensor(self, session, request, sensor):
		while True:
			response = session.send(request)
			# add result to the queue
			self.resultsQueue.put(SensorResult(sensor.id, response))
			# sleep for the interval duration specified for this sensor
			time.sleep(sensor.testInterval)
	
	def addSensor(self, sensor):
		self._sensors.append(sensor)
		
	def startSensors(self):
		# start up the sensor threads
		session = requests.Session()
		for sensor in self._sensors:
			request = requests.Request(sensor.httpMethod, sensor.url, data = sensor.body, headers = sensor.headers)
			preppedRequest = request.prepare()
			
			t = threading.Thread(target = self.__testSensor, args = (session, preppedRequest, sensor))
			t.daemon = True
			t.start()
		
		# block until all tasks are done
		self.resultsQueue.join()
		


# Test Client
def main():
	def consumer(monitor):
		while True:
			# Reading the sensors results responses
			sensorResult = monitor.resultsQueue.get()
			response = sensorResult.response
			
			print(sensorResult.sensorId)
			print(response.url)
			print(response.status_code)
			#print(str(self.__timedelta_milliseconds(response.elapsed)) + ' ms')
			print(response.json())
			print()
		
			monitor.resultsQueue.task_done()
		
	# Testing with Spotify API
	headers = {}
	headers['content-type'] = 'application/json'

	# Using some existing test users
	sensor1 = Sensor('https://api.spotify.com/v1/users/test1', 'GET', headers, None, 200, 30000, 3.0)
	sensor2 = Sensor('https://api.spotify.com/v1/users/test2', 'GET', headers, None, 200, 30000, 7.0)
			
	monitor = Monitor()
	monitor.addSensor(sensor1)
	monitor.addSensor(sensor2)
	monitor.startSensors()
	
	# start consumer thread
	consumer = threading.Thread(target = consumer, args = [monitor])
	consumer.daemon = True
	consumer.start()
	# block until all tasks are done
	consumer.join()

if __name__ == "__main__":
    main()

