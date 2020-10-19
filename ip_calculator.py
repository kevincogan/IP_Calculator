classes={
    'A':{
        'network_bits':7,
        'host_bits':24,
        'first_address': "0" + (".0" * 3),
        'last_address': "127" + (".255" * 3),
        'subnet_mask': "0"
        },
    'B':{
        'network_bits':14,
        'host_bits':16,
        'first_address': "128" + (".0" * 3),
        'last_address': "191" + (".255" * 3)
        },
    'C':{
        'network_bits':21,
        'host_bits':8,
        'first_address': "192" + (".0" * 3),
        'last_address': "223" + (".255" * 3)
        },
    'D':{
        'network_bits':'N/A',
        'host_bits':'N/A',
        'first_address': "224" + (".0" * 3),
        'last_address': "239" + (".255" * 3)
        },
    'E':{
        'network_bits':'N/A',
        'host_bits':'N/A',
        'first_address': "240" + (".0" * 3),
        'last_address': "225" + (".255" * 3)
        },
        }

def to_binary_string(ip_addr):
    #split into array of four ["136","206","19","9"]
    byte_split = ip_addr.split(".")
    # convert each number into a int, format it as binary, turn it back intoa stirng
    # and return it as an array, isn't python great !
    return ['{0:08b}'.format(int(x)) for x in byte_split]



def to_decimal_dot(ip_addr_list):
    # for each string in the list
    # use str(int(x,2)) to convert it into a decimal number
    # and then turn that number into a string e.g. '10000100' -> '132'
    # put all converted numbers into a list ["132","206","19","7"]
    # call ".".join on the list to merge them into a string separated by "."
    return ".".join([str(int(x,2)) for x in ip_addr_list])


def get_network_class(byte): #The first eight bits of the network address will identify the network class

    #Identifies if the IP address is a class A network.
    if int(byte) <= 127: #Range of network A.
        class_type = "A"

    #Identifies if IP address is a class B network.
    elif int(byte) > 127 and int(byte) <= 191: #Range of network B.
        class_type = "B"

    #Identifies if IP address is a class C network.
    elif int(byte) > 191 and int(byte) <= 223: #Range of network C.
        class_type = "C"

    #Identifies if IP address is a class D network.
    elif int(byte) > 223 and int(byte) <= 239: #Range of network D.
        class_type = "D"

    #Identifies if IP address is a class E network.
    elif int(byte) > 239 and int(byte) <= 255: #Range of network E.
        class_type = "E"

    else:
        return ("Invalid network address")

    return class_type #returns a string eith the class of the inputted network.

#Converts the string to binary the counts the number of ones in the binary string to get the CIDR notation.
def get_CIDR(subnet_mask_address):
    return str(("".join(subnet_mask_address)).count("1")) #Counts and retuns the number of ones.

#Calcuates the number of subnets by counting the number of ones in the host bytes and putting that value over the power of two.
def get_subnets(subnet_mask, network_class):

    if network_class == "C":
        return str(2 ** subnet_mask[2:3].count("1")) #Gets the class C host bytes, counts the ones, and puts the value over the power of two.

    elif network_class == "B":
        return str(2 ** "".join(subnet_mask[1:3]).count("1")) #Gets the class B host bytes, counts the ones, and puts the value over the power of two.

    elif network_class == "A":
        return str(2 ** "".join(subnet_mask[0:3]).count("1")) #Gets the class A host bytes, counts the ones, and puts the value over the power of two.

#This calculates of addressable host for each class
def get_host_per_subnet(subnet_mask, network_class):

    #Calculates the the addressable host for class C by counting all the zeros in the host bytes, putting that value to the power of two, then substracting 2.
    if network_class == "C":
        return str(2 ** subnet_mask[2:3].count("0") - 2)

    #Calculates the the addressable host for class B by counting all the zeros in the host bytes, putting that value to the power of two, then substracting 2.
    elif network_class == "B":
        return str(2 ** "".join(subnet_mask[1:3]).count("0") - 2)

    #Calculates the the addressable host for class A by counting all the zeros in the host bytes, putting that value to the power of two, then substracting 2.
    elif network_class == "A":
        return str(2 ** "".join(subnet_mask[0:3]).count("0") - 2)

