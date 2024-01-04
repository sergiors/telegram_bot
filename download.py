import gspread
from datetime import date
from configs import GOOGLE_SERVICE_ACCOUNT_FILENAME, SPREADSHEET_ID
from spread import get_all_records, copy_spreadsheet


gc = gspread.service_account(filename=GOOGLE_SERVICE_ACCOUNT_FILENAME)
today = date.today()


if __name__ == '__main__':
    sh = gc.open_by_key(SPREADSHEET_ID)
    wks = sh.worksheet(str(today.year))

    copy_spreadsheet(
        filename=f'downloads/{today.year}.csv',
        records=get_all_records(wks),
    )
