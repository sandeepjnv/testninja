login_wf = {
    "url":"http://192.168.2.57:9196",
    "actions":{
        "1":{
            "type":"input",
            "element": "login_username",
            "interaction" : "write",
            "value"       : "nucoreadmin"
        },
        "2":{
            "type":"input",
            "element": "login_password",
            "interaction" : "write",
            "value"       : "traacs123"
        },
        "3":{
            "type":"input",
            "element": "login_button",
            "interaction" : "click"
        }
    },
    "components":{
        "login_username":{
            "identifier":"id",
            "value":"txtLoginName"
        },
        "login_password":{
            "identifier":"id",
            "value":"txtPassword"
        },
        "login_button":{
            "identifier":"id",
            "value":"btnLoginSubmit"
        }
    }
}

new_city = {
    "url":"http://192.168.2.57:9196/traacs/basic_city_city/city/strMenuId/mnu_finance_master",
    "actions":{
        "1":{
            "type":"input",
            "element": "new_city_link",
            "interaction" : "click"
        },
        "2":{
            "type":"input",
            "element": "city_name",
            "interaction" : "write",
            "value"       : "Jomy city"
        },
        "3":{
            "type":"input",
            "element": "city_country",
            "interaction" : "write",
            "value"       : "Zambia"
        },
        "4":{
            "type":"input",
            "element": "city_save",
            "interaction" : "click"
        },
        "6":{
            "type":"validation",
            "element": "city_message",
            "interaction" : "read",
            "message" : "City has been saved"
        },
        "7":{
            "type":"validation",
            "element": "city_err_message",
            "interaction" : "read",
            "message" : "City already exists"
        },
        "8":{
            "type":"validation",
            "element": "city_err_message",
            "interaction" : "read",
            "message" : "City is required "
        }
    },
    "components":{
        "new_city_link":{
            "identifier":"id",
            "value":"lnkCityAdd"
        },
        "city_name":{
            "identifier":"id",
            "value":"txtCity"
        },
        "city_country":{
            "identifier":"id",
            "value":"txtCountry"
        },
        "city_save":{
            "identifier":"id",
            "value":"btnCitySave"
        },
        "city_message":{
            "identifier":"id",
            "value": "message"
        },
        "city_err_message":{
            "identifier":"xpath",
            "value": '//*[@id="errFrmCity"]/label'
        }
    }
}

new_airline = {
    "url":"http://192.168.2.57:9196/traacs/basic_airline_airline/airline/strMenuId/mnu_finance_master",
    "actions":{
        "1":{
            "type":"input",
            "element": "new_airline_link",
            "interaction" : "click"
        },
        "2":{
            "type":"input",
            "element": "airline_code",
            "interaction" : "write",
            "value"       : "B3B"
        },
        "3":{
            "type":"input",
            "element": "airline_name",
            "interaction" : "write",
            "value"       : "Jomy Airways"
        },
        "4":{
            "type":"input",
            "element": "airline_numeric",
            "interaction" : "write",
            "value"       : "327"
        },
        "5":{
            "type":"input",
            "element": "airline_curr_cmb",
            "interaction" : "drop",
            "value"       : "SAR"
        },
        "6":{
            "type":"input",
            "element": "airline_save",
            "interaction" : "click"
        },
        "7":{
            "type":"validation",
            "element": "airline_message",
            "interaction" : "read",
            "message" : "Airline has been saved"
        },
        "8":{
            "type":"validation",
            "element": "airline_err_message",
            "interaction" : "read",
            "message" : "This chr. code has been already assigned to"
        }
    },
    "components":{
        "new_airline_link":{
            "identifier":"xpath",
            "value":'//*[@id="smnu_newairline"]/a'
        },
        "airline_code":{
            "identifier":"id",
            "value":"txtChrCode"
        },
        "airline_name":{
            "identifier":"id",
            "value":"txtAirlineName"
        },
        "airline_numeric":{
            "identifier":"id",
            "value":"txtAirCode"
        },
        "airline_curr_cmb":{
            "identifier":"select",
            "value": "cmbCurrency"
        },
        "airline_save":{
            "identifier":"id",
            "value":"btnAirlineSave"
        },
        "airline_message":{
            "identifier":"id",
            "value": "message"
        },
        "airline_err_message":{
            "identifier":"xpath",
            "value": '//*[@id="errFrmAirline"]/label'
        }
    }
}
