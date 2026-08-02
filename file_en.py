import os

def file_encode(inputFile):
    with open(inputFile, "rb") as f:
        path = inputFile.split(os.sep)[-1]
        data = f.read()
        encoded = data.hex()
        out = f"{path}|{encoded}"
        return out

def file_decode(encodedString,outputFileDir="."):
    fileName,encoded = encodedString.split("|")
    data = bytes.fromhex(encoded)
    with open(f"{outputFileDir}{os.sep}{fileName}", "wb") as f:
        f.write(data)

