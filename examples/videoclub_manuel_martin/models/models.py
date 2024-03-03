from odoo import models, fields, api

class videoclub_modelo(models.Model):
    _name = 'videoclub.genero'
    _description = 'videoclub.genero'
    _rec_name = 'nombre' # Utiliza el campo 'nombre' como representación de nombre
    nombre = fields.Selection([
        ('0', 'Acción'),
        ('1', 'Comedia'),
        ('2', 'Musical'),
        ('3', 'Drama'),
        ('4', 'Aventura'),
        ('5', 'Wenstern'),
        ('6', 'Terror'),
        ('7', 'Suspense')
    ], string="Nombre", default='0', help="Género de la película")
    peliculas = fields.One2many("videoclub.pelicula", "genero", string="Películas")

class videoclub_pelicula(models.Model):
    _name = 'videoclub.pelicula'
    _description = 'videoclub.pelicula'
    _rec_name = 'titulo' # Utiliza el campo 'titulo' como representación de nombre
    titulo = fields.Char(string="Titulo", required=True, help="Título del película")
    director = fields.Text(string="Director", required=True, help="Director de la película")
    industria = fields.Selection([
        ('0', 'Hollywood'),
        ('1', 'Europea'),
        ('2', 'Descatalogado'),
        ('3', 'Española'),
        ('4', 'Bollywood'),
        ('5', 'Disney'),
        ('6', 'Otras'),
    ], string="Industria", default='0', help="Industria de la película")
    duracion = fields.Integer(string="Duración", required=True, help="Duración en minutos")
    sinopsis = fields.Text(string="Sinopsis", required=True, help="Sinopsis de la película")
    # Relación
    genero = fields.Many2one("videoclub.genero", string="Género", ondelete="cascade")


