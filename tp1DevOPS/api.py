from requests import Request, Session, Response
import os

def weather(lat, lon, apiKey):
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'lat': lat,
            'lon': lon,
            'appid': apiKey
        }
        sess = Session()
        req = Request('GET', url, params=params)
        prepped = req.prepare()
        resp = sess.send(prepped)
        return resp.json()
    except Exception as e:
        return e


lat = os.environ['LAT']
lon = os.environ['LONG']
apiKey = os.environ['API_KEY']

print(weather(lat,lon,apiKey))