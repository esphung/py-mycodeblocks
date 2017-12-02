# format valid json data
data = { 'hello' : 'world' }
data = str(data)
data = data.replace("\\","")
data = data.replace('\n','')
data = data.replace('\'','"')

# write the data
with open('data{}.json'.format(""), 'w') as f:
	f.write(data + '')

print('Wrote json file')