import cv2
from core.checker import KannadaChecker

checker = KannadaChecker()

image = cv2.imread("dataset/image-50.png")
image = checker.add_annotation(image)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
