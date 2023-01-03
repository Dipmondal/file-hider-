from os import path
import shutil,pyfiglet,time,os,readline
#from PIL import Image
import platform
import psutil
bold = "\33[1m"
fnc = "\033[1;31;40m"
fnc1 = "\033[1;34;40m"
fnc2 = "\033[1;35;40m"
fnc3 = "\033[1;32;40m"
bnc = "\033[0m"
bgc = "\033[6;39;44m"
bgcf = "\033[0m"
os.chdir("/storage/emulated/0/")
next = "/storage/emulated/0/.Next_file"
if not os.path.exists(".Next_file"):
    os.mkdir(".Next_file")
else:    
    pass
os.chdir("/storage/emulated/0/.Next_File")
#'/storage/emulated/0/.Next_File/.userdata/
if not os.path.exists(".userdata"):
	os.mkdir(".userdata")
else:
	pass
if not os.path.exists("image"):
	os.mkdir("image")
else:
	pass
if not os.path.exists("audio"):
	os.mkdir("audio")
else:
	pass
if not os.path.exists("video"):
	os.mkdir("video")
else:
	pass
if not os.path.exists("text"):
	os.mkdir("text")
else:
	pass
if not os.path.exists("app"):
	os.mkdir("app")
else:
	pass
if not os.path.exists("program"):
	os.mkdir("program")
else:
	pass
if not os.path.exists("other"):
	os.mkdir("other")
else:
	pass
next = pyfiglet.figlet_format("NEXT FILE")
print(fnc3+next+bnc)
def creator():
	global bold,bgc,bgcf
	print(bold,bgc,'Created By Dip Mondal',bgcf)
	print(bold,fnc,'I Take Some code From Other',bnc)
	print(bold,bgc,'I Have This Idea From Youtub Video But That A Time I Dont Know How to Make Project Like This',bgcf)
def nextex():
	print(fnc2,)
	print(f"Mechile type : {platform.machine()}")
	print(f"os : {platform.system()}")
	print(f"os release : {platform.release()}")
	print(f"os version : {platform.version()}")
	print(f"physical core : {psutil.cpu_count(logical=False)}")
	print(f"current CPU fre : {psutil.cpu_freq().current}")
	print(f"Total RAM installed: {round(psutil.virtual_memory().total/1000000000, 2)} GB")
	#Available RAM
	print(f"Available RAM: {round(psutil.virtual_memory().available/1000000000, 2)} GB")
	#Used RAM
	print(f"Used RAM: {round(psutil.virtual_memory().used/1000000000, 2)} GB")
	#RAM usage
	print(f"RAM usage: {psutil.virtual_memory().percent}%")
	print('',bnc)
	print(bgc+ 'creator © Dip Mondal ',bgcf)
nextex()
op = '/storage/emulated/0/.Next_File/.userdata/'
def restart():
	global op,fnc3,fnc2
#####################################
	if path.isfile(op+".question1.txt") and (op+'.question2.txt') and (op+'.ans.txt') and (op+'.ans2.txt'):
		pass
	else:
	#######QUESTION---WRITE########
		with open(op+'.question1.txt','w') as question_write:
			print(fnc3,'Enter Your First Question\n',bnc)
			question_input = input()
			question_write.write(question_input)
			question_write.close()
			###############
			# fast answer #
			#    WRITE    #
			###############
		with open(op+'.answer.txt','w') as answer_write:
			print(fnc3,'Enter Your Fast Answer \n ',bnc)
			ansin = input()
			answer_write.write(ansin)
			answer_write.close()

			###############
			#secound q & a#
			#    ANSWER   #
			###############
		with open(op+'.question2.txt','w') as question_write2:
			print(fnc3,'Enter Your Secound Question \n',bnc)
			question_input2 = input()
			question_write2.write(question_input2)
			question_write2.close()
			
		######Answer#######
		with open(op+'.answer2.txt','w') as answer_write2:
			print(fnc,'Enter Your Secuond Answer\n',bnc)
			ans2in= input()
			answer_write2.write(ans2in)
			answer_write.close()
#####################################
			######Read#####
		  	#QUESTION#
	with open(op+'.question1.txt','r') as question_read:
		question = question_read.read()
		question_read.close()
	with open(op+'.question2.txt','r') as question_read2:
		question2 = question_read2.read()
		question_read2.close()
#####################################
	with open(op+'.answer.txt','r') as RA: #TKAN TAKE ANSWER FROM USER
		TKAN = RA.read()
		RA.close()
	with open(op+'.answer2.txt','r')as RA2:
		TAKE2 = RA2.read()
		RA2.close()
