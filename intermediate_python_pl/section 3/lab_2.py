ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connections = ((port1, port2) for port1 in ports for port2 in ports)
counter = 0
for conn in connections:
    print(conn, end='')
    counter += 1
else:
    print('')
print(counter)

connections = ((port1, port2) for port1 in ports for port2 in ports if port1 != port2)
counter = 0
for conn in connections:
    print(conn, end='')
    counter += 1
else:
    print('')
print(counter)

connections = ((port1, port2) for port1 in ports for port2 in ports if port1 < port2)
counter = 0
for conn in connections:
    print(conn, end='')
    counter += 1
else:
    print('')
print(counter)
