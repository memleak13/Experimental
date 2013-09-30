#!/usr/bin/python

#import os
import difflib
#import datetime
#import sys

def run():
	source = open ('./source', 'U')
	target = open ('./target', 'U')
	result = open ('./result.html', 'w')

	create_html_header(result)
	compare_files(source, target, result)
	create_html_footer(result)

	#Alternitave way to build complete page
	#diff = difflib.HtmlDiff().make_file(source,target)
	#result.writelines(diff)

def compare_files(source, target, result):
	"""Compare files and create html"""
	diff = difflib.HtmlDiff().make_table(source,target)
	result.writelines(diff)
	#sys.stdout.writelines(diff)

def create_html_header(result):
	"""Writes HTML Header"""
	result.write('<!DOCTYPE HTML>\n')
	result.write('<html>\n')
	result.write('<head>\n')
	result.write('<style type="text/css">')	
	
	result.write('.diff{\n')
	result.write('width: 1200px;\n')
	result.write('font-family:arial;\n')
	result.write('font-size: 10pt;\n')
	result.write('text-align: left;\n')
	result.write('margin-left: auto;\n')
	result.write('margin-right: auto;\n')
	result.write('table-layout: auto;\n')
	result.write('background-color: Gainsboro\n')
	result.write('}\n')

	result.write('.diff_next{\n')
	result.write('width: 15px;\n')
	result.write('background-color: silver\n')
	result.write('}\n')

	result.write('.diff_header{\n')
	result.write('width: 15px;\n')
	result.write('background-color: LightSteelBlue\n')
	result.write('}\n')

	result.write('.diff_sub{\n')
	result.write('background-color: LightYellow\n')
	result.write('}\n')

	result.write('.diff_add{\n')
	result.write('background-color: GreenYellow\n')
	result.write('}\n')

	result.write('.diff_chg{\n')
	result.write('background-color: Aquamarine\n')
	result.write('}\n')

	result.write('</style>')	
	result.write('</head>\n')
	result.write('<body>\n')

def create_html_footer(result):
	"""Writes HTML footer"""	
	result.write('</table>\n')
	result.write('</body>\n')
	result.write('</html>\n')
	
if __name__ == "__main__":
    run()

