
import nmap
import os

nm = nmap.PortScanner()


print ("##################################################################################################################")
print ("# Welcome to DiscoAttack #")
print ("This tool is a prototype for Discovering, Testing the vulnerabilities, and analysing of the packets.\nThe Intention of this tool is only and only educational.")
print ("Thank you for yor using this tool.")
print ("##################################################################################################################\n")


print ("##################################################################################################################")
print ("Scan type: pingScan, osScan, udpScan")
print ("##################################################################################################################\n")

userInput = input("Please specify the type of scanning: ")

# Nmap ping scan function, with out put to outputs repo in .csv format.
def pingScan():
  print (userInput, "selected.\n")
  ip = input("Please enter an ip address range: ")
  print ("Network range acquired successfully.\n")
  print ("Attempting Ping scan...")
  nm.scan(hosts = ip, arguments='-sn')
  hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
  with open("outputs/pingscanresult.csv", "w") as scanout:
    for host, status in hosts_list:
      print(('{0}:{1}'.format(host, status)), file= scanout)
    scanout.close()
  print ("Look inside the outputs folder for scan result.")


# Nmap OS scan function
def osScan():
  print (userInput, "selected.\n")
  ip = input("Please enter an ip address to scan for OS type: ")
  print(nm.scan(hosts= ip, arguments=" -O")['scan'][ip]['osmatch'][1])

# Nmap Advanced scan function 
def advancedScan();

# Nmap 
    

  

if userInput == "pingScan":
  pingScan()
elif userInput == "osScan":
  osScan()
else:
  print ("Please specify a correct type of scan.")
