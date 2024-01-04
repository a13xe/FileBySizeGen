def generate_file(file_size, file_name):
    try:
        with open(file_name, 'wb') as file:
            file.seek(file_size - 1)
            file.write(b'\0')
        print(f"File '{file_name}' with size {file_size} created successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    size_units = {
        'TB': 1024**4,
        'GB': 1024**3,
        'MB': 1024**2,
        'KB': 1024,
        'B': 1
    }
    try:
        size_input = input("Enter the file size (e.g., '1 GB', '100 MB'): ").strip().split()
        if len(size_input) != 2:
            raise ValueError("Invalid input format")

        size, unit = float(size_input[0]), size_input[1].upper()
        if unit not in size_units:
            raise ValueError("Invalid unit. Use TB, GB, MB, KB, or B")

        file_size = int(size * size_units[unit])
        file_name = input("Enter the file name: ").strip()

        generate_file(file_size, file_name)
    except ValueError as e:
        print(f"Invalid input: {str(e)}")
    except KeyboardInterrupt:
        print("\nOperation aborted by user.")


if __name__ == "__main__":
    main()
