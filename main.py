import sys
import os
import file_en

if len(sys.argv) < 2 or len(sys.argv) > 3:
    raise ValueError("Usage: python main.py <input_file> [output_directory]")


def main():
    inputFile = sys.argv[1]
    outputFileDir = sys.argv[2] if len(sys.argv) > 2 else "."
    mode = sys.argv[3] if len(sys.argv) > 3 else "decode" 

    if mode == "encode":
        encoded = file_en.file_encode(inputFile)
        print(f"Encoded: {encoded}")

    elif mode == "decode":
        file_en.file_decode(temp,outputFileDir)
    else:
        raise ValueError("Invalid mode. Use 'encode' or 'decode'.")

if __name__ == "__main__":
    main()