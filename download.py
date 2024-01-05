import gspread
import redis
from datetime import date
from configs import SPREADSHEET_ID
from spread import get_all_records, copy_spreadsheet
from rq import Queue

gc = gspread.service_account(filename='.config/service_account.json')
today = date.today()


redis_conn = redis.from_url('redis://localhost')
q = Queue(connection=redis_conn)  # no args implies the default queue


sh = gc.open_by_key(SPREADSHEET_ID)
wks = sh.worksheet(str(today.year))
job = q.enqueue(
    copy_spreadsheet,
    filename=f'app/downloads/{today.year}.csv',
    records=get_all_records(wks),
)

print('Job id: %s' % job.id)
