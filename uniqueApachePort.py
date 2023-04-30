# Need to write exceptions try, catch, etc.
# Regardless I need to figure out how to keep track of all the new ports, either saved in a separate log, or saved in
# instance of the class as a global static variable (will look into it)
# Currently if there is no existing port it will show the user, 'none' for new ports, when it should be XX001
# should be assigned to APACHE port XXXX1 if available
import portCompare

while True:
    query = input("Please enter the first 2 digit of lookup port: ")
    result = portCompare.lookupPort(query)

    print("List of all ports that start with ", query)
    print("LocalPort \tStatus\n------\t\t------")
    for index, ports in enumerate(result):
        print(result[index], "\t\tListen")

    print("\nPress 'enter' to generate new ports, press 'n' to end the program")
    print("These the new unique ports: ")
    count = 0
    while True:  # generate multiple ports maybe
        result = portCompare.generateNewPort(result)  # Final result this is the unique Port
        print(portCompare.newPort(result))
        user_input = input()
        if user_input == 'n':
            count += 1
            break

    print("\npress 'e' to exit...")
    print("press 'enter' to lookup Ports...")
    user_input = input()
    if user_input == 'e':
        break

print("developed by Matthew Brian Darmadi, thank you.")
input()