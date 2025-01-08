# Subnetting and Supernetting for IP Address Classes

## Overview
This program adds functionality to handle subnetting for **Class A IP addresses**, alongside existing support for Classes B, C, D, and E. The program provides utilities to:

1. Identify the class of an IP address.
2. Perform subnet calculations, such as determining valid subnets, CIDR notation, broadcasting addresses, first and last addresses, and the number of hosts per subnet.
3. Handle supernetting tasks, such as merging contiguous subnets and finding common bits among multiple IP addresses.

## Features

### Class Identification
The program can identify the class of an IP address (A, B, C, D, or E) based on the first byte of the address.
- **Class A**: 0 - 127
- **Class B**: 128 - 191
- **Class C**: 192 - 223
- **Class D**: 224 - 239
- **Class E**: 240 - 255

### Subnetting
For Classes A, B, and C, the program calculates:
- CIDR Notation
- Number of subnets
- Addressable hosts per subnet
- Valid subnets
- Broadcasting addresses
- First and last usable addresses in each subnet

### Supernetting
The program merges contiguous subnets and calculates:
- Common bits among IP addresses
- Network mask for the supernet
- Supernet CIDR notation

## Modules and Functions
### Class Identification Module
- **`get_class_stats(ip_addr)`**:
  Identifies the class of the given IP address and prints attributes, including the first and last address ranges, network count, and host count (if applicable).

#### Example
```python
get_class_stats("136.206.18.7")
```

### Subnetting Module
- **`get_subnet_stats(ip_addr, subnet_mask)`**:
  Performs subnetting calculations for the given IP address and subnet mask.

#### Outputs:
1. CIDR Notation
2. Number of Subnets
3. Addressable Hosts per Subnet
4. Valid Subnets
5. Broadcasting Addresses
6. First Addresses
7. Last Addresses

#### Example
```python
get_subnet_stats("192.168.10.0", "255.255.255.192")
```

### Supernetting Module
- **`get_supernet_stats(addresses)`**:
  Calculates the common network bits and the corresponding network mask for a set of IP addresses.

#### Example
```python
get_supernet_stats(["205.100.0.0", "205.100.1.0", "205.100.2.0", "205.100.3.0"])
```

## Implementation Details
### Classes Dictionary
A dictionary defines attributes for each IP address class (A-E), such as network and host bits, first and last address ranges, and default subnet masks.

```python
classes = {
    'A': {
        'network_bits': 7,
        'host_bits': 24,
        'first_address': "0.0.0.0",
        'last_address': "127.255.255.255",
        'subnet_mask': "0"
    },
    ...
}
```

### Key Helper Functions
1. **`to_binary_string(ip_addr)`**:
   Converts an IP address into its binary representation.

2. **`get_network_class(byte)`**:
   Determines the class of an IP address from its first byte.

3. **`get_CIDR(subnet_mask_address)`**:
   Counts the number of "1" bits in a subnet mask to calculate CIDR notation.

4. **`get_subnets(subnet_mask, network_class)`**:
   Calculates the total number of subnets.

5. **`get_host_per_subnet(subnet_mask, network_class)`**:
   Determines the number of addressable hosts per subnet.

6. **`get_valid_subnet(ip_addr_bytes, network_class, subnet_mask)`**:
   Returns a list of valid subnet addresses for a given class.

7. **`get_broadcasting_address(valid_subnet, ip_addr_bytes, network_class, subnet_mask)`**:
   Finds broadcasting addresses for each subnet.

8. **`get_first_address(valid_subnet)`** and **`get_last_address(broadcast_address)`**:
   Calculate the first and last usable addresses for each subnet.

9. **`get_network_mask(same_bytes)`**:
   Generates a network mask from common bits in supernetting.

## Test Cases
### Class Identification
```python
get_class_stats("200.206.18.7")
get_class_stats("136.206.18.7")
get_class_stats("240.192.16.5")
```

### Subnetting
```python
get_subnet_stats("136.209.19.9", "255.255.255.192")  # /26
get_subnet_stats("136.209.19.9", "255.255.252.0")    # /22
```

### Supernetting
```python
get_supernet_stats(["205.100.0.0", "205.100.1.0", "205.100.2.0", "205.100.3.0"])
```

## Usage
The script provides flexible functionality for analyzing, calculating, and managing IP address subnetting and supernetting.

Run the script with desired test cases to validate outputs or integrate into larger networking tools.

