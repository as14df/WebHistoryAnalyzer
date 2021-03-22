import os.path
import db_reader
import data_formatter
import data_plotter

appData = os.getenv('LOCALAPPDATA')
db_path = os.path.join(appData, "Google", "Chrome", "User Data", "Default", "History")
#db_path = os.path.abspath("History")

# Get data from db
dbReader = db_reader.DatabaseReader(db_path)

viewsNotBlockedPerDate = dbReader.getNumberOfViewsNotBlockedPerDate()
viewsBlockedPerDate = dbReader.getNumberOfViewsBlockedPerDate()

viewsPerDomain = dbReader.getNumberOfViewsPerDomain()
viewsBlockedPerDomain = dbReader.getNumberOfViewsBlockedPerDomain()

# Format data
dataFormatter = data_formatter.DataFormatter()

seriesNotBlocked = dataFormatter.getContinuousDateCountSeries(viewsNotBlockedPerDate, viewsNotBlockedPerDate[0][0], viewsNotBlockedPerDate[-1][0])
seriesBlocked = dataFormatter.getContinuousDateCountSeries(viewsBlockedPerDate, viewsNotBlockedPerDate[0][0], viewsNotBlockedPerDate[-1][0])

# plot data
dataPlotter = data_plotter.DataPlotter()

dataPlotter.plotNumberOfViewsPerDateStackedBarChart(seriesNotBlocked, seriesBlocked)
dataPlotter.plotNumberOfViewsBarChart(seriesBlocked)

dataPlotter.plotNumberOfViewsPerDomainBarChart(viewsPerDomain)
dataPlotter.plotNumberOfViewsPerDomainBarChart(viewsBlockedPerDomain)

dataPlotter.showPlot()