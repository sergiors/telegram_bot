import locale


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def currency(val: float) -> str:
    return 'R$ %s' % locale.currency(val, symbol=False)
