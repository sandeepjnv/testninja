from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time

from .driver import createDriverInstance

def executeWorkflow(workflow):
    actionLog = []
    try:
        # driver instance
        driver = createDriverInstance()

        if "url" in workflow:
            driver.get(workflow["url"])
        
        # components = workflow["actions"]
        # loop all next actions

        actions = workflow["actions"]
        for action in actions:
            time.sleep(1)
            # @todo -builtin
            # action = actions[index]
            component = action["target"]
            value = component["value"]

            # element
            if(action["actionType"] not in ["wait"]):
                if component["identifier"] == "id":
                    elementStr = (By.ID,value)
                    element = driver.find_element(By.ID,value)
                elif component["identifier"] == "xpath":
                    elementStr = (By.XPATH,value)
                    element = driver.find_element(By.XPATH,value)
                elif component["identifier"] == "select":
                    elementStr = (Select(driver.find_element(By.ID,value)))
                    element = Select(driver.find_element(By.ID,value))
            

            # interaction 
            try:
                if(action["actionType"] == "write"):
                    element.send_keys("")
                    element.send_keys(action["value"])
                    element.send_keys(Keys.TAB)
                elif(action["actionType"] == "forcewrite"):
                    driver.execute_script("arguments[0].value = arguments[1];", element,action["value"])
                    driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", element)
                    element.send_keys("")
                    element.send_keys(Keys.TAB)
                elif(action["actionType"] == "click"):
                    element.click()
                elif(action["actionType"] == "drop"):
                    element.select_by_value(action["value"])
                elif(action["actionType"] == "element-wait"):
                    wait = WebDriverWait(driver, 20)
                    wait.until(EC.visibility_of_element_located(elementStr))
                elif(action["actionType"]=="wait"):
                    time.sleep(int(action["value"]))
                elif(action["actionType"] == "scrolltoview"):
                    element.location_once_scrolled_into_view


                elif(action["actionType"] == "validate"):
                    data = element.text
                    if action['value'] in data:
                        print("Test Case : Passed")

                # action types
                # if(action["type"] == "validation"):
                #     # @todo - Screen shot log
                #     if action['message'] in data:
                #         print("Test Case : Passed")
                #     else:
                #         print("Test Case : Failed")
                actionLog.append({"status":1,"message":""})
            except Exception as e:
                #@todo driver.screenshot
                print(e)
                actionLog.append({"status":0,"message":str(e)})
        

        driver.close()
        driver.quit()

    except Exception as e:
        driver.close()
        driver.quit()
        print(e)

    return actionLog
