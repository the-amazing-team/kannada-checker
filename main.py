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

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
