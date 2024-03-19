import os
import shutil
import easyocr

reader = easyocr.Reader(['en'])

input_directory = 'input'
output_directory = 'output'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def extract_text_easyocr(image_path):
    print("processing :", image_path)

    result = reader.readtext(image_path)
    
    extracted_text = " ".join([text for _, text, _ in result])
    print("Extraction Complete :", extracted_text)
    
    return extracted_text.strip()

for file_name in os.listdir(input_directory):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_directory, file_name)

        text = extract_text_easyocr(image_path)
        
        valid_filename = "".join(c for c in text if c.isalnum())
        
        if not valid_filename:
            valid_filename = "no_text_found_" + os.path.splitext(file_name)[0]
        
        new_file_name = f"{valid_filename}.jpg"
        
        new_file_path = os.path.join(output_directory, new_file_name)
        
        shutil.move(image_path, new_file_path)

print("Text extraction and renaming complete.")
