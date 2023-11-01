
import numpy as np
from scipy.stats import norm
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


class NormalDist:
    def __init__(self, dframe, variable):
        self.dframe = dframe
        self.variable = variable
        self.mu = round(self.dframe[self.variable].mean(), 2)
        self.sigma = round(self.dframe[self.variable].std(), 2)
        self.density = pd.DataFrame()
        self.density['x'] = np.linspace(
            self.dframe[variable].min() - 0.01, self.dframe[variable].max() + 0.01, 100
        )
        self.density['pdf'] = norm.pdf(self.density['x'], self.mu, self.sigma)

    def plot_normal_dist(self):
        fig, ax = plt.subplots()
        sns.histplot(self.dframe[self.variable], ax=ax, kde=True, stat='density')
        ax.plot(self.density['x'], self.density['pdf'], color='red')
        plt.title("Distribucion normal")
        plt.show()

    # The probability that a student will score less than SCORE
    def prob_score_less_than(self, score):
        prob_less_than_score = norm.cdf(score, self.mu, self.sigma)
        prob_less_than_score = round(prob_less_than_score, 4)
        str_prob_less_than_score = str(round(prob_less_than_score * 100, 4)) + "%"
        print("Prob less than is:", score, " is :", str_prob_less_than_score)
        print("----------------------------")
        plt.plot(self.density["x"], self.density["pdf"])  # plot the pdf of the normal distribution
        plt.axvline(x=score, c="r")  # draw a red vertical line at x = SCORE
        x1 = np.linspace(self.density["x"].min(), score,
                         50)  # create an array of 50 numbers between min SAT score and SCORE
        plt.fill_between(x1, norm.pdf(x1, self.mu, self.sigma), color="b")  # fill the specified region with red color
        plt.xlabel(self.variable)  # set the x-axis label
        plt.ylabel("Probability")  # set the y-axis label
        plt.title("Normal Distribution")  # set the title
        plt.annotate(' Prob less ' + str(score) + '= ' + str_prob_less_than_score,
                     xy=(score, 0),
                     fontsize=12)
        plt.show()  # display the plot

    def prob_score_more_than(self, score):
        prob_more_than_score = norm.sf(score, self.mu, self.sigma)
        prob_more_than_score = round(prob_more_than_score, 4)
        str_prob_more_than_score = str(round(prob_more_than_score * 100, 4)) + "%"
        print("Prob more than is:", score, " is :", str_prob_more_than_score)
        print("----------------------------")
        print(self.density['pdf'].median())
        plt.plot(self.density["x"], self.density["pdf"])  # plot the pdf of the normal distribution
        plt.axvline(x=score, c="r")  # draw a red vertical line at x = SCORE
        x1 = np.linspace(score, self.density["x"].max(),
                         50)  # create an array of 50 numbers between min SAT score and SCORE
        plt.fill_between(x1, norm.pdf(x1, self.mu, self.sigma), color="b")  # fill the specified region with red color
        plt.xlabel(self.variable)  # set the x-axis label
        plt.ylabel("Probability")  # set the y-axis label
        plt.title("Normal Distribution")  # set the title
        plt.annotate(' Prob more ' + str(score) + '= ' + str_prob_more_than_score,
                     xy=(score, self.density['pdf'].median()),
                     fontsize=12)
        plt.show()  # display the plot

    # calculate the 90th percentile score using ppf() function
    def calculate_percentile(self, percentile):
        percentile_score = norm.ppf(percentile, self.mu, self.sigma)
        percentile_score = round(percentile_score, 2)
        print("The {}th percentile score is {}".format(percentile * 100, percentile_score))
        print("----------------------------")
        plt.plot(self.density["x"], self.density["pdf"])  # plot the pdf of the normal distribution
        plt.axvline(x=percentile_score, c="r")  # draw a red vertical line at x = score
        x1 = np.linspace(self.density["x"].min(), percentile_score,
                         50)  # create an array of 50 numbers between min SAT score and score
        # plt.fill_between(x1, norm.pdf(x1, self.mu, self.sigma), color="b") # fill the specified region with red color
        plt.xlabel(self.variable)  # set the x-axis label
        plt.ylabel("Probability")  # set the y-axis label
        plt.title("Normal Distribution")  # set the title
        plt.annotate(' {}th percentile score = {}'.format(percentile * 100, percentile_score),
                     xy=(percentile_score-(percentile_score/2), 0),
                     fontsize=12)
        plt.show()  # display the plot


class BinomialDist:
    def __init__(self):
        pass


data = pd.read_csv('sat_score.csv')
nd = NormalDist(data, 'score')
nd.plot_normal_dist()
nd.prob_score_less_than(800)
nd.prob_score_more_than(1300)
nd.calculate_percentile(0.9)
nd.calculate_percentile(0.95)


