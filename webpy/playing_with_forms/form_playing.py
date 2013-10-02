#!/usr/bin/python
import os
import web
from web import net,utils

#Important: 
# 1. Template Files need to end with .html !!!!
# 2.App needs to be run with full path from the dir containing the script: 
#/Users/business/Desktop/Git/Experimental/webpy/playing_with_forms

#Creating a subclase of form and overwrite render so I can get rid of <table>

class CustomForm (web.form.Form):
    def render(self):
    #out = ''
    #out += self.rendernote(self.note)
    #out += '<table>\n'
	    out = '<div id="form">'
	    
	    for i in self.inputs:
	        html = (utils.safeunicode(i.pre) + i.render() 
	        	+ self.rendernote(i.note) + utils.safeunicode(i.post))
	        #if i.is_hidden():
	        #    out += '    <tr style="display: none;"><th></th><td>%s</td></tr>\n' % (html)
	        #else:
	            #out += '    <tr><th><label for="%s">%s</label></th><td>%s</td></tr>\n' % (i.id, net.websafe(i.description), html)

	        #to remove the label remove first %s and i.id !!
	        out += ('<div id="%s_div"> %s %s</div>' % 
	        	(i.id, net.websafe(i.description), html))
	    #out += "</table>"
	    out += "</div>"
	    return out	


#Getting dir listing, duplicating each entry and adding as tupple to a list
files = os.listdir('./')
dd_values = []
for entry in files:
	t = entry, entry
	dd_values.append(t)

render = web.template.render('templates/')
urls = ('/', 'index',)

myform = CustomForm(
	#web.form.Dropdown('source', [('value1', 'description1'), 
	#	('value2', 'description2')]),
	web.form.Dropdown('source', dd_values),
	web.form.Dropdown('target', dd_values),
	web.form.Button('compare')
	)

class index:
	def GET(self):
		f1 = myform()
		f2 = myform()
		return render.formtest(f1,f2,"test")
	def POST(self):
		value = web.input()
		return (value.source + ' ' + value.target)

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()    