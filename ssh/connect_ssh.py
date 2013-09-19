#!/usr/bin/python

import paramiko

def run():
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect('172.16.83.129', username='root', password='coyonetadmin')
	stdin, stdout, stderr = ssh.exec_command('ifconfig')
	#print stdout.readlines()
	#using readlines ignorees the newlines, that is why:
	for line in stdout:
		print (line)
	ssh.close()
	
if __name__ == "__main__":
    run()