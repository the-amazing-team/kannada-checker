import cv2
import easyocr

image = cv2.imread("images/sample-image.png")
reader = easyocr.Reader(["kn", "en"])
result = reader.readtext(image)

print(result)

result = [
    ([[168, 26], [732, 26], [732, 346], [168, 346]], "ಕನ್ನಡ", 0.9976149112476682),
    ([[139, 353], [425, 353], [425, 397], [139, 397]], "KANNADA", 0.4158211641361065),
    ([[448, 350], [762, 350], [762, 398], [448, 398]], "LAN GUAGE", 0.8482427654646876),
]
