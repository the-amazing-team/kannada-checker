import cv2
from core.checker import KannadaChecker


image = cv2.imread("sample/sample.png")
checker = KannadaChecker()

image = checker.add_annotation(image)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
