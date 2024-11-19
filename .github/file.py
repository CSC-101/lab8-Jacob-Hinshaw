import sys

# This function takes a file in the command line. This file must have 2 numbers in each line, and these numbers will
# be summed together for each line and printed as an output.
def main():
    if len(sys.argv) != 2:
        print("Error: Please provide the name of a file as a command-line argument.")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                parts = line.split()
                if len(parts) != 2:
                    print(f"Error on line {line_number}: Expected 2 values but found {len(parts)}.")
                    continue
                try:
                    num1 = float(parts[0])
                    num2 = float(parts[1])

                    print(f"Line {line_number}: {num1 + num2}")
                except ValueError:
                    print(f"Error on line {line_number}: Non-numeric value encountered.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)


if __name__ == "__main__":
    main()