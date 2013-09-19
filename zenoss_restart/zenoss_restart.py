#!/usr/bin/python

import os
import datetime

def run():
	fh = open('./zenoss_restart.log', 'a')
	date = str(datetime.datetime.now())
	fh.write(date + '\n')
	log = os.popen("service zenoss restart").readlines()
	for line in log:
		fh.write(line)
	fh.write('\n\n')
	fh.close()

if __name__ == "__main__":
    run()
