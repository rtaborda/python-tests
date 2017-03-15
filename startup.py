from subprocess import Popen

class Startup:
	def __init__(self, paths):
		self.paths = paths

	def Start(self):
		for path in self.paths:
			try:
				Popen([path])
			except:
				print("There was an error openning the program with path: " + path)
				pass

programsPaths = [
	r"C:\Program Files (x86)\Skype\Phone\Skype.exe",					# Skype
	r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",		# Chrome
	r"C:\Users\RTaborda\AppData\Roaming\Spotify\Spotify.exe",			# Spotify
	r"C:\Program Files (x86)\Notepad++\notepad++.exe",					# Notepad++
	r"C:\Program Files (x86)\Microsoft Office\Office16\OUTLOOK.EXE"		# Outlook
]
s = Startup(programsPaths)
s.Start()

