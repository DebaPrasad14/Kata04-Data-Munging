# Part One: Weather Data

def getData(file, headers=None):
	'''@file - input param "weather.dat" '''
	f = open(file)		# open a file to read Data
	headersData = f.readline().split()    # get headers from file as list
	headers = headersData if headers is None else headers
	return [dict(zip(headers, data.split())) for data in f.readlines()]  # return data as list of dictionary with headers as keys


def getMinData(lst, func, minSpread=None):
	'''Get min spread temp from lst by applying ftion 'f' '''
	return (minSpread if lst == []
			else( getMinData(lst[1:], func, lst[0]) if func(lst[0]) is not None
				and (minSpread is None or func(lst[0]) < func(minSpread) )
					else (getMinData(lst[1:], func, minSpread) )
				)
			)


def weatherData():
	'''@lambda function is used to get temp spread for valid rows'''
	file = 'weather.dat'  # file where weather data present
	data = getData(file)
	day	 = getMinData(data, lambda temp: abs(float(temp['MxT'].replace('*','')) - float(temp['MnT'].replace('*','')))
			if 'Dy' in temp else None)
	print('The required day Number is - {}'.format(day['Dy']))


def soccerLeague():
	'''@lambda function to get the difference in "for" and "against" goals'''
	file = 'football.dat'    # file where all football points data present
	data = getData(file, headers=['Nr','Team','P','W','L','D','F','-','A','Pts'])
	team = getMinData(data, lambda t: abs(int(t['F']) - int(t['A'])) if 'Team' in t else None)
	print('Name of the team is - {}'.format(team['Team']))


# start of program
weatherData()
soccerLeague()
