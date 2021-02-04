# -*- coding: utf-8 -*-

from odoo import models, fields, api
class artista(models.Model):
  _name = 'artista'
  _description = 'Lista de Artistas'
  name = fields.Char('Artista', required=True)
  name2 = fields.Char('Canción TOP', required=True)
  is_done = fields.Boolean('Me Gusta', default=True)
  active = fields.Boolean('Sin escuchar',default=True)

  def do_marcar(self):
        self.is_done = not self.is_done
        return True
        
  def do_limpiar(self):
        done_recs = self.search([('is_done', '=', False)])
        done_recs.write({'active': False})
        return True
