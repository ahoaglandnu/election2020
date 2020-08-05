import numpy as np
import pandas as pd
import random
from datetime import datetime
random.seed(2020)

# sim functions
def poll_df(data):
    cols = ['cand1','cand2','moe','segment']
    df = pd.DataFrame(data=data.T,columns=cols)
    df[['cand1', 'cand2','moe']] = df[['cand1', 'cand2','moe']].apply(pd.to_numeric)
    return df
    
def wt_avg(df,cand1,cand2,moe,segment):
    df['seg_wt'] = np.where(df.iloc[:,segment] == 'LV',3,1)
    cand1wt = (df.iloc[:,cand1] * df.iloc[:,moe].rank(ascending=False) * df['seg_wt']).sum()/(df.iloc[:,moe].rank(ascending=False) * df['seg_wt']).sum()
    cand2wt = (df.iloc[:,cand2] * df.iloc[:,moe].rank(ascending=False) * df['seg_wt']).sum()/(df.iloc[:,moe].rank(ascending=False) * df['seg_wt']).sum()
    return cand1wt, cand2wt 
    
def average(c):
    return sum(c) / len(c)

def moe(x, y, n):
    min_x = x - n
    max_x = x + n
    std_x = (max_x - min_x) / 4
    min_y = y - n
    max_y = y + n
    std_y = (max_y - min_y) / 4
    return round(random.gauss(x, std_x),1), round(random.gauss(y, std_y),1)

def undecided(x,y,n):
    cand1, cand2 = moe(x, y, n)
    u = round((100 - cand1 - cand2),1)
    return round(cand1,1),round(cand2,1),round(u,1)

def sim(x,y,n,num_sims):
    c1 = []
    c2 = []
    u = []
    c1_wins = 0
    c2_wins = 0
    for i in range(num_sims):
        x1,y1,u1 = undecided(x,y,n)
        c1.append(x1)
        c2.append(y1)
        u.append(u1)
        if x1 > 50:
            c1_wins += 1
        if y1 > 50:
            c2_wins += 1
    return c1_wins/num_sims, round(average(c1),1),c2_wins/num_sims,round(average(c2),1), round(average(u),1) 

def poll_to_prob(data,n=3,num_sims=20000):
    df = poll_df(data)
    x, y = wt_avg(df,cand1=df.columns.get_loc('cand1'),cand2=df.columns.get_loc('cand2'),
       moe=df.columns.get_loc('moe'),segment=df.columns.get_loc('segment'))
    return sim(x,y,n,num_sims)

filename = 'election_polls_' + datetime.now().strftime("%Y%m%d") + '.csv'
df = pd.read_csv(filename)

results = pd.DataFrame(columns=['state','d_prob_wo_unk','d_avg','r_prob_wo_unk','r_avg','unk'])
for i in range(len(df['State'].unique())):
    data = df[(df['State'] == list(df['State'].unique())[i]) & (df["MoE"] != "--") ][['Biden (D)','Trump (R)','MoE','Segment']].dropna().to_numpy().T
    raw = list(poll_to_prob(data))
    raw.insert(0,list(df['State'].unique())[i])
    results.loc[i] = raw
    print(i+1,'of',len(df['State'].unique()),'complete')
    print()
    
ec = {'mt':3,'sc':9,'tx':38,'me':4,'nc':15, 'co':9, 'nv':6, 'tn':11, 'az':11, 'ny':29, 'wi':10,
       'ga':16, 'fl':29, 'ar':6, 'oh':18, 'va':13, 'ut':6, 'mn':10, 'nm':5, 'nj':14, 'ks':6, 'ky':8,
       'ms':6, 'wa':12, 'mo':10, 'in':11, 'al':9, 'ma':11, 'nh':4, 'de':3, 'ia':6, 'ca':55, 'mi':16,
       'pa':20, 'ak':3, 'ct':7}

states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}
states =  {k.lower(): v.lower() for k, v in states.items()}
states = {v: k for k, v in states.items()}

