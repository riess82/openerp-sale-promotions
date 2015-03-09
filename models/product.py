from osv import osv, fields

class product_product(osv.osv):
    _inherit = 'product.product'
    
    _columns = {
        'promotion':fields.boolean('Promotion Product', help="This product is used in conjunction with promotion codes. Not to be used in regular Sales."),
    }