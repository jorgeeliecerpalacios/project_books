
CREATE SCHEMA books_project DEFAULT CHARACTER SET utf8 ;

use books_project;
CREATE TABLE books (
  id int NOT NULL AUTO_INCREMENT,
  name varchar(100) NOT NULL,
  quality varchar(100) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE book (
  id int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `collection` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  books_id int NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (books_id) REFERENCES books(id)
);

-- ++++++++++ inserting some data ++++++++

INSERT INTO books (name, quality)
VALUES 
('harry Poter', 'Paste'),
('Pragmatic programer', 'Kindle'),
('Cracking the coding interview', 'Paste');


INSERT INTO book (books_id, name, collection, location)
VALUES 
(1,'harry Poter', 'fiction','station1'),
(2,'Pragmatic programer', 'developers','station2'),
(3,'Cracking the coding interview', 'developers','station2');


-- +++++++++++ some usefull querys +++++++++++++++

-- query to get all the data
-- SELECT 
-- bks.name, bks.quality, bk.collection, bk.location 
-- FROM book as bk
-- join books as bks on bk.books_id=bks.id
-- ;

-- query to get only one book 
-- SELECT 
-- bks.name, bks.quality, bk.collection, bk.location 
-- FROM book as bk
-- join books as bks on bk.books_id=bks.id
-- where bks.id = 1
-- ;