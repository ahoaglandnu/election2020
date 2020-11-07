import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def poll_list(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    tags = soup.find_all('a')
    links = []
    for tag in tags:
        link = tag.get('href')
        links.append(link)
    clean = [x for x in links if x != None]
    polls = [x for x in clean if x.startswith('/epolls')]
    dedup = list(set(polls))
    dedup = [ x for x in dedup if "2020_" not in x ]
    return [ x for x in dedup if "create_your" not in x ]

def states(new_url):
    page = requests.get(new_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    tables = soup.findChildren('table')
    if tables:
        rows = tables[0].findChildren(['th', 'tr'])
        l = []
        for tr in rows:
            td = tr.find_all('td')
            row = [tr.text for tr in td]
            l.append(row)
        clean = [x for x in l if x != []]
        df = pd.DataFrame(clean, columns=[tr.text for tr in rows[0].find_all('th')])
        df['State'] = new_url.split("/", 7)[6]
        df.Sample = df.Sample.replace('\s+', ' ', regex=True)
        df[['SampleSize','Segment']] = df.Sample.str.split(" ",expand=True,)
        del df['Sample']
        df = df.reindex(sorted(df.columns), axis=1)
        return df
    else:
        pass
    
def poll_update(polls):
    df = pd.DataFrame(columns=['Biden (D)','Date','MoE','Poll','SampleSize','Segment','Spread','State','Trump (R)'])
    for i in range(len(polls)):
        new_url = "https://www.realclearpolitics.com" + polls[i]
        print('starting: ',new_url)
        test_df = states(new_url)
        df = df.append(test_df, ignore_index=True,sort=False)
        df = df.reset_index(drop=True)
    cols = ['State','Poll','Date','SampleSize','Segment','MoE','Biden (D)','Trump (R)','Spread']
    return df[cols] 

url = "https://www.realclearpolitics.com/epolls/2020/president/2020_elections_electoral_college_map.html"
polls = poll_list(url)
df = poll_update(polls)
df.to_csv('election_polls_' + datetime.now().strftime("%Y%m%d") + '.csv',index=False)