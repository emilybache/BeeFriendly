CREATE DATABASE IF NOT EXISTS users;

USE users;

CREATE TABLE IF NOT EXISTS users.people (
    name        VARCHAR(100),
    title       VARCHAR(10),
    description VARCHAR(100),
    PRIMARY KEY (name)
);

DELETE FROM users.people;

INSERT INTO users.people VALUES ('Gru', 'Felonius', 'Where are the minions?');
INSERT INTO users.people VALUES ('Nefario', 'Dr.', 'Why ... why are you so old?');
INSERT INTO users.people VALUES ('Agnes', '', 'Your unicorn is so fluffy!');
INSERT INTO users.people VALUES ('Edith', '', "Don't touch anything!");
INSERT INTO users.people VALUES ('Vector', '', 'Committing crimes with both direction and magnitude!');
INSERT INTO users.people VALUES ('Dave', 'Minion', 'Ngaaahaaa! Patalaki patalaku Big Boss!!');
