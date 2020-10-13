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
    """
    Take in an array of four strings represting the bytes of an ip address
    and convert it back into decimal dot notation
    :param ip_addr_list: An array of four binary strings each
    representing one byte of ip_addr e.g. ['10000100', '11001110',
    '00010011', '00000111']
    :return: The ip address as a string in decimal dot notation e.g.
    '132.206.19.7'
    """
    # for each string in the list
    # use str(int(x,2)) to convert it into a decimal number
    # and then turn that number into a string e.g. '10000100' -> '132'
    # put all converted numbers into a list ["132","206","19","7"]
    # call ".".join on the list to merge them into a string separated by "."
    return ".".join([str(int(x,2)) for x in ip_addr_list])




def convert_decimal_to_binary(num): #This converts the given decimal number to binary.
    num = int(num)
    binary_list=[]
    result = ""

    #This uses a modulus to convert the decimal to a binary number which is the appended to a list.
    while(num > 0):
        binary_number = num % 2
        binary_list.append(binary_number)
        num = num // 2

    #The list is reverse as the binary_list as the number were inputed backwards.
    binary_list.reverse()

    #This creates a string of the binary in the binary_list.
    for i in binary_list:
        result = result + str(i)

    #This ensures that all binary numbers are eight digits long.
    if len(result) != 8:
        result = "0" * (8 - len(result)) + result
    return str(result)


def get_network_class(byte): #The first eight bits of the network address will identify the network class


    #Identifies if the IP address is a class A network.
    if int(byte) <= 127:
        class_type = "A"

    #Identifies if IP address is a class B network.
    elif int(byte) > 127 and int(byte) <= 191:
        class_type = "B"

    #Identifies if IP address is a class C network.
    elif int(byte) > 191 and int(byte) <= 223:
        class_type = "C"

    #Identifies if IP address is a class D network.
    elif int(byte) > 223 and int(byte) <= 239:
        class_type = "D"

    #Identifies if IP address is a class E network.
    elif int(byte) > 239 and int(byte) <= 255:
        class_type = "E"

    else:
        return ("Invalid network address")

    return class_type #returns a string eith the class of the inputted network.

def get_CIDR(subnet_mask_address): #converts the string to binary the counts the number of ones in the binary string to get the CIDR notation.
    return str(("".join(subnet_mask_address)).count("1"))

def get_subnets(subnet_mask, network_class):
    if network_class == "C":
        return str(2 ** subnet_mask[1].count("1"))

    elif network_class == "B":
        return str(2 ** "".join(subnet_mask[0:2]).count("1"))


def get_host_per_subnet(subnet_mask, network_class):
    if network_class == "C":
        return str(2 ** subnet_mask[1].count("0") - 2)

    elif network_class == "B":
        return str(2 ** "".join(subnet_mask[0:2]).count("0") - 2)

def get_valid_subnet(ip_addr_bytes, number_of_hosts, network_class):
    valid_subnet_list = [".".join(ip_addr_bytes)]
    counter = 0

    while counter != 192:
        counter = counter + 64
        if network_class == "C":
            new_byte = ".".join(ip_addr_bytes[0:3]) + "." + str(counter)
            valid_subnet_list.append(new_byte)

        elif network_class == "B":
            new_byte = ".".join(ip_addr_bytes[0:2]) + "." + str(counter) + "." + ip_addr_bytes[3]
            valid_subnet_list.append(new_byte)

    return valid_subnet_list


def get_broadcasting_address(valid_subnet, ip_addr_bytes, network_class):
    broadcast_list = []
    for address in valid_subnet[1:4]:
        address = address.split(".")
        if network_class == "C":
            broadcast_list.append(".".join(address[0:3])+ "." + str(int(address[3]) - 1))
            byte = address[2]

        elif network_class == "B":
            broadcast_list.append(".".join(address[0:2])+ "." + str(int(address[2]) - 1) + "." + "255")
            byte = 255

    broadcast_list.append(".".join(ip_addr_bytes[0:2]) + "." + str(byte) + "." + "255")
    return broadcast_list


def get_first_address(valid_subnet):
    first_address = [".".join(byte.split(".")[0:3]) + "." + str(int(byte.split(".")[3]) + 1) for byte in valid_subnet]
    return first_address

def get_last_address(broadcast_address):
    first_address = [".".join(byte.split(".")[0:3]) + "." + str(int(byte.split(".")[3]) - 1) for byte in broadcast_address]
    return first_address


#################################################################################
def get_subnet_stats(ip_addr,subnet_mask):
    ip_addr_bytes = ip_addr.split(".")
    subnet_mask_address = to_binary_string(subnet_mask)
    network_class = (get_network_class(ip_addr_bytes[0]))

    #Gets the CIDR notation and adds it to the end of the IP address.
    cidr_notation = get_CIDR(subnet_mask_address)
    print("Address: " + ip_addr + "/" + cidr_notation)

    #Calculating the subnets.
    subnets = get_subnets(subnet_mask_address[2:4], network_class)
    print("Subnets: " + subnets)

    #Calculating the addressable hosts per subnet.
    number_of_hosts = get_host_per_subnet(subnet_mask_address[2:4], network_class)
    print("Addressable hosts per subnet: " + number_of_hosts)

    #Creating the valid subnet subnet_mask_address.
    valid_subnet = get_valid_subnet(ip_addr_bytes, number_of_hosts, network_class)
    print("Valid subnets: " + str(valid_subnet))

    #Get the valid Broafcasting addresses
    broadcast_address = get_broadcasting_address(valid_subnet, ip_addr_bytes, network_class)
    print("Broadcast addresses: " + str(broadcast_address))

    first_address = get_first_address(valid_subnet)
    print("First addresses: " + str(first_address))

    last_address = get_last_address(broadcast_address)
    print("Broadcast addresses: " + str(last_address))






get_subnet_stats("172.16.0.0","255.255.192.0")
#get_subnet_stats("192.168.10.0","255.255.255.192")
#################################################################################
#def get_class_stats(ip_addr):
#    each_byte = ip_addr.split(".") #Slipt the eight bits into a list.
#
#    #Finds the clas of the network inputted and store it in a variable so it can be used in other tasks.
#    network_class = get_network_class(each_byte[0])
#    print("Class: " + network_class)
#
#    if network_class <= "C":
#        print("Network: " + str(2 ** classes[network_class]["network_bits"]))
#        print("Host: " + str(2 ** classes[network_class]['host_bits']))
#
#    elif network_class == "D" or network_class == "E":
#        print("Network: " + classes[network_class]["network_bits"])
#        print("Host: " + classes[network_class]['host_bits'])
#
#    print("First address:" + classes[network_class]["first_address"])
#    print("Last address:" + classes[network_class]["last_address"])


#get_class_stats("245.206.18.7")
