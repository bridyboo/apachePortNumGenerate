# Need to write exceptions try, catch, etc.
# Another bug found, if the exception is caught I think it closes out the window immediately could be wrong tho
# I think needs a function 'add multiple newPorts'
# Regardless I need to figure out how to keep track of all the new ports, either saved in a separate log, or saved in
# instance of the class as a global static variable (will look into it)
# should be assigned to APACHE port XXXX1 if available
import portCompare

query = input("Please enter the first 2 digit of lookup port: ")
result = portCompare.lookupPort(query)
sortedResult = sorted(result)

print("List of all ports that start with ", query)
print("LocalPort \tStatus\n------\t\t------")
for index, ports in enumerate(sortedResult):
    print(sortedResult[index], "\t\tListen")

result = portCompare.newPort(sortedResult) # Final result this is the unique Port
print("\nthis is the new unique port: ", result)
input("press 'enter' to continue")
print("\n\n*warning if using with TD this will only query the current state of the server, this means\n"
      "*until TEST has finished deploying port", str(result), ",this will always be the 'unique port' for this server\n"
      "*I will look further for a solution in the future for now there's still some 'manual' work needed\n"
      "-Matthew Brian Darmadi")

print("\npress 'enter' to exit...")
input()