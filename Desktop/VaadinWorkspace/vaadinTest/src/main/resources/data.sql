CREATE TABLE IF NOT EXISTS Todo(id IDENTITY PRIMARY KEY, done BOOLEAN, text VARCHAR(200));
DELETE FROM Todo;
INSERT INTO Todo VALUES(1, TRUE, 'go to grocery store');
INSERT INTO Todo VALUES(2, TRUE, 'create Vaadin project');
INSERT INTO Todo VALUES(3, FALSE, 'bake rye bread');
