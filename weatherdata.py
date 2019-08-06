# Part One: Weather Data

def getData(file):
	'''@file - input param "weather.dat" '''
	f = open(file)		# open a file to read Data
	headers = f.readline().split()    # get headers from file as list
	return [dict(zip(headers, data.split())) for data in f.readlines()]  # return data as list of dictionary with headers as keys

def getMinTempSpread(lst, func, minSpread=None):
	'''Get min spread temp from lst by applying ftion 'f' '''
	return (minSpread if lst == []
			else( getMinTempSpread(lst[1:], func, lst[0]) if func(lst[0]) is not None
				and (minSpread is None or func(lst[0]) < func(minSpread) )
					else (getMinTempSpread(lst[1:], func, minSpread) )
				)
			)


def weatherData():
	'''lambda f is used to get temp spread for valid rows'''
	file = 'weather.dat'  # file where weather data present
	data = getData(file)
	day	 = getMinTempSpread(data, lambda temp: abs(float(temp['MxT'].replace('*','')) - float(temp['MnT'].replace('*','')))
			if 'Dy' in temp else None)
	print('The required day is - {}'.format(day['Dy']))

# start of program
weatherData()
