# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ArentiModel(models.Model):
    _name = "hotel.list"
    _description = "List that contains all the hotels in the hotel chain"

    name = fields.Char(string="Hotel name", required=True)
    country = fields.Char(string="Country", required=True)
    city = fields.Char(string="City", requiredd=True)
    manager = fields.Char(string="Manager", required=True)
    rooms = fields.Integer(string="Rooms", required=True)
    postal_code = fields.Integer(string="Postal Code", required=True)
    is_active = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="is Active")
    picture = fields.Binary(string="Image")

    @api.multi
    def get_hotel1(self):
        hotels = self.env['hotel.list'].search([])
        for hotel in hotels:
            break
        return {
            'name': 'Hotel List',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hotel.list',
            'res_id': hotel.id,
        }

    @api.multi
    def get_hotel2(self):
        hotels = self.env['hotel.list'].search([])
        i = 2
        for hotel in hotels:
            i = i - 1
            if i == 0:
                break
        return {
            'name': 'Hotel List',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hotel.list',
            'res_id': hotel.id,
        }

    @api.multi
    def get_hotel3(self):
        hotels = self.env['hotel.list'].search([])
        i = 3
        for hotel in hotels:
            i = i - 1
            if i == 0:
                break
        return {
            'name': 'Hotel List',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hotel.list',
            'res_id': hotel.id,
        }

    @api.multi
    def get_hotel4(self):
        hotels = self.env['hotel.list'].search([])
        i = 4
        for hotel in hotels:
            i = i - 1
            if i == 0:
                break
        return {
            'name': 'Hotel List',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hotel.list',
            'res_id': hotel.id,
        }

    class Managerlist(models.Model):
        _name = "manager.list"

        name = fields.Char(string="Name", required=True)
        surname = fields.Char(string="Surname", required=True)
        age = fields.Integer(string="Age", required=True)
        nationality = fields.Char(string="Nationality", required=True)
        gender = fields.Selection([('male', 'Male'),
                                   ('female', 'Female')],
                                  string="Gender", required=True)
        phone = fields.Char(string="Phone number", required=True)
        email = fields.Char(string="Email")
        address = fields.Char(string="Address")
        salary = fields.Char(string="Salary", required=True)
        language = fields.Char(string="Language", required=True)
        picture = fields.Binary(string="Picture")

        @api.multi
        def get_manager1(self):
            managers = self.env['manager.list'].search([])
            for manager in managers:
                break
            return {
                'name': 'Manager List',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'manager.list',
                'res_id': manager.id,
            }
        @api.multi
        def get_manager2(self):
            managers = self.env['manager.list'].search([])
            i = 2
            for manager in managers:
                i = i - 1
                if i == 0:
                    break
            return {
                'name': 'Manager List',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'manager.list',
                'res_id': manager.id,
            }

        @api.multi
        def get_manager3(self):
            managers = self.env['manager.list'].search([])
            i = 3
            for manager in managers:
                i = i - 1
                if i == 0:
                    break
            return {
                'name': 'Manager List',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'manager.list',
                'res_id': manager.id,
            }

        @api.multi
        def get_manager4(self):
            managers = self.env['manager.list'].search([])
            i = 4
            for manager in managers:
                i = i - 1
                if i == 0:
                    break
            return {
                'name': 'Manager List',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'manager.list',
                'res_id': manager.id,
            }
