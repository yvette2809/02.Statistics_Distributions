class Distribution:
	
	def __init__(self, mu=0, sigma=1):
		
		"""
		Generic distribution class for calculating and visualizing a probability distribution.
		
		Attributes:
		mean (float): the mean of given dataset
		stdev (float): the standard deviation of given dataset
		data (list): stores the dataset
		"""

		self.mean = mu
		self.stdev = sigma
		self.data = []
