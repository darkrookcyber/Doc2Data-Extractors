import argparse
import PyPDF2

def extract_text_from_pdf(pdf_path):
    """
    Extracts all text from a PDF file.

    :param pdf_path: Path to the PDF file from which to extract text.
    :return: Extracted text as a single string.
    """
    extracted_text = ""

    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Iterate over all the pages
        for page in pdf_reader.pages:
            extracted_text += page.extract_text() + "\n"

    return extracted_text

def save_text_to_file(text, file_path):
    """
    Saves the extracted text to a text file.

    :param text: Extracted text to be saved.
    :param file_path: Path where the text file will be saved.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

def main():
    # Setting up argument parsing
    parser = argparse.ArgumentParser(description="Extract text from a PDF file and save it to a text file.")
    parser.add_argument("-i", "--input_pdf", help="Path to the input PDF file.", type=str)
    parser.add_argument("-o", "--output_txt", help="Path to the output text file.", type=str)
    args = parser.parse_args()

    # Determining the input PDF and output text file paths
    input_pdf = args.input_pdf if args.input_pdf else input("Enter the path to the PDF file: ")
    output_txt = args.output_txt if args.output_txt else input("Enter the path for the output text file: ")

    # Extracting text from the PDF
    extracted_text = extract_text_from_pdf(input_pdf)

    # Saving the extracted text to a file
    save_text_to_file(extracted_text, output_txt)

# void main (argv* input, argv* output) {}
main()
# end main()

