#!/usr/bin/python

import os
import difflib
import datetime
import sys

def run():
	source = open ('./source', 'U')
	target = open ('./target', 'U')
	result = open ('./result.html', 'w')

	diff = difflib.HtmlDiff(100, 100).make_table(source,target)
	#sys.stdout.writelines(diff)
	result.writelines(diff)
	
if __name__ == "__main__":
    run()

