# Calls psutil to lookup all listening TCP ports that start with a specific 2 digits.
# newPort is used to return a new port that isn't being used, avoiding duplicate ports.
import psutil


# This method returns all ports that start with the first 2 digit of 'port_number'
# Returns the list of ports that start with the query-ed port numbers
def lookupPort(port_number):
    port = psutil.net_connections('tcp')
    list = []

    for ports in port:
        laddr, localport = ports.laddr  # this is the localport from the port[] tuple
        if str(localport).startswith(port_number):
            list.append(localport)

    return list


# This method returns a new apache port as a string of integer
# Catches exception if there are no ports available
def newPort(listOfPort):
    try:  # if list is 0 that means psutil didn't find any matching ports should catch exception here
        startingNum = listOfPort[0]
    except IndexError:
        print("There are no ports that start with the first 2 digit you are looking for")
        return

    for index, newPort in enumerate(
            listOfPort):  # If startingNum is equal to the port in the list add by 1 until unique portNum
        if startingNum == listOfPort[index]:
            startingNum += 1

    return startingNum
