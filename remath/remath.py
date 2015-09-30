# -*- coding: utf-8 -*-
__author__ = 'Austin McConnell'


def downpayment(purchaseprice, percentdown):
    """ Return amount of downpayment in dollars.

    :param purchaseprice: Contract price of property.
    :type purchaseprice: double
    :param percentdown: Percent of purchase price that is not being financed.
    :type percentdown: double
    :return: double

    """
    return purchaseprice * percentdown


def financedamount(purchaseprice, downpayment):
    """ Return dollar amount financed.

    :param purchaseprice: Contract price of property.
    :type purchaseprice: double
    :param downpayment: Out-of-pocket money paid to reduce loan-to-value.
    :type downpayment: double
    :return: double

    """
    return purchaseprice - downpayment


def loantovalue(purchaseprice, financedamount):
    """Return ratio of financed amount to purchase price.

    :param purchaseprice: Contract price of property.
    :type purchaseprice: double
    :param financedamount: Amount of money borrowed.
    :type financedamount: double
    :return: double

    """
    return financedamount / purchaseprice


def debtservice(financedamount, interestrate, years):
    """Return annual debt service cost.

    :param financedamount: Amount of money borrowed.
    :type financedamount: double
    :param interestrate: Percent interest charged to borrow money.
    :type interestrate: double
    :param years: length of financing term in years.
    :type years: double
    :return: double

    """
    i = interestrate / 12
    n = years * 12
    return financedamount * i * pow(1 + i, n) / (pow(1 + i, n) - 1) * 12


def pmi(financedamount, pmirate):
    """Return annual private mortgage insurance cost.

    :param financedamount: Amount of money borrowed.
    :type financedamount: double
    :param pmirate: Rate charged when loan-to-value > 80%.
    :type pmirate: double
    :return: double

    """
    return financedamount * pmirate


def taxes(assessedvalue, propertytaxrate):
    """Return annual taxes for property.

    :param assessedvalue: Property value calculated using a 6 month CMA as of January 1st of given year.
    :type assessedvalue: double
    :param propertytaxrate: Rate charged by city for owning property.
    :type propertytaxrate: double
    :return: double

    """
    return assessedvalue * propertytaxrate


def netrentalincome(annualrent, vacancyrate):
    """Return annual net rental income.

    :param annualrent: Yearly rental income if no vacancy.
    :type annualrent: double
    :param vacancyrate: Percent vacancy expected in a given year.
    :type vacancyrate: double
    :return: double

    """
    return annualrent * (1 - vacancyrate)


def managementfee(managementrate, netrentalincome):
    """Return annual cost of property management.

    :param managementrate: Rate charged by property management company.
    :type managementrate: double
    :param netrentalincome: anual net income from rental.
    :type netrentalincome: double
    :return: double

    """
    return managementrate * netrentalincome


def insurance(homeownerinsurance):
    """Return annual cost of homeowners insurance.

    :param homeownerinsurance: annual cost of homeowners insurance.
    :type homeownerinsurance: double
    :return: double

    """
    return homeownerinsurance


def hoafee(yearlyhoafee):
    """ Return annual cost of homeowners association.

    :param yearlyhoafee: Annual homeowners association fee.
    :type yearlyhoafee: double
    :return: double

    """
    return yearlyhoafee


def operatingexpenses(taxes, insurance, pmi, managementfee, hoafee):
    """Annual expenses occured through normal cost of business.

    :param taxes: Annual taxes.
    :type taxes: double
    :param insurance: Annual insurance.
    :type insurance: double
    :param pmi: Annual pmi payment.
    :type pmi: double
    :param managementfee: Annual management fee.
    :type managementfee: double
    :param hoafee: Annual homeowners association fee.
    :type hoafee: double
    :return: double

    """
    return taxes + insurance + pmi + managementfee + hoafee


def grossrentalincome(netrentalincome, otherincome):
    """ Annual income from property.

    :param netrentalincome: Annual income from rent collection.
    :type netrentalincome: double
    :param otherincome: Annual income from other sources (e.g. coin-operated laundry).
    :type otherincome: double
    :return: double

    """
    return netrentalincome + otherincome


def netoperatingincome(grossrentalincome, operatingexpenses):
    """ Annual income from property after subtracting all expenses related to operating the property.

    :param grossrentalincome: Annual income from property.
    :type grossrentalincome: double
    :param operatingexpenses: Annual expenses associated with operating property.
    :type operatingexpenses: double
    :return: double

    """
    return grossrentalincome - operatingexpenses


def cashflow(netoperatingincome, debtservice):
    """Return annual profit from rental property.

    :param netoperatingincome: Annual income from property after subtracting all expenses related to operating the property.
    :type netoperatingincome: double
    :param debtservice: Cost of financing.
    :type debtservice: double
    :return: double

    """
    return netoperatingincome - debtservice


def cashoncashreturn(cashflow, downpayment):
    """Annual return on the property in relation to the downpayment.

    :param cashflow: annual profit from rental property.
    :type cashflow: double
    :param downpayment: Out-of-pocket money paid to reduce loan-to-value.
    :type downpayment: double
    :return: double

    """
    return cashflow / downpayment


def capitalizationrate(netoperatingincome, purchaseprice):
    """Annual return on the property if an investor paid all cash.

    :param netoperatingincome: Annual income from property after subtracting all expenses related to operating the property.
    :type netoperatingincome: double
    :param purchaseprice: Contract price of property.
    :type purchaseprice: double
    :return: double

    """
    return netoperatingincome / purchaseprice
