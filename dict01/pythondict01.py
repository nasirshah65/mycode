#!/usr/bin/env pyton3
#create a dir
switch = {"hostname" : "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

#display pats of dic
print( switch["hostname"])
print(switch["ip"])

print(switch["lynx"])


print("first test - .get()")
print(switch.get("lynx"))

print("Second test - .get()")
print(switch.get("lynx", "The Key is another Castle!"))

print( "Third test - .get()")
print( switch.get("version"))

print("Fourth test - .keys()")
print(switch.keys())

print("Fifth test - .values()")
print(switch.vales())

