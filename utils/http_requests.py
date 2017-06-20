# Playing around with http requests and threads
# Requires https://github.com/kennethreitz/requests which can be installed with the following command: pip install requests
import requests
import queue
import threading
import time

class Sensor:
	def __init__(self, url, httpMethod, headers, body, expectedStatusCode, maxResponsetime, testInterval):
		self.url = url
		self.httpMethod = httpMethod
		self.headers = headers
		self.body = body
		self.expectedStatusCode = expectedStatusCode
		self.maxResponsetime = maxResponsetime
		self.testInterval = testInterval
		
class Monitor:
	def __init__(self):
		self.sensors = []
		self.q = queue.Queue()
	
	def __timedelta_milliseconds(self, td):
		return td.days*86400000 + td.seconds*1000 + td.microseconds/1000

	def __testSensor(self, session, request, interval):
		while True:
			response = session.send(request)
			self.q.put(response)
			time.sleep(interval)
	
	def __consumer(self):
		while True:
			# print responses
			response = self.q.get()
			
			print(response.url)
			print(response.status_code)
			print(str(self.__timedelta_milliseconds(response.elapsed)) + ' ms')
			print(response.json())
			print()
		
			self.q.task_done()
	
	def addSensor(self, sensor):
		self.sensors.append(sensor)
		
	def start(self):
		# start consumer thread
		consumer = threading.Thread(target = self.__consumer)
		consumer.daemon = True
		consumer.start()
		
		# start up the sensor threads
		session = requests.Session()
		for sensor in self.sensors:
			request = requests.Request(sensor.httpMethod, sensor.url, data = sensor.body, headers = sensor.headers)
			preppedRequest = request.prepare()
			
			t = threading.Thread(target = self.__testSensor, args = (session, preppedRequest, sensor.testInterval))
			t.daemon = True
			t.start()
		
		# block until all tasks are done
		self.q.join()
		consumer.join()
		

# Testing with Spotify API
headers = {}
headers['content-type'] = 'application/json'

# Using some existing test users
sensor1 = Sensor('https://api.spotify.com/v1/users/test1', 'GET', headers, None, 200, 30000, 3.0)
sensor2 = Sensor('https://api.spotify.com/v1/users/test2', 'GET', headers, None, 200, 30000, 7.0)

monitor = Monitor()
monitor.addSensor(sensor1)
monitor.addSensor(sensor2)
monitor.start()

