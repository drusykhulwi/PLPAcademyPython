def read_and_modify_file_with_error_handling():
    input_file = input("Enter the input filename: ")
    output_file = input("Enter the output filename: ")

    try:
        with open(input_file, 'r') as file:
            content = file.readlines()

        # Modify the content as needed. For example, let's convert all text to uppercase.
        modified_content = [line.upper() for line in content]

        with open(output_file, 'w') as file:
            file.writelines(modified_content)

        print(f"Modified content has been written to {output_file}")
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except IOError:
        print(f"An error occurred while reading from or writing to the file.")

# Example usage:
read_and_modify_file_with_error_handling()
