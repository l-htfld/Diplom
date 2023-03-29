from bs4 import BeautifulSoup as bs
import os
import pandas as pd
import re

ajfa = []

folder = r"C:\Users\HP\Documents\python\diplom\texts"

for name in os.listdir(folder):
    path = os.path.join(folder, name)

    with open(path, encoding='utf8') as file:
        soup = bs(file, 'html.parser')
        for txt in soup.find_all('text'):
            mastof = {}
            if txt['birthdate'] == '':
                continue
            mastof['year']=txt['year']
            mastof['text']=re.sub(r'http\S+', '', txt.get_text())
            mastof['birthdate']=txt['birthdate']
            ajfa.append(mastof)
            
    data = pd.DataFrame(ajfa)

    data.to_csv(r'C:\Users\HP\Documents\python\diplom\parsed_texts\pars.csv', index=False)
            