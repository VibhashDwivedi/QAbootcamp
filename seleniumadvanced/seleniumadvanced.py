from navigation import Navigation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def handle_browser_alerts(mydriver):
    n.goto_toolsqa_page("alerts")
    clk_btn = n.get_element((By.ID, "alertButton"))
    clk_btn.click()
    time.sleep(3)
    print(mydriver.switch_to.alert.text)
    mydriver.switch_to.alert.accept()
    time.sleep(3)

def delayed_alert(mydriver):
    n.goto_toolsqa_page("alerts")
    clk_btn = n.get_element((By.ID, "timerAlertButton"))
    clk_btn.click()
    WebDriverWait(mydriver, 10).until(EC.alert_is_present())
    print(mydriver.switch_to.alert.text)
    mydriver.switch_to.alert.accept()

def handle_cancelok_alerts(mydriver):
    n.goto_toolsqa_page("alerts")
    clk_btn = n.get_element((By.ID, "confirmButton"))
    clk_btn.click()
    WebDriverWait(mydriver, 10).until(EC.alert_is_present())
    print(mydriver.switch_to.alert.text)
    time.sleep(3)
    mydriver.switch_to.alert.accept()
    conf_res = n.get_element((By.ID, "confirmResult"))
    print(conf_res.text)
    time.sleep(3)
    clk_btn.click()
    WebDriverWait(mydriver, 10).until(EC.alert_is_present())
    print(mydriver.switch_to.alert.text)
    time.sleep(3)
    mydriver.switch_to.alert.dismiss()
    print(conf_res.text)

def handle_text_alerts(mydriver):
    n.goto_toolsqa_page("alerts")
    clk_btn = n.get_element((By.ID, "promtButton"))
    clk_btn.click()
    WebDriverWait(mydriver, 10).until(EC.alert_is_present())
    print(mydriver.switch_to.alert.text)
    mydriver.switch_to.alert.send_keys("Vibhash")
    time.sleep(3)
    mydriver.switch_to.alert.accept()
    enter_txt = n.get_element((By.ID, "promptResult"))
    print(enter_txt.text)    




if __name__ == '__main__':
    try:
        n = Navigation()
        driver = n.get_driver()
        # handle_browser_alerts(driver)
        # delayed_alert(driver)
        # handle_cancelok_alerts(driver)
        handle_text_alerts(driver)

    finally:
        driver.close()
        driver.quit()

