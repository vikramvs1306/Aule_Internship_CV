import fitz  # PyMuPDF

# Path to the PDF file
pdf_path = '/home/vikram/Aule_space/Computer Vision Challenge.pdf'

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# Extract images from the first page (page 0)
page = pdf_document[0]
images = page.get_images(full=True)

# Save each image found on the first page
for img_index, img in enumerate(images):
    xref = img[0]  # Image XREF
    base_image = pdf_document.extract_image(xref)
    image_bytes = base_image["image"]
    image_filename = f"first_page_img_{img_index + 1}.png"

    # Save the image
    with open(image_filename, "wb") as image_file:
        image_file.write(image_bytes)
        print(f"Saved: {image_filename}")

# Close the document
pdf_document.close()
