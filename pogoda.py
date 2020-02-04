import pyowm
import config


def getpogoda(x, y):
    result = []
    key = config.owm
    owm = pyowm.OWM(key, language='ua')
    # observation = owm.weather_at_place(location)
    observation = owm.weather_around_coords(x, y)
    print('Coordinates >>',  x, y)
    # print ('>>>>>>>>>>>>>', observation, len(observation))
    for w in observation:
        print(w.get_location())
    w = observation[0].get_weather()
    # print (">>>>>>", observation_list)
    if w.get_status() == 'Clouds':
        xm = 'хмарно'
    else:
        xm = 'ясно'

    p = {'wind_spped': w.get_wind()['speed'],
           'wologist': w.get_humidity(),
             'temp': w.get_temperature('celsius')['temp'],
             'temp_max': w.get_temperature('celsius')['temp_max'],
             'temp_min': w.get_temperature('celsius')['temp_min'],
             'hmarnist': xm
            }

    return p


if __name__ == "__main__":

    # fl =  getpogoda('London,GB')
    fl = getpogoda(48.139946, 23.029067)
    print(fl)
