from pygeocoder import Geocoder

address = "1222, Lins de Vasconcelos, Sao Paulo, SP"

print(Geocoder("api-key").geocode(address).coordinates)


