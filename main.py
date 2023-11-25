import bit_handler as bit
import img_handler as img
import file_handler as file

binary = file.binary_string_from_file("img.png")

bits = bit.convert_to_groups(binary, 2)
bits = bit.convert_to_bit_groups(bits)

images = img.generate_image(bits, 20, 1280, 720)

for image in images:
    image.save(f"image-{images.index(image)}")
    image.show()

# Wannabe Commit
