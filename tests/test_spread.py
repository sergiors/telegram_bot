from decimal import Decimal
from spread import _create_future_objs_from_desc, Future
from datetime import date


def test_valid():
    s = 'iPhone 1/3'
    unitprice = Decimal(3899)
    start_dt = date(2023, 1, 1)
    frac_unitprice = Decimal('1299.66')

    expected = [
        Future(
            date=date(2023, 1, 1),
            desc='iPhone 1/3',
            unitprice=frac_unitprice,
        ),
        Future(
            date=date(2023, 2, 1),
            desc='iPhone 2/3',
            unitprice=frac_unitprice,
        ),
        Future(
            date=date(2023, 3, 1),
            desc='iPhone 3/3',
            unitprice=frac_unitprice,
        ),
    ]
    actual = _create_future_objs_from_desc(s, start_dt, unitprice)

    assert actual == expected


def test_does_not_future_objs():
    s = 'iPhone'
    unitprice = Decimal(3899)
    start_dt = date(2023, 1, 1)

    expected = [
        Future(date=date(2023, 1, 1), desc='iPhone', unitprice=unitprice)
    ]
    actual = _create_future_objs_from_desc(s, start_dt, unitprice)

    assert actual == expected
