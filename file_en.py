import os
import re

def file_encode(inputFile):
    with open(inputFile, "rb") as f:
        data = f.read()
        encoded = data.hex()
        out = f"{encoded}"
        return out

def data_gather(data,outputFileDir):
    index,TotalCodes,fileName,rawData = data.split("|")

    TotalCodes = int(TotalCodes)
    path = f"./Decoded/{outputFileDir}/TMP/{fileName}.txt"


    #Duplicate check
    duplicate = False
    line_count = 0
    try:
        with open(path, "r") as rf:
            for line in rf:
                if line.startswith(f"{index}|"):
                    duplicate = True
                    break
                line_count += 1
    except FileNotFoundError:
        line_count = 0

    if duplicate:
        print(f"Duplication found, {index}")
        return line_count,TotalCodes,fileName

    with open(path, "a+") as f:
        f.write(f"{index}|{rawData}\n")
        line_count += 1

    if line_count == TotalCodes:
        print(f"All QR codes received for {fileName}. Decoding...")
        return line_count,TotalCodes

def decode_pass(Total_codes,outputFileDir="."):
    path = f"./Decoded/{outputFileDir}/TMP"

    with open(f"{path}/decoded.txt", "r") as f:
        lines = f.readlines()
        for i in range(0, Total_codes):
            for line in lines:
                if line.startswith(f"{i}|"):
                    _,rawData = line.split("|",1)
                    with open(f"{path}/decoded.txt", "a+") as df:
                        df.write(rawData)
                    break
            
def file_decode(fileName,outputFileDir="."):
    path = f"./Decoded/{outputFileDir}"
    with open(f"{path}/TMP/decoded.txt" ,"r") as rf:
         lines = rf.readlines
         for line in lines:
            try:
                if not re.match(r"^[0-9a-fA-f]+",line):
                    bad_chars = [c for c in line if c not in "0123456789abcdefABCDEF"]
                    raise ValueError("Invalid Hex Chars found: " + ",".join(bad_chars))
                data = bytes.fromhex(line)
                out_path = os.path.join(path, fileName)
                with open(out_path, "wb") as f:
                    f.write(data)
                print(f"File successfully decoded to {out_path}")

            except Exception as e:
                print(f"Error decoding file: {e}")

def code_split(encodedString,name):
    x = ""
    for i, ch in enumerate(encodedString, start=1):
        x += ch
        if i % 900 == 0:
            with open(f".Encode/{name}/{name}.txt", "a+") as f:
                f.write(x + "\n")
            x = ""
    if x:
        with open(f".Encode/{name}/{name}.txt", "a+") as f:
            f.write(x + "\n")