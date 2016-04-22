import numpy as np
import math
from sklearn.neighbors import KNeighborsRegressor
## Implementation of the Knn algorithm: 
class Knn:

	complexity = 0;

	numInputs = 0;

	discreteOutput = 0;

	discreteInputs = [];

	#  Number of observations - a running count of the unique numbe of
    #  observations
    numObservations = 0;

    # Matrix model - each row represents a new input vector
    #eg. x_Obs = array([[ 1.,  2.,  3.],
    #   				[ 2.,  1.,  5.]])
	x_Obs = np.empty([0, 0])；

	# Output observation array
	# eg. y = [0, 1]
	y_Obs = np.empty([0]);

	#trained result
	knn = KNeighborsRegressor(n_neighbors=2, weights='uniform');

	def __init__(self, complexity, numInputs, discreteOutputs, discreteInputs):
		self.complexity = complexity;
		self.numInputs = numInputs;
		self.discreteOutputs = discreteOutputs;
		self.discreteInputs = discreteInputs;
		x_Obs = np.empty([0,numInputs]);

	#  Add a new training observation. Requirements: newInputObs must be a
    #  row array of size numInputs. newOutputObs must be a single value.
	def addSingleObservation(self, newInputObs, newOutputObs): 
		if (len(newInputObs) == self.numInputs
            and type(newOutputObs) not in (tuple, list)):
	        print("All good!");
	        self.x_Obs = np.vstack((self.x_Obs,newInputObs));
	        self.y_Obs = np.append(self.y_Obs, newOutputObs);
	        self.numObservations += 1;
	    else:
	    	print("Wrong dimensions!");

	#  Add a set of training observations, with the newInputObsMatrix being a
    #  set of correctly-sized vectors and newOutputVector being a vector of
    #  individual values.
	def addBatchObservations(self, newInputObsMatrix, newOutputVector):
        for newInputVector in newInputObsMatrix:
            outputValue = newOutputVector.pop();
            self.addSingleObservation(newInputVector, newInputObsMatrix);


    #  Train the coefficients on the existing observation matrix if there are
    #  enough observations.
    def train(self):
        if (self.numObservations > 0):
            print("Training started");
            self.knn.fit(x_Obs,y_Obs);
            return True;
        else:
            print("Not enough observations to train!");
            return False;

    #  Execute the trained matrix against the given input observation
    def execute(self, inputObsVector):
        y_test = self.knn.predict(T);
        return y_test;



