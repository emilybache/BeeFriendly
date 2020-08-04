CREATE DATABASE IF NOT EXISTS master;
CREATE DATABASE IF NOT EXISTS users;

USE users;

CREATE TABLE IF NOT EXISTS users.people (
    name        VARCHAR(100),
    title       VARCHAR(10),
    description VARCHAR(100),
    PRIMARY KEY (name)
);

DELETE FROM users.people;

INSERT INTO users.people VALUES ('Charles Darwin', 'Dr.', 'On the origin of species');
INSERT INTO users.people VALUES ('Carl Linnaeus', 'Prof.', 'Species Plantarum');
INSERT INTO users.people VALUES ('Sophie Lutterlough', 'Mrs.', 'Pygmephorus lutterloughae');
INSERT INTO users.people VALUES ('Karl von Frisch', 'Dr.', 'The Dancing Bees: An Account of the Life and Senses of the Honey Bee');
INSERT INTO users.people VALUES ('Dave Goulson', 'Prof.', 'Bumblebees: Their Behaviour and Ecology');
INSERT INTO users.people VALUES ('Charles Duncan Michener', 'Dr.', 'The Social Behavior of the Bees');
INSERT INTO users.people VALUES ('Emily Dickinson', 'Ms.', "The Bumble-Bee's Religion");
INSERT INTO users.people VALUES ('Nikolai Rimsky-Korsakov', 'Mr.', 'Flight of the Bumblebee');
