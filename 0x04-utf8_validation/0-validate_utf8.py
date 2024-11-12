#!/usr/bin/python3
""" A python script that validates data as valid UTF-8 encoding """


def validUTF8(data):
    """ Returns True if data is valid UTF-8 encoding, else returns False """
    num_bytes = 0

    for bytes in data:
        # Mask to get the last 8 bits (a byte)
        bytes = bytes & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (bytes >> 5) == 0b110:
                num_bytes = 1   # 2-byte character
            elif (bytes >> 4) == 0b1110:
                num_bytes = 2   # 3 byte character
            elif (bytes >> 3) == 0b11110:
                num_bytes = 3   # 4 byte character
            elif (bytes >> 7):
                return False    # If it starts with 1 (not 0) it's invalid
        else:
            # Check if the byte is in the format `10xxxxxx`
            if (bytes >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
