from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time
from datetime import datetime

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
            singleActionLog = {}
            start_time = time.time()
            time.sleep(1)
            # @todo -builtin
            # action = actions[index]
            component = action["target"]
            value = component["value"]


            try:
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
                singleActionLog["status"] = 1
            except Exception as e:
                #@todo driver.screenshot
                print(e)
                singleActionLog["status"] = 0
                singleActionLog["message"] = str(e)
        

            end_time = time.time()  # Record the end time

            # Calculate the elapsed time for this iteration
            elapsed_time = end_time - start_time  
            singleActionLog["duration"] =   f"{elapsed_time:.2f}"
            singleActionLog["startTime"] =   datetime.fromtimestamp(start_time).strftime('%H:%M:%S')

            actionLog.append(singleActionLog)  


        driver.close()
        driver.quit()
        status = 1

    except Exception as e:
        driver.close()
        driver.quit()
        print(e)
        status = 0

    response = {"status":status,"log":actionLog}
    return response
