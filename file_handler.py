def binary_string_from_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            # Read binary data from the file
            binary_data = file.read()

            # Convert binary data to a formatted binary string
            binary_string = ''.join(format(byte, '08b') for byte in binary_data)

            return binary_string
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"Error reading file: {e}"

# Wannabe Commit
