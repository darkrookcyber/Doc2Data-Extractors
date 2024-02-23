"""
Name: fixLineBreaks.py

Description: used to join lines that end with a letter, comma, or space with the next line, replacing the newline character with a space
	- Mimics the sed command "sed -r ':a /[a-zA-Z,\ ]$/N;s/(.)\n/\1 /;ta' kc.txt > kc_reformat.txt"

USE: python fix_line_breaks.py input.txt output.txt
"""



import argparse

def fix_line_breaks(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        buffer = ''  # Holds the line being processed

        for line in infile:
            # Check if the line ends with a letter, comma, or space (excluding the newline character)
            if buffer and (buffer[-1].isalpha() or buffer.endswith(',') or buffer.endswith(' ')):
                # Remove the newline character and append the current line to the buffer
                buffer = buffer.rstrip() + ' ' + line.strip()
            else:
                # Write the buffer to the output file and start a new buffer
                if buffer:
                    outfile.write(buffer + '\n')
                buffer = line.strip()

        # Write any remaining content in the buffer to the output file
        if buffer:
            outfile.write(buffer)

def main():
    parser = argparse.ArgumentParser(description="Fix line breaks in a text file.")
    parser.add_argument('input_file', type=str, help="Path to the input text file.")
    parser.add_argument('output_file', type=str, help="Path to the output text file.")

    args = parser.parse_args()

    fix_line_breaks(args.input_file, args.output_file)
    print(f"Processed {args.input_file} and saved the result to {args.output_file}")

if __name__ == "__main__":
    main()