# Need to write exceptions try, catch, etc.
# Another bug found, if the exception is caught I think it closes out the window immediately could be wrong tho
# should be assigned to APACHE port XXXX1 if available
import portCompare

query = input("Please enter the first 2 digit of lookup port: ")
result = portCompare.lookupPort(query)
sortedResult = sorted(result)

print("List of all ports that start with ", query)
for index, ports in enumerate(sortedResult):
    print(sortedResult[index])

print("\nthis is the new unique port: ", portCompare.newPort(sortedResult))
input()