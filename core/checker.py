import cv2
import easyocr
from translate import Translator
from langdetect import detect


class KannadaChecker:
    def __init__(self):
        self.translator = Translator(from_lang="kn-IN", to_lang="en")
        self.reader = easyocr.Reader(["en", "kn"])

    def _is_english(self, text):
        try:
            text.encode(encoding="utf-8").decode("ascii")
        except UnicodeDecodeError:
            return False
        else:
            return True

    def _detect_language(self, text):
        if self._is_english(text):
            return "en"
        else:
            return detect(text)

    def _draw_box(self, image, rect, text, confidence, language, is_translated=False):
        p1 = rect[0]
        p2 = rect[2]
        height = p2[1] - p1[1]
        width = p2[0] - p1[0]

        if is_translated:
            text = text + " (Translated)"

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

    def _add_kannada_progress_bar(self, image, percentage):
        image = cv2.copyMakeBorder(image, 50, 0, 0, 0, cv2.BORDER_CONSTANT)

        height, width, _ = image.shape
        cv2.rectangle(image, (0, 0), (width, 50), (0, 0, 0), -1)
        cv2.rectangle(
            image, (0, 0), (int(width * percentage / 100), 50), (0, 255, 0), -1
        )
        cv2.putText(
            image,
            "Percent (KN) : " + str(round(percentage, 2)) + "%",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
        )
        return image

    def read_image_text(self, image):
        results = self.reader.readtext(image)
        return results

    def add_annotation(self, image):
        results = self.read_image_text(image)

        kannada_count = 0
        for result in results:
            rect = result[0]
            text = result[1]
            confidence = result[2]
            language = self._detect_language(text)
            is_translated = False
            if language != "en":
                text = self.translator.translate(text)
                is_translated = True
            if language == "kn":
                kannada_count += 1
            image = self._draw_box(
                image, rect, text, confidence, language, is_translated
            )

        percentage = kannada_count / len(results) * 100
        image = self._add_kannada_progress_bar(image, percentage)

        return image
