# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ClientsModel(models.Model):
    _name = "clients.list"

    name = fields.Char(string = "Name")
    surname = fields.Char(string = "Surname")
    nationality = fields.Char(string = "Nationality")
    phone = fields.Char(string = "Phone number")
    email = fields.Char(string = "Email")
    address = fields.Char(string = "Address")
    hotel_list = fields.Many2many('hotel.list', string = "Hotel")

class ViewModel(models.Model):
    _name = "view.list"

    view_name = fields.Char(string="View")
    view_image = fields.Binary(string="View_image")

class RoomType(models.Model):
    _name = "room.list"

    room_type = fields.Char(string="Room type")
    bed_number = fields.Integer(string="Bed number")
    bathroom = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Bathroom")
    room_image = fields.Binary(string="Room_image")


class BookingsModel(models.Model):
    _name = "bookings.list"

    hotel_id = fields.Many2one('hotel.list', string="Hotel")
    client_name_id = fields.Many2one('clients.list', string="Name")
    client_surname_id = fields.Many2one('clients.list', string="Surname")
    view_id = fields.Many2one('view.list', string="View")
    client_phone = fields.Many2one('clients.list', string="Phone number")
    client_email = fields.Many2one('clients.list', string="Email")
    booked_date = fields.Date(string = "Booked date")
    arrival_date = fields.Date(string = "Arrival date")
    departure_date = fields.Date(string = "Departure date")
    #name_get()
    room_type = fields.Many2one('room.list', string="Room type")
    number = fields.Char(string = "Number of rooms")
    nights = fields.Char(string = "Nights")
    price = fields.Integer(string = "Price")
    is_cancelled = fields.Selection([('yes', 'Yes'),
                                     ('no', 'No')])
    cancellation_date = fields.Date(string = "Cancellation date")
    hotel_number = fields.Integer(string="Hotel Number")
    current_month = fields.Integer(string="current month")
    current_year = fields.Integer(string="year")

    #add these fields in the csv file and re import


class InvoiceModel(models.Model):
    _name = "invoice.list"
    _inherit = "bookings.list"

    current_month = fields.Integer(string="current month")
    current_year = fields.Integer(string="current_year")
    amount = fields.Float(string="Tax")
    type = fields.Char(string="Type")

    @api.multi
    def calculate_invoice(self):
        count_month = self.current_month
        count_year = self.current_year
        if self.current_month != 12:
            count_month = self.current_month + 1
        else:
            count_month = 1
            count_year = self.current_year + 1                       #self.current_year
        bookings = self.env['bookings.list'].search([('current_year', '=', count_year), ('current_month', '=', count_month)])
        amountt = sum(bookings.mapped('price')) * 0.14
        vals = {
            'current_month' : count_month,
            'current_year' : count_year,
            'amount' : amountt,
            'type' : 'Comission'
        }
        self.env['invoice.list'].create(vals)
        #return self.env.ref('hclients.report_invoice').report_action(self)






