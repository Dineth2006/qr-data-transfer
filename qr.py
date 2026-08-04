import os
import cv2
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import file_en


def repeat(capture):
    while True:
        ret, frame = capture.read()
        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

def scan_qr_stream(source=1):
    capture = cv2.VideoCapture(source)
    while True:
        ret, frame = capture.read()
        if not ret:
            break

        decoded_objects = decode(frame)
        for obj in decoded_objects:
            print("QR detected")
            file_en.data_gather(obj.data.decode("utf-8"))


        cv2.imshow("QR Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


def generate_qr_code(data,index,folder,path,TotalCodes):   
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"{index}|{TotalCodes}|{path}|{data}")
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((1850, 1850), Image.NEAREST)
    img.save(f"./{folder}/QR/QR_{index}.png")

def repeat_qr(name,path):
    with open(f"./{name}/{name}.txt", "r") as f:
        lines = f.readlines()
        TotalCodes = len(lines)
        for index, line in enumerate(lines):
            generate_qr_code(line.strip(), index, name, path, TotalCodes)
            print(f"Generated QR code for line {index + 1}")

def generate_video(path, name, fps=30):
    print(f"Generating video from {path}...")

    images = [img for img in os.listdir(path) if img.endswith(".png")]
    print(f"Images {images}");

    frame = cv2.imread(os.path.join(path, images[0]))
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(f"./{name}/{name}.avi", fourcc, fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(path, image)))

    video.release()
    cv2.destroyAllWindows()
    print("Video generated successfully!")