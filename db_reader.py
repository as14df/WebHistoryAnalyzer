import sqlite3

class DatabaseReader:

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = sqlite3.connect('file:' + db_path + '?mode=ro', uri=True)
        self.cursor = self.connection.cursor()

    def get_history(self):
        self.cursor.execute("SELECT u.title, u.url, DATE(v.visit_time/1000000-11644473600,'unixepoch','localtime') FROM visits AS v, urls AS u WHERE u.id == v.url ORDER BY v.visit_time DESC Limit 100;")
        return self.cursor.fetchall()

    def getNumberOfViewsNotBlockedPerDate(self):
        self.cursor.execute("SELECT DATE(v.visit_time/1000000-11644473600,'unixepoch','localtime') AS date, COUNT(*) AS numberOfViews FROM visits AS v, urls AS u WHERE u.id == v.url AND NOT(Title like 'Access Blocked') GROUP BY date ORDER BY date ASC;")
        return self.cursor.fetchall()
    
    def getNumberOfViewsBlockedPerDate(self):
        self.cursor.execute("SELECT DATE(v.visit_time/1000000-11644473600,'unixepoch','localtime') AS date, COUNT(*) AS numberOfViews FROM visits AS v, urls AS u WHERE u.id == v.url AND Title like 'Access Blocked' GROUP BY date ORDER BY date ASC;")
        return self.cursor.fetchall()

    def getNumberOfViewsPerDomain(self):
        self.cursor.execute("SELECT COUNT(*) AS numberOfViews, SUBSTR(SUBSTR(u.url, INSTR(u.url, '//') + 2), 0, INSTR(SUBSTR(u.url, INSTR(u.url, '//') + 2), '/')) AS domain FROM visits AS v, urls AS u WHERE u.id == v.url GROUP BY domain ORDER BY numberOfViews DESC LIMIT 30")
        return self.cursor.fetchall()

    def getNumberOfViewsBlockedPerDomain(self):
        self.cursor.execute("SELECT COUNT(*) AS numberOfViews, SUBSTR(SUBSTR(u.url, INSTR(u.url, '//') + 2), 0, INSTR(SUBSTR(u.url, INSTR(u.url, '//') + 2), '/')) AS domain FROM visits AS v, urls AS u WHERE u.id == v.url AND u.title LIKE 'Access Blocked' GROUP BY domain ORDER BY numberOfViews DESC LIMIT 10;")
        return self.cursor.fetchall()

    def __del__(self):
        self.connection.close()
