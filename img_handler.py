from PIL import Image
from tqdm import tqdm

def generate_image(bit_groups, image_size, pixels_per_row, height):
    # Calculate the number of rows needed
    num_rows = (len(bit_groups) * image_size) // pixels_per_row + 1

    # Calculate the number of images needed based on the specified height
    num_images = (num_rows * image_size) // height + 1

    # Create a list to store the generated images
    images = []

    # Create a tqdm instance to display the progress bar
    progress_bar = tqdm(total=(int(num_images * pixels_per_row * height)),
                        desc='Generating Images', unit=' x20 pixels')

    # Counter for the total number of pixels processed
    total_pixels_processed = 0

    # Iterate over each set of rows corresponding to an image
    for i in range(num_images):
        # Calculate the starting and ending rows for each image
        start_row = i * height
        end_row = min((i + 1) * height, num_rows * image_size)

        # Create an image with the specified size
        img = Image.new('RGB', (pixels_per_row, end_row - start_row))

        # Draw the colored squares on the image
        for j in range(start_row, end_row, image_size):
            for k, bit_group in enumerate(bit_groups):
                color = color_mapping.get(bit_group, (255, 255, 255))  # Default to white if not in mapping
                x_start = (k * image_size) % pixels_per_row
                y_start = (k * image_size) // pixels_per_row * image_size
                for x in range(x_start, x_start + image_size):
                    for y in range(j, j + image_size):
                        img.putpixel((x, y - start_row), color)
                        total_pixels_processed += 1
                        # Update the progress bar for each pixel processed
                progress_bar.update(1)

        # Append the generated image to the list
        images.append(img)

    # Close the progress bar
    progress_bar.close()

    return images


def convert_image_to_bit_groups(image, image_size, pixels_per_row):
    bit_groups = []

    color_mapping = {
        (255, 255, 255): '00',  # White
        (0, 0, 0): '10',  # Black
        (255, 0, 0): '01',  # Red
        (0, 255, 0): '11'  # Green
    }

    # Iterate over each row
    # Iterate over each row
    for y_start in range(0, image.size[1], image_size):
        # Iterate over each block in the row
        for x_start in range(0, pixels_per_row, image_size):
            # Extract the color of the top-left pixel in the block
            color = image.getpixel((x_start, y_start))

            bit_group = color_mapping[color]

            if bit_group is not None:
                bit_groups.append(bit_group)

    return bit_groups


color_mapping = {
        "00": (255, 255, 255),
        "10": (0, 0, 0),
        "01": (255, 0, 0),
        "11": (0, 255, 0)
    }

# Wannabe Commit
