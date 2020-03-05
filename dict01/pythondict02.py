#!/usr/bin/env python3

switch = {"hostname": "sw1", "ip" : "10.0.1.1", "version" : "1.2", "vendor": "cisco"}

print( switch["hostname"])
print( switch["ip"])

print( switch["lynx"])

print( "First test - .get()")
print( switch.get("lynx"))

print("Third test - .get()"))
print( switch.get("version"))

print( "Fourth test - .keys()")
print(switch.keys())

print( "Fifth Test - .values()")
print(switch.values())
