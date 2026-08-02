import sys
import os
import file_en

if len(sys.argv) < 2 or len(sys.argv) > 3:
    raise ValueError("Usage: python main.py <input_file> [output_directory]")


def main():
    inputFile = sys.argv[1]
    outputFileDir = sys.argv[2] if len(sys.argv) > 2 else "."

    encoded = file_en.file_encode(inputFile)
    print(f"Encoded: {encoded}")

    file_en.file_decode(encoded, outputFileDir)

if __name__ == "__main__":
    main()