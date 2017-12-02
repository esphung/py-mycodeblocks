''' ____    ____    ____    __  __  ______  __       __  __  ____    ____
/\  _`\ /\  _`\ /\  _`\ /\ \/\ \/\  _  \/\ \     /\ \/\ \/\  _`\ /\  _`\
\ \ \L\ \ \ \L\_\ \ \L\_\ \ \ \ \ \ \L\ \ \ \    \ \ \ \ \ \ \L\_\ \,\L\_\
 \ \ ,  /\ \  _\L\ \ \L_L\ \ \ \ \ \  __ \ \ \  __\ \ \ \ \ \  _\L\/_\__ \
  \ \ \\ \\ \ \L\ \ \ \/, \ \ \_/ \ \ \/\ \ \ \L\ \\ \ \_\ \ \ \L\ \/\ \L\ \
   \ \_\ \_\ \____/\ \____/\ `\___/\ \_\ \_\ \____/ \ \_____\ \____/\ `\____\
    \/_/\/ /\/___/  \/___/  `\/__/  \/_/\/_/\/___/   \/_____/\/___/  \/_____/
'''

# REQUIRED LIBRARY
import re

#============================================================

def findValue(key,value_list):

	# filter out value by patter
	for item in value_list:
		value = item.lower()
		pattern = re.compile(key)
		match = pattern.match(value)
		if match:
			return item

def getDataSet(data):

	# matches
	fullname = r'^[a-z ,.-]+$'
	date = r'(0[1-9]|1[012])[- \/.](0[1-9]|[12][0-9]|3[01])[- \/.](19|20)\d\d'
	numeric = r'[0-9]{7}'
	email = r'[^@]+@[^@]+\.[^@]+'

	keepGoing = True
	while keepGoing:

		i = 0
		data_set = {}
		# match if name
		if findValue(fullname,data):
			data_set['fullname'] = findValue(fullname,data)
			data.remove(findValue(fullname,data))

		# match if date
		if findValue(date,data):
			data_set['date'] = findValue(date,data)
			data.remove(findValue(date,data))

		# match if booking id
		if findValue(numeric,data):
			data_set['numeric'] = findValue(numeric,data)
			data.remove(findValue(numeric,data))

		# match if email
		if findValue(email,data):
			data_set['email'] = findValue(email,data)
			data.remove(findValue(email,data))

		return data_set
		keepGoing = False


def getMatchedDataFromLinks(keys,raw_values):

	collection = []
	record = {}
	limit = (len(raw_values) - len(keys))
	i = 0

	keepGoing = True
	while keepGoing:
		#print('Remaining {}: {}'.format(len(raw_values),raw_values))

		if (len(raw_values)) <= 0:
			keepGoing = False
		else:
			data = getDataSet(raw_values)
			record['record_{}'.format(i)] = data
			collection.append(data)
			i += 1
			#keepGoing = False

	return collection

#============================================================

# FAKE RANDOW VALUES FROM BODY OF TEXT
test_values = [
  "JobS, Steven S",
  "1117468",
  "000000634681",
  "09/30/2011",
  "04/27/1978",
  "Gates, Bill W",
  "1230392",
  "000000234181",
  "iam@anemail.com",
  "07/13/2013",
  "BROWN, JAMES WILLIAM",
  "fuck you"
]

# KEYS OF YOUR CHOOSING TO MATCH THE DATA
keyLabels = [ 'numeric', 'fullname', 'date', 'email','integer' ]

#============================================================


test = getMatchedDataFromLinks(keyLabels,test_values)
print(test)