#Gets all the valid subnets for Class A, B, and C.
def get_valid_subnet(ip_addr_bytes, network_class, subnet_mask):

    if network_class == "C": #This identifys what class the IP address belongs to so we can assign the correct postfixes and get the correct portion of the subnet mask to calculate the valid addresses.
        byte_limit = (subnet_mask.split("."))[3] #This gives us the host value of the byte directly after the network_bytes, this allows us to find the value that tells our loop below when to stop.
        postfix = "" #This applies the appropriate ending to the subnet depending on the class the IP address belongs to.
        index = 3 #provides the appropriate index to format the subnet correctly.

    elif network_class == "B": #This identifys what class the IP address belongs to so we can assign the correct postfixes and get the correct portion of the subnet mask to calculate the valid addresses.
        byte_limit = (subnet_mask.split("."))[2] #This gives us the host value of the byte directly after the network_bytes, this allows us to find the value that tells our loop below when to stop.
        postfix = "." + ip_addr_bytes[3] #This applies the appropriate ending to the subnet depending on the class the IP address belongs to.
        index = 2 #provides the appropriate index to format the subnet correctly.

    elif network_class == "A": #This identifys what class the IP address belongs to so we can assign the correct postfixes and get the correct portion of the subnet mask to calculate the valid addresses.
        ip_addr_bytes[1] = "0" # This formats the IP address to create a first valid address.
        byte_limit = (subnet_mask.split("."))[1] #This gives us the host value of the byte directly after the network_bytes, this allows us to find the value that tells our loop below when to stop.
        postfix = "." + ip_addr_bytes[2] +"." + ip_addr_bytes[3] #This applies the appropriate ending to the subnet depending on the class the IP address belongs to.
        index = 1 #provides the appropriate index to format the subnet correctly.

    valid_subnet_list = [".".join(ip_addr_bytes)] #Here we add the first formatted valid ip address into the list, format is determined by the boolean statements above which identifies the class of the IP address.

    counter = 0 #Initialises the counter to 0.
    while counter < int(byte_limit): #This loop will continue looping until the counter is greater than the the first host byte after the network bytes in the subnet mask.
        counter = counter + (256 - int(byte_limit)) #Finds how many bits to increment by for the valid subnets
        valid_subnet = ".".join(ip_addr_bytes[0:index]) + "." + str(counter) + postfix #This formats the information above into a valid subnet.
        valid_subnet_list.append(valid_subnet) #The valid subnet is add to the valid subnet list.

    return valid_subnet_list

#Gets a list of broadcasting addresses for the IP addresses
def get_broadcasting_address(valid_subnet, ip_addr_bytes, network_class):
    broadcast_list = [] #Contains all broadcasting address.

    #Gets the values from valid subnet to calculate the broadcast address.
    for address in valid_subnet[1:4]:
        address = address.split(".") #splits each byte.

        if network_class == "C": #Checks the class of the IP address.
            broadcast_list.append(".".join(address[0:3])+ "." + str(int(address[3]) - 1)) #Takes the subnet value,starting from the second in the list, and subtracts one from the last byte.
            index = 3 #Index to format the final broadcating address below.
            postfix = ".255" # postfix to format the final broadcating address below.

        elif network_class == "B": #Checks the class of the IP address.
            broadcast_list.append(".".join(address[0:2])+ "." + str(int(address[2]) - 1) + "." + "255") #Takes the subnet value,starting from the second in the list, and subtracts one from the last byte plus the 255 ending added in.
            index = 2 #Index to format the final broadcating address below.
            postfix = ".255" * 2 # postfix to format the final broadcating address below.

        elif network_class == "A": #Checks the class of the IP address.
            broadcast_list.append(".".join(address[0:1])+ "." + str(int(address[1]) - 1) + ".255" * 2) #Takes the subnet value,starting from the second in the list, and subtracts one from the last byte plus the 255 * 2 ending added in.
            index = 1 #Index to format the final broadcating address below.
            postfix = ".255" * 3 # postfix to format the final broadcating address below.

    broadcast_list.append(".".join(ip_addr_bytes[0:index]) + postfix) #creates the last broadcasting address and adds it to the broadcast list.
    return broadcast_list

#Finds the first address of the IP address.
def get_first_address(valid_subnet):
    first_address = [".".join(byte.split(".")[0:3]) + "." + str(int(byte.split(".")[3]) + 1) for byte in valid_subnet] #The valid subnet list is taken and one bit is added to the last byte of every subnet address to make the first address.
    return first_address

#Finds the last address of the IP address.
def get_last_address(broadcast_address):
    last_address = [".".join(byte.split(".")[0:3]) + "." + str(int(byte.split(".")[3]) - 1) for byte in broadcast_address] #The broadcast address is used and one bit is substracted from the last byte of every address
    return last_address

