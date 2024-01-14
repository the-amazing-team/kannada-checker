import cv2
from core.checker import KannadaChecker
import os
from tqdm import tqdm

checker = KannadaChecker()

dataset_image_names = os.listdir("dataset")

for image_name in dataset_image_names:
    dataset_image_path = "dataset/" + image_name
    print(dataset_image_path)
    image = cv2.imread(dataset_image_path)

    cv2.imshow("image", image)
    cv2.waitKey(0)

# image = cv2.imread("dataset/" + image_name)
# image = checker.add_annotation(image)
# cv2.imwrite("annotated/" + image_name, image)

# image = cv2.imread("dataset/image11.png")
# # image = checker.add_annotation(image)
# cv2.imshow("image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
