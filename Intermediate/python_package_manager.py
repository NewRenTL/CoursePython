### Python Package Manager ###

# PIP
def separated_lines():
    print("-"*20)

import numpy

print(numpy.version.version)
numpy_array = numpy.array([35,20,56,23,11,23,111,650])
print(type(numpy_array))
print(numpy_array*2)

import requests
import json

json_file = open("Intermediate/my_pokes.json","w+");
response = requests.get("https://pokeapi.co/api/v2/pokedex")
json.dump(response.json(),json_file,indent=4)
json_file.close()

print(response)
#print(response.json())


separated_lines()
# Arithmetics Package
print("Using my own package arithmetics")
from my_package import arithmetics_x

print(arithmetics_x.sum_x(1,2))