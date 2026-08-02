import cv2
import qrcode

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

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("testQR.png")

generate_qr_code("Hello, World!")