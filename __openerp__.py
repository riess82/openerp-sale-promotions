# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (C) 2010, Open Labs Business Solution
#    Copyright (C) 2011, Zikzakmedia                                        #
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'Promotions for OpenERP',
    'version' : '2.7',
    'author' : 'Openlabs Technologies & Consulting (P) Limited',
    'website': 'http://openlabs.co.in',
    'category' : 'Generic Modules/Sales & Purchases',
    'depends' : [
                 "base",
                 "sale",
                 "product",
                 ],
    'init_xml' : [],
    'demo_xml' : [],
    'description': """
    Promotions on Sale Order for OpenERP
    = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    Features:
    1. Promotions based on conditions and coupons
    2. Web services API compliance
    
    Credits:
        This design is based/inspired by the Magento commerce
        Special Thanks to Yannick Buron for analysis
        Migration Module OpenERP 6: Zikzakmedia
	ENHANCEMENTS / CHANGES:
		Add Checkbox to Product view "Promotion Product". These are not selectable in Sales Order Form and should only be added through the Promotion Module.
		Disabled Discount on Total because it now works without inserting a product, resulting it being impossible to invoice (product has info on tax and accounting).
		Add Action "Buy X get Z Promotion Product": If Product is found in Cart then 1 piece of Promotion Product is added to cart.
		Changed Permissions to Allow everything for all Sales people. not good!
    """,
    'update_xml': [
        'security/ir.model.access.csv',
        'views/rule.xml',
        'views/sale.xml',
        'views/product.xml',
                ],
    'installable': True,
    'active': False,
}
