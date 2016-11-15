# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp.addons.connector.backend import Backend

jira = Backend('qoqa')
""" Generic QoQa Backend. """

jira_7_2_2 = Backend(parent=jira, version='7.2.2')
""" Backend for version 7.2.2 of Jira """
