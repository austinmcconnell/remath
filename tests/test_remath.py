#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_remath
----------------------------------

Tests for `remath` module.
"""

import unittest

from remath import remath


class TestRemath(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_downpayment(self):
        assert remath.downpayment(150000, .05) == 7500

    def test_financedamount(self):
        assert remath.financedamount(150000, 7500) == 142500

    def test_loantovalue(self):
        assert remath.loantovalue(150000, 142500) == .95

    def test_debtservice(self):
        assert round(remath.debtservice(142500, .04, 30)) == 8164

    def test_pmi(self):
        assert round(remath.pmi(142500, .0096)) == 1368

    def test_taxes(self):
        assert remath.taxes(150000, .03) == 4500

    def test_netrentalincome(self):
        assert remath.netrentalincome(18000, .08) == 16560

    def test_managementfee(self):
        assert remath.managementfee(.08, 16560) == 1324.8

    def test_insurance(self):
        assert remath.insurance(1200) == 1200

    def test_hoafee(self):
        assert round(remath.hoafee(250)) == 250

    def test_operatingexpenses(self):
        assert remath.operatingexpenses(4500, 1200, 1368, 1325, 250) == 8643

    def test_grossrentalincome(self):
        assert remath.grossrentalincome(19872, 0) == 19872

    def test_netoperatingincome(self):
        assert remath.netoperatingincome(19872, 11068) == 8804

    def test_cashflow(self):
        assert remath.cashflow(8804, 8164) == 640

    def test_cashoncashreturn(self):
        assert round(remath.cashoncashreturn(1000, 7500), 2) == .13

    def test_capitalizationrate(self):
        assert remath.capitalizationrate(7920, 150000) == .0528
