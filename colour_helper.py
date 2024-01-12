# Kyle LI 
# december 13

# Do you need help with colours?
# This is for you!


def pixel_to_string(pixel: tuple) -> str:
    """Take a rbg 3-tuple and "interpret it"
    as a colour and return that colour's names
    Params:
        pixel - 3-tuple of (red, green, blue)
    Return:
        String representing the colour
    """
    r, g, b = pixel
    if g > 170 and r < 78 and b < 70:
        return "green"
    # TODO: Implement detecting the colour red
    if g < 25 and b < 25 and r > 150:
        return "red"
    if g >= 80 and b < 55 and r < 55:
        return "jelly bean green"
    if r >= 190 and 60 <= g <= 110 and 99 <= b <= 1:
        return "jelly bean pink"

def is_light(pixel:tuple) -> bool:
    """ Take a pixel
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    # calculate the average value of all three (red, green, blue)
    average = (red + green + blue) / 3

    # if the average >= 128 return True
    if average >= 128:
        return True
    # else return false
    else: 
        return False
    
black_pixel = (0, 0, 0)
dark_gray_pixel = (127, 127, 127)
light_gray_pixel = (128 ,128, 128)
white_pixel = (255, 255, 255)
print(is_light(black_pixel)) # False
print(is_light(dark_gray_pixel)) # False
print(is_light(light_gray_pixel)) # True
print(is_light(white_pixel)) # True

def pixel_to_grayscale(pixel: tuple) -> tuple:
    """Returns a grayscale version of the given pixel"""
    gray = int(pixel[0] * 0.3 + pixel[1] * 0.59 + pixel[2] * 0.11)

    return (gray, gray, gray)