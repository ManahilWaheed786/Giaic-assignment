import qrcode
import cv2

def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,  # controls size of QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

def decode_qr(filename):
    # Read image with OpenCV
    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()

    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    if data:
        print(f"Decoded data from {filename}: {data}")
    else:
        print("QR code not detected or could not decode.")

def main():
    print("QR Code Encoder / Decoder")

    while True:
        choice = input("\nChoose an option:\n1. Generate QR Code\n2. Decode QR Code\n3. Exit\nEnter choice: ")
        
        if choice == '1':
            data = input("Enter the data/text to encode in the QR code: ")
            filename = input("Enter the filename to save the QR code image (e.g. 'myqr.png'): ")
            generate_qr(data, filename)
        
        elif choice == '2':
            filename = input("Enter the filename of the QR code image to decode: ")
            decode_qr(filename)
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2 or 3.")

if __name__ == "__main__":
    main()
