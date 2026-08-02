import os
import re

def file_encode(inputFile):
    with open(inputFile, "rb") as f:
        path = inputFile.split(os.sep)[-1]
        data = f.read()
        encoded = data.hex()
        out = f"{path}|{encoded}"
        return out

def file_decode(encodedString,outputFileDir="."):
    # l = encodedString.split("|")
    # fileName = l[0]
    # encoded = l[1]
    # encoded = encoded.strip()
    # data = bytes.fromhex(encoded)
    # with open(f"{outputFileDir}{os.sep}{fileName}", "wb") as f:
    #     f.write(data)


    try:
        l = encodedString.split("|")
        fileName = l[0]
        encoded = l[1].strip()
        if not re.match(r"^[0-9a-fA-f]+",encoded):
            bad_chars = [c for c in encoded if c not in "0123456789abcdefABCDEF"]
            raise ValueError("Invalid Hex Chars found: " + ",".join(bad_chars))
        data = bytes.fromhex(encoded)
        out_path = os.path.join(outputFileDir, fileName)
        with open(out_path, "wb") as f:
            f.write(data)
        print(f"File successfully decoded to {out_path}")

    except Exception as e:
        print(f"Error decoding file: {e}")
