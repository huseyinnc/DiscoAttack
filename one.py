from cmath import pi
from operator import truediv
import nmap


nm = nmap.PortScanner()


print ("##################################################################################################################")
print ("# Welcome to DiscoAttack #")
print ("This tool is a prototype for Discovering, Testing the vulnerabilities, and analysing of the packets.\nThe Intention of this tool is only and only educational.")
print ("Thank you for yor using this tool.")
print ("##################################################################################################################\n")


##############################################################################################
# The network discovery part starts here.
##############################################################################################






ip = input("Please enter an ip address range: ")
print ("Network range acquired successfully.\n")
print ("##################################################################################################################")
print ("Scan type: pingScan, osScan, udpScan")
print ("##################################################################################################################\n")

userInput = input("Please define the type of scanning: ")

def pingScan():
  print(nm.scan(hosts = ip, arguments = "-sn"))




while (True):
    if userInput == "pingScan":
        pingScan()
    else:
        print ("Please specify a type of scan.")
