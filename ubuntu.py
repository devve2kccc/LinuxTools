import os
import sys

os.system("clear && clear && clear")


menu = """
    {1} Install Apache2
    {2} Install PHP
    {3} Install Webmin
    {4} Update All
    {5} Exit
    """
		
phpsubmenu = """
		{1} PHP 5.6
		{2} PHP 7.3

	"""

print(menu)

def quit():
            print("Finished")
            exit()
            exit()
                

def submenu():
	submenu = int(input("Devve~# "))
	if submenu == 1:
		os.system("clear")
		os.system("sudo apt-get install python-software-properties")
		os.system("sudo add-apt-repository ppa:ondrej/php")
		os.system("sudo apt-get update")
		os.system("sudo apt-get install -y php5.6")
		os.system("clear")
		print("To show your php version, put php -v")
		quit()
	if submenu == 2:
		os.system("clear")
		os.system("sudo apt-get install python-software-properties")
		os.system("sudo add-apt-repository ppa:ondrej/php")
		os.system("sudo apt-get update")
		os.system("sudo apt-get install -y php7.2")
		os.system("clear")
		print("To show your php version, put php -v")
		quit()


def select():
	try:
		choice = int(input("Devve~# "))
		
		if choice == 1:
			os.system("sudo apt-get update")
			os.system("sudo apt install apache2")
			os.system("sudo ufw app list")
			os.system("sudo ufw allow 'Apache'")
			os.system("sudo ufw status")
			os.system("sudo systemctl restart apache2")
			os.system("sudo systemctl status apache2")
			print("Go to http://your_server_ip")
			quit()

		elif choice == 2:
			print(phpsubmenu)
			submenu()
			quit()

		elif choice == 3:
			os.system("clear")
			os.system("cd /etc/apt/")
			f = open("sources.list", "a")
			f.write("deb http://download.webmin.com/download/repository sarge contrib")
			f.close()
			os.system("wget http://www.webmin.com/jcameron-key.asc")
			os.system("sudo apt-key add jcameron-key.asc")
			os.system("sudo apt update")
			os.system("sudo apt install webmin")
			quit()

		elif choice == 4:
			os.system("sudo apt-get update")
			os.system("sudo apt-get upgrade")
			quit()

	except (KeyboardInterrupt):
		print("")
select()