import pygsheets
from login import check
from datetime import datetime

def listfromgoogle():
    gc = pygsheets.authorize(service_account_file='./credentials.json')
    survey_url = 'https://docs.google.com/spreadsheets/d/11QWG9ynsKwTNXM6R3J7yih0dDZdPg7qLgVSWz5DgTPk/'
    sh = gc.open_by_url(survey_url)

    ws = sh.worksheet_by_title('train')
    cell_list = ws.range('A1:I72')
    ws.update_value((1, 7), str(datetime.now()))

    for i in range(72):
        if cell_list[0][3].value == '1':
            try:
                check(cell_list[i][0].value, cell_list[i][1].value)
            except:
                ws.update_value((i+1, 4), '0')