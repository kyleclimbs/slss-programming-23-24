# Images and Python
from PIL import Image
# Open an image and read the information from the image
def pixel_to_name(pixel: tuple) -> str:
    """take a tuple and give its name"""
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    if red < 150 and blue < 150 and green > 119:
        return "green"
    else:
        return "some other colour"
# open the file
with Image.open("./Images/kid-green.jpg") as im:
    # visit every pixel in the image
    image_height = im.height
    image_width = im.width
    # open the beach image
    bg_im = Image.open("./Images/beach.jpg")
    # left-to-right, top-to-bottom
    for y in range(image_height):
        for x in range(image_width):
            pixel = im.getpixel((x, y))
            # if the pixel is green
            if pixel_to_name(pixel) == "green":
                # getpixel from the beach picture in the exact same spot
                bg_pixel = bg_im.getpixel((x, y))
                # put that pixel in the original green screen picture
                im.putpixel((x, y), bg_pixel)
                print(bg_pixel, x, y)
    im.save("./Images/output.jpg")