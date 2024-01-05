import re
import csv
from enum import Enum
from decimal import Decimal, ROUND_DOWN
from datetime import date
from dataclasses import dataclass

from pydantic import BaseModel, ConfigDict

from gspread import Worksheet
from gspread.utils import ValueInputOption

from dateutils import next_month


_DATE_FMT = '%Y-%m-%d'


def _quantize(val: Decimal) -> Decimal:
    return val.quantize(Decimal('0.00'), rounding=ROUND_DOWN)


class PaymentMethod(str, Enum):
    PIX = 'PIX'
    CASH = 'CASH'
    BANK_SLIP = 'BANK_SLIP'
    CREDIT_CARD = 'CREDIT_CARD'
    DEBIT_CARD = 'DEBIT_CARD'

    def __str__(self) -> str:
        return str.__str__(self)


class Category(str, Enum):
    UTILITIES = 'UTILITIES'
    TRANSPORTATION = 'TRANSPORTATION'
    GROCERIES = 'GROCERIES'
    FOOD = 'FOOD'
    DRINK = 'DRINK'
    SHOPPING = 'SHOPPING'
    HEALTH = 'HEALTH'
    EDUCATION = 'EDUCATION'
    TRAVEL = 'TRAVEL'
    HOUSING = 'HOUSING'
    ENTERTAINMENT = 'ENTERTAINMENT'
    OTHERS = 'OTHERS'

    def __str__(self) -> str:
        return str.__str__(self)


class Bill(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    text: str
    unitprice: Decimal
    date: date
    payment_method: PaymentMethod
    category: Category = Category.OTHERS
    split_it: bool = True

    def asrow(self) -> list:
        unitprice = float(_quantize(self.unitprice))
        valformula = '=%s/%s' % (unitprice, 2) if self.split_it else unitprice

        return [
            self.date.strftime(_DATE_FMT),
            valformula,
            self.text,
            str(self.category),
            str(self.payment_method),
            self.split_it,
        ]


@dataclass
class Future:
    date: date
    text: str
    unitprice: Decimal


def _create_future_objs_from_desc(
    s: str, start_dt: date, unitprice: Decimal
) -> list[Future]:
    """Analyzes the description and creates a list of Future objects"""

    match = re.match(r'^([\s\S]+)(\d+)/(\d+)$', s)
    if not match:
        return [Future(date=start_dt, text=s, unitprice=_quantize(unitprice))]

    text, start, stop = match.groups()
    text = text.rstrip()

    next_dt = start_dt
    rows = []

    for idx in range(int(start), int(stop) + 1):
        rows.append(
            Future(
                date=next_dt,
                text=f'{text} {idx}/{stop}',
                unitprice=_quantize(unitprice / int(stop)),
            )
        )
        next_dt = next_month(next_dt)

    return rows


def append_row(wks: Worksheet, bill: Bill) -> dict:
    """Adds multiple rows to the worksheet"""
    objs = _create_future_objs_from_desc(bill.text, bill.date, bill.unitprice)
    args = {
        'category': bill.category,
        'payment_method': bill.payment_method,
        'split_it': bill.split_it,
    }
    values = [
        Bill(unitprice=x.unitprice, text=x.text, date=x.date, **args).asrow()
        for x in objs
    ]

    return wks.append_rows(
        values=values,
        value_input_option=ValueInputOption.user_entered,
        table_range='A1',
    )


def get_all_records(wks: Worksheet) -> list[Bill]:
    records = []

    for record in wks.get_all_records():
        record: dict
        records.append(Bill(**record))

    return records


def copy_spreadsheet(filename: str, records: list[Bill]):
    """Copy contents of the spreadsheet to local csv file"""
    fieldnames = [
        'date',
        'unitprice',
        'desc',
        'category',
        'payment_method',
        'split_it',
    ]

    with open(filename, mode='w', encoding='utf-8') as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()

        for record in records:
            writer.writerow(record.model_dump())
