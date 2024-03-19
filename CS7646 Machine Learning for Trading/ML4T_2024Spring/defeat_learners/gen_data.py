""""""  		  	   		 	   			  		 			     			  	 
"""  		  	   		 	   			  		 			     			  	 
template for generating data to fool learners (c) 2016 Tucker Balch  		  	   		 	   			  		 			     			  	 
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
  		  	   		 	   			  		 			     			  	 
Student Name: Tucker Balch (replace with your name)  		  	   		 	   			  		 			     			  	 
GT User ID: tb34 (replace with your User ID)  		  	   		 	   			  		 			     			  	 
GT ID: 900897987 (replace with your GT ID)  		  	   		 	   			  		 			     			  	 
"""  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import math  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import numpy as np  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
# this function should return a dataset (X and Y) that will work  		  	   		 	   			  		 			     			  	 
# better for linear regression than decision trees  		  	   		 	   			  		 			     			  	 
def best_4_lin_reg(seed=1489683273):
    """  		  	   		 	   			  		 			     			  	 
    Returns data that performs significantly better with LinRegLearner than DTLearner.  		  	   		 	   			  		 			     			  	 
    The data set should include from 2 to 10 columns in X, and one column in Y.  		  	   		 	   			  		 			     			  	 
    The data should contain from 10 (minimum) to 1000 (maximum) rows.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    :param seed: The random seed for your data generation.  		  	   		 	   			  		 			     			  	 
    :type seed: int  		  	   		 	   			  		 			     			  	 
    :return: Returns data that performs significantly better with LinRegLearner than DTLearner.  		  	   		 	   			  		 			     			  	 
    :rtype: numpy.ndarray  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    np.random.seed(seed)  		  	   		 	   			  		 			     			  	 
    X = np.random.uniform(low=100, high=1000, size=(300, 4))
    Y = 2.3 * X[:, 0] + 4.2 * X[:, 1] + 1.23 * X[:, 2] + 6.7 * X[:, 3] + np.random.normal(scale=18, size=300)

    return X, Y
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
def best_4_dt(seed=1489683273):
    """  		  	   		 	   			  		 			     			  	 
    Returns data that performs significantly better with DTLearner than LinRegLearner.  		  	   		 	   			  		 			     			  	 
    The data set should include from 2 to 10 columns in X, and one column in Y.  		  	   		 	   			  		 			     			  	 
    The data should contain from 10 (minimum) to 1000 (maximum) rows.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    :param seed: The random seed for your data generation.  		  	   		 	   			  		 			     			  	 
    :type seed: int  		  	   		 	   			  		 			     			  	 
    :return: Returns data that performs significantly better with DTLearner than LinRegLearner.  		  	   		 	   			  		 			     			  	 
    :rtype: numpy.ndarray  		  	   		 	   			  		 			     			  	 
    """
    np.random.seed(seed)
    X = np.random.uniform(low=100, high=1000, size=(300, 4))
    Y = np.power(X[:, 0], 2) + np.sin(X[:, 1]) * X[:, 2] + np.power(X[:, 2], 3) + np.random.normal(scale=18, size=300)
    return X, Y
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
def author():  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    :return: The GT username of the student  		  	   		 	   			  		 			     			  	 
    :rtype: str  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    return "ovaidya3"  # Change this to your user ID
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
# if __name__ == "__main__":
#     print("they call me Tim.")