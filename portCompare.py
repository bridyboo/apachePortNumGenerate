# Calls psutil to lookup all listening TCP ports that start with a specific 2 digits.
# newPort is used to return a new port that isn't being used, avoiding duplicate ports.
# I guess technically I can specify how many digits the new ports are 33###
import psutil
import sys

# This method returns all ports that start with the first 2 digit of 'port_number'
# Returns the list of ports that start with the query-ed port numbers
def lookupPort(port_number):
    port = psutil.net_connections('tcp')
    list = []

    for ports in port:
        laddr, localport = ports.laddr  # this is the localport from the port[] tuple
        if str(localport).startswith(port_number) and ports.status == "LISTEN":  # only listening and startswith ports
            list.append(localport)

    return sorted(list)

# This method returns a new apache port as a string of integer
# Catches exception if there are no ports available
def generateNewPort(listOfPort):
    try:  # if list is 0 that means psutil didn't find any matching ports should catch exception here
        startingNum = listOfPort[0]
    except IndexError:
        print("There are no ports that start with the first 2 digit you are looking for")
        sys.exit()

    for index, newPort in enumerate(listOfPort):
        if startingNum == listOfPort[index]:
            startingNum += 1
    listOfPort.append(startingNum)
    return listOfPort  # Updates list of port, the last index is the new port.

# Need to expand on this with a global variable or composition
#
def newPort(listOfPort):
    try:  # if list is 0 that means psutil didn't find any matching ports should catch exception here
        startingNum = listOfPort[0]
    except IndexError:
        sys.exit()

    lastIndex = len(listOfPort) - 1
    newPort = listOfPort[lastIndex]
    return newPort


