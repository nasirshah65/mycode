#!/usr/bin/env/ python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") #this line will add "dns" to the end of the list
protoa.append("dns") #this line will add 
print(proto)
proto2 = [22, 80, 443, 53] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument
print(proto)
protoa.append(proto2) # pass proot2 as an argument to the append method
print(protoa)

