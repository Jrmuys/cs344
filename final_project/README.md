# CS 344 Final Project: Generating fonts with GANs

## Project Overview
The goal of this project was to create a network model that could come up with text like images based off computer fonts so that new fonts could be generated. A generative network is one that generates new things based off a statistical model that is learned from to adversarial networks which try to beat eachother. 

The code in implementation_1.py is based on the tutorial found [here](https://machinelearningmastery.com/how-to-develop-a-generative-adversarial-network-for-an-mnist-handwritten-digits-from-scratch-in-keras/) The code in implementation_2.py is based on the tutorial found [here](https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/8.5-introduction-to-gans.ipynb).

## Running the code

The database needed to train the networks can be found [here](https://www.kaggle.com/thomasqazwsxedc/alphabet-characters-fonts-dataset). It is referenced to be in the same folder as the code is run from.

After the database is downloaded, the code should run. The training could take hours depending on the hardware it is being run on. Make sure you are using a GPU acceleration as it will greatly increase the speed of training. Using Google's Collabratory, it took around 3 hours to train implementation 1 and around 1.5 to train implementation 2. 

The generate_new.py only works to generate new images based on implemenetaion 1. Put the file name of the model you wish to create more examples of instead of the one in place.
