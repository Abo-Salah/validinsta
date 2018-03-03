try:
	from torrequest import TorRequest
except:
	print(' [=] Error: if TOR not install RUN : apt-get install tor')
	print(' [=] Error: python TorRequest not installed RUN : apt-get install torrequest')
	os._exit(1)
import re
from colorama import Fore, Back, Style
import os
from time import sleep
import argparse
tr = TorRequest()

def changeip():
	while True:
		try:
			tr.reset_identity()
			response = tr.get('http://ipecho.net/plain')
			print(Fore.BLUE + '[*] Trying New IP : ' + response.text)
		except:
			continue
		break

def saveavailable(email):
	file = open(outfile,"a") 
	file.write(email + "\n") 
	file.close()

def checkuser(email):
	try:
		response = tr.get('https://www.instagram.com/accounts/fb_linked_account/?check_email=' + email)
	except tr.exceptions.RequestException as e:
		print ("[!] Error Request , trying again")
		changeip()
		checkuser(email)
	except KeyboardInterrupt:
		print ("[!] Canceled ..")
	if response.status_code == 200 and re.search('{"email_taken":', response.text):
		if re.search('{"email_taken": true', response.text):
			print (Fore.GREEN + email + ' [+] Registered')
			saveavailable(email)
		else:
			print (Fore.YELLOW + email + ' [-] Not Exist')
	else:
		changeip()
		checkuser(email)
def welcome():

	print (Fore.RED + """                  )       (              (                 ) 
	   (       (   ( /(       )\ )    (      )\ )    (      ( /( 
	   )\    ( )\  )\())     (()/(    )\    (()/(    )\     )\())
	((((_)(  )((_)((_)\  ___  /(_))((((_)(   /(_))((((_)(  ((_)\ 
	 )\ _ )\((_)_   ((_)|___|(_))   )\ _ )\ (_))   )\ _ )\  _((_)
	 (_)_\(_)| _ ) / _ \     / __|  (_)_\(_)| |    (_)_\(_)| || |
	  / _ \  | _ \| (_) |    \__ \   / _ \  | |__   / _ \  | __ |
	 /_/ \_\ |___/ \___/     |___/  /_/ \_\ |____| /_/ \_\ |_||_|
	""")
	print (Style.RESET_ALL + Back.RED + '[!]STAY TRUE' + Style.RESET_ALL+Fore.WHITE + ' [!]STAY FREE')
	print (Fore.GREEN + "[!]Instagram Email Validation [!]BY AboSalah [!]twitter : @abosalahps")
	print(Style.RESET_ALL)
	sleep(1.5) # Time in seconds.


def main():
	parser = argparse.ArgumentParser(prog='instavalid.py', description='Instagram Email Validation Using TOR')
	parser.add_argument('inputfile', type=str, help='emails file to check')
	parser.add_argument('outfile', type=str, help='file name to save registered emails')
	args = parser.parse_args()
	global outfile
	outfile = args.outfile
	if not os.path.isfile(args.inputfile):
		print(" [-] input file does not exist.\n")
		exit(0)
	with open(args.inputfile) as f:
		for lines in f:
			checkuser (lines.rstrip('\n'))
	print(Fore.BLUE + '[!] Finished [!]')


if __name__ == '__main__':
	welcome()
	main()