#finds all the bytes that the addresses have in common.
def common_bytes(addresses):
    index = 0
    common_bytes = []
    flag = True
    binary_addresses = [to_binary_string(address) for address in addresses] # Converts all the addresses into a binary string.
    binary_addresses = ["".join(address) for address in binary_addresses] #Joins each binary byte together in each sublist.

    #Compares each string to find the common bytes in all four address.
    while index != len(binary_addresses[0]) and flag == True: #Loops through the list until no more bits in common or reaches the end of the list.
        if binary_addresses[0][index] == binary_addresses[1][index] and binary_addresses[2][index] == binary_addresses[3][index] and binary_addresses[1][index] == binary_addresses[2][index] and binary_addresses[0][index] == binary_addresses[3][index]: #checks if the indexed address are all equal.
            common_bytes.append(binary_addresses[0][index]) #Same bit are appended to the common_bytes list.
            flag = True #Flag indicastes to a loop that a common bit was found and allow the loop to continue.
        else:
            flag = False #Flag indicates to the loop that common bit was not found and the loop will stop.
        index += 1 #Move onto the next indexed bit in the list.

    return "".join(common_bytes) #Join all the common bits in the list and return.

#This will make the network mask for the fiven addresses.
def get_network_mask(same_bytes):
    post_fix_bits = 32 - len(same_bytes) #Calcuates the number of zeros in the binary subnet mask.
    network_mask = "1" * len(same_bytes) + ("0" * post_fix_bits) #Creates the network mask in binary

    network_mask_list = [network_mask[0:8], network_mask[8:16], network_mask[16:24], network_mask[24:32]] #Formates the network mask into a list with sublist to be converted into decimal dot notation.
    return to_decimal_dot(network_mask_list) #Converts binary list to decimal dot notation.

#################################################################################
#def get_supernet_stats(addresses):
#    #Gets a list of the same bytes from the inputed addresses.
#    same_bytes = common_bytes(addresses)
#    print("Address: " + addresses[0] + "/" + str(len(same_bytes))) #Formatting onto an address and finding the length of the common bits for to create CIDR Notation.
#
#    #retrieves the network mask.
#    network_mask = get_network_mask(same_bytes)
#    print("Network: " + network_mask) #Formatting for output.
#
#
#get_supernet_stats(["205.100.0.0","205.100.1.0","205.100.2.0","205.100.3.0"])
#################################################################################
#def get_subnet_stats(ip_addr,subnet_mask):
#    ip_addr_bytes = ip_addr.split(".")
#    subnet_mask_address = to_binary_string(subnet_mask)
#    network_class = (get_network_class(ip_addr_bytes[0]))
#
#    #print(network_class)
#
#    #Gets the CIDR notation and adds it to the end of the IP address.
#    cidr_notation = get_CIDR(subnet_mask_address)
#    print("Address: " + ip_addr + "/" + cidr_notation)
#
#    #Calculating the subnets.
#    subnets = get_subnets(subnet_mask_address[1:4], network_class)
#    print("Subnets: " + subnets)
#
#    #Calculating the addressable hosts per subnet.
#    number_of_hosts = get_host_per_subnet(subnet_mask_address[1:4], network_class)
#    print("Addressable hosts per subnet: " + number_of_hosts)
#
#    #Creating the valid subnet subnet_mask_address.
#    valid_subnet = get_valid_subnet(ip_addr_bytes, network_class,subnet_mask)
#    print("Valid subnets: " + str(valid_subnet))
#
#    #Get the valid Broafcasting addresses
#    broadcast_address = get_broadcasting_address(valid_subnet, ip_addr_bytes, network_class)
#    print("Broadcast addresses: " + str(broadcast_address))
#
#    first_address = get_first_address(valid_subnet)
#    print("First addresses: " + str(first_address))
#
#    last_address = get_last_address(broadcast_address)
#    print("Last addresses: " + str(last_address))
#
#get_subnet_stats("127.16.0.0", "255.192.0.0")
#get_subnet_stats("172.16.0.0","255.255.192.0")
#get_subnet_stats("192.168.10.0","255.255.255.192")
#################################################################################
def get_class_stats(ip_addr):
    each_byte = ip_addr.split(".") #Slipt the eight bits into a list.

    #Finds the clas of the network inputted and store it in a variable so it can be used in other tasks.
    network_class = get_network_class(each_byte[0])
    print("Class: " + network_class)

    if network_class <= "C":
        print("Network: " + str(2 ** classes[network_class]["network_bits"]))
        print("Host: " + str(2 ** classes[network_class]['host_bits']))

    elif network_class == "D" or network_class == "E":
        print("Network: " + classes[network_class]["network_bits"])
        print("Host: " + classes[network_class]['host_bits'])

    print("First address:" + classes[network_class]["first_address"])
    print("Last address:" + classes[network_class]["last_address"])


get_class_stats("200.206.18.7")
