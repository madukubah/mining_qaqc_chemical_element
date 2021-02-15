 # -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import time

class QaqcDensity(models.Model):
	_name = "qaqc.density"
	_order = "id desc"

	name = fields.Char(string="Name", size=100 , required=True )
	density = fields.Float( string="Density (Ton/m^3)", required=True, default=0, digits=0 )