# -*- coding: utf-8 -*-

from odoo import models, fields, api


class libreria_autor(models.Model):
    _name = 'mms.autor'
    _description = 'mms.autor'
    nombre = fields.Char(string="Nombre", required=True, help="Nombre del autor")
    apellidos = fields.Text(string="Apellidos", required=True, help="Apellidos del autor")
    nacionalidad = fields.Text(string="Nacionalidad", help="Nacionalidad del autor")
    nacimiento = fields.Date(string="Nacimiento", help="Fecha de nacimiento del autor")
    # Relación
    libros = fields.One2many("mms.libro", "autor", string="Libros")

class libreria_genero(models.Model):
    _name = 'mms.genero'
    _description = 'mms.genero'
    nombre = fields.Selection([
        ('0', 'Aventuras'),
        ('1', 'Ficción'),
        ('2', 'Drama'),
        ('3', 'Fantasía'),
        ('4', 'Infantil'),
        ('5', 'Juvenil'),
        ('6', 'Novela'),
        ('7', 'Romántica'),
        ('8', 'Terror')
    ], string="Nombre", required=True, help="Nombre del genero")
    # Relación
    libros = fields.One2many("mms.libro", "genero", string="Libros")


class libreria_libro(models.Model):
    _name = 'mms.libro'
    _description = 'mms.libro'
    titulo = fields.Char(string="Título", required=True, help="Título del libro")
    isbn = fields.Char(string="ISBN", required=True, help="ISBN del libro")
    editorial = fields.Char(string="Editorial", required=True, help="Editorial del libro")
    paginas = fields.Integer(string="Páginas", required=True, help="Número de páginas del libro")
    # Relación
    autor = fields.Many2one("mms.autor", string="Autor")
    genero = fields.Many2one("mms.genero", string="Genero")