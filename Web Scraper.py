# %% [markdown]
# 

# %%
import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np

# %%
url="https://www.iqair.com/in-en/world-most-polluted-cities?sort=-rank&page=1&perPage=50&cities="

page=requests.get(url)

soup=BeautifulSoup(page.text,'html.parser')



# %%
h=soup.find_all('th')
h=[ title.text.strip() for title in h]

h


# %%
df=pd.DataFrame(columns=h)



# %%


num_pages=147
for page_number in range(1,num_pages+1):
    url=f"https://www.iqair.com/in-en/world-most-polluted-cities?sort=-rank&page={page_number}&perPage=50&cities="

  
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    tr=soup.find_all('tr')
    for row in tr[1:]:
        td=row.find_all('td')
        td=[title.text.strip() for title in td]

        length=len(df)
        df.loc[length]=td


# %%
df.to_csv('WebScrapingProject.xlsx')




# %%



