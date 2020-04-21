CREATE TABLE Country(
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR (50)
);

CREATE TABLE Athlete(
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR (50),
    id_country INT NOT NULL REFERENCES Country(id)
);

CREATE TABLE Sport(
    id INT NOT NULL PRIMARY KEY,
    category VARCHAR (50),
    discipline VARCHAR (50),
    event VARCHAR (50)
);

CREATE TABLE Competition(
    id INT NOT NULL PRIMARY KEY,
    year INT,
    city VARCHAR (50)
);

CREATE TABLE Medal(
    id INT NOT NULL PRIMARY KEY,
    color VARCHAR (10),
    id_athlete INT NOT NULL REFERENCES Athlete(id),
    id_sport INT NOT NULL REFERENCES Sport(id),
    id_competition INT NOT NULL REFERENCES Competition(id)
);

