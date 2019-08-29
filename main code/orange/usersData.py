from datetime import datetime
from flask import session
from databaseConnection import database
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from exception import Error


class UserAuthentication(object):
    def __init__(self, user_id, password, first_name, last_name, address, email_address, cell_phone):
        self.userID = user_id
        self.password = password
        self.firstName = first_name
        self.lastName = last_name
        self.address = address
        self.emailAddress = email_address
        self.cellPhone = cell_phone

    @classmethod
    def registration_details(cls, form):
        first_name = form.firstName.data
        last_name = form.lastName.data
        address = form.address.data
        email_address = form.emailAddress.data
        cell_phone = form.cellPhone.data
        password = form.password.data
        user_id = form.cellPhone.data
        return cls(user_id, password, first_name, last_name, address, email_address, cell_phone)

    @classmethod
    def login_details(cls, form):
        return cls(form.username.data, form.password.data, None, None, None, None, None)

    def store_record(self):
        data_cursor = database.cursor()
        sql = "INSERT INTO user_details " \
              "(userID,password,firstName,lastName,address,cellPhoneNumber,emailAddress,status)" \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (self.cellPhone, self.password, self.firstName, self.lastName, self.address,
                  self.cellPhone, self.emailAddress, "active")
        data_cursor.execute(sql, values)
        database.commit()
        data_cursor.close()

    def login_user(self):
        data_cursor = database.cursor(dictionary=True)
        sql = "SELECT password,firstName FROM user_details WHERE userID = %s"
        data_cursor.execute(sql, (self.userID,))
        sql_result = data_cursor.fetchone()
        data_cursor.close()
        if sql_result is not None:
            if self.password == sql_result['password']:
                timestamp = datetime.now().timestamp()
                session['logged_in'] = True
                session['user_id'] = self.userID
                session['username'] = sql_result['firstName']
                session['session_id'] = self.userID + str(timestamp)
                session['cart'] = 0
                return True
            else:
                raise Error("Passwords did not match")
        else:
            raise Error("Username NOT found")


class RegistrationForm(Form):
    firstName = StringField('First Name', [validators.Length(min=1, max=50)])
    lastName = StringField('Last Name', [validators.Length(min=1, max=50)])
    address = StringField('Address', [validators.Length(min=1, max=50)])
    emailAddress = StringField('Email Address', [validators.Length(min=5, max=50)])
    cellPhone = StringField('Cell Phone Number', [validators.Length(min=11, max=11)])
    password = PasswordField('Password', [validators.DataRequired(),
                                          validators.Length(min=8),
                                          validators.EqualTo('confirmPassword')])
    confirmPassword = PasswordField('Repeat Password', [validators.DataRequired(),
                                                        validators.Length(min=8)])


class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=11, max=11)])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=8)])

