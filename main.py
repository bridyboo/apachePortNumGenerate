# Need to write exceptions try, catch, etc.
# 1 specific exception is if the 2 digit lookup port doesn't exist; needs to show "port doesn't exist" instead of
# exception
# input() at the end so it doesn't close the window immediately
#
import portCompare

query = input("Please enter the first 2 digit of lookup port: ")
result = portCompare.lookupPort(query)
sortedResult = sorted(result)

print("List of all ports that start with ", query)
for index, ports in enumerate(sortedResult):
    print(sortedResult[index])

print("\nthis is the new unique port: ", portCompare.newPort(sortedResult))
input()