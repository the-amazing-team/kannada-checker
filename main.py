import cv2
from core.checker import KannadaChecker
import os
from tqdm import tqdm

checker = KannadaChecker()

dataset_image_names = os.listdir("dataset")

for image_name in tqdm(dataset_image_names):
    dataset_image_path = "dataset/" + image_name
    image = cv2.imread(dataset_image_path)
    image = checker.add_annotation(image)
    cv2.imwrite("annotated/" + image_name, image)
