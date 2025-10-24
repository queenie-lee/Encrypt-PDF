import os
import shutil

from pypdf import PdfReader, PdfWriter

def app():
    source = "./files/input"
    destination = "./files/output"
    completed = "./files/completed"
    input_file = "input.pdf"

    input_file_path = os.path.join(source, input_file)
    output_file_path = os.path.join(destination, "output.pdf")
    reader = PdfReader(input_file_path)
    writer = PdfWriter(clone_from=reader)

    # Add a password to the new PDF
    writer.encrypt("a_password", algorithm="AES-256-R5")

    # Save the new PDF to a file
    with open(output_file_path, "wb") as f:
        writer.write(f)

    # Move content of source to completed
    shutil.move(input_file_path, os.path.join(completed, input_file))

if __name__ == "__main__":
    app()
