import os
import sys

os.system("clear && clear && clear")


menu = '''
		{1} Install HTTPD
		{2} Install PHP
		{3} Install CWP
		{4} Update All
		{5} Exit
		'''
		
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
	submenu = input("Devve~# ")
	if submenu == 1:
		os.system("clear")
		os.system("yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm")
		os.system("yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm")
		os.system("yum install -y yum-utils")
		os.system("yum-config-manager --enable remi-php56")
		os.system("yum install -y php php-mcrypt php-cli php-gd php-curl php-mysql php-ldap php-zip php-fileinfo")
		os.system("clear")
		print("To show your php version, put php -v")
		quit()
	if submenu == 2:
		os.system("clear")
		os.system("sudo yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm")
		os.system("sudo yum -y install epel-release yum-utils")
		os.system("sudo yum-config-manager --enable remi-php73")
		os.system("sudo yum -y install php php-cli php-fpm php-mysqlnd php-zip php-devel php-gd php-mcrypt php-mbstring php-curl php-xml php-pear php-bcmath php-json")
		os.system("clear")		
		print("To show your php version, put php -v")
		quit()


def select():
	try:
		choice = input("Devve~# ")
		
		if choice == 1:
			os.system("yum -y update")
			os.system("yum -y install httpd")
			os.system("service httpd restart")
			os.system("clear")
			os.system("clear")
			print("Edit ServerName in /etc/httpd/conf/httpd.conf")
			quit()

		elif choice == 2:
			print(phpsubmenu)
			submenu()
			quit()

		elif choice == 3:
			os.system("cd /usr/local/src")
			os.system("wget http://centos-webpanel.com/cwp-el7-latest")
			os.system("sh cwp-el7-latest")
			os.system("reboot")
			quit()

		elif choice == 4:
			os.system("yum -y update")

	except (KeyboardInterrupt):
		print("")
select()
		

