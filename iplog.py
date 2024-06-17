from pyfiglet import figlet_format                      from socket import gethostbyname                        from os import system                                                                                           system("clear")                                                                                                 print("\033[31m"+figlet_format("Ip4Log"))                                                                       print("_"*64+"\n")                                      Input = input("\033[32m"+"Link_Address: ")                                                                      get_ip = gethostbyname(Input)                                   from pyfiglet import figlet_format
from socket import gethostbyname
from os import system

system("clear")

print("\033[31m"+figlet_format("Ip4Log"))

print("_"*64+"\n")
Input = input("\033[32m"+"Link_Address: ")

get_ip = gethostbyname(Input)

print("\n"+get_ip)
