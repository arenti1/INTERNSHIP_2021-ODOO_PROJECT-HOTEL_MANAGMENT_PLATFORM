from odoo import models, fields, api

class EmployeeModel(models.Model):
    _name = "employee.list"
    _description = "List that contains all the employees of the hotel chain"

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    age = fields.Char(string="Age", required=True)
    nationality = fields.Char(string="Nationality", required=True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female')],
                              string="Gender", required=True)
    phone = fields.Char(string="Phone Number", required = True)
    email = fields.Char(string="Email")
    salary = fields.Char(string="Salary", required=True)
    picture = fields.Binary(string="Picture")
    hotel_number = fields.Integer(string="Hotel Number")

