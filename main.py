import sys
import os
import file_en
import qr

if len(sys.argv) < 2 or len(sys.argv) > 4:
    raise ValueError("Usage: python main.py <input_file> [output_directory] [method]")


def main():
    inputFile = sys.argv[1]
    outputFileDir = sys.argv[2] if len(sys.argv) > 2 else "."
    mode = sys.argv[3] if len(sys.argv) > 3 else "decode" 

    if mode == "encode":
        path = inputFile.split(os.sep)[-1]
        name = path.split(".")[0]
        encoded = file_en.file_encode(inputFile)
        os.mkdir(f"./Encode")
        os.mkdir(f"./Encode/{name}")
        os.mkdir(f"./Encode/{name}/QR")
        file_en.code_split(encoded,name)
        print(f"Successfully encoded {inputFile} to {name}.txt")
        qr.repeat_qr(name,path)
        qr.generate_video(f"./Encode/{name}/QR", name)
        

    elif mode == "decode":
        if not os.path.exists(f"./Decoded"):
            os.mkdir(f"./Decoded")
        if not os.path.exists(f"./Decoded/{outputFileDir}"):
            os.mkdir(f"./Decoded/{outputFileDir}")
        if not os.path.exists(f"./Decoded/{outputFileDir}/TMP"):
            os.mkdir(f"./Decoded/{outputFileDir}/TMP")
        qr.scan_qr_stream(outputFileDir)
    
    else:
        raise ValueError("Invalid mode. Use 'encode' or 'decode'.")

if __name__ == "__main__":
    main()