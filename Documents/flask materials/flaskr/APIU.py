from flask import Flask
from flask import render_template
from flask import request


import requests

APIU = Flask(__name__)
weather = ""

 

@APIU.route('/')
def indexA ():
    return render_template('indexA.html')

@APIU.route('/apiReq', methods = ['GET','POST'])
def apiReq ():
    if request.method == 'POST':
        cityName = request.form['cityName']
        print(cityName)
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ cityName +'&APPID=9ccd389d6515664d6c9d610aaca4113d')
        obj = r.json()
        weather = str(obj['weather'][0]['main'])
        temp_k = int(obj['main']['temp'])
        temp_f = (1.8*(temp_k-273) + 32)
        windsp = str(int(obj['wind']['speed']))
        humidity = int(obj['main']['humidity'])
        temp_min  = int(obj['main']['temp_min'])
        tempmax = int(obj['main']['temp_max'])
        highTemp = (1.8*(tempmax-273) + 32)
        temp_min = (1.8*(temp_min-273) + 32)

    return '<h1 style="font-family:courier;">  Weather:' + weather + ' <br/> Temprature(F) :'+ str(temp_f) +'<br/> Wind(mph): '+ str(windsp) + '<br/> Humidity:' +str(humidity) +'%<br/> High(F):'+str(highTemp)+' <br/> Low(F):'+str(temp_min)+'</h1>'
    
    

if __name__ == '__main__':
    APIU.run()