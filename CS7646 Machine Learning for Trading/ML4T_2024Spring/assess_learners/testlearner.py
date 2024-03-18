""""""  		  	   		 	   			  		 			     			  	 
"""  		  	   		 	   			  		 			     			  	 
Test a learner.  (c) 2015 Tucker Balch  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
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
  		  	   		 	   			  		 			     			  	 
import math  		  	   		 	   			  		 			     			  	 
import sys
  		  	   		 	   			  		 			     			  	 
import numpy as np
  		  	   		 	   			  		 			     			  	 
import DTLearner as dt
import RTLearner as rt
import BagLearner as bl
import LinRegLearner as lrl
import InsaneLearner as it
import matplotlib.pyplot as plt
import timeit
  		  	   		 	   			  		 			     			  	 
if __name__ == "__main__":
    # print(sys.argv[1])
    # if len(sys.argv[0]) != 2:
    #     print("Usage: python testlearner.py <filename>")
    #     sys.exit(1)

    inf = np.genfromtxt(sys.argv[1], delimiter=',', skip_header=1, dtype=float, usecols=range(1, 10))

    data = inf.copy()
    # inf = open(sys.argv[1])
    # data = np.array(
    #     [list(map(float, s.strip().split(","))) for s in inf.readlines()]
    # )
  		  	   		 	   			  		 			     			  	 
    # compute how much of the data is training and testing  		  	   		 	   			  		 			     			  	 
    train_rows = int(0.6 * data.shape[0])  		  	   		 	   			  		 			     			  	 
    test_rows = data.shape[0] - train_rows  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # separate out training and testing data  		  	   		 	   			  		 			     			  	 
    train_x = data[:train_rows, 0:-1]  		  	   		 	   			  		 			     			  	 
    train_y = data[:train_rows, -1]  		  	   		 	   			  		 			     			  	 
    test_x = data[train_rows:, 0:-1]  		  	   		 	   			  		 			     			  	 
    test_y = data[train_rows:, -1]  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # print(f"{test_x.shape}")
    # print(f"{test_y.shape}")
  		  	   		 	   			  		 			     			  	 
    # create a learner and train it  		  	   		 	   			  		 			     			  	 
    # learner = bl.BagLearner(learner = lrl.LinRegLearner, kwargs = {}, bags = 10, boost = False, verbose = False)  # create a dtlearner
    learner = it.InsaneLearner(verbose=False)
    learner.add_evidence(train_x, train_y)  # train it

    # print(learner.author())
  		  	   		 	   			  		 			     			  	 
    # evaluate in sample  		  	   		 	   			  		 			     			  	 
    pred_y = learner.query(train_x)  # get the predictions

    rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])  		  	   		 	   			  		 			     			  	 

    # print("In sample results")
    # print(f"RMSE: {rmse}")
    c = np.corrcoef(pred_y, y=train_y)  		  	   		 	   			  		 			     			  	 
    # print(f"corr: {c[0,1]}")
  		  	   		 	   			  		 			     			  	 
    # evaluate out of sample  		  	   		 	   			  		 			     			  	 
    pred_y = learner.query(test_x)  # get the predictions  		  	   		 	   			  		 			     			  	 
    rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])  		  	   		 	   			  		 			     			  	 

    # print("Out of sample results")
    # print(f"RMSE: {rmse}")
    c = np.corrcoef(pred_y, y=test_y)  		  	   		 	   			  		 			     			  	 
    # print(f"corr: {c[0,1]}")

    correlations = np.corrcoef(train_x, train_y, rowvar=False)[:-1, -1]
    np.savetxt('p3_results.txt', correlations, delimiter=',', fmt='%.5f', header='Initial Correlation of Features to Response Variable')

    # Experiment 1:

    leaf_num = 50

    num_leafs = list(range(1, leaf_num))
    rmse_out = []
    rmse_in = []

    for i in num_leafs:
        learner_ex1 = dt.DTLearner(leaf_size=i, verbose=False)
        learner_ex1.add_evidence(train_x, train_y)

        #in sample
        pred_y_in = learner_ex1.query(train_x)
        rmse_in_val = math.sqrt(((train_y - pred_y_in) ** 2).sum() / train_y.shape[0])

        #out sample
        pred_y_out = learner_ex1.query(test_x)
        rmse_out_val = math.sqrt(((test_y - pred_y_out) ** 2).sum() / test_y.shape[0])

        rmse_in.append(rmse_in_val)
        rmse_out.append(rmse_out_val)

    plt.figure(1)
    plt.plot(num_leafs, rmse_out, label='RMSE Out of Sample')
    plt.plot(num_leafs, rmse_in, label='RMSE In Sample')

    plt.xlabel('Leaf Size')
    plt.ylabel('RMSE Values')
    plt.gca().invert_xaxis()
    plt.title('DTLearner RMSE vs. Leaf Size')
    plt.legend()
    plt.savefig("Ex_1_assess_learners.png")


    # Experiment 2

    leaf_num = 50

    num_leafs = list(range(1, leaf_num))
    rmse_out = []
    rmse_in = []

    for i in num_leafs:
        learner_ex2 = bl.BagLearner(learner = dt.DTLearner, kwargs = {"leaf_size":i}, bags = 20, boost = False, verbose = False)
        learner_ex2.add_evidence(train_x, train_y)

        # in sample
        pred_y_in = learner_ex2.query(train_x)
        rmse_in_val = math.sqrt(((train_y - pred_y_in) ** 2).sum() / train_y.shape[0])

        # out sample
        pred_y_out = learner_ex2.query(test_x)
        rmse_out_val = math.sqrt(((test_y - pred_y_out) ** 2).sum() / test_y.shape[0])

        rmse_in.append(rmse_in_val)
        rmse_out.append(rmse_out_val)

    plt.figure(2)
    plt.plot(num_leafs, rmse_out, label='RMSE Out of Sample')
    plt.plot(num_leafs, rmse_in, label='RMSE In Sample')

    plt.xlabel('Leaf Size')
    plt.ylabel('RMSE Values')
    plt.gca().invert_xaxis()
    plt.title('BagLearner RMSE vs. Leaf Size')
    plt.legend()
    plt.savefig("Ex_2_assess_learners.png")

    # Experiment 3

    leaf_num = 50

    num_leafs = list(range(1, leaf_num))
    time_dt = []
    time_rt = []

    for i in num_leafs:
        learner_ex3_dt = dt.DTLearner(leaf_size=i, verbose=False)

        learner_dt = lambda: learner_ex3_dt.add_evidence(train_x, train_y)
        time_dtlearner = timeit.timeit(learner_dt, number=5) / 5


        learner_ex3_rt = rt.RTLearner(leaf_size=i, verbose=False)

        learner_rt = lambda: learner_ex3_rt.add_evidence(train_x, train_y)
        time_rtlearner = timeit.timeit(learner_rt, number=5) / 5

        time_dt.append(time_dtlearner)
        time_rt.append(time_rtlearner)

    plt.figure(3)
    plt.plot(num_leafs, time_dt, label='Decision Tree Train Time')
    plt.plot(num_leafs, time_rt, label='Random Tree Train Time')

    plt.xlabel('Leaf Size')
    plt.ylabel('Time to Train')
    plt.gca().invert_xaxis()
    plt.title('DT Train Time vs. RT Train Time')
    plt.legend()
    plt.savefig("Ex_3_1_assess_learners.png")


    # Experiment 3 Part 2

    leaf_num = 50

    num_leafs = list(range(1, leaf_num))
    MAE_dt = []
    MAE_rt = []

    for i in num_leafs:
        learner_ex3_dt = dt.DTLearner(leaf_size=i, verbose=False)
        learner_ex3_dt.add_evidence(train_x, train_y)

        pred_y_dt = learner_ex3_dt.query(test_x)
        MAE_dtlearner = np.sum(abs(test_y - pred_y_dt) / test_y.shape[0])

        learner_ex3_rt = rt.RTLearner(leaf_size=i, verbose=False)
        learner_ex3_rt.add_evidence(train_x, train_y)

        pred_y_rt = learner_ex3_rt.query(test_x)
        MAE_rtlearner = np.sum(abs(test_y - pred_y_rt) / test_y.shape[0])

        MAE_dt.append(MAE_dtlearner)
        MAE_rt.append(MAE_rtlearner)

    plt.figure(4)
    plt.plot(num_leafs, MAE_dt, label='MAE Decision Tree')
    plt.plot(num_leafs, MAE_rt, label='MAE Random Tree')

    plt.xlabel('Leaf Size')
    plt.ylabel('Mean Absolute Error (MAE)')
    plt.gca().invert_xaxis()
    plt.title('DT MAE vs. RT MAE')
    plt.legend()
    plt.savefig("Ex_3_2_assess_learners.png")
