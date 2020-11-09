while True:
	import os
	os.system('clear')
	print('Press 1 to proceeed for Docker Installation.')
	print('Press 2 to Exit')
	choice=input('Enter your choice :')
	if int(choice) == 1:
		os.system("echo -e '[docker] \nbaseurl=http://download.docker.com/linux/centos/7/x86_64/stable \ngpgcheck=0' > /etc/yum.repos.d/dockerI.repo")
		os.system('systemctl start firewalld > file.txt')
		os.system('firewall-cmd --zone=public --add-masquerade --permanent > file.txt')
		os.system('firewall-cmd --zone=public --add-port=80/tcp > file.txt')
		os.system('firewall-cmd --zone=public --add-port=443/tcp > file.txt')
		os.system('firewall-cmd --reload > file.txt')
		os.system('systemctl restart docker > file.txt')

		os.system('yum install docker-ce --nobest -y')
		while True:
			os.system('clear')
			print('Docker Installed !')
			print('\t\t\tPress 1 : To pull an container image')
			print('\t\t\tPress 2 : To run a new container/OS and launch')
			print('\t\t\tPress 3 : To start any existing container/OS')
			print('\t\t\tPress 4 : To attach a container/OS')
			print('\t\t\tPress 5 : To see status of all containers')
			print('\t\t\tPress 6 : To see all the images and its details')
			print('\t\t\tPress 7 : To remove/delete containers')
			print('\t\t\tPress 8 : To remove/delete a image')
			print('\t\t\tPress 9 : To install httpd (web-server) in a docker container and start services (for centos)')
			print('\t\t\tPress 10 : To install python interpreter in docker container (for centos)')			
			print('\t\t\tPress 11 : Exit to main menu')
			choice=input('Enter your choice:')
			if int(choice) == 1:
				x=input('Enter the name of image: ')
				y=input('Enter the version of image: ')	
				if y == '':
					os.system('docker pull {}'.format(x))
				else:				
					os.system('docker pull {}:{}'.format(x,y))
			elif int(choice) == 2:
				x=input('Enter the OS name you want to launch:')
				y=input('Enter the version:')
				if y == '':
					os.system('docker pull {}'.format(x))
				else:				
					os.system('docker pull {}:{}'.format(x,y))
				z=input('Enter a unique name you want to give to your OS:')
				os.system('docker run -it --name {} {}:{}'.format(z,x,y))
			elif int(choice) == 3:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker start {}'.format(x))
				print('Container Started ! Now, you have to attach it to run!')
			elif int(choice) == 4:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker attach {}'.format(x))
			elif int(choice) == 5:
				os.system('docker ps -a')
			elif int(choice) == 6:
				os.system('docker images')
			elif int(choice) == 7:
				while True:
					os.system('clear')
					print('\t\t\tPress 1: To remove a single container')
					print('\t\t\tPress 2: To remove all container')
					print('\t\t\tPress 3: Exit to previous menu')
					choice=input('Enter your choice : ')
					if int(choice) == 1:
						x=input('Enter the name given to OS or enter the initial letters of container id :')
						os.system('docker rm {}'.format(x))
					elif int(choice) ==2:
						os.system('docker rm `docker ps -a -q`')
					elif int(choice) == 3:
						break
					input('Press Enter to continue')
			elif int(choice) == 8:
				x=input('Enter the name of the image you want to delete/remove:')
				y=input('Enter the version of the image:')
				os.system('docker rmi {}:{}'.format(x,y))
			elif int(choice) == 9:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker start {}'.format(x))
				os.system('docker exec {} yum install httpd -y'.format(x))
				os.system('docker exec {} /usr/sbin/httpd'.format(x))
			elif int(choice) == 10:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker start {}'.format(x))
				os.system('docker exec {} yum install python3 -y'.format(x))

			elif int(choice) == 11:
				break
			else:
				print('This is not a valid number! Please type correct number in digit !')
				continue
				
			input('Press Enter to continue or confirm !')
	elif int(choice) == 2:
		quit()
	else:
		print('This is not a valid number! Please type correct number in digit !')
		continue
