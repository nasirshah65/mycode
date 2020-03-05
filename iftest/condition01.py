#!/usr/bin/env python3

hostname = "MTG"


if hostname =="MTG":
    print("The hostname was found to be mtg")

hostname = input("what value should we set for hostname?")

if hostname.lower() =="mtg":
    print("The hostname was found to be mtg")
elif hostname.lower()!="mtg":
    print("The hostname is not mtg")
