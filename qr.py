import os
import cv2
import qrcode
from PIL import Image

capture = cv2.VideoCapture(0)
def repeat():
    while True:
        ret, frame = capture.read()
        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

def detect_qr_code():
    while True:
        ret, frame = capture.read()
        decoded_objects = cv2.QRCodeDetector().detectAndDecode(frame)

        if decoded_objects[0]:
            return decoded_objects[0]  # return the decoded data if a QR code is detected
            break

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

def generate_qr_code(data,index,folder,path):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"{index}|{path}|{data}")
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"./{folder}/QR/QR_{index}.png")

def repeat_qr(name,path):
    with open(f"./{name}/{name}.txt", "r") as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            generate_qr_code(line.strip(), index,name,path)
            print(f"Generated QR code for line {index + 1}: {line.strip()}")

def generate_video(path, name, fps=30):
    print(f"Generating video from {path}...")

    images = [img for img in os.listdir(path) if img.endswith(".png")]
    print(f"Images {images}");

    frame = cv2.imread(os.path.join(path, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(f"./{name}.avi", cv2.VideoWriter_fourcc(*'DIVX'), fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(path, image)))

    video.release()
    cv2.destroyAllWindows()
    print("Video generated successfully!")


#generate_video("./QR","qr_video", fps=30)