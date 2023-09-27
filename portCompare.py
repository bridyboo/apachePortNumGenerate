# Calls psutil to lookup all listening TCP ports that start with a specific 2 digits.
# newPort is used to return a new port that isn't being used, avoiding duplicate ports.
# I guess technically I can specify how many digits the new ports are 33###
import psutil
import sys


# This method returns all ports that start with the first 2 digit of 'port_number'
# Returns the list of ports that start with the query-ed port numbers
def lookupPort(port_number):
    port = psutil.net_connections('tcp')
    result = set()  # Using a set to ensure unique port numbers

    previous_port = None

    for ports in port:
        laddr, localport = ports.laddr
        if str(localport).startswith(port_number) and ports.status == "LISTEN":
            if localport != previous_port:
                result.add(localport)
            previous_port = localport

    return sorted(result)


# This method returns a new apache port as a string of integer
# Catches exception if there are no ports available
# I need to sort here as well at the end
def generateNewPort(listOfPort):
    try:  # if list is 0 that means psutil didn't find any matching ports should catch exception here
        startingNum = min(listOfPort)  # startingNum is the smallest port in the list
    except ValueError:
        print("\n\n\tThere are no ports that start with the first 2 digit you are looking for\n")
        return

    newPort = startingNum + 1
    while newPort in listOfPort:
        newPort += 1

    listOfPort.append(newPort)
    return listOfPort  # Updates list of port, the last index is the new port.


# Need to expand on this with a global variable or composition
#
def newPort(listOfPort):
    try:  # if list is 0 that means psutil didn't find any matching ports should catch exception here
        lastIndex = len(listOfPort) - 1
    except TypeError:
        return

    newPort = listOfPort[lastIndex]
    return newPort
