
#-*- coding: utf-8 -*-
from odoo import models, fields, api
class TodoMusic(models.Model):
   _name = 'artista'
   _inherit = ['artista','mail.thread']
   premios = fields.Integer('Premios')
   user_id = fields.Many2one('res.users', 'Manager')
   date_deadline = fields.Date('Disponible Hasta:')
   name = fields.Char(help="Lista de Artistas.")

   def do_marcar(self):
      if self.user_id != self.env.user:
     	  raise Exception('Solo el responsable puede marcarla Me gusta!')
      else:
         return super(TodoMusic, self).do_marcar()

   def do_limpiar(self):
      domain = [('is_done', '=', True), '|', ('user_id', '=', self.env.uid), ('user_id', '=', False)]
      done_recs = self.search(domain)
      done_recs.write({'active': False})
      return True

