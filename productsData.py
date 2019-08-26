from databaseConnection import database


class ProductsData(object):
    def __init__(self, category_id, product_id, name, price, cost, quantity_left, view):
        self.view = view
        self.categoryID = category_id
        self.productID = product_id
        self.name = name
        self.price = price
        self.cost = cost
        self.quantityLeft = quantity_left
        self.columnName = None
        self.sql = None
        self.values = None

    @classmethod
    def view(cls, view):
        return cls(None, None, None, None, None, None, view)

    @classmethod
    def new_product(cls, category_id, product_id, name, price, cost, quantity_left):
        return cls(category_id, product_id, name, price, cost, quantity_left, 'admin')

    def category_info(self):
        data_cursor = database.cursor(dictionary=True)
        if self.view == "women":
            data_cursor.execute("SELECT * FROM product_category WHERE categoryID BETWEEN 1000 AND 1999")
        elif self.view == "men":
            data_cursor.execute("SELECT * FROM product_category WHERE categoryID BETWEEN 2000 AND 2999")
        elif self.view == 'admin':
            data_cursor.execute("SELECT * FROM product_category")
        sql_result = data_cursor.fetchall()
        data_cursor.close()
        return sql_result

    def products_info(self):
        data_cursor = database.cursor(dictionary=True)
        if self.view == "women":
            data_cursor.execute("SELECT * FROM product_details WHERE categoryID BETWEEN 1000 AND 1999")
        elif self.view == "men":
            data_cursor.execute("SELECT * FROM product_details WHERE categoryID BETWEEN 2000 AND 2999")
        elif self.view == 'admin':
            data_cursor.execute("SELECT * FROM product_details")
        sql_result = data_cursor.fetchall()
        data_cursor.close()
        return sql_result

    def add_product(self):
        data_cursor = database.cursor(dictionary=True)
        sql = "INSERT INTO product_details (categoryID,productID,name,price,cost,quantityLeft) " \
              "VALUES (%s, %s, %s, %s, %s, %s)"
        values = (self.categoryID, self.productID, self.name, self.price, self.cost, self.quantityLeft)
        data_cursor.execute(sql, values)
        database.commit()

    def add_category(self, category_id, category_name):
        data_cursor = database.cursor(dictionary=True)
        sql = "INSERT INTO product_category(categoryID,categoryName)VALUES(%s, %s)"
        values = (category_id, category_name)
        data_cursor.execute(sql, values)
        database.commit()

    def delete_category(self, category_id):
        data_cursor = database.cursor(dictionary=True)
        sql = "DELETE FROM product_category WHERE categoryID=%s"
        data_cursor.execute(sql, (category_id,))
        database.commit()

    def update_category(self, column_name, new_value, target_category_id):
        self.sql = f"UPDATE product_category SET {column_name}=%s WHERE categoryID=%s"
        self.values = (new_value, target_category_id,)
        data_cursor = database.cursor(dictionary=True)
        data_cursor.execute(self.sql, self.values)
        database.commit()
        data_cursor.close()

    def update_product_details(self, column_name, new_value, target_category_id, target_product_id):
        self.sql = f"UPDATE product_details SET {column_name}=%s WHERE categoryID=%s AND productID=%s"
        self.values = (new_value, target_category_id, target_product_id,)
        data_cursor = database.cursor(dictionary=True)
        data_cursor.execute(self.sql, self.values)
        database.commit()
        data_cursor.close()
