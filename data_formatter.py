import pandas as pd

class DataFormatter:

    def getContinuousDateCountSeries(self, rows: list, startDate: str, endDate: str):
        dates = [row[0] for row in rows]
        counts = [row[1] for row in rows]

        index = pd.date_range(startDate, endDate)
        series = pd.Series(counts, index=pd.DatetimeIndex(dates))
        return series.reindex(index, fill_value=0)    
