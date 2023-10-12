t = ()
print(type(t)) # tuple

coordsGps = (45.9632, 21.7891)
print(coordsGps)
print("Latitude", coordsGps[0])
print("Longitude", coordsGps[1])

# Les tuples ne sont accessibles qu'en lecture seule
#coordsGps[0] = 46.8899
#coordsGps.append(43.4344) # AttributeError: 'tuple' object has no attribute 'append'

lat, lng = coordsGps # tuple unpacked
print(lat, lng)