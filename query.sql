--�����1: ������� ������ ������� �������� ����� ����� �� 2008 ��, �� �������� ������� ������� ����� 30.
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

--�����2: ������� ������ �������, ������ � ��������� ������� �������� ������ �� �� ����.
Select color, Count(color) AS Cnt
From Medal, (Select Athlete.id AS AthleteID
             From Athlete
             Where (Athlete.id_country = 114))
Where (Medal.id_athlete = AthleteID)
GROUP BY color
Order By Cnt asc;

--�����3: ������� ������ ������� �������� ��� �� �����.
Select year, Count(color) AS Cnt
From  Competition, Medal, (Select Athlete.id AS AthleteID
             From Athlete
             Where (Athlete.id_country = 118))
Where (Medal.id_athlete = AthleteID)
And (Medal.id_competition = Competition.id)
GROUP BY year;