print()
print("states without polls...)
for k,v in states.items():
    if k not in results['state'].values:
        print(v)
print()

results['full_state'] = results["state"].map(lambda x:states[x])
results['ec'] = results["state"].map(lambda x:ec[x])
df = results.rename(columns={"d_prob_wo_unk": "Biden_probability", "d_avg": "Biden_avg",
                       "r_prob_wo_unk": "Trump_probability","r_avg":"Trump_avg","unk":"undecideds",
                       "full_state":"State"})
df = df[["State","undecideds","Biden_probability","Biden_avg",
                                 "Trump_probability","Trump_avg","ec"]].sort_values('State').reset_index(drop=True)

# https://cookpolitical.com/sites/default/files/2020-07/EC%20Ratings071420.pdf
cook = {'California': 'Solid Dem' ,
        'Connecticut': 'Solid Dem' ,
        'Delaware': 'Solid Dem' ,
        'District of Columbia': 'Solid Dem',
        'Hawaii': 'Solid Dem' ,
        'Illinois': 'Solid Dem' ,
        'Maine 1st CD': 'Solid Dem' ,
        'Maryland': 'Solid Dem' ,
        'Massachusetts': 'Solid Dem' ,
        'New Jersey': 'Solid Dem' ,
        'New Mexico': 'Solid Dem' ,
        'New York': 'Solid Dem' ,
        'Oregon': 'Solid Dem' ,
        'Rhode Island': 'Solid Dem' ,
        'Vermont': 'Solid Dem' ,
        'Washington': 'Solid Dem' ,
        'Colorado': 'Likely Dem' ,
        'Maine': 'Likely Dem' ,
        'Nevada': 'Likely Dem' ,
        'Virginia': 'Likely Dem' ,
        'Michigan': 'Lean Dem' ,
        'Minnesota': 'Lean Dem' ,
        'Nebraska 2nd CD': 'Lean Dem' ,
        'New Hampshire': 'Lean Dem' ,
        'Pennsylvania': 'Lean Dem' ,
        'Wisconsin': 'Lean Dem' ,
        'Arizona': 'Toss Up' ,
        'Florida': 'Toss Up' ,
        'Georgia': 'Toss Up' ,
        'Maine 2nd CD': 'Toss Up' ,
        'North Carolina': 'Toss Up' ,
        'Iowa': 'Lean Rep' ,
        'Ohio': 'Lean Rep' ,
        'Texas': 'Lean Rep' ,
        'Alaska': 'Likely Rep' ,
        'Montana': 'Likely Rep' ,
        'South Carolina': 'Likely Rep' ,
        'Utah': 'Likely Rep' ,
        'Alabama': 'Solid Rep' ,
        'Arkansas': 'Solid Rep' ,
        'Idaho': 'Solid Rep' ,
        'Indiana': 'Solid Rep' ,
        'Kansas': 'Solid Rep' ,
        'Kentucky': 'Solid Rep' ,
        'Louisiana': 'Solid Rep' ,
        'Mississippi': 'Solid Rep' ,
        'Missouri': 'Solid Rep' ,
        'Nebraska': 'Solid Rep' ,
        'Nebraska 1st CD': 'Solid Rep' ,
        'Nebraska 3rd CD': 'Solid Rep' ,
        'North Dakota': 'Solid Rep' ,
        'Oklahoma': 'Solid Rep' ,
        'South Dakota': 'Solid Rep' ,
        'Tennessee': 'Solid Rep' ,
        'West Virginia': 'Solid Rep' ,
        'Wyoming': 'Solid Rep'
       }
cook =  {k.lower(): v for k, v in cook.items()}
df['cook'] = df["State"].map(lambda x:cook[x])
df['spread'] = abs(df['Biden_avg']-df['Trump_avg'])
df['within_moe'] = np.where(df['spread'] <= 3,1,0)
df['within_spread'] = np.where(df['spread']<df['undecideds'],1,0)

# additional fields and field clean up
def f(x):
    if x['within_moe'] == 0 and x['within_spread'] ==0 and x['Biden_avg'] > 53: return 'Solid Dem'
    elif x['within_moe'] == 0 and x['within_spread'] ==0 and x['Trump_avg'] > 53: return 'Solid Rep'
    elif x['Biden_avg'] < 54  and x['Biden_avg'] > 50 : return 'Likely Dem'
    elif x['Trump_avg'] < 54  and x['Trump_avg'] > 50 : return 'Likely Rep'
    elif x['within_spread'] == 1 and x['Trump_avg'] >= 47  and x['Trump_avg'] < 50 and x['Trump_avg'] > x['Biden_avg'] : return 'Lean Rep'
    elif x['within_spread'] == 1 and x['Biden_avg'] >= 47 and x['Biden_avg'] < 50 and x['Biden_avg'] > x['Trump_avg'] : return 'Lean Dem'
    else: return "Toss Up"

def cook(x):
    if x['cook'] == 'Solid Dem' : return 1
    elif x['cook'] == 'Likely Dem' : return 2
    elif x['cook'] == 'Lean Dem' : return 3
    elif x['cook'] == 'Toss Up' : return 4
    elif x['cook'] == 'Lean Rep' : return 5
    elif x['cook'] == 'Likely Rep' : return 6
    else: return 7
      
def poll(x):
    if x['polls'] == 'Solid Dem' : return 1
    elif x['polls'] == 'Likely Dem' : return 2
    elif x['polls'] == 'Lean Dem' : return 3
    elif x['polls'] == 'Toss Up' : return 4
    elif x['polls'] == 'Lean Rep' : return 5
    elif x['polls'] == 'Likely Rep' : return 6
    else: return 7

df['polls'] = df.apply(f, axis=1)
df['consensus'] = np.where(df['cook']==df['polls'],1,0)
df['Hidden_trump'] = df['Trump_avg'] + df['undecideds']
df['Hidden_win'] = np.where(df['Hidden_trump'] > df['Biden_avg'],1,0)
df['average_trump_win'] = np.where(df['Trump_avg'] > df['Biden_avg'],1,0)
df['average_biden_win'] = np.where(df['Biden_avg'] > df['Trump_avg'],1,0)
df['cook_n'] = df.apply(cook, axis=1)
df['polls_n'] = df.apply(poll, axis=1)
df['gap'] = np.where(abs(df['cook_n']-df['polls_n'])>1,1,0)
df['score'] = df['cook_n'] + df['polls_n']
print()
print('saving csv file')
df.to_csv('results_' + datetime.now().strftime("%Y%m%d") + '.csv',index=False)
print('sim saved and complete')
print()