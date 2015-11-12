def forecast(days):
	d = {"rain": 0, 'sunshine': 0, 'snow': 0}
	tomorrow = ''
	li = []
	for item in days:
		if item == 'rain':
			d['rain'] += 1
		if item == 'sunshine':
			d['sunshine'] += 1
		if item == 'snow':
			d['snow'] += 1
	for values in d.values():
		li.append(values)
	li.sort()
	print(li)
	if li[2] > li[1]:
		for key, value in d.items():
			if value == li[2]:
				tomorrow = key
	if li[2] == li[1]:
		if li[2] == li[0]:
			tomorrow = days[len(days)-1]
		else:
			for key, value in d.items():
				if value == li[0]:
					tomorrow = key
	return tomorrow

print(forecast(["rain", "rain", "sunshine", "sunshine"]))