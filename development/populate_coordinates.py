import sqlite3
import requests
conn = sqlite3.connect(r'E:\scanner\Eastside Fire Alerts\data\data.sqlite3')
cur = conn.cursor()
cur.execute('SELECT station_number from Stations')
for station in [row[0] for row in cur.fetchall()]:
    cur.execute('SELECT station_address from Stations WHERE station_number = ?',(station,))
    address = cur.fetchone()
    city = input('What city is station {} in? '.format(station))
    response = requests.get('https://geocoding.geo.census.gov/geocoder/locations/address?benchmark=2020&street={}&city={}&state=WA&format=json'.format(address[0].replace(' ','+'),city)).json()['result']
    print(response)
    lat = response['addressMatches'][0]['coordinates']['y']
    lon = response['addressMatches'][0]['coordinates']['x']
    print(station,address,lat,lon)
    #cur.execute('UPDATE Station SET station_lat = ? WHERE station_id = ?',(lat,station))

#conn.commit()

#https://geocoding.geo.census.gov/geocoder/locations/address?benchmark=2020&street=9621+NE+24th+St&city=bellevue&state=WA&format=json