import cv2
import easyocr


def draw_box(image, rect, text, confidence):
    p1 = rect[0]
    p2 = rect[2]
    cv2.rectangle(image, p1, p2, (0, 255, 0), 2)
    cv2.putText(
        image, text, (p1[0], p1[1] + 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
    )
    cv2.putText(
        image,
        str(confidence),
        (p1[0], p1[1] - 25),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )
    return image


def draw_boxes(image, results):
    for result in results:
        rect = result[0]
        text = result[1]
        confidence = result[2]
        image = draw_box(image, rect, text, confidence)
    return image


reader = easyocr.Reader(["en"])

image = cv2.imread("image.jpg")

results = reader.readtext(image)
result = results[0]
rect = result[0]
text = result[1]
confidence = result[2]

image = draw_box(image, rect, text, confidence)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
