# -*- encoding: utf-8 -*-
##############################################################################
#
#    Avanzosc - Avanced Open Source Consulting
#    Copyright (C) 2011 - 2012 Avanzosc <http://www.avanzosc.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

import time

from crm import crm
from osv import fields, osv
from tools.translate import _

class training_course_ext(osv.osv):
    _inherit = 'training.course'
    
    _columns = {
	    'course_code': fields.char('Course Code', size=32, required=True),
        'product_id':fields.many2one('product.product', 'Product'),
        'tipo_docencia':fields.selection([('F', 'F'),('L', 'L'),('N', 'N'),('X', 'X')], 'Type teaching', required=True),
		'credits': fields.integer('Credits', required=True, help="Course credits"),	
		'offer_ids' : fields.one2many('training.course.offer.rel', 'course_id', 'Offers', help='A course could be included on some offers'),
		'seance_ids' : fields.one2many('training.seance', 'course_id', 'Offers', help='A course could generate some seances'),

    }

training_course_ext()

class training_course_offer_rel(osv.osv):
    _inherit = 'training.course.offer.rel'

    _columns = {
        'tipology': fields.selection([('mandatory', 'mandatory'),('trunk', 'trunk'),('optional', 'optional'),('free', 'free'),('complementary', 'complementary'),('replace', 'replace')], 'Tipology', required=True),
     }

training_course_offer_rel()
class training_session_ext(osv.osv):
    _inherit = 'training.session'

    _columns = {
        'date_from' : fields.datetime('Date From', required=True, help="The data when course begins"),
        'date_end' : fields.datetime('Date End', required=True, help="The data when course ends"),    
     }

training_session_ext()

class training_seance_ext(osv.osv):
    _inherit = 'training.seance'

    _columns = {
        'date_from' : fields.datetime('Date From', required=True, help="The data when course begins"),
        'date_to' : fields.datetime('Date To', required=True, help="The data when course ends"),    
     }

training_seance_ext()



