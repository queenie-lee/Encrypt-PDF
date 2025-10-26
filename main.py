import argparse
import json
import os
import shutil

from pypdf import PdfReader, PdfWriter


def app(args):
    data = dict()

    if args.file:
        with open(args.file, "r") as jf:
            data = json.load(jf)  # reading json file

    mode = args.mode
    source = args.source or data.get("source")
    destination = args.destination or data.get("destination")
    completed = args.completed or data.get("completed")
    password = args.password or data.get("password")

    if source is not None and destination is not None and password is not None:
        # Get list of files in the source directory
        input_files = os.listdir(source)

        for file in input_files:
            read_encrypt_save_file(mode, file, password, destination, source, completed)
        return 0

    else:
        print(f"Some arguments are empty. Source: {source}, destination: {destination}, completed: {completed}, "
              f"password: {password}.")
        return 1


def read_encrypt_save_file(mode, input_file, password, destination, source, completed):

    input_file_path = os.path.join(source, input_file)
    reader = PdfReader(input_file_path)

    if mode == "decrypt":
        # Decrypt PDF using password
        reader.decrypt(password)
    writer = PdfWriter(clone_from=reader)

    if mode == "encrypt":
        # Add a password to the new PDF
        writer.encrypt(password, algorithm="AES-256-R5")

    output_file_path = os.path.join(destination, input_file)

    # Save the new PDF to a file
    with open(output_file_path, "wb") as f:
        writer.write(f)
        print(f"{mode.title()}ed {input_file} and saved to {output_file_path}")

    # Optional
    if completed:
        # Move content of source to completed
        shutil.move(input_file_path, os.path.join(completed, input_file))
        print(f"Moved {input_file} to {completed}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", help="encrypt or decrypt", choices=["encrypt", "decrypt"])
    parser.add_argument("-f", "--file", help="config file containing directory and password details")
    parser.add_argument("-s", "--source", help="source directory")
    parser.add_argument("-d", "--destination", help="destination directory")
    parser.add_argument("-p", "--password", help="password")
    parser.add_argument("-c", "--completed", help="move source files to this directory when processed")
    args = parser.parse_args()

    return app(args)


if __name__ == "__main__":
    exit(main())
