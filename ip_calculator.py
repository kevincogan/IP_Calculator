classes={
    'A':{
        'network_bits':7,
        'host_bits':24,
        'first_address': "0" + (".0" * 3),
        'last_address': "127" + (".255" * 3)
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



get_class_stats("245.206.18.7")
