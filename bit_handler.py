def convert_to_groups(binary_string, group_size):
    # Pad the binary string to make its length a multiple of group_size
    padded_binary = binary_string + '0' * ((group_size - len(binary_string) % group_size) % group_size)

    # Split the binary string into groups of group_size
    groups = [padded_binary[i:i + group_size] for i in range(0, len(padded_binary), group_size)]

    # Convert each group back to decimal
    decimal_values = [int(group, 2) for group in groups]

    return decimal_values


def convert_to_bit_groups(decimal_values):
    # Convert each decimal value to binary with leading zeros, and concatenate them
    binary_string = ''.join(format(value, '08b') for value in decimal_values)

    # Split the binary string into groups of 2 bits
    bit_groups = [binary_string[i:i+2] for i in range(0, len(binary_string), 2)]

    return bit_groups


def convert_to_decimal(bit_groups):
    binary_string = ''.join(bit_groups)

    # Convert the binary string to decimal values
    decimal_values = [int(binary_string[i:i + 8], 2) for i in range(0, len(binary_string), 8)]

    for dec in decimal_values:
        if dec > 3:
            decimal_values.remove(dec)

    return decimal_values


def unconvert_to_binary(decimal_values, group_size):
    # Convert each decimal value to binary and concatenate them
    binary_string = ''.join(format(value, f'0{group_size}b') for value in decimal_values)

    return binary_string

# Wannabe Commit
