import sys
import os
import file_en
import qr

if len(sys.argv) < 2 or len(sys.argv) > 3:
    raise ValueError("Usage: python main.py <input_file> [output_directory]")


def main():
    inputFile = sys.argv[1]
    outputFileDir = sys.argv[2] if len(sys.argv) > 2 else "."
    mode = sys.argv[3] if len(sys.argv) > 3 else "encode" 

    if mode == "encode":
        path = inputFile.split(os.sep)[-1]
        name = path.split(".")[0]
        encoded = file_en.file_encode(inputFile)
        os.mkdir(f"./{name}")
        os.mkdir(f"./{name}/QR")
        file_en.code_split(encoded,name)
        print(f"Successfully encoded {inputFile} to {name}.txt")
        qr.repeat_qr(name,path)

        

    elif mode == "decode":
        file_en.file_decode(inputFile, outputFileDir)
    else:
        raise ValueError("Invalid mode. Use 'encode' or 'decode'.")

if __name__ == "__main__":
    main()