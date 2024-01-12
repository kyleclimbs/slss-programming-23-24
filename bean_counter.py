# Author: Kyle Li
# 9 01 24

# Version 0.1 ---
# Count all red pixels
# Report on the percentage of all red
# Version 0.2 ---
# Count all the green pixels
# Report on the percentage of all green jellybeans
# Version 0.3 ---
# Count all the _____ pixels
# Report on the percentae of all _____ jellybeans

from PIL import Image
import colour_helper
RED_PIXEL = (150, 0, 0)
GREEN_PIXEL = (0, 150, 0)
PINK_PIXEL = (255, 192, 203)
jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")
red_pixels = []
green_pixels = []
pink_pixels = []
# Visit every pixel in the imade
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
        current_pixel = jelly_bean_img.getpixel((x,y))
        # If that pixel is red, store the location
        if colour_helper.pixel_to_string(current_pixel) == "red":
            red_pixels.append((x,y))
        elif colour_helper.pixel_to_string(current_pixel) == "jelly bean green":
            green_pixels.append((x,y))
        elif colour_helper.pixel_to_string(current_pixel) == "jelly bean pink":
            pink_pixels.append((x,y))
# Calculate the percentag of all jelly bean colours
# Divide that number by the total pixels in the image
red_percentage = len(red_pixels) / (jelly_bean_img.width * jelly_bean_img.height) * 100
green_percentage = len(green_pixels) / (jelly_bean_img.width * jelly_bean_img.height) * 100
pink_percentage = len(pink_pixels) / (jelly_bean_img.width * jelly_bean_img.height) * 100
# Create a map of all "found" pixiels for a respective colour
# Create a new image that is the same size as the original
original_size = (jelly_bean_img.width, jelly_bean_img.height)
pink_pixel_map = Image.new("RGB", original_size)
# For every pixel in "found" pixel list place a red pixel on that new image
for pixel_loc in pink_pixels:
    pink_pixel_map.putpixel(pixel_loc, PINK_PIXEL)
pink_pixel_map.save("./Images/pink_pixel_map.jpg")
pink_pixel_map.close()
jelly_bean_img.close()
# Display Report
print(f"Red Jelly Beans: {round(red_percentage,2)}%")
print(f"Green Jelly Beans:{round(green_percentage,2)}%")
print(f"Pink Jelly Beans:{round(pink_percentage,2)}%")