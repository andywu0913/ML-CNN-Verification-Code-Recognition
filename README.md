# Verification Code Recognition using Machine Learning CNN

The inspiration of doing this side project comes from the course selection system in my college. Students are required to fill in additional varification code field [](/data/199798.png) before logging in the system since few years ago. Therefore, I am interested in building up a CNN for recognizing the varification code.

## Usage

- `data/`: Varification code images for training should go here.
- `model/`: After training the model should be saved in here.
- `downloadData.py`: Download varification code images from the course selection system in my college. It can take a parameter as the number of varification code images to download.
- `train.py`: Run the training for our CNN model. If the model is already exists in `model/`, load it and continue training. Otherwise, create a new model.
- `predict.py`: Predict the varification code from a given varification code images. It can take a parameter as the path to the varification code images.

