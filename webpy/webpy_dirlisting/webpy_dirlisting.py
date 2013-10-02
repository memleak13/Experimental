#!/usr/bin/python
import os
import web

#Important: 
# 1. Template Files need to end with .html !!!!
# 2.App needs to be run with full path from the dir containing the script: 
#/Users/business/Desktop/Git/Experimental/webpy/webpy_dirlisting/webpy_dirlisting.py 

#Getting dir listing, duplicating each entry and adding as tupple to a list
files = os.listdir('./')
dd_values = []
for entry in files:
	t = entry, entry
	dd_values.append(t)

render = web.template.render('templates/')
urls = ('/', 'index',)
myform = web.form.Form(
	#web.form.Dropdown('source', [('value1', 'description1'), 
	#	('value2', 'description2')]),
	web.form.Dropdown('source', dd_values),
	web.form.Dropdown('target', dd_values),
	web.form.Button('compare')
	)

class index:
	def GET(self):
		f1 = myform()
		return render.formtest(f1)
	def POST(self):
		value = web.input()
		return (value.source + ' ' + value.target)

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()    