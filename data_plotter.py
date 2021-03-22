import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from statistics import mean

class DataPlotter:

    def plotNumberOfViewsPerDateStackedBarChart(self, seriesNotBlocked: pd.Series, seriesBlocked: pd.Series):
        _, ax = plt.subplots(figsize=(18,7))                         # create new figure

        ax.bar(seriesNotBlocked.index, seriesNotBlocked.values)
        ax.bar(seriesBlocked.index, seriesBlocked.values, bottom=seriesNotBlocked.values)
        ax.set_xticklabels(seriesNotBlocked.index, rotation='vertical')
        ax.xaxis.set_major_locator(mdates.DayLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
        ax.grid(linestyle='dotted')

        # add means 
        seriesNotBlockedMean = mean([v for v in seriesNotBlocked.values if v != 0])
        seriesBlockedMean = mean([v for v in seriesBlocked.values if v != 0])
        plt.axhline(y=seriesNotBlockedMean, linewidth=2, color='blue')
        plt.axhline(y=seriesBlockedMean, linewidth=2, color='red')

        # add labels of means
        trans = transforms.blended_transform_factory(ax.get_yticklabels()[0].get_transform(), ax.transData)
        ax.text(0, seriesNotBlockedMean, "{:.0f}".format(seriesNotBlockedMean), color="blue", transform=trans, ha="right", va="center")
        ax.text(0, seriesBlockedMean, "{:.0f}".format(seriesBlockedMean), color="red", transform=trans, ha="right", va="bottom")

    def plotNumberOfViewsBarChart(self, series):
        _, ax = plt.subplots(figsize=(18,7))

        ax.bar(series.index, series.values)
        ax.set_xticklabels(series.index, rotation='vertical')
        ax.xaxis.set_major_locator(mdates.DayLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
        ax.grid(linestyle='dotted')

        # add means 
        seriesMean = mean([v for v in series.values if v != 0])
        plt.axhline(y=seriesMean, linewidth=2, color='red')

        # add label of mean
        trans = transforms.blended_transform_factory(ax.get_yticklabels()[0].get_transform(), ax.transData)
        ax.text(0, seriesMean, "{:.0f}".format(seriesMean), color="red", transform=trans, ha="right", va="center")

    def plotNumberOfViewsPerDomainBarChart(self, rows: list):
        counts = [row[0] for row in rows]
        labels = [row[1] for row in rows]

        frame = pd.DataFrame({'labels': labels, 'counts': counts}).sort_values(by='counts')
        ax = frame.plot.barh(x ='labels', y='counts', figsize=(18, 7))
        ax.grid(which='major', linestyle='dotted')

    def showPlot(self):
        plt.tight_layout()
        plt.show()
