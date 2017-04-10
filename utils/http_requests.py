# Playing around with http requests and threads
# Requires https://github.com/kennethreitz/requests which can be installed with the following command: pip install requests
import requests
import queue
import threading
#import time

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

	def __testSensor(self, session, request):
		response = session.send(request)
		self.q.put(response)
		
	def addSensor(self, sensor):
		self.sensors.append(sensor)
		
	def start(self):
		preppedRequests = []
		
		# prepare the requests
		for sensor in self.sensors:
			request = requests.Request(sensor.httpMethod, sensor.url, data = sensor.body, headers = sensor.headers)
			preppedRequest = request.prepare()
			preppedRequests.append(preppedRequest)
		
		session = requests.Session()		
		
		for req in preppedRequests:
			t = threading.Thread(target = self.__testSensor, args = (session, req))
			t.daemon = True
			t.start()
		
		# print responses
		response = self.q.get()
		
		print(response.status_code)
		print(str(self.__timedelta_milliseconds(response.elapsed)) + ' ms')
		print(response.json())
		
		self.q.task_done()
			
		# block until all tasks are done
		self.q.join()
		

# Testing with Spotify API
headers = {}
headers['content-type'] = 'application/json'

# Using some existing test users
sensor1 = Sensor('https://api.spotify.com/v1/users/test1', 'GET', headers, None, 200, 30000, 60000)
sensor2 = Sensor('https://api.spotify.com/v1/users/test2', 'GET', headers, None, 200, 30000, 60000)

monitor = Monitor()
monitor.addSensor(sensor1)
monitor.addSensor(sensor2)
monitor.start()

