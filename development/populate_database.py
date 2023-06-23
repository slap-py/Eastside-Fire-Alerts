import sqlite3

conn = sqlite3.connect(r'E:\scanner\Eastside Fire Alerts\data\data.sqlite3')
cur = conn.cursor()

while True:
    station_number = int(input('What is the station number? '))
    station_jurisdiction = input('What is the station jurisdiction? ')
    station_address = input('What is the station address? ')
    while True:
        unit_id = int(input('What is the unit number? '))
        if unit_id == 0:
            break
        unit_extended_name = input('What is the unit\'s extended name? ')
        unit_shortened_name = input('What is the unit\'s shortened name? ')
        unit_type = input('What is the unit\'s type? ')
        u_data = (unit_id,unit_extended_name,unit_shortened_name,unit_type,station_number)
        cur.execute('INSERT INTO Units (unit_id,unit_extended_name,unit_shortened_name,unit_type,unit_station) VALUES (?,?,?,?,?)',u_data)
    cur.execute('INSERT INTO Stations (station_number,station_jurisdiction,station_address) VALUES (?,?,?)',(station_number,station_jurisdiction,station_address))
    conn.commit()