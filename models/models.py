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

from odoo import models, fields, api, exceptions
from dateutil.relativedelta import *
from datetime import date

class suscripcion(models.Model):
    _name = 'alquileres.suscripcion'
    _description = 'Define los atributos de la suscripcion'

    # Atributos
    nombreSus = fields.Char(string='Nombre suscripcion', required=True)
    tipoSuscripcion = fields.Selection(string='Tipo de suscripcion', selection=[('a','platinun'),('b','Gold'),('c','Gold+'),('d','Vip')], help='Tipo de suscripcion que tiene el cliente', required=True)
    descripcionSuscripcion = fields.Text(string='Descripcion de la suscripcion')

    def name_get(self):
        listaSus = []
        for sus in self:
            listaSus.append((sus.id, sus.nombreSus))
        return listaSus



    #Relacion entre tablas
    cliente_id = fields.One2many('alquileres.cliente','suscripcion_id', string='Suscripcion')

class cliente(models.Model):
    _name = 'alquileres.cliente'
    _description = 'Define los atributos de un ciente'

    # Atributos
    nombreCliente = fields.Char(string='Nombre', required=True)
    apellidosCliente = fields.Char(string='Apellidos', required=True)
    dniCliente = fields.Char(string='DNI', required=True)
    fechaNacimiento = fields.Date(string='Fecha Nacimiento', required=True, default = fields.date.today())
    direccionCliente = fields.Char(string='Direccion', required=True)
    telefonoCliente = fields.Char(string='Telefono', required=True)
    provincia = fields.Selection(string='Provincia', selection=[('a','Madrid'),('b','Toledo'),('c','Burgos'),('d','Cantabria'),('e','Albacete')], help='Tipo de provincia', required=True)
    edad = fields.Integer('Edad', compute='_getEdad')


    #Relacion entre tablas
    suscripcion_id = fields.Many2one('alquileres.suscripcion', string='Suscripcion')
    alquiler_ids = fields.Many2many('alquileres.alquiler', string='Alquiler' )
    devoluciones_id = fields.Many2many('incidencias.devoluciones', string='Devoluciones')


    @api.depends('fechaNacimiento')
    def _getEdad(self):
        hoy = date.today()
        for cliente in self:
            cliente.edad = relativedelta(hoy, cliente.fechaNacimiento).years

    @api.constrains('fechaNacimiento')
    def _checkEdad(self):
        for cliente in self:
            if (cliente.edad < 18):
                raise exceptions.ValidationError("El cliente debe ser mayor de edad")

    @api.constrains('dniCliente')
    def _checkDNI(self):
        for cliente in self:
            if (len(cliente.dniCliente) > 9):
                raise exceptions.ValidationError("El DNI no puede tener mas de 9 caracteres")
            if (len(cliente.dniCliente) < 9):
                raise exceptions.ValidationError("El DNI no puede tener menos de 9 caracteres")







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


    @api.constrains('fechaFin')
    def _checkFechaFin(self):
        for alquiler in self:
            if relativedelta(alquiler.fechaInicio, alquiler.fechaFin).days > 0:
                raise exceptions.ValidationError("La fecha de fin no puede ser inferior a la del inicio del alquiler")


    @api.constrains('fechaInicio')
    def _checkFechainicio(self):
        hoy = date.today()
        for alquiler in self:
            diasCalculados = relativedelta(hoy, alquiler.fechaInicio).days
            if (diasCalculados > 0):
                raise exceptions.ValidationError("El alquiler no puede ser anterior a hoy")


