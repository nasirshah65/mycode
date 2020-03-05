#!/use/bin/env python3
my_list = ["192,168.0.05",5060, "down"]
print("The first item on the list (IP):" +my_list[0])
print("The second item in the list (port):" +str(my_list[1]))
print("The third item on the list (state):" +my_list[2])
new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]
print("When I " +new_list[5], " into IP Address:" +new_list[3])
print("or " +new_list[4] + " I am unable to ping ports")
print(+new_list[0], ", " +new_list[1],  ", or ",  +new_list[2])
