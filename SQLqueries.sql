SELECT quantity
from orders
where category id=1001** Product Categories 1000 to 1999 are for women.
** Product Categories 2000 to 2999 are for men.
** Product Categories 8000 is for Deleted products.

Fetching all product categories for women
Select*
From 'product_category'
Where catagory _id Between 1000 AND 1999


Fetching all product categories for men
Select *
From 'product_category'
Where catagory _id Between 2000 AND 2999


Fetching all product details for women
Select *
From 'product_details'
Where catagory _id Between 1000 AND 1999


Fetching all product details for men
Select *
From 'product_details'
Where catagory _id Between 2000 AND 2999


Fetching the password of a given user_id  from user_details
select password 
from user_details
where User-id=1

Fetching the password of a given user_id  from user_details
select password 
from user_details
where User-id=2

Inserting values of every column of table Cart
Insert Into cart(salesid ,userid , totalAmmount, date)
VALUES(10 ,1 ,300 ,10-01-19) 


Inserting values of every column of table Cart
Insert Into cart(salesid ,userid , totalAmmount, date)
VALUES(30 ,2 ,400 ,15-01-19) 

Fetcing Quantity left/Quantity for a random product
SELECT quantityLeft 
FROM `product_details`
 WHERE categoryID=1001

Updating quantity of a product
UPDATE 'Product_details'
SET quantityleft=120
WHERE category_Id=1001

Updating quantity of a product for unique category_id and product_id
UPDATE 'Product_details'
SET quantityleft=130
WHERE category_Id=1001 AND product_id=2

Updating Name of a product for unique category_id and product_id
UPDATE 'Product_details'
SET Product1=ProductP
WHERE category_Id=1001 AND product_id=1

Updating cost of a product for unique category_id and product_id
UPDATE 'Product_details'
SET cost=200
WHERE category_Id=1001 AND product_id=1

Updating price of a product for unique category_id and product_id
UPDATE 'Product_details'
SET price=600
WHERE category_Id=1001 AND product_id=1

Inserting in column of cart
Insert Into cart(salesid ,userid , totalAmmount, date)
VALUES(10 ,1 ,300 ,10-01-19)


Updating price of a product for unique category_id and product_id
UPDATE 'Product_details'
SET price=600
WHERE category_Id=1001 AND product_id=1

Fetching quantity from table orders
SELECT quantity
from orders
where category id=1001

Updating quantity from table orderds
Update 'Orders'
SET quantity=250
where product id=2

Inserting values in table orders
Insert INTO orders(sales_id ,category_id,product_id ,quantity)
values(1 ,1001,1,140)


Insrting query to add column Name in table orders
Alter TABLE orders
ADD Name varchar(25)

Updating column 'Name' of table orders
Update orders
SET Name='shirt'
where sales-id=1

Update orders
SET Name='pant'
where sales-id=2

Update orders
SET Name='kurti'
where sales-id=3

Adding column price in table orders
ALTER TABLE orders
ADD price float;

Updating price in table orders
UPDATE orders
SET price=150
where sales_id=1

Adding column totalprice in table orders
 ALTER TABLE orders
ADD totalprice float;

Updating values in column totalprice in table orders
UPDATE orders
SET totalprice=500
where sale_id=2

Fething name and price for a particular sales-id from table orders
SELECT  Name , price
FROM `orders`
where salesID=2

Fething name and totalprice for a particular sales-id from table orders
SELECT  Name , totalprice
FROM `orders`
 where salesID=2
Deopping column name and price from table orders
ALTER TABLE orders
DROP COLUMN price



ALTER TABLE orders
DROP COLUMN name


Fetching name, price , subtotal price for a given sales_id
SELECT orders.salesID, product_details.price, product_details.name,  orders.quantity,SUM(price), quantity*price AS subtotal
FROM orders
INNER JOIN product_details ON orders.categoryID =product_details.categoryID
AND salesID=1
 

Fetching total price for a product for a given salesid
SELECT orders.salesID, product_details.price, product_details.name,SUM(price) AS totalprice
 
FROM orders

INNER JOIN product_details ON orders.categoryID =product_details.categoryID
AND salesID=1


Query for removing entire row  from table orders for a unique sales_ id
 DELETE FROM orders
where sales_id=1