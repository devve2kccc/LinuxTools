import os
import sys 

os.system("clear && clear && clear")

os = """
    {1} Centos
    {2} Ubuntu
    {3} Debian

      """
print(os)

choice = input("Devve~# ")

if choice == 1:
	import centos

elif choice == 2:
	import ubuntu

elif choice == 3:
	import debian
