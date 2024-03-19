""""""  		  	   		 	   			  		 			     			  	 
"""Assess a betting strategy.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
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
  		  	   		 	   			  		 			     			  	 
Student Name: Omkar Kiran Vaidya (replace with your name)  		  	   		 	   			  		 			     			  	 
GT User ID: ovaidya3 (replace with your User ID)  		  	   		 	   			  		 			     			  	 
GT ID: 903867937 (replace with your GT ID)  		  	   		 	   			  		 			     			  	 
"""  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import numpy as np  
import matplotlib.pyplot as plt		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
def author():  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    :return: The GT username of the student  		  	   		 	   			  		 			     			  	 
    :rtype: str  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    return "ovaidya3"  # replace tb34 with your Georgia Tech username.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
def gtid():  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    :return: The GT ID of the student  		  	   		 	   			  		 			     			  	 
    :rtype: int  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    return 903867937  # replace with your GT ID number  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
def get_spin_result(win_prob):  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    :param win_prob: The probability of winning  		  	   		 	   			  		 			     			  	 
    :type win_prob: float  		  	   		 	   			  		 			     			  	 
    :return: The result of the spin.  		  	   		 	   			  		 			     			  	 
    :rtype: bool  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    result = False  		  	   		 	   			  		 			     			  	 
    if np.random.random() <= win_prob:  		  	   		 	   			  		 			     			  	 
        result = True  		  	   		 	   			  		 			     			  	 
    return result  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
def test_code():  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    Method to test your code  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    win_prob = 9. / 19  # set appropriately to the probability of a win  		  	   		 	   			  		 			     			  	 
    np.random.seed(gtid())  # do this only once  		 	   		 	   			  		 			     			  	 
    # np.random.seed(876)  # For checking regression slopes for different seeds in question 3. Remember to uncomment the code in the ex1_fig2 function. 
    
    # print(get_spin_result(win_prob))  # test the roulette spin  		  	   		 	   			  		 			     			  	 
    # add your code here to implement the experiments  		  	   		 	   			  		 		

    
    ex1_fig1(episode_creator=episode_winnings, fig_num=1, exp_num=1)
    ex1_fig2(episode_creator=episode_winnings, fig_num=2, exp_num=1)
    ex1_fig3(episode_creator=episode_winnings, fig_num=3, exp_num=1)

    ex1_fig2(episode_creator=episode_winnings_2, fig_num=4, exp_num=2)
    ex1_fig3(episode_creator=episode_winnings_2, fig_num=5, exp_num=2)

    # probability_calc(episode_winnings)
    # probability_calc(episode_winnings_2)  # Uncomment these two lines to find out the probabilities and standard deviations


def episode_winnings(n):

    episode_winnings = 0

    episode_record = np.empty(n+1, dtype=int)

    win_prob = 9. / 19

    episode_record[0] = 0

    count = 1

    while episode_winnings < 80 and count != n+1:
        won = False
        bet_amount = 1
        while not won and count != n+1:
            
            won = get_spin_result(win_prob)
            if won == True:
                episode_winnings += bet_amount
            else:
                episode_winnings -= bet_amount
                bet_amount = bet_amount * 2
                
            episode_record[count] = episode_winnings
            count += 1
    
    episode_record[count:] = 80

    return episode_record

def episode_winnings_2(n):
    episode_winnings = 0

    episode_record = np.empty(n+1, dtype=int)

    win_prob = 9. / 19

    episode_record[0] = 0

    count = 1
    hit_80 = False
    hit_256 = False

    while hit_80 == False and count != n+1 and hit_256 == False:
        won = False
        bet_amount = 1

        while not won and count != n+1 and hit_256 == False:
            
            if bet_amount > episode_winnings + 256:
                bet_amount = episode_winnings + 256

            won = get_spin_result(win_prob)
            if won == True:
                episode_winnings += bet_amount
            else:
                episode_winnings -= bet_amount
                bet_amount = bet_amount * 2
                
            episode_record[count] = episode_winnings
            count += 1
            if episode_winnings <= -256:
                hit_256 = True
    
        if episode_winnings >= 80:
            hit_80 = True
    
    if hit_80 == True:
        episode_record[count:] = 80
    if hit_256 == True:
        episode_record[count:] = -256
    return episode_record


