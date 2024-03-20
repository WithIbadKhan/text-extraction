from PIL import Image
import easyocr
import numpy as np

# Function to crop the upper part of the image, save it, and extract text from the lower part using EasyOCR
def crop_upper_save_and_extract_text_from_lower(image_path):
    # Load the image
    image = Image.open(image_path)

    # Calculate the dimensions for the upper and lower parts
    one_third_height = image.height // 3
    two_third_height = 2 * one_third_height

    # Define the area for the upper part (one third) and crop it
    upper_area = (0, 0, image.width, one_third_height)
    upper_part = image.crop(upper_area)

    # Save the cropped upper part
    upper_part_path = 'upper_part.jpg'
    upper_part.save(upper_part_path)

    # Define the area for the lower part (remaining two thirds) and crop it
    lower_area = (0, two_third_height, image.width, image.height)
    lower_part = image.crop(lower_area)

    # Convert the PIL image to a numpy array for EasyOCR
    lower_part_np = np.array(lower_part)
    lower_part_np = lower_part_np[:, :, ::-1].copy()  # Convert RGB to BGR

    # Initialize EasyOCR reader (specify the languages as per your requirement)
    reader = easyocr.Reader(['en'])

    # Use EasyOCR to extract text from the lower part
    results = reader.readtext(lower_part_np)

    # Extract text and return it along with the path to the saved upper part image
    extracted_text = "\n".join([result[1] for result in results])

    return upper_part_path, extracted_text

# Path to the uploaded image
image_path = 'DSCF0006.JPG'  # Replace with the correct path to your image

# Crop the upper part, save it, and extract text from the lower part
upper_part_saved, text_from_lower = crop_upper_save_and_extract_text_from_lower(image_path)

print(f"The upper part of the image has been saved as: {upper_part_saved}")
print("The extracted text from the lower part is:")
print(text_from_lower)