while True:
	import os
	os.system('clear')
	print('Press 1: Docker Installation and its other features.')
	print('Press 2: Hadoop')
	print('Press 3: Amazon Web Services')
	print('Press 4: Exit')
	choice=input('Enter your choice :')
	if int(choice) == 1:
		os.system("echo -e '[docker] \nbaseurl=http://download.docker.com/linux/centos/7/x86_64/stable \ngpgcheck=0' > /etc/yum.repos.d/dockerI.repo")
		os.system('systemctl start firewalld > file.txt')
		os.system('firewall-cmd --zone=public --add-masquerade --permanent > file.txt')
		os.system('firewall-cmd --zone=public --add-port=80/tcp > file.txt')
		os.system('firewall-cmd --zone=public --add-port=443/tcp > file.txt')
		os.system('firewall-cmd --reload > file.txt')
		os.system('systemctl restart docker > file.txt')

		os.system('yum install docker-ce --nobest -y')
		while True:
			os.system('clear')
			print('Docker Installed !')
			print('\t\t\tPress 1 : To pull an container image')
			print('\t\t\tPress 2 : To run a new container/OS and launch')
			print('\t\t\tPress 3 : To start any existing container/OS')
			print('\t\t\tPress 4 : To attach a container/OS')
			print('\t\t\tPress 5 : To see status of all containers')
			print('\t\t\tPress 6 : To see all the images and its details')
			print('\t\t\tPress 7 : To remove/delete containers')
			print('\t\t\tPress 8 : To remove/delete a image')
			print('\t\t\tPress 9 : To install httpd (web-server) in a docker container and start services (for centos)')
			print('\t\t\tPress 10 : To install python interpreter in docker container (for centos)')			
			print('\t\t\tPress 11 : Exit to main menu')
			choice=input('Enter your choice:')
			if int(choice) == 1:
				x=input('Enter the name of image: ')
				y=input('Enter the version of image: ')	
				if y == '':
					os.system('docker pull {}'.format(x))
				else:				
					os.system('docker pull {}:{}'.format(x,y))
			elif int(choice) == 2:
				x=input('Enter the OS name you want to launch:')
				y=input('Enter the version:')
				if y == '':
					os.system('docker pull {}'.format(x))
				else:				
					os.system('docker pull {}:{}'.format(x,y))
				z=input('Enter a unique name you want to give to your OS:')
				os.system('docker run -it --name {} {}:{}'.format(z,x,y))
			elif int(choice) == 3:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker start {}'.format(x))
				print('Container Started ! Now, you have to attach it to run!')
			elif int(choice) == 4:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker attach {}'.format(x))
			elif int(choice) == 5:
				os.system('docker ps -a')
			elif int(choice) == 6:
				os.system('docker images')
			elif int(choice) == 7:
				while True:
					os.system('clear')
					print('\t\t\tPress 1: To remove a single container')
					print('\t\t\tPress 2: To remove all container')
					print('\t\t\tPress 3: Exit to previous menu')
					choice=input('Enter your choice : ')
					if int(choice) == 1:
						x=input('Enter the name given to OS or enter the initial letters of container id :')
						os.system('docker rm {}'.format(x))
					elif int(choice) ==2:
						os.system('docker rm `docker ps -a -q`')
					elif int(choice) == 3:
						break
					input('Press Enter to continue')
			elif int(choice) == 8:
				x=input('Enter the name of the image you want to delete/remove:')
				y=input('Enter the version of the image:')
				os.system('docker rmi {}:{}'.format(x,y))
			elif int(choice) == 9:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker start {}'.format(x))
				os.system('docker exec {} yum install httpd -y'.format(x))
				os.system('docker exec {} /usr/sbin/httpd'.format(x))
			elif int(choice) == 10:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker start {}'.format(x))
				os.system('docker exec {} yum install python3 -y'.format(x))

			elif int(choice) == 11:
				break
			else:
				print('This is not a valid number! Please type correct number in digit !')
				continue
				
			input('Press Enter to continue or confirm !')
	elif int(choice) == 4:
		quit()
	else:
		print('This is not a valid number! Please type correct number in digit !')
		continue
