# This file is part commission_user module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = ['Opportunity']


class Opportunity:
    __metaclass__ = PoolMeta
    __name__ = 'sale.opportunity'

    def _get_sale_opportunity(self):
        User = Pool().get('res.user')
        user = User(Transaction().user)
        sale = super(Opportunity, self)._get_sale_opportunity()
        sale.agent = user.agent
        return sale
