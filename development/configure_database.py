import sqlite3

conn = sqlite3.connect(r'E:\scanner\Eastside Fire Alerts\data\data.sqlite3')
cur = conn.cursor()

cur.execute('''
CREATE TABLE Units (
    unit_id SERIAL PRIMARY KEY,
    unit_number INTEGER,
    unit_extended_name VARCHAR(255),
    unit_shortened_name VARCHAR(255),
    unit_type VARCHAR(255),
    unit_station INTEGER
)''')

cur.execute('''
CREATE TABLE Stations (
    station_number INTEGER PRIMARY KEY,
    station_jurisdiction VARCHAR(255),
    station_address VARCHAR(255)
)
''')

conn.commit()
cur.close()
conn.close()