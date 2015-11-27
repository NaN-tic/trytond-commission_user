# This file is part commission_user module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .commission import *
from .user import *
from .sale import *
from .opportunity import *
from .invoice import *

def register():
    Pool.register(
        AgentUser,
        User,
        Sale,
        Opportunity,
        Invoice,
        module='commission_user', type_='model')
