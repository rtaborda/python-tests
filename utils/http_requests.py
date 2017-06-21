# Playing around with http requests and threads
# Requires https://github.com/kennethreitz/requests which can be installed with the following command: pip install requests
import requests
import multiprocessing
import threading
import time
import uuid

# This class represents a sensor
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

# This class represents a sensor result, every time a sensor is tested a SensorResult is created
class SensorResult:
	def __init__(self, sensorId, success, elapsedMilliseconds):
		self.sensorId = sensorId
		self.success = success
		self.elapsedMilliseconds = elapsedMilliseconds

# This class handles the sensors, performs the tests on the sensor and generates the results
class Monitor:
	def __init__(self):
		self._sensors = []
		self._running = False
		manager = multiprocessing.Manager()
		self.resultsQueue = manager.Queue()
	
	def __timedelta_milliseconds(self, td):
		return td.days*86400000 + td.seconds*1000 + td.microseconds/1000

	def __buildSensorResult(self, sensor, response):
		elapsedMilliseconds = self.__timedelta_milliseconds(response.elapsed)
		success = response.status_code == sensor.expectedStatusCode and elapsedMilliseconds <= sensor.maxResponsetime
	
		return SensorResult(sensor.id, success, elapsedMilliseconds)
		
	def __testSensor(self, session, request, sensor):
		while self._running:
			response = session.send(request)
			
			# Add result to the queue
			result = self.__buildSensorResult(sensor, response)
			self.resultsQueue.put(result)
			
			# Sleep for the interval duration specified for this sensor
			time.sleep(sensor.testInterval)
	
	def addSensor(self, sensor):
		self._sensors.append(sensor)
		
	def startSensors(self):
		self._running = True
		
		# Start up the sensor threads
		session = requests.Session()
		for sensor in self._sensors:
			request = requests.Request(sensor.httpMethod, sensor.url, data = sensor.body, headers = sensor.headers)
			preppedRequest = request.prepare()
			
			thread = threading.Thread(target = self.__testSensor, args = (session, preppedRequest, sensor))
			thread.daemon = True
			thread.start()
		
		# Block until all tasks are done
		self.resultsQueue.join()
	
	def isRunning(self):
		return self._running;
	
	def stopSensors(self):
		self._running = False


		

# Test Client
def main():
	def consumer(monitor):
		while monitor.isRunning:
			# Reading the sensors results responses
			sensorResult = monitor.resultsQueue.get()
			print(sensorResult.sensorId)
			print('success' if sensorResult.success else 'failed')
			print(str(sensorResult.elapsedMilliseconds) + ' ms')
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
	
	# Start consumer thread
	consumer = threading.Thread(target = consumer, args = [monitor])
	consumer.daemon = True
	consumer.start()
	
	# Stop the sensors after 60 seconds
	time.sleep(60.0)
	monitor.stopSensors()

if __name__ == "__main__":
    main()

