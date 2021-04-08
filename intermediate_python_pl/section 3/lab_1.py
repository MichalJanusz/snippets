ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connections = [(port1, port2) for port1 in ports for port2 in ports]
print(connections)
print(len(connections))

connections = [(port1, port2) for port1 in ports for port2 in ports if port1 != port2]
print(connections)
print(len(connections))

connections = [(port1, port2) for port1 in ports for port2 in ports if port1 < port2]
print(connections)
print(len(connections))
