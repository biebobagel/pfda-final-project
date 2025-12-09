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
    userTheme = input(">>> ".strip.lowercase())

    # Ask the user to select an output image name.
    
    print("What would you like the name of your new file to be?")
    newFilename = input(">>> ")

    # Display the new file.

    newImg = Image.open(newFilename)

    print("Here is your new image!")
    newImg.show()
    newImg.close()

    print("Thank you!")

def color_distance():

if __name__ == "__main__":
    main()