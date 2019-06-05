# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Session(models.Model):
    _name = 'open_academy.session'
    _description = 'This is the session model for the Open Academy module.'

    name = fields.Char(string='Title', required=True)
    date_start = fields.Date(string='Start Date')
    date_stop = fields.Date(string='Stop Date')
    course = fields.Many2one('open_academy.course', required=True)
    teacher = fields.Many2one('open_academy.teacher', required=True)