''' simple file writing '''
argument = "Hello WOrld";		#	arg to write
file = "hello.txt";				#	file to read/write
f = open(file,mode='a');		# set file mode
f.write(argument); 					# output function
f.write("\n");							# newline
f.truncate();								#	remove everything after entry (optional)
f.close();									# close file

'''simple file reading'''
file = "hello.txt";							# define file
file = open(file,mode='r');				# file object
data = file.read();								# read file

print('wrote file')