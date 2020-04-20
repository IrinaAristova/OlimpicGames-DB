import cx_Oracle

username = 'Aristova'
password = 'Aristova'
databaseName = 'localhost/xe'
connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()

# query1
print("1.Вивести скільки медалей отримала кожна країна за 2008 рік, де загальна кількість медалей більше 30.\n")
query = """
SELECT CountryName, Cnt FROM
(SELECT CountryName, Count(CountryName) AS Cnt
From Medal, Competition, (Select Athlete.id AS AthleteID, Country.name AS CountryName
From Athlete
LEFT OUTER JOIN Country ON Athlete.id_country = Country.id)
Where (Medal.id_athlete = AthleteID)
And (Medal.id_competition = Competition.id)
And (Competition.year = 2008)
GROUP BY CountryName)
WHERE (Cnt > 30)
"""

cursor.execute(query)

for row in cursor:
    print(row)

# query2
print("2.Вивести скільки золотих, срібних і бронзових медалей отримала Україна за всі роки.\n")
query = """
Select color, Count(color) AS Cnt
From Medal INNER JOIN (Select Athlete.id AS AthleteID
From Athlete
Where (Athlete.id_country = 114))
ON (Medal.id_athlete = AthleteID)
GROUP BY color
Order By Cnt asc
"""

cursor.execute(query)

for row in cursor:
    print(row)

# query3
print("3.Вивести скільки медалей отримали США по роках.\n")
query = """
Select year, Count(color) AS Cnt
From Medal INNER JOIN (Select Athlete.id AS AthleteID
From Athlete
Where (Athlete.id_country = 118))
ON (Medal.id_athlete = AthleteID)
INNER JOIN Competition ON (Medal.id_competition = Competition.id)
GROUP BY year ORDER BY year
"""

cursor.execute(query)

for row in cursor:
    print(row)
cursor.close()
connection.close()
