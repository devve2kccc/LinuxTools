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
		os.system("sudo apt update")
		os.system("sudo apt upgrade")
		os.system("sudo apt install ca-certificates apt-transport-https")
		os.system("wget -q https://packages.sury.org/php/apt.gpg -O- | sudo apt-key add -")
		os.system("cd /etc/apt/sources.list.d/")
		f = open("php.list", "a")
		f.write("deb https://packages.sury.org/php/ stretch main")
		f.close()
		os.system("sudo apt update")
		os.system("sudo apt install php5.6")
		os.system("sudo apt install php5.6-cli php5.6-common php5.6-curl php5.6-mbstring php5.6-mysql php5.6-xml")
		print("To show your php version, put php -v")
		quit()

	if submenu == 2:
		os.system("clear")
		os.system("sudo apt update")
		os.system("sudo apt upgrade")
		os.system("sudo apt install ca-certificates apt-transport-https")
		os.system("wget -q https://packages.sury.org/php/apt.gpg -O- | sudo apt-key add -")
		os.system("cd /etc/apt/sources.list.d/")
		f = open("php.list", "a")
		f.write("deb https://packages.sury.org/php/ stretch main")
		f.close()
		os.system("sudo apt update")
		os.system("sudo apt install php7.3")
		os.system("sudo apt install php7.3-cli php7.3-common php7.3-curl php7.3-mbstring php7.3-mysql php7.3-xml")
		print("To show your php version, put php -v")
		quit()


def select():
	try:
		choice = int(input("Devve~# "))
		
		if choice == 1:
			os.system("sudo apt-get update")
			os.system("sudo apt install apache2")
			os.system("sudo ufw app list")
			os.system("sudo ufw allow 'WWW'")
			os.system("sudo ufw status")
			os.system("sudo systemctl restart apache2")
			os.system("sudo systemctl status apache2")
			os.system("hostname -I")
			os.system("sudo apt-get install curl")
			os.system("curl -4 icanhazip.com")
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
			f.write("deb https://download.webmin.com/download/repository sarge contrib")
			f.close()
			os.system("cd /root")
			os.system("wget http://www.webmin.com/jcameron-key.asc")
			os.system("apt-key add jcameron-key.asc")
			os.system("apt-get install apt-transport-https")
			os.system("apt-get update")
			os.system("sudo apt install webmin")
			quit()

		elif choice == 4:
			os.system("sudo apt-get update")
			os.system("sudo apt-get upgrade")
			quit()

	except (KeyboardInterrupt):
		print("")
select()