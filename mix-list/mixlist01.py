#!/use/bin/env python3
my_list = ["192,168.0.05",5060, "UP"]
print("The first item on the list (IP):" +my_list[0])
print("The second item in the lsit (port):" +str(my_list[1]))
print("The third item on the list (state):" +my_list[2])
new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]
When I ssh into IP Address 10.0.0.1 or 10.20.30.1 I am unable to ping ports 5060, 80, or 55.
