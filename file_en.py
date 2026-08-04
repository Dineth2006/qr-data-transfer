import os
import re

def file_encode(inputFile):
    with open(inputFile, "rb") as f:
        data = f.read()
        encoded = data.hex()
        out = f"{encoded}"
        return out

def file_decode(encodedString,outputFileDir="."):
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

def code_split(encodedString,name):
    x = ""
    for i, ch in enumerate(encodedString, start=1):
        x += ch
        if i % 2900 == 0:
            with open(f"./{name}/{name}.txt", "a+") as f:
                f.write(x + "\n")
            x = ""
    if x:
        with open(f"./{name}/{name}.txt", "a+") as f:
            f.write(x + "\n")