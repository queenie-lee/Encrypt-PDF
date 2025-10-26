import json
import os
import shutil

from pypdf import PdfReader, PdfWriter


def app():
    with open("config.json", "r") as jf:
        data = json.load(jf)  # reading json file
        jf.close()

    source = data["source"]
    destination = data["destination"]
    completed = data["completed"]
    password = data["password"]

    # Get list of files in the source directory
    input_files = os.listdir(source)

    for file in input_files:
        read_encrypt_save_file(file, password, destination, source, completed)


def read_encrypt_save_file(input_file, password, destination, source, completed):

    input_file_path = os.path.join(source, input_file)
    reader = PdfReader(input_file_path)
    writer = PdfWriter(clone_from=reader)

    # Add a password to the new PDF
    writer.encrypt(password, algorithm="AES-256-R5")

    output_file_path = os.path.join(destination, input_file)

    # Save the new PDF to a file
    with open(output_file_path, "wb") as f:
        writer.write(f)
        print(f"Encrypted {input_file} and saved to {output_file_path}")

    # Move content of source to completed
    shutil.move(input_file_path, os.path.join(completed, input_file))
    print(f"Moved {input_file} to {completed}")


if __name__ == "__main__":
    app()
