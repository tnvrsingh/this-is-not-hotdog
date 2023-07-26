import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
import matplotlib.pyplot as plt

#GPU test
print(tf.config.list_physical_devices('GPU'))

image_size = (180, 180)
batch_size = 32
PATH = '../../data/hotdog-nothotdog/'
train_dir = os.path.join(PATH, 'train')
test_dir = os.path.join(PATH, 'test')


# training
train_dataset = image_dataset_from_directory(train_dir,
    shuffle=True,
    validation_split=0.2,
    subset="training",
    seed=42,
    batch_size=batch_size,
    image_size=image_size
)

# Found 3000 files belonging to 2 classes.
# Using 2400 files for training.

# validation
validation_dataset = image_dataset_from_directory(train_dir,
    shuffle=True,
    validation_split=0.2,
    subset="validation",
    seed=42,
    batch_size=batch_size,
    image_size=image_size
)

# Found 3000 files belonging to 2 classes.
# Using 600 files for validation.

class_names = train_dataset.class_names
print(class_names) # ['hotdog', 'nothotdog']

plt.figure(figsize=(10, 10))
for images, labels in train_dataset.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")
plt.show()
