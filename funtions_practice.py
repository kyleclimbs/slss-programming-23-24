# Kyle Li
# NOvember 24




def area_of_a_square(sidelength: float) -> float:
    """Return the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    return area


def print_area_of_a_square(sidelength: float) -> None:
    """Calculate and print the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    print(
        f"The area of a square with side length {sidelength} is: {area} square units."
    )


print(print_area_of_a_square(12.2))


def stars(num_of_stars: int) -> str:
    """Return the area of stars.

    Params:

    num_stars - The numbers of stars to return
    """

    return "*" * num_of_stars

print(stars(100))


# biggest_of_three

def biggest_of_three(num_one: int, num_two: int, num_three: int) -> int:
    if num_one > num_two and num_one > num_three:
        return num_one
    elif num_two > num_one and num_two > num_three:
        return num_two 
    else:
        return num_three
print(biggest_of_three(2, 3,
4))