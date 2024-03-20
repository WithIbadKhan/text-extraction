from PIL import Image
import easyocr
import numpy as np
import re
import os

# Function to crop the image, extract text, and save the upper part with the extracted text as the name
def crop_and_name_upper_with_text(image_path):
    # Load the image
    image = Image.open(image_path)

    # Calculate the dimensions for the lower third part
    two_third_height = 2 * (image.height // 3)

    # Define the area for the lower third part and crop it
    lower_area = (0, two_third_height, image.width, image.height)
    lower_part = image.crop(lower_area)

    # Convert the PIL image to a numpy array for EasyOCR
    lower_part_np = np.array(lower_part)
    lower_part_np = lower_part_np[:, :, ::-1].copy()  # Convert RGB to BGR

    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Use EasyOCR to extract text from the lower part
    results = reader.readtext(lower_part_np)
    
    # Extract text and sanitize it to create a valid file name
    extracted_text = " ".join([result[1] for result in results])
    file_name = re.sub(r'[\\/*?:"<>|]', "", extracted_text)
    file_name = re.sub(r'\s+', "_", file_name)  # Replace spaces with underscores
    file_name = file_name[:50]  # Truncate to first 50 characters to avoid very long file names
    file_name = file_name.strip('_')  # Remove any leading or trailing underscores

    # Ensure the file name is not empty
    if not file_name:
        file_name = "upper_part"

    # Add the image extension
    file_name += ".jpg"

    # Define the area for the upper two-thirds part and crop it
    upper_area = (0, 0, image.width, two_third_height)
    upper_part = image.crop(upper_area)

    # Save the cropped upper part with the new name
    upper_part_path = os.path.join(os.path.dirname(image_path), file_name)
    upper_part.save(upper_part_path)

    # Return the path to the saved upper part image
    return upper_part_path

# Path to the uploaded image
image_path = 'DSCF0006.JPG'  # Replace with the correct path to your image

# Crop the image, extract text, and save the upper part with the text as the name
saved_image_path = crop_and_name_upper_with_text(image_path)

print(f"The upper part of the image has been saved as: {saved_image_path}")
