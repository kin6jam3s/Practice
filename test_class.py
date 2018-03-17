class router(object):
	def __init__(self, vendor, model):
		self.vendor = vendor
		self.model = model	

	def assigninterfaceCount(self):
		if(self.vendor == 'Cisco' and self.model == '9516'):
			self.num10GInterface = 2304
		elif(self.vendor == 'Cisco' and self.model == '9508'):
			self.num10GInterface = 1024
		

