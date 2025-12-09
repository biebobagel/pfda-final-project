#This is where the main project code will be.

from PIL import Image
from math import sqrt
from palettes import PALETTES

# Create a sepearate python file containing preset color palettes with RGB color codes.

def main():

    # Ask the user to upload an image of their choice (preferrably a JPEG). Then store it into a variable.

    print("Hello! Welcome to the Lighting Transformation Program! Please input the name of your file below that you would like to change. ")

    filename = input(">>> ")
    img = Image.open(filename)

    print("Here is your image: ")
    img.show()
    img.close()
    print("")

    # Prompt the user to select a color palette theme (the options will be listed out for them). Strip and lowercase the response.

    print("Here are some color themes you could choose from: type which one you'd like below.")
    for theme in PALETTES:
        print ("> ", theme, "\n")
    userTheme = input(">>> ")

    # Ask the user to select an output image name.
    
    print("What would you like the name of your new file to be?")
    newFilename = input(">>> ").strip()

    # Edit the original image to the new color palette.

    newImg = recolor_image(filename, newFilename, userTheme)

    # Display the new image.

    print("Here is your new image!")
    newImg.show()
    newImg.close()

    print("Thank you!")

# Create a function that takes the color distance between the original red, green, and blues with the chosen palette colors.

def color_distance(c1, c2):
    return sqrt(
        (c1[0] - c2[0]) ** 2 +
        (c1[1] - c2[1]) ** 2 +
        (c1[2] - c2[2]) ** 2
    )

# Create a function that loops through the color palette RGB's and matches it to a closest RGB of the user image.

def find_closest_palette_color(pixel, palette):
    best_color = None
    best_distance = float("inf")

    # Check every palette color
    for pal_color in palette:
        distance = color_distance(pixel, pal_color)

        # If the palette color is closer, update to best match
        if distance < best_distance:
            best_distance = distance
            best_color = pal_color

    return best_color

# Now create a function that will recolor the image to the new color palette

def recolor_image(input_path, output_path, theme):
    palette = PALETTES[theme] 

    image = Image.open(input_path).convert("RGB")
    width, height = image.size

    # Load all the pixels for RGB values

    pixels = image.load()

    # Create a new output image
    new_img = Image.new("RGB", (width, height))
    new_pixels = new_img.load()

    # Process each pixel to the new color from the chosen palette using a nested for loop
    for y in range(height):
        for x in range(width):
            original_color = pixels[x, y]
            new_pixels[x, y] = find_closest_palette_color(original_color, palette)

    new_img.save(output_path)
    print("Saved recolored image to:", output_path)

    return new_img

if __name__ == "__main__":
    main()