# from PIL import Image

# # Load the image from the provided path
# image_path = 'DSCF0006.JPG'
# image = Image.open(image_path)

# # Calculate the dimensions to split the image into upper and lower parts
# width, height = image.size
# middle = height // 2

# # Define the box for the upper part (left, upper, right, lower)
# upper_box = (0, 0, width, middle)
# upper_part = image.crop(upper_box)

# # Define the box for the lower part
# lower_box = (0, middle, width, height)
# lower_part = image.crop(lower_box)

# # Save the cropped images to the same directory as the script
# upper_part_path = 'upper_part.jpg'
# lower_part_path = 'lower_part.jpg'
# upper_part.save(upper_part_path)
# lower_part.save(lower_part_path)

# # Return the paths to the saved images
# upper_part_path, lower_part_path


from PIL import Image

def crop_image_upper_lower_parts(image_path):
    # Load the image
    image = Image.open('DSCF0006.JPG')

    # Calculate the dimensions to split the image into upper and lower parts
    width, height = image.size
    middle = height // 2

    # Define the box for the upper part (left, upper, right, lower)
    upper_box = (0, 0, width, middle)
    upper_part = image.crop(upper_box)

    # Define the box for the lower part
    lower_box = (0, middle, width, height)
    lower_part = image.crop(lower_box)

    # Save the cropped images
    upper_part.save('1upper_part.jpg')
    lower_part.save('1lower_part.jpg')

    print("The image has been cropped into upper and lower parts and saved as 'upper_part.jpg' and 'lower_part.jpg'.")

# Example usage
# Replace "path_to_your_image.jpg" with the path to your image file
crop_image_upper_lower_parts("croped.JPG")
