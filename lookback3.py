#PostgreSQL

SELECT last_name, first_name from actor;

SELECT * from actor;


#How many unique release year do we have inside this table?

SELECT DISTINCT release_year FROM film;

SELECT DISTINCT rental_rate FROM film;


#Return the number of rows in the table

SELECT COUNT(name) FROM table;


SELECT COUNT(*) FROM table;

#Total number of unique payment

SELECT COUNT (DISTINCT amount) FROM payment;