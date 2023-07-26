# README

### Notes

27/07/2023

[The dataset](https://www.kaggle.com/yashvrdnjain/hotdognothotdog/metadata)

[Keras Docs](https://keras.io/examples/vision/image_classification_from_scratch/#setup)

(Un)Fortunately, I don't need to do resizing as part of preprocessing. It is done already.

What did I do/learn till now:
1. Got it running on the GPU. On Windows. What a mess.
   2. I don't want to dual boot. As much as it would make things easy.
2. Set basic params like image and batch size which will be needed for training
3. A subset (20%) of training will be used for validation
3. Got the detection in the training folders right `# ['hotdog', 'nothotdog']`
4. Visualized the first 9 images in the training dataset