import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5, 'tax': 7.5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10, 'tax': 7.5}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalculateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_CanCalculateTotalTax(invoice, products):
    invoice.totalTax(products)
    assert invoice.totalTax(products) == 10.41

def test_CanCalculatePurePriceWithTax(invoice, products):
    invoice.totalPurePriceWithTax(products)
    assert invoice.totalPurePriceWithTax(products) == 79.79






