--Запит1: Вивести скільки медалей отримала кожна країна за 2008 рік, де загальна кількість медалей більше 30.
SELECT CountryName, Cnt FROM
(SELECT CountryName, Count(CountryName) AS Cnt
From Medal, Competition, (Select Athlete.id AS AthleteID, Country.name AS CountryName
             From Athlete, Country
             Where Athlete.id_country = Country.id)
Where (Medal.id_athlete = AthleteID)
And (Medal.id_competition = Competition.id)
And (Competition.year = 2008)
GROUP BY CountryName)
WHERE (Cnt > 30);

--Запит2: Вивести скільки золотих, срібних і бронзових медалей отримала Україна за всі роки.
Select color, Count(color) AS Cnt
From Medal, (Select Athlete.id AS AthleteID
             From Athlete
             Where (Athlete.id_country = 114))
Where (Medal.id_athlete = AthleteID)
GROUP BY color
Order By Cnt asc;

--Запит3: Вивести скільки медалей отримали США по роках.
Select year, Count(color) AS Cnt
From  Competition, Medal, (Select Athlete.id AS AthleteID
             From Athlete
             Where (Athlete.id_country = 118))
Where (Medal.id_athlete = AthleteID)
And (Medal.id_competition = Competition.id)
GROUP BY year;


