import sys
import os
import cv2
import file_en
import qr

if len(sys.argv) < 2 or len(sys.argv) > 3:
    raise ValueError("Usage: python main.py <input_file> [output_directory]")


def main():
    inputFile = sys.argv[1]
    outputFileDir = sys.argv[2] if len(sys.argv) > 2 else "."
    mode = sys.argv[3] if len(sys.argv) > 3 else "decode" 

    if mode == "encode":
        path = inputFile.split(os.sep)[-1]
        name = path.split(".")[0]
        encoded = file_en.file_encode(inputFile)
        os.mkdir(f"./{name}")
        os.mkdir(f"./{name}/QR")
        file_en.code_split(encoded,name)
        print(f"Successfully encoded {inputFile} to {name}.txt")
        qr.repeat_qr(name,path)
        qr.generate_video(f"./{name}/QR", name)
        

    elif mode == "decode":
        if not os.path.exists(f"./{outputFileDir}"):
            os.mkdir(f"./{outputFileDir}")
        if not os.path.exists(f"./{outputFileDir}/TMP"):
            os.mkdir(f"./{outputFileDir}/TMP")
        qr.scan_qr_stream()
    
    else:
        raise ValueError("Invalid mode. Use 'encode' or 'decode'.")

if __name__ == "__main__":
    main()