while True:
	import os
	os.system('clear')
	print('Press 1: Docker Installation and its other features.')
	print('Press 2: Hadoop')
	print('Press 3: Amazon Web Services')
	print('Press 4: Exit')
	choice=input('Enter your choice :')
	if int(choice) == 1:
		os.system("echo -e '[docker] \nbaseurl=http://download.docker.com/linux/centos/7/x86_64/stable \ngpgcheck=0' > /etc/yum.repos.d/dockerI.repo")
		os.system('systemctl start firewalld > file.txt')
		os.system('firewall-cmd --zone=public --add-masquerade --permanent > file.txt')
		os.system('firewall-cmd --zone=public --add-port=80/tcp > file.txt')
		os.system('firewall-cmd --zone=public --add-port=443/tcp > file.txt')
		os.system('firewall-cmd --reload > file.txt')
		os.system('systemctl restart docker > file.txt')

		os.system('yum install docker-ce --nobest -y')
		while True:
			os.system('clear')
			print('Docker Installed !')
			print('\t\t\tPress 1 : To pull an container image')
			print('\t\t\tPress 2 : To run a new container/OS and launch')
			print('\t\t\tPress 3 : To start any existing container/OS')
			print('\t\t\tPress 4 : To attach a container/OS')
			print('\t\t\tPress 5 : To see status of all containers')
			print('\t\t\tPress 6 : To see all the images and its details')
			print('\t\t\tPress 7 : To remove/delete containers')
			print('\t\t\tPress 8 : To remove/delete a image')
			print('\t\t\tPress 9 : To install httpd (web-server) in a docker container and start services (for centos)')
			print('\t\t\tPress 10 : To install python interpreter in docker container (for centos)')			
			print('\t\t\tPress 11 : Exit to main menu')
			choice=input('Enter your choice:')
			if int(choice) == 1:
				x=input('Enter the name of image: ')
				y=input('Enter the version of image: ')	
				if y == '':
					os.system('docker pull {}'.format(x))
				else:				
					os.system('docker pull {}:{}'.format(x,y))
			elif int(choice) == 2:
				x=input('Enter the OS name you want to launch:')
				y=input('Enter the version:')
				if y == '':
					os.system('docker pull {}'.format(x))
				else:				
					os.system('docker pull {}:{}'.format(x,y))
				z=input('Enter a unique name you want to give to your OS:')
				os.system('docker run -it --name {} {}:{}'.format(z,x,y))
			elif int(choice) == 3:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker start {}'.format(x))
				print('Container Started ! Now, you have to attach it to run!')
			elif int(choice) == 4:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker attach {}'.format(x))
			elif int(choice) == 5:
				os.system('docker ps -a')
			elif int(choice) == 6:
				os.system('docker images')
			elif int(choice) == 7:
				while True:
					os.system('clear')
					print('\t\t\tPress 1: To remove a single container')
					print('\t\t\tPress 2: To remove all container')
					print('\t\t\tPress 3: Exit to previous menu')
					choice=input('Enter your choice : ')
					if int(choice) == 1:
						x=input('Enter the name given to OS or enter the initial letters of container id :')
						os.system('docker rm {}'.format(x))
					elif int(choice) ==2:
						os.system('docker rm `docker ps -a -q`')
					elif int(choice) == 3:
						break
					input('Press Enter to continue')
			elif int(choice) == 8:
				x=input('Enter the name of the image you want to delete/remove:')
				y=input('Enter the version of the image:')
				os.system('docker rmi {}:{}'.format(x,y))
			elif int(choice) == 9:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker start {}'.format(x))
				os.system('docker exec {} yum install httpd -y'.format(x))
				os.system('docker exec {} /usr/sbin/httpd'.format(x))
			elif int(choice) == 10:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker start {}'.format(x))
				os.system('docker exec {} yum install python3 -y'.format(x))

			elif int(choice) == 11:
				break
			else:
				print('This is not a valid number! Please type correct number in digit !')
				continue
				
			input('Press Enter to continue or confirm !')
	elif int(choice) == 4:
		quit()
	else:
		print('This is not a valid number! Please type correct number in digit !')
		continue
