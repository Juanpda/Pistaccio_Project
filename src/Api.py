import json
import requests
import os
from dotenv import load_dotenv
import pandas as pd
from pandas import json_normalize

def Api_get(url):
    load_dotenv()
    tk = os.getenv("tkaemet")
    parameters = {"Authorization": f"token {tk}"}
    aem = requests.get(url, params=parameters)
    aem_j = aem.json()
    a = json_normalize(aem_j)
    return (a)