# Verification Code Recognition using Machine Learning CNN

Students are required to fill in an additional varification code field before logging in the system since few years ago. Therefore, I am inspired to build up a CNN model for recognizing the varification code.


A sample of the varification code in the course selection system.

![varification code image](data/627318.png)

## Structure

### Directories

- `data/`: Varification code images for training should go here.
- `model/`: The model should be saved in this directory after training.
- `predict/`: Other downloaded varification code images for you to test the model.

### Python files

- `downloadData.py`: Download varification code images from the course selection system in my college. It can take a parameter as the number of varification code images to download.
- `train.py`: Run the training on the CNN model. If the model is already existed in `model/`, load it and continue training. Otherwise, create a new model.
- `predict.py`: Predict the varification code from a given varification code images. It can take a parameter as the path to the varification code images.

## Usage

Download 100 new varification code images.
```
python downloadData.py 100
```

Train the model with images inside `data/`.
```
python train.py
```

Predict a provided varification code image that the model has never seen before.
```
python predict.py predict/702203.png
```
