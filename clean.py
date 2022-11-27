import datetime
import pandas as pd
import ipdb
import matplotlib.pyplot as plt

class Clean:
    """
    Cleans the columns to form plots
    """

    def __init__(self):
        pass

    def aggregate_month(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Aggregates month data and return mean for each month
        """
        df = df[['Period', 'Value']]
        df['Period'] = df.apply(lambda x : datetime.datetime.strptime(x['Period'],  '%Y-%m-%d'), axis=1)
        months = df.Period.dt.to_period("M")

        grouped_month = df.groupby(months)

        mean = grouped_month.mean().reset_index()

        return mean

    def plot_scatter(self, x: list, y: list) -> None:
        """
        Generates a scatter plot and saves it in the current working directory
        """

        plt.title('Correlation between bank yield and mortgages taken')

        plt.scatter(x, y, s= 10, c='red')

        plt.xlabel('Period')
        plt.ylabel('Bank yield')

        plt.savefig('scatter plot.png')

        return
