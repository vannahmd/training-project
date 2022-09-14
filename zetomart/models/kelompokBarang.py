from odoo import api, fields, models

class kelompokBarang(models.Model):
    _name = 'zetomart.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
    ('makananbasah', 'Makanan Basah'), ('makanankering', 'Makanan Kering'), ('minuman', 'Minuman')], string='Nama Kelompok Barang')
    kode_kelompok = fields.Char(string='Kode kelompok Barang')

    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if (self.name == 'makananbasah'):
            self.kode_kelompok = 'mak01'
        elif (self.name == 'makanankering'):
            self.kode_kelompok = 'mak02'
        elif (self.name == 'minuman'):
            self.kode_kelompok = 'min'

    kode_rak = fields.Char(string='Kode Rak')

    barang_ids = fields.One2many(comodel_name='zetomart.barang',
                                inverse_name='kelompokbarang_id', 
                                string='Daftar Barang')

    jml_item = fields.Char(compute='_compute_jml_item', string='Jml Item')

    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for record in self:
            a = self.env['zetomart.barang'].search([('kelompokbarang_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar isi')