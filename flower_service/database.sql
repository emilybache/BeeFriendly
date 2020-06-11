CREATE DATABASE IF NOT EXISTS flowerdb;

USE flowerdb;

CREATE TABLE IF NOT EXISTS flowerdb.flowers (
    name        VARCHAR(100),
    flowering_months       VARCHAR(10),
    description VARCHAR(100),
    PRIMARY KEY (name)
);

DELETE FROM flowerdb.flowers;

INSERT INTO flowerdb.flowers VALUES ('azalea', 'may,june', 'Azalea');
INSERT INTO flowerdb.flowers VALUES ('daisy', 'may,june,july,august', 'Daisy');
INSERT INTO flowerdb.flowers VALUES ('forsythia', 'may', 'Forsythia');
INSERT INTO flowerdb.flowers VALUES ('giant_daisy', 'may,june', 'Giant Daisy');
INSERT INTO flowerdb.flowers VALUES ('lilac', 'may,june', 'Lilac');
INSERT INTO flowerdb.flowers VALUES ('peony', 'may,june', 'Peony');
INSERT INTO flowerdb.flowers VALUES ('rhododendron', 'may,june', 'Rhododendron');
INSERT INTO flowerdb.flowers VALUES ('wild_strawberry', 'may,june,july', 'Wild Strawberry');