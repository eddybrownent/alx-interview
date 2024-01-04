#!/usr/bin/python3
"""
method to  determine if data set represents valid UTF-8 encoding
"""


def validUTF8(data):
    """
    checks id given data rep valid UTF-8 encoding

    Args:
        data: List of ints representing the bytes of data set

    Returns:
        True if the data is valid else False
    """
    def isContinue(byte):
        """
        Help check if a byte is a valid continuation byte
        """
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        byte = data[i]

        if (byte & 0b10000000) == 0:  # 1-byte character
            i += 1
        elif (byte & 0b11100000) == 0b11000000:  # 2-byte character
            i += 2
            if i > len(data) or not (isContinue(data[i - 1])):
                return False
        elif (byte & 0b11110000) == 0b11100000:  # 3-byte character
            i += 3
            if i > len(data) or not (isContinue(data[i - 2])
                                     and isContinue(data[i - 1])):
                return False
        elif (byte & 0b11111000) == 0b11110000:  # 4-byte character
            i += 4
            if i > len(data) or not (isContinue(data[i - 3])
                                     and isContinue(data[i - 2])
                                     and isContinue(data[i - 1])):
                return False
        else:
            return False

    return True
#
