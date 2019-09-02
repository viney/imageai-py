class Prediction(object):
	def __init__(self, prediction, probability):
		self.prediction = prediction
		self.probability = probability

	def info(self):
	    	print(self.prediction + " : ", self.probability)
