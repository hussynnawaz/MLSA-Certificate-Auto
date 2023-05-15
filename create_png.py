import os
from pdf2image import convert_from_path

poppler_path = r"H:\poppler-0.68.0\bin"


try:
    os.makedirs("Output/PNG")
except OSError:
    pass

# get all pdf files in Output/PDF directory
pdf_files = [os.path.join("Output/PDF", file) for file in os.listdir("Output/PDF") if file.endswith(".pdf")]

# convert pdf files to png files
for pdf_file in pdf_files:
    images = convert_from_path(pdf_file, poppler_path=poppler_path)
    for image in images:
        image.save(os.path.join("Output/PNG", os.path.basename(pdf_file).replace(".pdf", ".png")))
