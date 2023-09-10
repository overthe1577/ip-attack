#!/usr/bin/python
#
#
# 	<=== IP ATTACK ===>
#
#  Name 	:  IP Attack
#  Coded by	:  overthe1577

#
#
#
#

import sys
import time
import os
from urllib2 import *
from platform import system
print
print
print
os.system("clear")
os.system("bash logo.sh")
print
print
print
print "\033[1m\033[32m\t\t \033[1m\033[31m<==\033[33m[\033[32m Author Info \033[33m]\033[31m==>\033[0m"
time.sleep(3)
print
print
print
print "\033[1m\033[33m\n\tDeveloper : \033[32m \033[33mo\033[overthe1577 \033[33mt\033[team1577\033[0m"
time.sleep(1)

time.sleep(2)
print
print

def ping():
	print
	print
	os.system("toilet -f pagga 'Ping Attack       ' | lolcat")
	time.sleep(1)
	print
	
	os.system("curl https://api.hackertarget.com/nping/?q=" + ip)
	print(" ")
	
def http():
	print
	print
	os.system("toilet -f pagga 'Http Header       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/httpheaders/?q=" + ip)
	print(" ")



def whois():
	print
	print

	os.system("toilet -f pagga 'Whois       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl http://api.hackertarget.com/whois/?q=" + ip)
	print(" ")


def trace():
	print
	print
	os.system("toilet -f pagga 'Traceroute       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/mtr/?q=" + ip)
	print(" ")



def dns():
	print
	print
	os.system("toilet -f pagga 'DNS Lookup       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/dnslookup/?q=" + ip)
	print(" ")


def reversedns():
	print
	print
	os.system("toilet -f pagga 'Reverse Dns       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/reversedns/?q=" + ip)
	print(" ")


def geoip():
	print
	print
	os.system("toilet -f pagga 'Geo Ip       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/geoip/?q=" + ip)
	print(" ")


def reverseip():
	print
	print
	os.system("toilet -f pagga 'Reverse IP       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/reverseiplookup/?q=" + ip)
	print(" ")
	

def nmap():
	print
	print
	os.system("toilet -f pagga 'Nmap       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/nmap/?q=" + ip)
	print(" ")



def plink():
	print
	print
	os.system("toilet -f pagga 'Page Link       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/pagelinks/?q=" + ip)
	print(" ")


	print
	print
	time.sleep(3)
	print
os.system("clear")
print
os.system( "bash logo.sh" )
print
def mnu():
	print "\033[1m\033[32m[+]\033[36m Whois lookup"
	print "\033[32m[+] \033[36mDNS lookup"
	print "\033[32m[+]\033[36m Reverse DNS lookup"
	print "\033[32m[+]\033[36m GeoIP lookup"
	print "\033[32m[+] \033[36mReverse IP lookup"
	print "\033[32m[+] \033[36mHttp Response"
	print "\033[32m[+] \033[36mPing"
	print "\033[32m[+] \033[36mPage Link"
	print "\033[32m[+] \033[36mNmap"
	print "\033[32m[+] \033[36mTraceroute"
	
print
print
print
mnu()
print
print
print "\033[1m\033[32mEnter Your IP Or Domain..."
print
ip = raw_input("\033[1m\033[32m IP or Domain : \033[33m\033[1m")
print
time.sleep(3)
whois()
dns()
reversedns()
geoip()
reverseip()
http()
ping()
plink()
nmap()
trace()
sys.exit()
	
