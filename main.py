import cv2
import easyocr
from translate import Translator
from langdetect import detect


def isEnglish(text):
    try:
        text.encode(encoding="utf-8").decode("ascii")
    except UnicodeDecodeError:
        return False
    else:
        return True


def detect_language(text):
    if isEnglish(text):
        return "en"
    else:
        return detect(text)


def draw_box(image, rect, text, confidence, language):
    p1 = rect[0]
    p2 = rect[2]
    height = p2[1] - p1[1]
    width = p2[0] - p1[0]
    cv2.rectangle(image, p1, p2, (0, 255, 0), 2)
    cv2.putText(
        image,
        "Text : " + text,
        (p1[0] + 10, p1[1] + 25),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2,
    )
    cv2.putText(
        image,
        "Confidence : " + str(round(confidence, 5)),
        (p1[0] + 10, p1[1] + 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2,
    )
    cv2.putText(
        image,
        "Lang : " + language,
        (p1[0] + 10, p1[1] + 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2,
    )
    return image


def draw_boxes(image, results):
    for result in results:
        rect = result[0]
        text = result[1]
        confidence = result[2]
        language = detect(text)
        image = draw_box(image, rect, text, confidence, language)
    return image


def add_kannada_progress_bar(image, percentage):
    # shift the image down by 50 pixels
    image = cv2.copyMakeBorder(image, 50, 0, 0, 0, cv2.BORDER_CONSTANT)

    height, width, _ = image.shape
    cv2.rectangle(image, (0, 0), (width, 50), (0, 0, 0), -1)
    cv2.rectangle(image, (0, 0), (int(width * percentage / 100), 50), (0, 255, 0), -1)
    cv2.putText(
        image,
        "Progress : " + str(round(percentage, 2)) + "%",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2,
    )
    return image


reader = easyocr.Reader(["en", "kn"])
translator = Translator(from_lang="kn-IN", to_lang="en")

image = cv2.imread("sample.png")

results = reader.readtext(image)

print(results)

for result in results:
    rect = result[0]
    text = result[1]
    confidence = result[2]
    language = detect_language(text)
    if language != "en":
        text = translator.translate(text)
    image = draw_box(image, rect, text, confidence, language)

image = add_kannada_progress_bar(image, 70)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
