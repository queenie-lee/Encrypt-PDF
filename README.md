# Encrypt-PDF

A simple Python tool to encrypt and decrypt PDF files in batch.

## Features

- Encrypt PDF files with AES-256-R5 encryption
- Decrypt password-protected PDF files
- Batch process multiple PDF files from a directory
- Configure settings via command-line arguments or JSON config file
- _Optional:_ Automatically move processed files to a completed directory

## Requirements

- Python 3.x
- pypdf library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/queenie-lee/Encrypt-PDF.git
cd Encrypt-PDF
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Arguments

**Encrypt PDFs:**
```bash
python main.py encrypt -s /path/to/source -d /path/to/destination -p yourpassword
```

**Decrypt PDFs:**
```bash
python main.py decrypt -s /path/to/source -d /path/to/destination -p yourpassword
```

**With completed directory _(optional)_:**
```bash
python main.py encrypt -s /path/to/source -d /path/to/destination -p yourpassword -c /path/to/completed
```

### Using a Config File

Create a `config.json` file with your settings:

```json
{
  "source": "files/input",
  "destination": "files/output",
  "completed": "files/completed",
  "password": "yourpassword"
}
```

Then run:
```bash
python main.py encrypt -f config.json
```

or

```bash
python main.py decrypt -f config.json
```

### Arguments

- `mode` (required): `encrypt` or `decrypt`
- `-f, --file`: Path to JSON config file
- `-s, --source`: Source directory containing PDF files
- `-d, --destination`: Destination directory for processed files
- `-p, --password`: Password for encryption/decryption
- `-c, --completed`: Directory to move source files after processing (optional)

**Note:** Command-line arguments override config file settings.

## Examples

**Example 1: Encrypt all PDFs in a folder**
```bash
python main.py encrypt -s ./documents -d ./encrypted -p MySecurePass123
```

**Example 2: Decrypt PDFs and archive originals**
```bash
python main.py decrypt -s ./encrypted -d ./decrypted -p MySecurePass123 -c ./archive
```

**Example 3: Use config file for encryption**
```bash
python main.py encrypt -f config.json
```

## License

See LICENSE file for details.