#####################################
	print(fnc,question)
	ansIn = input('Answer : ')
	print(question2)
	ansIn2 = input('Answer : ')
	print('',bnc)
	if TKAN == ansIn and TAKE2 == ansIn2:
		print()
		pass
		os.system('clear')
	else:
		print('Answer Not Valid')
		restart()
		
			
	with open(op+'.userpass.txt','w')as newpass:
		wps = input(fnc3+'Enter Your New Password \n')
		newpass.write(wps)
		newpass.close()
		pass		
def help():
	print(fnc3+"")
	print('#		:	for Move File Into Safe File')
	print('G or home	:	for Go To Home')
	print('cd		:	For Change Dirtory')
	print('ls		:	For chek List Of File')
	print('mkdir		:	For Make Dirtory')
	print('pwd		:	For Chek Dirtory')
	print('clear		:	For Clear terminal')
	print('hoistory	:	For Chek History')
	print('cd home		:	Go to home')
	print('exit		:	For Exit'+bnc)
def split():
	#ned = ".userpass.txt" and '.question1.txt' and '.question.txt' and '.answer2.txt' and '.answer.txt'
#	main_file= ned
#directory paths
	source="/storage/emulated/0/.Next_File"
#file = "/storage/emulated/0/.Next_File"
	audio ="/storage/emulated/0/.Next_File/audio"
	video = "/storage/emulated/0/.Next_File/video"
	other = "/storage/emulated/0/.Next_File/other"
	image = "/storage/emulated/0/.Next_File/photo"
	text = "/storage/emulated/0/.Next_File/text"
	program = "/storage/emulated/0/.Next_File/program"
	files = os.listdir()
#file formats list
	audio_file_formats=['mp3','wav']
	doc_file_formats=['doc','docx','xlsx,pdf,zip']
	text_file_formats=['txt']
	video_file_formates=['mp4','mkv']
	programming_file_formats=['py','js','cpp','html','css','java']
	images_file_formats= ['PNG','jpg','png','jpeg']
	app_file_formats = ['apk','exe']
	other_file_formats = ['csv','TTF','AVI','psd','Tiff']
	
#delete app.py file from list
#	if main_file in files:
#	    main_fille = '.userdata'
#	    get_file_index=files.index(main_fille)
#	    del files[get_file_index]
	
	for file in files:
		
	    file_ext= file.split('.')[-1]
	    if file_ext in app_file_formats:
	    	shutil.move(file,app)
	
	    if file_ext in audio_file_formats:
	        shutil.move(file,audio)
	
	    if file_ext in doc_file_formats:
	        shutil.move(file,text)
	        
	
	    if file_ext in text_file_formats:
	        shutil.move(file,text)
	        
	
	    if file_ext in video_file_formates:
	        shutil.move(file,video)
	        
	
	    if file_ext in programming_file_formats:
	    	shutil.move(file,program) 
	
	    if file_ext in images_file_formats:
	    	shutil.move(file,image)
	    if file_ext in other_file_formats:
	    	shutil.move(file,other)
		
split()	
def move():
	global fnc2,bnc,fnc3
	print(fnc3,)
	print('[cd home] 	for change dir and see list dir')
	print('[cd] 		for change dir')
	print('[m] 		fore move file')
	print('[ls -h] 	hiden file list')
	print('[ls] 		list')
	print('[pwd] 		current working dir')
	print('[home] 		safe file')
	print('',bnc)
	os.chdir('/storage/emulated/0/')
	move = "/storage/emulated/0/.Next_file"
	while True:
		try:
			print(fnc2,)
			inp = input('⟩ ')
			print('',bnc)
			#try:
			if inp == 'cd':
				os.system('ls')
				os.chdir(input('Enter Your dir : '))
			elif inp == 'creator':
				print(creator())
			elif inp == 'cd home':
				os.chdir('/storage/emulated/0/')
				#local file list
			#	cwi = os.getcwd()
				#local = os.listdir(cwi)
				print(os.system('ls'))
				print(fnc2,)
				#print(*local,sep="\n")
				inpu = input('DIR : ')
				print('',bnc)
				
				user_change = '/storage/emulated/0/'+inpu
				os.chdir(user_change)
				print(os.system('ls'))
				#show_dir = os.listdir()
				#print(*show_dir,sep="\n")
			elif inp == 'pwd':
				print(os.getcwd())
			elif inp == 'ls -h' or inp == 'ls -h' or inp == 'ls-h':
				print(fnc2,fnc,)
				show_dir = os.listdir()
				print(*show_dir,sep="\n")
				print('',bnc)
			elif inp == 'ls':
				print(os.system('ls'))
			elif inp == 'm':
				#print(os.listdir())
				source = input(bold+fnc3+'Enter Your Source File : '+bnc)
				cwdf = os.getcwd()
				source_final = cwdf+"/"+source
				shutil.move(source_final,move)
				print('done')
			elif inp == 'G':
				con()
			elif inp == 'home':
				con()
			else:
				move()
	
		except:
			print(fnc+'File Not Exict'+bnc)
