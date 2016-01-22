print "\nBRANDON WONG - Required HW Week 1"
print "\n"

#Part 1

print "\nPART 1" #Title
print "\n" #New empty opening paragraph
import csv
with open('C:\Users\Brandon\SG_DAT1\data\drinks.csv', 'rU') as f:
	header = csv.reader(f).next()
	data = [row for row in csv.reader(f)]
	print header

print "\n" #New empty closing paragraph

#Part 2

print "\nPART 2"
print "\n"
beers = [int(row[1]) for row in data]
print "beers == ", beers
print "len(beers) == ", len(beers)

print "\n"

#Part 3

print "\nPART 3"
print "\n"
NA_beers = [int(row[1]) for row in data if row[5].upper() == 'NA']
print "NA_beers == ", NA_beers
print "len(NA_beers) == ", len(NA_beers)

print "\n" #just to differentiate

EU_beers = [int(row[1]) for row in data if row[5].upper() == 'EU']
print "EU_beers == ", EU_beers
print "len(EU_beers) == ", len(EU_beers)

print "\n"


#Part 4

print "\nPART4"
print "\n"
NA_avg = round(float(sum(NA_beers))/len(NA_beers),2)
print "NA_avg == ", NA_avg

print "\n"

EU_avg = round(float(sum(EU_beers))/len(EU_beers),2)
print "EU_avg == ", EU_avg

print "\n"


#Part 5

print "\nPART 5"
print "\n"
avg_dict = {"NA":NA_avg, "EU":EU_avg}
output_folder = 'C:\\Users\\Brandon\\SG_DAT1_Brandon\\' #need double slash "\\" to clearly define folder
outputfile_name = 'avg_beer.csv' #no need to add "\" before outputfile_name
outputfile_path = output_folder + outputfile_name
with open(outputfile_path,'wb') as outputfile:
    outputwriter = csv.writer(outputfile)
    outputwriter.writerow(['continent','avg_beer'])
    for continent in avg_dict:
        outputwriter.writerow([continent,avg_dict[continent]])
print "wrote output to %s" % outputfile_path

print "\n"


#Part 6

print "\nPART 6"
print "\n"

import requests

api_endpoint = 'http://api.openweathermap.org/data/2.5/forecast/city'

params = {}
params['id'] = 1880252 #Singapore ID
params['units'] = 'metric'
params['APPID'] = '85c936ecf55d1973bf69098c9e5b62f1' #unique APPID
request = requests.get(api_endpoint, params = params)

data = request.json()
city_data = data['city']
city_name = city_data['name']
country_code = city_data['country']
lat = city_data['coord']['lat']
lon = city_data['coord']['lon']
print "Working on %s in %s (lat %s and lon %s)" % (city_name, country_code, lat, lon)

weather_data = data['list']
from datetime import datetime
format_string = '%Y-%m-%d %H:%M:%S'
dates = [datetime.strptime(row['dt_txt'], format_string) for row in weather_data]
temperatures = [row['main']['temp'] for row in weather_data]
humidities = [row['main']['humidity'] for row in weather_data]
for data_row in zip(dates,temperatures,humidities):
    print data_row

print "\n"


#Part 7

print "\nPART 7"
print "\n"

import matplotlib.pyplot as plt

pressures = [row['main']['pressure'] for row in weather_data]
plt.xlabel("Time")
plt.ylabel("Pressure [hPa]")
plt.title("Pressure in Singapore")
plt.plot(dates,pressures)
plt.show()
print "Graph printed out"

print "\n"


#Part 8

print "\nPART 8"
print "\n"

fig, ax1 = plt.subplots()
temp_scatter = ax1.scatter(pressures,temperatures, label='Temperature')
ax1.set_xlabel("Pressure [hPa]")
ax1.set_ylabel("Temperature [C]")
ax2 = ax1.twinx()
pres_scatter = ax2.scatter(pressures,humidities, marker='x', color='r', label='Humidity')
ax2.set_ylabel("Humidity [%]")
plt.legend(handles = [temp_scatter, pres_scatter])
plt.title("Pressure vs Temperature & Humidity: Singapore")
plt.show()
print "Scatterplot printed out"