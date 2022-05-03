class NameOfClass(): #camel case
	class_attribute = 'value'
	def __init__(self, param1, param2):
		self.param1 = param1
		self.param2 = param2
		# instantiating objects
		# init runs on every instantiation

	def method(self): # each object we instantiate has access to the methods
		# code

	@classmethod #can be called on the class without instantiating it into an object
	def cls_methhod(cls, param1, param2):
		# code

	@staticmethod #can be called on the class without instantiating it into an object
	def stc_method(param1, param2):
		# code