def con():
	em = ("")
	global bold,fnc,fnc2,fnc3,bnc,bgc,bgcf
	chose = input('[G] or [#] ≥ ')
	if chose == em:
		con()
	elif chose == 'G':
		os.chdir('/storage/emulated/0/.Next_file')
	
	elif chose == '#':
		move()
	elif chose == 'exit':
		exit(fnc3+'Thank You For Useing'+bnc)
	elif chose == 'creator':
		print(creator())
	else:
		con()
	while True:
		dirh = os.getcwd()
		usen = bold + bgc+"$ " +dirh+ " ➢  "+ bgcf
		inputs = input(usen).lower()
		if inputs == 'ls':
		#	ls_split = os.listdir()
			#print(*ls_split,sep='\n')
			os.system('ls')
	##############################
	####open video,image,audio####
	#							#
	#							#
			 	#start#
		#image
	#	elif inputs == "rm":
		#	try:
			#	os.remove(input())
		#	except:
				#print("folder not exist")
		elif inputs == 'creator':
			print(creator())
		elif inputs == 'show image':
			file = input('input your image name with extension : ')
			img = "/storage/emulated/0/.Next_File/"+file
			img = Image.open(img)
			img.show()
		#video
		elif inputs == 'show video':
			Video = input('Input Video')
			Video_path = "/storage/emulated/0/.Next_File/" + Video
			asa_plays = vlc.MediaPlayer(Video_path)
			asa_plays.play
	##############################
		elif inputs == 'open':
			try:
				print(fnc3,)
				name = input('Enter File Name : ')
				extension = input('Enter File Extension : ')
				print('',bnc)
				with open(name+extension,'r') as user_read:
					print(fnc2,)
					print(user_read.read())
			except:
				print('File dosent exist',bnc)
		elif inputs == 'home':
			con()
		elif inputs == 'restart':
			restart()
		elif inputs == 'rm':
			try:
				print(fnc,)
				rmi = input('Enter File Name : ')
				os.remove(rmi)
				print(rmi,'Delete Doen')
			except:
				print(rmi, 'Not Found ')
			print('',bnc)
		elif inputs == '#':
			move()
		elif inputs == "mkdir":
			try:
				print(fnc3)	
				folder_name = input("Enter Your Folder Name : ")
				os.mkdir(folder_name)
				print(folder_name,'created succesfull')
				print('',bnc)
			except:
				print(fnc,'						⚠',bnc)
		elif inputs == 'exit':
			exit()
		elif inputs == 'cd':
			try:
				print(fnc3,)
				chd = input()
				os.chdir(chd)
				print(os.getcwd())
				print('',bnc)
			except:
				print(chd,'dost not excist')
		elif inputs == 'help':
			help()
		elif inputs == 'clear':
			os.system('clear')
		elif inputs== "history":
			for i in range(readline.get_current_history_length()):
				print (fnc2+readline.get_history_item(i+1)+bnc)
		elif inputs == 'pwd':
			print(fnc2,)
			print(os.getcwd())
			print('',bnc)	
def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 

        timer = '{:02d}:{:02d}'.format(mins, secs) 

        print(timer, end="\r") 

        time.sleep(1) 

        t -= 1
t = 30#input("Enter the time in seconds: ")
# function call 	
def login():
	global bold,fnc,fnc2,fnc3,bnc,bgc,bgcf,fnc1,op
	if path.isfile(op+".userpass.txt"):
		pass
	else:
		with open(op+".userpass.txt","w") as use:
			userNm= input("enter user name : ")
			use.write(userNm)
			use.close()
#####################################
#								   #
#	  creat pass and chek pass	 #
#####################################
	with open(op+".userpass.txt","r") as fc:
		pcr = fc.read()
		fc.close()
	for x in range(1,11):
		print(bold+fnc,x,"ENTER YOUR PASSWORD\n",bnc)
		print(fnc2,)
		pc = input()
		print('',bnc)
		if pc == pcr:
			print(bold+fnc3+'LOG IN SUCCESSFUL '+bnc)
			print(bold+fnc2+'[#] Move File Manager content')
			print('[G]Go to Safe File'+bnc)
			con()
		elif pc == 'restart':
			restart()
		elif pc == 'creator':
			print(creator())
			x = 0
########################################
		if x == 10:
			print(bold+fnc3+'			time start \n\n\n'+bnc)
			countdown(int(t))		
		#	finally
	chp = input(bold+fnc3+'DO YOU FORGET PASSWORD y/n '+bnc)
	if chp == 'y':
			restart()
			login()
	elif chp == 'n':
		login()
	elif chp == 'creator':
		print(creator())
	else:
		login()
login()
