import cx_Oracle
import chart_studio
import re
chart_studio.tools.set_credentials_file(username='AristovaIrina', api_key='b6ZYIennqI2QDGG5DZJu')
import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dash

def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId = re.findall("~[0-z.]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

username = 'Aristova'
password = 'Aristova'

database = 'localhost/xe'
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()



print('1.Вивести скільки медалей отримала кожна країна за 2008 рік, де загальна кількість медалей більше 30.  \n')
names=[]
values=[]
query1 = '''
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
'''

cursor.execute(query1)

for row in cursor.fetchall():
    names.append (row[0])
    values.append(row[1])
bar = go.Bar (x = names, y = values)
bar = py.plot([bar],auto_open = True, file_name = "Plot1")




print("\n2.Вивести скільки золотих, срібних і бронзових медалей отримала Україна за всі роки. \n")
names=[]
values=[]
query2 = '''
SELECT color, Count(color) AS Cnt
From Medal INNER JOIN (Select Athlete.id AS AthleteID
             From Athlete
             Where (Athlete.id_country = 114))
ON (Medal.id_athlete = AthleteID)
GROUP BY color
Order By Cnt asc
'''
cursor.execute(query2)
for row in cursor.fetchall():
    names.append (row[0])
    values.append(row[1])
pie = go.Pie (labels = names, values = values)
pie = py.plot([pie],auto_open = True, file_name = "Plot2",)




print("\n3.Вивести скільки медалей отримали США по роках.\n")
names=[]
values=[]
query3 = '''
SELECT year, Count(color) AS Cnt
From Medal INNER JOIN (Select Athlete.id AS AthleteID
             From Athlete
             Where (Athlete.id_country = 118))
ON (Medal.id_athlete = AthleteID)
INNER JOIN Competition ON (Medal.id_competition = Competition.id)
GROUP BY year ORDER BY year
'''
cursor.execute(query3)

for row in cursor.fetchall():
    names.append (row[0])
    values.append(row[1])
scatter = go.Scatter (x = names, y = values)
scatter = py.plot([scatter],auto_open = True, file_name = "Plot3")



my_dboard = dash.Dashboard()
bar_id = fileId_from_url(bar)
pie_id =fileId_from_url(pie)
scatter_id = fileId_from_url(scatter)
box_1= {
    'type': 'box',
    'boxType': 'plot',
    'fileId': bar_id,
    'title': '1.Вивести скільки медалей отримала кожна країна за 2008 рік, де загальна кількість медалей більше 30.'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': pie_id,
    'title': '2.Вивести скільки золотих, срібних і бронзових медалей отримала Україна за всі роки.'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': scatter_id,
    'title': '3.Вивести скільки медалей отримали США по роках.'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)


py.dashboard_ops.upload(my_dboard, 'Aristova_Irina')


cursor.close()
connection.close()
