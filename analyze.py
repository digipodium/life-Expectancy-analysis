import pandas as pd

class Analyse:

    def __init__(self, path = 'datasets/lifeExpectancyAtBirth.csv'):
        self.df = pd.read_csv(path)


    def getDataframe(self):
        return self.df

    def getColumn(self, col):
        return self.df[col]