# WebHistoryAnalyzer

Chrome ``History`` file liegt hier:
> C:\Users\Username\AppData\Local\Google\Chrome\User Data\Default

Zum auslesen des files on Ubuntu:
- apt install sqlite
- apt install sqlitebrowser

File ``History`` umbenennen zu ``History.db3``

Öffnen mit sqlitebrowser

## Installation
- six
- python-dateutil
- cycler
- pillow
- kiwisolver
- pyparsing
- numpy
- matplotlib

## Selects

SELECT u.title, u.url,
DATETIME(v.visit_time/1000000-11644473600,'unixepoch','localtime') FROM visits
AS v, urls AS u WHERE u.id == v.url ORDER BY v.visit_time DESC Limit 100;

SELECT u.title, u.url,
DATETIME(v.visit_time/1000000-11644473600,'unixepoch','localtime') FROM visits
AS v, urls AS u WHERE u.id == v.url AND u.title LIKE 'Access Blocked' ORDER BY
v.visit_time DESC;

SELECT u.title, u.url, SUBSTR(SUBSTR(u.url, INSTR(u.url, '//') + 2), 0,
INSTR(SUBSTR(u.url, INSTR(u.url, '//') + 2), '/')) AS domain,
DATETIME(v.visit_time/1000000-11644473600,'unixepoch','localtime') FROM visits
AS v, urls AS u WHERE u.id == v.url AND u.title LIKE 'Access Blocked' ORDER BY
domain;

WITH Last100 AS (SELECT * FROM visits AS v, urls AS u WHERE u.id == v.url ORDER
BY v.visit_time DESC LIMIT 1000) SELECT count(*) FROM Last100 WHERE title LIKE
'Access Blocked';

SELECT COUNT(*) AS count, SUBSTR(SUBSTR(u.url, INSTR(u.url, '//') + 2), 0,
INSTR(SUBSTR(u.url, INSTR(u.url, '//') + 2), '/')) AS domain FROM visits AS v,
urls AS u WHERE u.id == v.url AND u.title LIKE 'Access Blocked' GROUP BY domain
ORDER BY count DESC;

SELECT COUNT(*) AS numberOfViews, SUBSTR(SUBSTR(u.url, INSTR(u.url, '//') + 2),
0, INSTR(SUBSTR(u.url, INSTR(u.url, '//') + 2), '/')) AS domain FROM visits AS
v, urls AS u WHERE u.id == v.url AND u.title LIKE 'Access Blocked' GROUP BY
domain ORDER BY numberOfViews DESC;