def ex1_fig1(episode_creator, fig_num, exp_num):

    episodes = np.empty((10, 1001), dtype=int)
    
    for i in range(len(episodes)):
        episodes[i][:] = episode_creator(1000)

    np.set_printoptions(threshold=np.inf)

    plt.figure(fig_num)
    plt.axis([0, 300, -256, 100])
    plt.plot(episodes.T)
    plt.legend(["Episode " + str(i) for i in range(1, 11)])
    plt.xlabel('Number of Spins')
    plt.ylabel('Total Winnings')
    plt.title(f'Experiment {exp_num}: Figure {fig_num}')
    plt.savefig(f"Figure_{fig_num}.png")


def ex1_fig2(episode_creator, fig_num, exp_num):

    episodes = np.empty((1000, 1001), dtype=int)

    for i in range(len(episodes)):
        episodes[i][:] = episode_creator(1000)


    means = np.mean(episodes, axis=0)
    stds = np.std(episodes, axis=0, ddof=0)

    top_means = means + stds
    bottom_means = means - stds

    aggregates = np.vstack((top_means, means, bottom_means))

    plt.figure(fig_num)
    plt.axis([0, 300, -256, 100])
    plt.plot(aggregates.T)

    plt.legend(["Mean + SD", "Mean", "Mean - SD"])
    plt.xlabel('Number of Spins')
    plt.ylabel('Mean Winnings')
    plt.title(f'Experiment {exp_num}: Figure {fig_num} (Mean)')
    plt.savefig(f"Figure_{fig_num}.png")

    # For Question 3 Only. Unomment it if you would like to see figs 6 & 7 from the report. Ignore the second output graph for Experiment 2. 

    # x_values = np.arange(aggregates.shape[1])

    # plt.figure(fig_num + 4)
    # plt.axis([0, 350, 0, 600])

    # coefficients = np.polyfit(x_values[:150], stds[:150], 1)
    # regression_line = np.polyval(coefficients, x_values[:150])

    # plt.plot(x_values[:150], stds[:150])
    # plt.plot(x_values[:150], regression_line, label=f'Regression Line {i+1}', linestyle='--')
    # plt.legend(["Actual Standard Deviation", "Regression Line"])
    # plt.xlabel('Number of Spins')
    # plt.ylabel('Standard Deviation')
    # seed_num = np.random.get_state()[1][0]
    # plt.title(f'Seed number: {seed_num} (Standard Deviation)')
    # plt.savefig(f"Figure_{seed_num}.png")


    

    


def ex1_fig3(episode_creator, fig_num, exp_num):

    episodes = np.empty((1000, 1001), dtype=int)

    for i in range(len(episodes)):
        episodes[i][:] = episode_creator(1000)

    medians = np.median(episodes, axis=0)
    stds = np.std(episodes, axis=0, ddof=0)

    top_medians = medians + stds
    bottom_medians = medians - stds

    aggregates = np.vstack((top_medians, medians, bottom_medians))

    plt.figure(fig_num)
    plt.axis([0, 300, -256, 100])
    plt.plot(aggregates.T)
    plt.legend(["Median + SD", "Median", "Median - SD"])
    plt.xlabel('Number of Spins')
    plt.ylabel('Median Winnings')
    plt.title(f'Experiment {exp_num}: Figure {fig_num} (Median)')
    plt.savefig(f"Figure_{fig_num}.png")

def probability_calc(episode_creator):
    episodes = np.empty((1000, 1001), dtype=int)

    for i in range(len(episodes)):
        episodes[i][:] = episode_creator(1000)
    
    last_col = episodes[:, -1]

    ans = np.sum((last_col >= 80)) / len(last_col)
    # ans = np.mean(last_col) # To check expected value

    print('probability', ans)

    stds = np.std(episodes, axis=0, ddof=0)

    print('standard deviation', stds[-1])

  		  	   		 	   			  		 			     			  	 
if __name__ == "__main__":  		  	   		 	   			  		 			     			  	 
    test_code()  		  	   		 	   			  		 			     			  	 

