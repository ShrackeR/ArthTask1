import os
print("\n\t\t\t############################################################")
print("\n\t\t\t\t\t\tHTTPD WEB_SERVER")
print("\n\t\t\t############################################################")
print("\n\n\n\n")
os.system("echo -e '[AppStream] \nname=Yum form AppStream  \nbaseurl=file:///run/media/root/RHEL-8-2-0-BaseOS-x86_64/AppStream \ngpgcheck=0 \n\n[BaseOS] \nname=Yum form BaseOS \nbaseurl=file:///run/media/root/RHEL-8-2-0-BaseOS-x86_64/BaseOS \ngpgcheck=0' > /etc/yum.repos.d/menuTeamTask.repo")
os.system('yum install httpd -y > file.txt' )
os.system('\t\t\thttpd installed successfully !')

while True:
	os.system('clear')
	print("\n\t\t\t############################################################")
	print("\n\t\t\t\t\t\tHTTPD WEB_SERVER")
	print("\n\t\t\t############################################################")
	print("\n\n")
	print('\t\t\tPress 1: To create a html file')
	print('\t\t\tPress 2: To start services')
	print('\t\t\tPress 3: To enable services')
	print('\t\t\tPress 4: To stop services')
	print('\t\t\tPress 5: Exit')
	choice=input('Enter your choice :')
	while True:
		if int(choice) == 1:
			file_name=input("Give a name of html file to open editor: ")
			os.system('vi  /var/www/html/{}.html'.format(file_name))
			print("\n############################################################")
			print("\t\t\tFILE CRETAED !")
			print("\n############################################################")
			
			yn=input("Do you want to create more html files (yes/no)?")
			if yn == 'yes':
				continue	
			elif yn == 'no':
				break
			else:
				input('Error occured ! Please press enter to start again !')
				continue 
			input('Press enter to continue')
		elif int(choice) == 2:
			os.system('systemctl start httpd')
		elif int(choice) == 3:
			os.system('systemctl enable httpd')
		elif int(choice) == 4:
			os.system('systemctl stop httpd')
		elif int(choice) == 5:
			quit()
		else:
			input('Please enter correct number ! Enter to continue or confirm')
		input('Press enter to continue')
		break

		
