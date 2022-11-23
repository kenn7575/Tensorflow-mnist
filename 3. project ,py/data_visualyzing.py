import keras.datasets.mnist
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# distrubute data
data = keras.datasets.mnist #get data
(train_images, train_labels), (test_images, test_labels) = data.load_data() #asign data


#output categorie classes
class_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]



class Visualyzation:
    def __init__(self, num, predictions):
        self.num = num
        self.predictions = predictions
        
    def visualyze(self):
        preticted_num = np.argmax(self.predictions[self.num])
        actiual_num = (test_labels[self.num])

        df = pd.DataFrame(test_images[self.num])
        print(df)
        print("The system thinks that the", actiual_num, "is a", class_names[preticted_num])

    def visualyze2(self):
        y = ("This is ctualy a :", class_names[test_labels[self.num]])
        x = ("Predicted to be a:", class_names[np.argmax(self.predictions[self.num])])

        output = Visualyzation(self.num, self.predictions)
        plt.grid(False)
        plt.imshow(test_images[self.num], cmap=plt.get_cmap("gray"))
        plt.xlabel(y)
        plt.title(x)
        plt.show()

