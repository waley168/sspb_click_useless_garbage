from googlesheet_connect import listfromgoogle
import schedule
import time

schedule.every().day.at("18:30").do(listfromgoogle)

while True:
    schedule.run_pending()
    time.sleep(1)