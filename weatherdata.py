# Part One: Weather Data

def getData(file):
	'''@file - input param "weather.dat" '''
	f = open(file)		# open a file to read Data
	headers = f.readline().split()    # get headers from file as list
	return [dict(zip(headers, data.split())) for data in f.readlines()]  # return data as list of dictionary with headers as keys


def weatherData():
	file = 'weather.dat'  # file in which weather data present
	data = getData(file)
	print(data)

weatherData()
