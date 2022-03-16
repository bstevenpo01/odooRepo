# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class alquiler(models.Model):
#     _name = 'alquiler.alquiler'
#     _description = 'alquiler.alquiler'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api

class suscripcion(models.Model):
    _name = 'alquileres.suscripcion'
    _description = 'Define los atributos de la suscripcion'

    # Atributos
    nombreSus = fields.Char(string='Nombre suscripcion', required=True)
    tipoSuscripcion = fields.Selection(string='Tipo de suscripcion', selection=[('a','platinun'),('b','Gold'),('c','Gold+'),('d','Vip')], help='Tipo de suscripcion que tiene el cliente', required=True)
    descripcionSuscripcion = fields.Text(string='Descripcion de la suscripcion')



    #Relacion entre tablas
    cliente_id = fields.One2many('alquileres.cliente','suscripcion_id', string='Suscripcion')

class cliente(models.Model):
    _name = 'alquileres.cliente'
    _description = 'Define los atributos de un ciente'

    # Atributos
    dniCliente = fields.Char(string='DNI', required=True)
    nombreCliente = fields.Char(string='Nombre y Apellidos', required=True)
    fechaNacimiento = fields.Date(string='Fecha Nacimiento', required=True, default = fields.date.today())
    direccionCliente = fields.Char(string='Direccion', required=True)
    telefonoCliente = fields.Char(string='Telefono', required=True)

    #Relacion entre tablas
    suscripcion_id = fields.Many2one('alquileres.suscripcion', string='Clientes')
    alquiler_ids = fields.Many2many('alquileres.alquiler', string='Alquiler' )


class alquiler(models.Model):
    _name = 'alquileres.alquiler'
    _description = 'Define los atributos del alquiler'

    #Atributos
    nombreVideojuego = fields.Char(string='Nombre Videojuego', required=True)
    tipoVideojuego = fields.Selection(string='Tipo de videojuego', selection=[('d','Deportes'),('a','Accion'),('c','Carreras'),('e','Estrategia')], help='Tipo de videojuego que esta alquilando')
    descripcionVideojuego = fields.Text(string='Descripcion del videojuego')
    fechaInicio = fields.Date(string="Fecha inicio alquiler", required=True)
    fechaFin = fields.Date(string="Fecha final alquiler", required=True)
    
    #Relacion entre tablas

    cliente_id = fields.Many2many('alquileres.cliente', string='Clientes')
