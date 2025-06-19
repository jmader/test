#def calculate_area_square(length: int | float) -> int | float:
def calculate_area_square(length):
    """
    Function to calculate the area of a square
    :param length: length of the square
    :return: area of the square
    """
    if not isinstance(length, (int, float)) or length <= 0:
        raise TypeError("Length must be a positive non-zero number")
    return length * length2
