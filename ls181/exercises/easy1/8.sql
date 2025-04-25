ALTER TABLE birds ADD CHECK (age > 0);

INSERT INTO birds (name, age, species)
    VALUES ('test', -1, 'test1');

INSERT INTO birds (name, age, species)
    VALUES ('test', 4, 'test1');