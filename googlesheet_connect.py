import pygsheets
import pandas as pd
from login import check

def listfromgoogle():
    gc = pygsheets.authorize(service_account_file='./credentials.json')
    survey_url = 'https://docs.google.com/spreadsheets/d/11QWG9ynsKwTNXM6R3J7yih0dDZdPg7qLgVSWz5DgTPk/'
    sh = gc.open_by_url(survey_url)

    ws = sh.worksheet_by_title('train')

    for i in range(72):
        if ws.get_value(i+1,4) == 1:
            try:
                check(ws.get_value(i+1,0),ws.get_value(i+1,1))
            except:
                ws.update_value((i+1,4), '0')