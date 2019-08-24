from databaseConnection import database
from exception import Error
from flask import session
from datetime import datetime, date


class Cart(object):
    def __init__(self, session_id):
        self.sessionID = session_id

    def fetch_quantity_left(self, category_id, product_id):
        data_cursor = database.cursor(dictionary=True)
        sql = "SELECT quantityLeft FROM product_details WHERE categoryID=%s AND productID=%s"
        data_cursor.execute(sql, (category_id, product_id,))
        sql_result = data_cursor.fetchone()
        data_cursor.close()
        return sql_result['quantityLeft']

    def update_quantity_left(self, quantity_left, category_id, product_id):
        data_cursor = database.cursor(dictionary=True)
        sql = "UPDATE product_details SET quantityLeft=%s WHERE categoryID=%s AND productID=%s"
        values = (quantity_left, category_id, product_id)
        data_cursor.execute(sql, values)
        database.commit()
        data_cursor.close()

    def fetch_cart_quantity(self, category_id, product_id):
        data_cursor = database.cursor(dictionary=True)
        sql = "SELECT quantity FROM orders WHERE salesID=%s AND categoryID=%s AND productID=%s"
        data_cursor.execute(sql, (self.sessionID, category_id, product_id,))
        sql_result = data_cursor.fetchone()
        data_cursor.close()
        if sql_result is not None:
            return sql_result['quantity']
        else:
            return None

    def update_cart_quantity(self, cart_quantity, category_id, product_id):
        data_cursor = database.cursor(dictionary=True)
        sql = "UPDATE orders SET quantity=%s WHERE salesID=%s AND categoryID=%s AND productID=%s"
        values = (cart_quantity, self.sessionID, category_id, product_id)
        data_cursor.execute(sql, values)
        database.commit()
        data_cursor.close()

    def insert_into_cart(self, category_id, product_id):
        data_cursor = database.cursor(dictionary=True)
        sql = "INSERT INTO orders(salesID,categoryID,productID,quantity) VALUES (%s, %s, %s, 1)"
        values = (self.sessionID, category_id, product_id,)
        data_cursor.execute(sql, values)
        database.commit()
        data_cursor.close()

    def add_to_cart(self, category_id, product_id):
        quantity_left = self.fetch_quantity_left(category_id, product_id)
        if quantity_left > 0:
            cart_quantity = self.fetch_cart_quantity(category_id, product_id)
            if cart_quantity is not None:
                cart_quantity += 1
                self.update_cart_quantity(cart_quantity, category_id, product_id)
                quantity_left -= 1
                self.update_quantity_left(quantity_left, category_id, product_id)
                session['cart'] += 1
            else:
                self.insert_into_cart(category_id, product_id)
                quantity_left -= 1
                self.update_quantity_left(quantity_left, category_id, product_id)
                session['cart'] += 1
        else:
            raise Error("Product Unavailable")

    def remove_from_cart(self, category_id, product_id):
        cart_quantity = self.fetch_cart_quantity(category_id, product_id)
        quantity_left = self.fetch_quantity_left(category_id, product_id)
        data_cursor = database.cursor(dictionary=True)
        sql = "DELETE FROM orders WHERE salesID=%s AND categoryID=%s AND productID=%s"
        data_cursor.execute(sql, (self.sessionID, category_id, product_id,))
        database.commit()
        data_cursor.close()
        self.update_quantity_left(quantity_left+cart_quantity, category_id, product_id)
        session['cart'] -= cart_quantity

    def cancel_cart(self,):
        data_cursor = database.cursor(dictionary=True)
        sql = "SELECT categoryID,productID,quantity FROM orders WHERE salesID=%s"
        data_cursor.execute(sql, (self.sessionID,))
        cart = data_cursor.fetchall()
        if cart is not None:
            sql = "DELETE FROM orders WHERE salesID=%s"
            data_cursor.execute(sql, (self.sessionID,))
            database.commit()
        data_cursor.close()
        for product in cart:
            cart_quantity = product['quantity']
            quantity_left = self.fetch_quantity_left(product['categoryID'], product['productID'])
            self.update_quantity_left(quantity_left+cart_quantity, product['categoryID'], product['productID'])
            session['cart'] -= cart_quantity

    def get_cart(self):
        data_cursor = database.cursor(dictionary=True)
        sql = "SELECT o.categoryID, o.productID, p.name, o.quantity, o.quantity*p.price AS amount " \
              "FROM orders AS o JOIN product_details AS p ON o.categoryID = p.categoryID " \
              "AND o.productID = p.productID WHERE salesID=%s"
        data_cursor.execute(sql, (self.sessionID,))
        sql_result = data_cursor.fetchall()
        data_cursor.close()
        return sql_result

    def get_cart_total_price(self):
        data_cursor = database.cursor(dictionary=True)
        sql = "SELECT SUM(o.quantity*p.price) AS sum FROM orders AS o " \
              "JOIN product_details AS p ON o.categoryID = p.categoryID AND o.productID = p.productID " \
              "WHERE salesID=%s"
        data_cursor.execute(sql, (self.sessionID,))
        total_price = data_cursor.fetchone()
        data_cursor.close()
        return total_price

    def save_transaction(self, order_id):
        now = str(date.today())
        total_amount = self.get_cart_total_price()
        data_cursor = database.cursor(dictionary=True)
        sql = "INSERT INTO sales(salesID,userID,orderID,totalAmount,date)VALUES(%s, %s, %s, %s, %s)"
        values = (session['session_id'], session['user_id'], order_id, total_amount['sum'], now)
        data_cursor.execute(sql, values)
        database.commit()
        timestamp = datetime.now().timestamp()
        session['session_id'] = session['user_id'] + str(timestamp)
        session['cart'] = 0

    def get_dashboard(self, user_id):
        data_cursor = database.cursor(dictionary=True)
        sql = "SELECT o.categoryID, o.productID, p.name, p.price, o.quantity, s.date FROM sales AS s " \
              "JOIN orders as o ON s.salesID=o.salesID " \
              "JOIN product_details as p ON o.categoryID=p.categoryID AND o.productID=p.productID " \
              "WHERE userID=%s ORDER BY s.date DESC"
        data_cursor.execute(sql, (user_id,))
        sql_result = data_cursor.fetchall()
        data_cursor.close()
        return sql_result

