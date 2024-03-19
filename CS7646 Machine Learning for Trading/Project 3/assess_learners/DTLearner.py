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


class DTLearner(object):


    def __init__(self,  leaf_size, verbose=False):
        """
        Constructor method
        """
        self.leaf_size = leaf_size
        self.verbose = verbose
        self.regression_tree = None


    def author(self):
        """
        :return: The GT username of the student
        :rtype: str
        """
        return "ovaidya3"  # replace tb34 with your Georgia Tech username

    @staticmethod
    def select_feature(data_x, data_y):

        correlation_coefs = np.corrcoef(data_x, data_y, rowvar=False)[:-1, -1]
        return np.nanargmax(correlation_coefs)

    @staticmethod
    def build_tree(leaf_size, data_x, data_y):

        data = np.hstack((data_x, data_y.reshape(-1, 1)))
        if data_x.shape[0] <= leaf_size:
            avg_val = np.mean(data_y)
            return np.array([['leaf', avg_val, np.nan, np.nan]])
        if len(np.unique(data_y)) == 1:
            return np.array([['leaf', data_y[0], np.nan, np.nan]])
        else:
            i = DTLearner.select_feature(data_x, data_y)


            SplitVal = np.median(data_x[:, i])

            if SplitVal == np.max(data_x[:, i]):

                SplitVal = np.mean(data_x[:, i])

            lefttree = DTLearner.build_tree(leaf_size, data_x[data_x[:, i] <= SplitVal], data_y[data_x[:, i] <= SplitVal])
            righttree = DTLearner.build_tree(leaf_size, data_x[data_x[:, i] > SplitVal], data_y[data_x[:, i] > SplitVal])

            root = np.array([[i, SplitVal, 1, lefttree.shape[0] + 1]])

            return np.vstack((np.vstack((root, lefttree)), righttree))


    def add_evidence(self, data_x, data_y):
        """
        Add training data to learner

        :param data_x: A set of feature values used to train the learner
        :type data_x: numpy.ndarray
        :param data_y: The value we are attempting to predict given the X data
        :type data_y: numpy.ndarray
        """

        self.regression_tree = DTLearner.build_tree(self.leaf_size, data_x, data_y)


    @staticmethod
    def traverse_tree(point, tree_data, tree_index=0):

        if tree_data[tree_index][0] == 'leaf':

            return float(tree_data[tree_index][1])

        factor = int(float(tree_data[tree_index][0]))
        SplitVal = float(tree_data[tree_index][1])
        left_ind = tree_index + int(float(tree_data[tree_index][2]))
        right_ind = tree_index + int(float(tree_data[tree_index][3]))

        if point[factor] <= SplitVal:
            return DTLearner.traverse_tree(point, tree_data, tree_index=left_ind)
        else:
            return DTLearner.traverse_tree(point, tree_data, tree_index=right_ind)

    def query(self, points):
        """
        Estimate a set of test points given the model we built.

        :param points: A numpy array with each row corresponding to a specific query.
        :type points: numpy.ndarray
        :return: The predicted result of the input data according to the trained model
        :rtype: numpy.ndarray
        """

        result = np.apply_along_axis(DTLearner.traverse_tree, axis=1, arr=points, tree_data=self.regression_tree, tree_index=0)
        return result

# if __name__ == "__main__":
#     print("the secret clue is 'zzyzx'")




