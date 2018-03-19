from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, IntegerField, SelectField, validators


# Order Form Class
class OrderForm(Form):
    productid = IntegerField('Product ID', [validators.NumberRange(min=1, max=3)])
    name = TextAreaField('Name', [validators.Length(min=2, max=30)])
    phone = IntegerField('Phone', [validators.NumberRange(min=1, max=99999999999999999999)])
    address = TextAreaField('Address', [validators.Length(min=6, max=50)])


