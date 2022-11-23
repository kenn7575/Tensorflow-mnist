import keras
import cv2
class_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

file = r"image.png"
image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
img_resized = cv2.resize(image, (28, 28), interpolation=cv2.INTER_LINEAR)
img_resized = cv2.bitwise_not(img_resized)
print(img_resized)

model = keras.models.load_model("digit_classifier.h5")

predection = model.predict(img_resized)
print(class_names[predection])
