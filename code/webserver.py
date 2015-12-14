#!/usr/bin/enc python
import MySQLdb
import web
import json
#import newtable
from time import strftime
from web import form

render = web.template.render('templates/')
db = web.database(dbn='mysql', user='root',pw='921104',db='IoTproject')

urls=(
	'/','index','/submit','submit'
)


global new
new = MySQLdb.connect("localhost","root","921104",'IoTproject')
global cursor
cursor = new.cursor()

control = form.Form(
	form.Dropdown('weather',[('sunny','sunny'),('rainy','rainy'),('snowy','snowy'),('cloudy','cloudy')]),
	form.Dropdown('color',[('red','red'),('green','green'),('blue','blue'),('yellow','yellow')]),
	form.Button("submit", type="submit", description="submit"),

)

class index:
	def GET(self):
		f = control()
		#print f.render()
		cursor.execute ("select weather, color from controller")
	        table = cursor.fetchall ()
        	#new.close()
        	tp = [0,0]
        	UserData = [["Weather","Color"]]
       		for row in table:
                	weather = row[0] #transform the format of IPs
                	color = row[1]
                	tp = [weather, color]
                	UserData.append(tp)
		return render.controlnew(f,json.dumps(UserData))
	def POST(self):
		f = control()
		if not f.validates():
			return render.control(f,json.dumps(UserData))
        	else:
			print f.d.weather
			print f.d.color
			print "==================="
			#db.update('controller', where = "weather='"+f.d.weather+"'", color = f.d.color)
			cursor.execute("UPDATE controller SET color='"+f.d.color+"' WHERE weather='"+f.d.weather+"'")
			new.commit()
			cursor.execute("select weather, color from controller")
	        	table = cursor.fetchall ()
        		#new.close()
        		tp = [0,0]
        		UserData = [["Weather","Color"]]
       			for row in table:
                		weather = row[0] #transform the format of IPs
                		color = row[1]
                		tp = [weather, color]
                		UserData.append(tp)
        		return render.controlnew(f,json.dumps(UserData))	


if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()

