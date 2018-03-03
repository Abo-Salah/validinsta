# validinsta
bulk Instagram Email Validation using tor

# requirement

python3

tor

torrequest

colorama

time

argparse


# installation
git clone https://github.com/Abo-Salah/validinsta.git

pip3 install argparse torrequest

apt-get install tor

#Configuring Tor server:

open tor configuration file /etc/tor/torrc

delete the # before 'ControlPort':

#ControlPort 9051

# usage 
restart tor service: service tor restart

python3 validinsta.py emailsfiletocheck filetosavevalis
