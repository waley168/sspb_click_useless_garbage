from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

LoginUrl= ('https://ssp.eportal.npa.gov.tw/portal/index.do')
BookUrl= ('https://oc.eportal.npa.gov.tw/NM106-508Web/index.jsp')
ReadUrl= ('https://oc.eportal.npa.gov.tw/NM106-508Web/OC02A01.jsp')
CheckUrl= ('https://oa2.eportal.npa.gov.tw/OA2/OA2V/OA2VACHECK.aspx')
LogoutUrl1= ('https://oc.eportal.npa.gov.tw/NM106-508Web/LogoutSuccess.jsp')
LogoutUrl2= ('https://ssp.eportal.npa.gov.tw/portal/logout.do')

def check(UserName,UserPass):
    Browser = webdriver.Chrome()
    Browser.get(LoginUrl)
    Browser.find_element_by_name('Ecom_User_ID').send_keys(UserName)
    Browser.find_element_by_name('Ecom_Password').send_keys(UserPass)
    Browser.find_element_by_name('loginButton2').submit()

    Browser.get(BookUrl)
    Browser.get(ReadUrl)

    time.sleep(1)

    while len(Browser.find_elements_by_xpath("//button[@id='btnDetail']"))>0 :
        Browser.find_element_by_xpath("//button[@id='btnDetail']").click()
        time.sleep(1)
        if len(Browser.find_elements_by_xpath("/html/body/div[5]/div[1]/button"))>0 :
            Browser.find_element_by_xpath("/html/body/div[5]/div[1]/button").click()
        else:
            Browser.find_element_by_xpath("/html/body/div[6]/div[1]/button").click()
        time.sleep(1)

    Browser.get(CheckUrl)
    time.sleep(1)
    Browser.find_element_by_xpath("//button[@id='ctl00_cphPage_btn_SelAll']").click()
    time.sleep(1)
    Browser.find_element_by_xpath("//button[@id='ctl00_cphPage_btn_Confirm21']").click()
    time.sleep(1)
    Browser.quit()


