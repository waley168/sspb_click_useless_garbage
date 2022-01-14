import xlwings as xw
from login import check

def list():
    app=xw.App(visible=True,add_book=False)
    wb=app.books.open('list.xlsx')  #開檔案
    wcell=wb.sheets['工作表1']      #開工作表

    rng=wcell.range('A1:B35').value    #預先載入

    for i in range(35):
        if wcell.range(i+1,4).value == 1:
            try:
                check((rng[i][0]),(rng[i][1]))
            except:
                wcell.range(i+1,4).value='0'
    wb.save()
    wb.close()
    app.quit()