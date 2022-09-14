from odoo import api, fields, models


class SupplierBaru(models.TransientModel):
    _name = 'zetomart.supplierbaru'

    supplier_id = fields.Many2one(
        comodel_name='zetomart.supplier', 
        string='Nama Supplier',
        required=True)

    alamat = fields.Char(string='Alamat',required=False)

    no_telp = fields.Char(string='No Telepon',required=False)

    barang_id = fields.Many2one(
        comodel_name='zetomart.barang', 
        string='Input Barang',
        required=True)

    def button_supplier_baru(self):
        for rec in self:
            self.env["zetomart.supplier"].search([('id','=', rec.supplier_id.id)]).write({'alamat' : rec.alamat, 'no_telp' : rec.no_telp, 'barang_id' : rec.barang_id})