while True:
	import os
	os.system('clear')
	print('Press 1: Docker Installation and its other features.')
	print('Press 2: Hadoop')
	print('Press 3: Amazon Web Services')
	print('Press 4: Exit')
	choice=input('Enter your choice :')
	if int(choice) == 1:
		os.system("echo -e '[docker] \nbaseurl=http://download.docker.com/linux/centos/7/x86_64/stable \ngpgcheck=0' > /etc/yum.repos.d/dockerI.repo")
		os.system('systemctl start firewalld > file.txt')
		os.system('firewall-cmd --zone=public --add-masquerade --permanent > file.txt')
		os.system('firewall-cmd --zone=public --add-port=80/tcp > file.txt')
		os.system('firewall-cmd --zone=public --add-port=443/tcp > file.txt')
		os.system('firewall-cmd --reload > file.txt')
		os.system('systemctl restart docker > file.txt')

		os.system('yum install docker-ce --nobest -y')
		while True:
			os.system('clear')
			print('Docker Installed !')
			print('\t\t\tPress 1 : To pull an container image')
			print('\t\t\tPress 2 : To run a new container/OS and launch')
			print('\t\t\tPress 3 : To start any existing container/OS')
			print('\t\t\tPress 4 : To attach a container/OS')
			print('\t\t\tPress 5 : To see status of all containers')
			print('\t\t\tPress 6 : To see all the images and its details')
			print('\t\t\tPress 7 : To remove/delete containers')
			print('\t\t\tPress 8 : To remove/delete a image')
			print('\t\t\tPress 9 : To install httpd (web-server) in a docker container and start services (for centos)')
			print('\t\t\tPress 10 : To install python interpreter in docker container (for centos)')			
			print('\t\t\tPress 11 : Exit to main menu')
			choice=input('Enter your choice:')
			if int(choice) == 1:
				x=input('Enter the name of image: ')
				y=input('Enter the version of image: ')	
				if y == '':
					os.system('docker pull {}'.format(x))
				else:				
					os.system('docker pull {}:{}'.format(x,y))
			elif int(choice) == 2:
				x=input('Enter the OS name you want to launch:')
				y=input('Enter the version:')
				if y == '':
					os.system('docker pull {}'.format(x))
				else:				
					os.system('docker pull {}:{}'.format(x,y))
				z=input('Enter a unique name you want to give to your OS:')
				os.system('docker run -it --name {} {}:{}'.format(z,x,y))
			elif int(choice) == 3:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker start {}'.format(x))
				print('Container Started ! Now, you have to attach it to run!')
			elif int(choice) == 4:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker attach {}'.format(x))
			elif int(choice) == 5:
				os.system('docker ps -a')
			elif int(choice) == 6:
				os.system('docker images')
			elif int(choice) == 7:
				while True:
					os.system('clear')
					print('\t\t\tPress 1: To remove a single container')
					print('\t\t\tPress 2: To remove all container')
					print('\t\t\tPress 3: Exit to previous menu')
					choice=input('Enter your choice : ')
					if int(choice) == 1:
						x=input('Enter the name given to OS or enter the initial letters of container id :')
						os.system('docker rm {}'.format(x))
					elif int(choice) ==2:
						os.system('docker rm `docker ps -a -q`')
					elif int(choice) == 3:
						break
					input('Press Enter to continue')
			elif int(choice) == 8:
				x=input('Enter the name of the image you want to delete/remove:')
				y=input('Enter the version of the image:')
				os.system('docker rmi {}:{}'.format(x,y))
			elif int(choice) == 9:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker start {}'.format(x))
				os.system('docker exec {} yum install httpd -y'.format(x))
				os.system('docker exec {} /usr/sbin/httpd'.format(x))
			elif int(choice) == 10:
				x=input('Enter the name given to OS or enter the initial letters of container id :')
				os.system('docker start {}'.format(x))
				os.system('docker exec {} yum install python3 -y'.format(x))

			elif int(choice) == 11:
				break
			else:
				print('This is not a valid number! Please type correct number in digit !')
				continue
				
			input('Press Enter to continue or confirm !')
	elif int(choice) == 4:
		quit()
	else:
		print('This is not a valid number! Please type correct number in digit !')
		continue
