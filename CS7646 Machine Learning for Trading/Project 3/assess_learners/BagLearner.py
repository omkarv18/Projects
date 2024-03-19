""""""
"""  		  	   		 	   			  		 			     			  	 
A simple wrapper for linear regression.  (c) 2015 Tucker Balch  		  	   		 	   			  		 			     			  	 

Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	   			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		 	   			  		 			     			  	 
All Rights Reserved  		  	   		 	   			  		 			     			  	 

Template code for CS 4646/7646  		  	   		 	   			  		 			     			  	 

Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	   			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		 	   			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			     			  	 
or edited.  		  	   		 	   			  		 			     			  	 

We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	   			  		 			     			  	 
GT honor code violation.  		  	   		 	   			  		 			     			  	 

-----do not edit anything above this line---  		  	   		 	   			  		 			     			  	 
"""

import numpy as np


class BagLearner(object):


    def __init__(self,  learner, kwargs, bags, boost=False, verbose=False):
        """
        Constructor method
        """
        self.verbose = verbose
        self.boost = boost
        self.bags = bags

        self.models = []
        for i in range(0, bags):
            self.models.append(learner(**kwargs))

    def author(self):
        """
        :return: The GT username of the student
        :rtype: str
        """
        return "ovaidya3"  # replace tb34 with your Georgia Tech username

    def add_evidence(self, data_x, data_y):
        """
        Add training data to learner

        :param data_x: A set of feature values used to train the learner
        :type data_x: numpy.ndarray
        :param data_y: The value we are attempting to predict given the X data
        :type data_y: numpy.ndarray
        """
        bag_bunch_x = []
        bag_bunch_y = []

        for i in range(self.bags):
            indices = np.random.randint(0, data_x.shape[0], size=data_x.shape[0])
            bag_bunch_x.append(data_x[indices])
            bag_bunch_y.append(data_y[indices])

        for i in range(len(bag_bunch_x)):
            self.models[i].add_evidence(bag_bunch_x[i], bag_bunch_y[i])

    def query(self, points):
        """
        Estimate a set of test points given the model we built.

        :param points: A numpy array with each row corresponding to a specific query.
        :type points: numpy.ndarray
        :return: The predicted result of the input data according to the trained model
        :rtype: numpy.ndarray
        """
        results = np.empty((points.shape[0], len(self.models)))
        for i in range(len(self.models)):
            results[:, i] = self.models[i].query(points)

        results = np.mean(results, axis=1)
        return results


# if __name__ == "__main__":
#     print("the secret clue is 'zzyzx'")




