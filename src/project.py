#This is where the main project code will be.

from PIL import Image

from palettes import PALETTES

# Create a sepearate python file containing preset color palettes with RGB color codes.

# Ask the user to upload an image of their choice (preferrably a JPEG). Then store it into a variable.

print("Hello! Welcome to the Lighting Transformation Program! Please input the name of your file below that you would like to change. ")

filename = input(">>> ")
img = Image.open(filename)

print("Here is your image: ")
img.show()
print("")

# Prompt the user to select a color palette theme (the options will be listed out for them). Strip and lowercase the response.

print("Here are some color themes you could choose from: type which one you'd like below.")
for theme in PALETTES:
    print ("> ", theme, "\n")
userTheme = input (">>> ".strip.lowercase())


# If possible, allow the user to input a color palette of their choice.

# Ask the user to select an output image name.