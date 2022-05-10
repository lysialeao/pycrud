CREATE DATABASE Pokemon;

USE Pokemon;

CREATE TABLE Pokemon(
	id INT PRIMARY KEY,
	name VARCHAR(200) NOT NULL,
	height INT NOT NULL,
	base_experience INT NOT NULL
);

INSERT INTO Pokemon VALUES(
	132, "ditto", 3, 101
);

INSERT INTO Pokemon VALUES(
	59, "arcanine", 19, 194
);

INSERT INTO Pokemon VALUES(
	25, "pikachu", 4, 112
);


