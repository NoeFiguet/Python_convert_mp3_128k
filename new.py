#Define the function

#########################################
#
#  Function name : remove
#  
#  Description : 
#
#  Parameters :
#
#########################################
def remove(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        print "file {} is not a file or dir.".format(path)


#########################################
#
#  Function name : print_and_wait
#  
#  Description : 
#
#  Parameters :
#
#########################################
def print_and_wait(text, wait):	
	import time
	print text
	time.sleep(wait)


#########################################
#
#  Function name : convert_mp3
#  
#  Description : 
#
#  Parameters :
#
#########################################
def convert_mp3(input_file, baudrate):
	print("Start convert_mp3")	
	import os
	output_folder = os.path.dirname(input_file) + '/out'
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)
	input_file_name = os.path.splitext(os.path.basename(input_file))[0]
	output_folder = output_folder + '/' + input_file_name
	print 'File will be placed in ' + output_folder
	print 'bp'	
	from pydub import AudioSegment
	sound = AudioSegment.from_mp3(input_file)
	sound.export(output_folder + ".mp3" , format="mp3", bitrate=baudrate)


#########################################
#
#  Function name : convert_mp3
#  
#  Description : 
#
#  Parameters :
#
#########################################
def show_files_folder(path, extension):
	print("Start show_files_folder")	
	import os
	for file in os.listdir(path):
		if file.endswith(extension):
			print(file)
			convert_mp3(path + '/' + file, "128k")
			print("Start Show Files")	



# Entry point of the file		
try:
	import sys, time, os
	file_location = os.getcwd()
	print_and_wait("Start", 0.1)
	show_files_folder(file_location, ".mp3")
	print_and_wait("End", 1)
except:
	print "AudioSegment Error"
	time.sleep(1)

