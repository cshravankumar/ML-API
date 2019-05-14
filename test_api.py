####THIS IS A TEST FUNCTION THAT TESTS IF THE API CALL WORKS
####POSITIVE TEST RESP:902

import requests
import json

input_json = {
    "Q1": "q1_other",
    "Q2": "q2_25_29",
    "Q3": "q3_united_",
    "Q4": "q4_other",
    "Q6": "q6_data_sc",
    "Q7": "q7_other2",
    "Q8": "q8_2_3",
    "Q10": "q10_we_rec",
    "q11_analyz": "on",
    "q11_run_a_": "on",
    "q11_build_": "on",
    "q15_amazon": "on",
    "other": "on",
    "q16_python": "on",
    "q16_sql": "on",
    "Q23": "q23_25_to_",
    "q31_catego": "on",
    "q31_geospa": "on",
    "q31_numeri": "on",
    "q31_tabula": "on",
    "q31_text_d": "on",
    "q31_time_s": "on",
    "q42_revenu": "on"
}

header = {'Content-Type': 'application/x-www-form-urlencoded'}
url = 'https://b8porbwafg.execute-api.us-east-1.amazonaws.com/Prod'

#url = 'https://httpbin.org/post'
#url = 'https://6eet1ls14c.execute-api.us-east-1.amazonaws.com/Prod'

getrq = requests.post(url, json=input_json, headers=header)
#getrq = requests.get(url)

print((getrq.json()['body']))

#r = json.dumps(getrq)
#loaded_r = json.loads(r)

#print(loaded_r['body'])