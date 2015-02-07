http://www.sqlcourse.com/

==============================
PART 1: Basic Select

Enter select statements to:

Display the first name and age for everyone that's in the table.
Display the first name, last name, and city for everyone that's not from Payson.
Display all columns for everyone that is over 40 years old.
Display the first and last names for everyone whose last name ends in an "ay".
Display all columns for everyone whose first name equals "Mary".
Display all columns for everyone whose first name contains "Mary".

select first, age from empinfo;
select first, last, city from empinfo where city <> 'Payson';
select * from empinfo where age > 40;
select first, last from empinfo where last like '%ay';
select * from empinfo where first = 'Mary';
select * from empinfo where first like '%Mary%';


==============================
PART 2: Using from

From the items_ordered table, select a list of all items purchased for customerid 10449. Display the customerid, item, and price for this customer.
Select all columns from the items_ordered table for whoever purchased a Tent.
Select the customerid, order_date, and item values from the items_ordered table for any items in the item column that start with the letter "S".
Select the distinct items in the items_ordered table. In other words, display a listing of each of the unique items from the items_ordered table.

select customerid, item, price from items_ordered where customerid = 10449;
select * from items_ordered where item = 'Tent';
select customerid, order_date, item from items_ordered where item like 'S%';
select distinct item from items_ordered order by item;

==============================
PART 3: Using aggregates

Select the maximum price of any item ordered in the items_ordered table. Hint: Select the maximum price only.
Select the average price of all of the items ordered that were purchased in the month of Dec.
What are the total number of rows in the items_ordered table?
For all of the tents that were ordered in the items_ordered table, what is the price of the lowest tent? Hint: Your query should return the price only.

select max(price) from items_ordered; 
select avg(price) from items_ordered  where order_date like '%Dec%';
select count(*) from items_ordered;
select min(price) from items_ordered where item = 'Tent';


==============================
PART 4: Using group by

How many people are in each unique state in the customers table? Select the state and display the number of people in each. Hint: count is used to count rows in a column, sum works on numeric data only.
From the items_ordered table, select the item, maximum price, and minimum price for each specific item in the table. Hint: The items will need to be broken up into separate groups.
How many orders did each customer make? Use the items_ordered table. Select the customerid, number of orders they made, and the sum of their orders.

select distinct state, count(*) from customers group by state;
select distinct item, max(price), min(price) from items_ordered group by item; 
select customerid, count(*), sum(price) from items_ordered group by customerid;

==============================
PART 5: Using having

How many people are in each unique state in the customers table that have more than one person in the state? Select the state and display the number of how many people are in each if it's greater than 1.
From the items_ordered table, select the item, maximum price, and minimum price for each specific item in the table. Only display the results if the maximum price for one of the items is greater than 190.00.
How many orders did each customer make? Use the items_ordered table. Select the customerid, number of orders they made, and the sum of their orders if they purchased more than 1 item.

select state, count(*) from customers group by state having count(*) > 1;
select item, max(price), min(price) from items_ordered group by item having max(price) > 190.00;
select customerid, count(*), sum(price) from items_ordered group by customerid having count(*) > 1;

==============================
PART 5: Using order by

Select the lastname, firstname, and city for all customers in the customers table. Display the results in Ascending Order based on the lastname.
Same thing as exercise #1, but display the results in Descending order.
Select the item and price for all of the items in the items_ordered table that the price is greater than 10.00. Display the results in Ascending order based on the price.



 select lastname, firstname, city from customers order by lastname;
 select lastname, firstname, city from customers order by lastname desc;
 select item, price from items_ordered where price > 10.00 order by price;

==============================
PART 6: Using conditions and booleans

Select the customerid, order_date, and item from the items_ordered table for all items unless they are 'Snow Shoes' or if they are 'Ear Muffs'. Display the rows as long as they are not either of these two items.
Select the item and price of all items that start with the letters 'S', 'P', or 'F'.

select customerid, order_date, item from items_ordered where (item <> 'Snow Shoes') and (item <> 'Ear Muffs');

select item, price from items_ordered where (item like 'S%') or (item like '%P') or (item like 'F%');

==============================
PART 7: Using in and between (these keywords can abbreviate statements that would otherwise need to be longer.)

Select the date, item, and price from the items_ordered table for all of the rows that have a price value ranging from 10.00 to 80.00.
Select the firstname, city, and state from the customers table for all of the rows where the state value is either: Arizona, Washington, Oklahoma, Colorado, or Hawaii.


select order_date, item, price from items_ordered where price between 10.00 and 80.00;

select firstname, city, state from customers where state in ('Arizona', 'Washington', 'Oklahoma', 'Colorado', 'Hawaii');


==============================
PART 8: Using mathematical operators

Select the item and per unit price for each item in the items_ordered table. Hint: Divide the price by the quantity.

select item, sum(price)/sum(quantity) from items_ordered group by item;

==============================
PART 9: Using joins

Write a query using a join to determine which items were ordered by each of the customers in the customers table. Select the customerid, firstname, lastname, order_date, item, and price for everything each customer purchased in the items_ordered table.
Repeat exercise #1, however display the results sorted by state in descending order.

select items_ordered.customerid, customers.firstname, customers.lastname, items_ordered.order_date, items_ordered.item, items_ordered.price
from customers inner join items_ordered on customers.customerid = items_ordered.customerid;

select items_ordered.state, items_ordered.customerid, customers.firstname, customers.lastname, items_ordered.order_date, items_ordered.item, items_ordered.price
from customers inner join items_ordered on customers.customerid = items_ordered.customerid order by customers.state desc;
