import sqlite3

conn = sqlite3.connect(r'E:\scanner\Eastside Fire Alerts\data\data.sqlite3')
cur = conn.cursor()

while True:
    station_number = int(input('What is the station number? '))
    station_jurisdiction = input('What is the station jurisdiction? ') #BVFD BOFD KIFD MIFD KCFD45 ESFR KCFD27 RDFD SFD SKYFD SNOFD SPFR
    station_address = input('What is the station address? ')
    print('\n')
    while True:
        unit_id = int(input('What is the unit number? '))
        if unit_id == 0:
            break
        unit_type = input('What is the unit\'s type? ').upper() # ENGINE LADDER RESCUE AID MEDIC HAZMAT BRUSH TENDER BATTALION AIR CHIEF DIVE BOAT MSO LF MCI K MIDI MARSHAL ATV DECON UAS REHAB
        unit_extended_name = input('What is the unit\'s extended name? ').title()
        unit_shortened_name = input('What is the unit\'s shortened name? ').upper()
        
        u_data = (unit_id,unit_extended_name,unit_shortened_name,unit_type,station_number)
        cur.execute('INSERT INTO Units (unit_number,unit_extended_name,unit_shortened_name,unit_type,unit_station) VALUES (?,?,?,?,?)',u_data)
        print('\n')
    cur.execute('INSERT INTO Stations (station_number,station_jurisdiction,station_address) VALUES (?,?,?)',(station_number,station_jurisdiction,station_address))
    print('\n')
    conn.commit()