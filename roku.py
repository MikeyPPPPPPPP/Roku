
import requests
class roku:
	def __init__(self, ip):
		self.ip = ip
		self.url = ''
	def _build_url(self,text):
		self.url = 'http://'+self.ip+':8060/keypress/'+text

	def power(self):
		build_url('Power')
		headers = {'User-Agent': "RoByte/2.1.8.2 CFNetwork/1220.1 Darwin/20.3.0"}
		response = requests.post(self.url, headers=headers)

	def rev(self):
		build_url('Rev')
		headers = {'User-Agent': "RoByte/2.1.8.2 CFNetwork/1220.1 Darwin/20.3.0"}
		response = requests.post(self.url, headers=headers)
	def fwd(self):
		build_url('Fwd')
		headers = {'User-Agent': "RoByte/2.1.8.2 CFNetwork/1220.1 Darwin/20.3.0"}
		response = requests.post(self.url, headers=headers)

	def info(self):
		build_url('Info')
		headers = {'User-Agent': "RoByte/2.1.8.2 CFNetwork/1220.1 Darwin/20.3.0"}
		response = requests.post(self.url, headers=headers)
	def replay(self):
		build_url('InstantReplay')
		headers = {'User-Agent': "RoByte/2.1.8.2 CFNetwork/1220.1 Darwin/20.3.0"}
		response = requests.post(self.url, headers=headers)
	def home(self):
		build_url('Home')
		headers = {'User-Agent': "RoByte/2.1.8.2 CFNetwork/1220.1 Darwin/20.3.0"}
		response = requests.post(self.url, headers=headers)

#ppak = roku("192.168.86.41")
#ppak.prank()
'''	
power = 'http://192.168.86.41:8060/keypress/Power'


Info
Fwd
Rev
Play
Back
down
up
left
right
InstantReplay
Home

Select

user-agent = "RoByte/2.1.8.2 CFNetwork/1220.1 Darwin/20.3.0"
'''
