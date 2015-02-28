''' writing CSV format '''
arg_list = ["Hello","World","I","am","a","CSV","line!",'in a ...','CSV','file','...',' hopefully :(' , "sdlkjdfs","3242112",'234inoMakeSEnSe!','01920$@^#%$^%*&()(*','[H-h][e][y][!]|[n][0],[I][a][m][r][e][G][e][x][e][d]'];				#	arg to write
file = "data.csv";										#	file to read/write
f = open(file,mode='a');								# set file mode
f.write(str(arg_list).lstrip('[').replace('  ','').rstrip(']').replace(',\n','').rstrip(','))			#	looong string strip down
					# output function
#f.write(",")
f.write("\n");													# newline
f.truncate();														#	remove everything after entry (optional)
f.close();															# close file