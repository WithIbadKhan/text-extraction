import easyocr

def extract_text_easyocr(image_path):
    """
    Extract text from the given image using EasyOCR.
    """
    reader = easyocr.Reader(['en'])  
    
    # Read the image
    result = reader.readtext(image_path)
    
    # The result includes the bounding box, text, and confidence score. Let's print the text:
    extracted_text = "\n".join([text for _, text, _ in result])
    
    return extracted_text

# Example usage
image_path = r'C:/Users/walee/OneDrive/Documents/GitHub/text-extraction/input/DSCF0006.JPG'
extracted_text = extract_text_easyocr(image_path)
print("Extracted Text:", extracted_text)