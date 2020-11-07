import plotly.graph_objects as go
import pandas as pd, numpy as np
import datetime
import random
random.seed(2020)

print('Update as of:', datetime.datetime.now())
filename = 'results_' + datetime.datetime.now().strftime("%Y%m%d") + '.csv'
df = pd.read_csv(filename)
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
states = {k: v.lower() for k,v in states.items()}
states = {v:k for k,v in states.items()}
df['code'] = df['State'].map(lambda x:states[x])
df2 = df[['State','polls','ec','trump_alt_prob','biden_alt_prob']]
for col in df.columns:
    df[col] = df[col].astype(str)
df['text'] = df['State'] + '<br>' + 'Electoral College Votes '+ df['ec'] +  '<br>' + 'Cook Political Report: ' + df['cook'] + '<br>' + 'Weighted Polling: ' + df['polls'] + '<br>' + 'Biden ' + df['Biden_avg'] + ' Trump ' + df['Trump_avg'] + ' Undecided ' + df['undecideds']

fig = go.Figure(data=go.Choropleth(
    locations=df['code'],
    z=df['Biden_probability'].astype(float),
    locationmode='USA-states',
    colorscale='blues',
    autocolorscale=False,
    text=df['text'], 
    marker_line_color='white',
    colorbar_title="Biden Probability"
))
fig.update_layout(
    title_text='Biden state probabilities with no undecided voters<br>(Hover for breakdown)',
    geo = dict(
        scope='usa',
        projection=go.layout.geo.Projection(type = 'albers usa'),
        showlakes=False, 
        lakecolor='rgb(255, 255, 255)'),
)
fig.write_html("biden_no_undecideds.html")
fig.write_image('biden_' + datetime.datetime.now().strftime("%m%d") + '.png')
print("Biden Solid States",df2[df2['polls'] == 'Solid Dem']['ec'].sum())
print("Biden Likely States",df2[df2['polls'] == 'Likely Dem']['ec'].sum())
print("Biden Solid + Likely States",df2[df2['polls'] == 'Solid Dem']['ec'].sum() + df2[df2['polls'] == 'Likely Dem']['ec'].sum())
print()


fig = go.Figure(data=go.Choropleth(
    locations=df['code'],
    z=df['Trump_probability'].astype(float),
    locationmode='USA-states',
    colorscale='reds',
    autocolorscale=False,
    text=df['text'], 
    marker_line_color='white',
    colorbar_title="Trump Probability"
))
fig.update_layout(
    title_text='Trump state probabilities with no undecided voters<br>(Hover for breakdown)',
    geo = dict(
        scope='usa',
        projection=go.layout.geo.Projection(type = 'albers usa'),
        showlakes=False, 
        lakecolor='rgb(255, 255, 255)'),
)
fig.write_html("trump_no_undecideds.html")
fig.write_image('trump_' + datetime.datetime.now().strftime("%m%d") + '.png')
print("Trump Solid States",df2[df2['polls'] == 'Solid Rep']['ec'].sum())
print("Trump Likely States",df2[df2['polls'] == 'Likely Rep']['ec'].sum())
print("Trump Solid + Likely States",df2[df2['polls'] == 'Solid Rep']['ec'].sum() + df2[df2['polls'] == 'Likely Rep']['ec'].sum())
print()

# Hidden Trump Vote Scenario

for col in df.columns:
    df[col] = df[col].astype(str)
df['text'] = df['State'] + '<br>' + 'Electoral College Votes '+ df['ec'] +  '<br>' + 'Cook Political Report: ' + df['cook'] + '<br>' + 'Weighted Polling: ' + df['polls'] + '<br>' + 'Biden ' + df['biden_alt_avg'] + ' Trump ' + df['trump_alt_avg'] + '<br>''Biden probability ' + df['biden_alt_prob'] + '<br>''Trump probability ' + df['trump_alt_prob']

fig = go.Figure(data=go.Choropleth(
    locations=df['code'],
    z=df['biden_alt_prob'].astype(float),
    locationmode='USA-states',
    colorscale='RdBu',
    autocolorscale=False,
    text=df['text'], 
    marker_line_color='white',
    colorbar_title="Biden Probability"
))
fig.update_layout(
    title_text='State probabilities with ALL undecided voters for Trump<br>(Hover for breakdown)',
    geo = dict(
        scope='usa',
        projection=go.layout.geo.Projection(type = 'albers usa'),
        showlakes=False, 
        lakecolor='rgb(255, 255, 255)'),
)

fig.write_html("hidden_trump.html")
fig.write_image('hidden_' + datetime.datetime.now().strftime("%m%d") + '.png')
print('Hidden Trump Vote Scenario')
print()
print("Trump Solid States",df2[df2['trump_alt_prob'] > .9]['ec'].sum())
print("Trump Likely States",df2[(df2['trump_alt_prob'] < .9) & (df2['trump_alt_prob'] > .5)]['ec'].sum())
print("Trump Solid + Likely States",df2[df2['trump_alt_prob'] > .5]['ec'].sum())
print()
print("Biden Solid States",df2[df2['biden_alt_prob'] > .9]['ec'].sum())
print("Biden Likely States",df2[(df2['biden_alt_prob'] < .9) &(df2['biden_alt_prob'] > .5)]['ec'].sum())
print("Biden Solid + Likely States",df2[df2['biden_alt_prob'] > .5]['ec'].sum())


# Randomized Distribution of Undecided Voters

def moe(x, y, n):
    min_x = x - n
    max_x = x + n
    std_x = (max_x - min_x) / 4
    min_y = y - n
    max_y = y + n
    std_y = (max_y - min_y) / 4
    return round(random.gauss(x, std_x),1), round(random.gauss(y, std_y),1)
def distro_sim(x, y, n=3, num_sims=20000):
    u = 100 - (x + y)
    x_wins = 0
    y_wins = 0
    for i in range(num_sims):
        rand = np.random.uniform(low=0.01,high=.99)
        x1 = x + (u * rand)
        y1 = y + (u * (1 - rand))
        x1, y1 = moe(x1, y1, n)
        if x1 > y1:
            x_wins += 1
        else:
            y_wins += 1
    return x_wins/num_sims, y_wins/num_sims 

df["Biden_avg"] = pd.to_numeric(df["Biden_avg"],errors='coerce')
df["Trump_avg"] = pd.to_numeric(df["Trump_avg"],errors='coerce')

b = df['Biden_avg'].values
t = df['Trump_avg'].values
rand_prob = []
for x, y in zip(b,t):
    rp = distro_sim(x,y)
    rand_prob.append(rp)
df['biden_rand_prob'] = [i[0] for i in rand_prob]
df['trump_rand_prob'] = [i[1] for i in rand_prob]
df.loc[(df['cook'] == 'Solid Dem') & (df['Biden_avg'].isnull()),'biden_rand_prob'] = 1.0
df.loc[(df['cook'] == 'Solid Dem') & (df['Biden_avg'].isnull()),'trump_rand_prob'] = 0.0
df.loc[(df['cook'] == 'Solid Rep') & (df['Trump_avg'].isnull()),'biden_rand_prob'] = 0.0
df.loc[(df['cook'] == 'Solid Rep') & (df['Trump_avg'].isnull()),'trump_rand_prob'] = 1.0

for col in df.columns:
    df[col] = df[col].astype(str)
df['text'] = df['State'] + '<br>' + 'Electoral College Votes '+ df['ec'] +  '<br>' + 'Cook Political Report: ' + df['cook'] + '<br>' + 'Weighted Polling: ' + df['polls'] + '<br>' + 'Biden ' + df['Biden_avg'] + ' Trump ' + df['Trump_avg'] + ' Undecided ' + df['undecideds'] + '<br>''Biden probability ' + df['biden_rand_prob'] + '<br>''Trump probability ' + df['trump_rand_prob']

fig = go.Figure(data=go.Choropleth(
    locations=df['code'],
    z=df['biden_rand_prob'].astype(float),
    locationmode='USA-states',
    colorscale='RdBu',
    autocolorscale=False,
    text=df['text'], 
    marker_line_color='white',
    colorbar_title="Biden Probability"
))
fig.update_layout(
    title_text='State probabilities with randomized distribution of undecided voters<br>(Hover for breakdown)',
    geo = dict(
        scope='usa',
        projection=go.layout.geo.Projection(type = 'albers usa'),
        showlakes=False, 
        lakecolor='rgb(255, 255, 255)'),
)

fig.write_html("random_undecided.html")
fig.write_image('random_' + datetime.datetime.now().strftime("%m%d") + '.png')
df["biden_rand_prob"] = pd.to_numeric(df["biden_rand_prob"])
df["trump_rand_prob"] = pd.to_numeric(df["trump_rand_prob"])
df['ec'] = pd.to_numeric(df['ec'])
print('Randomized distribution of undecided voters')
print("Trump Solid States",df[df['trump_rand_prob'] > .9]['ec'].sum())
print("Trump Likely States",df[(df['trump_rand_prob'] < .9) & (df['trump_rand_prob'] > .5)]['ec'].sum())
print("Trump Solid + Likely States",df[df['trump_rand_prob'] > .5]['ec'].sum())
print()
print("Biden Solid States",df[df['biden_rand_prob'] > .9]['ec'].sum())
print("Biden Likely States",df[(df['biden_rand_prob'] < .9) &(df['biden_rand_prob'] > .5)]['ec'].sum())
print("Biden Solid + Likely States",df[df['biden_rand_prob'] > .5]['ec'].sum())
print()

def polls_only_ec(ec, cand, state, sims=20000):
    cand_wins = 0
    cand_ec_total = []
    cand_states = []
    for i in range(sims):
        cand_ec = 0
        cand_state = []
        sim_election = np.random.uniform(low=0.05)
        lean_r_sim = np.random.uniform()
        lean_d_sim = np.random.uniform()
        for x, y, z in zip(cand, states, ec):
            if y in lean_r:
                sim_election = lean_r_sim
            elif y in lean_d:
                sim_election = lean_d_sim
            elif y in tossup:
                sim_election = np.random.uniform()
            if x > sim_election:
                cand_ec += z
                cand_state.append(y)
        cand_ec_total.append(cand_ec)
        cand_states.append(cand_state)
        if cand_ec > 269:
            cand_wins += 1
    return cand_wins, cand_ec_total, cand_states

def pvi_sim(x, y, u, score, n=3, num_sims=20000):
    x_wins = 0
    y_wins = 0
    for i in range(num_sims):
        solid_r_sim = np.random.uniform(high=.05)
        solid_d_sim = np.random.uniform(low=.95)
        likely_r_sim = np.random.uniform(low=0.05, high=.34)
        likely_d_sim = np.random.uniform(low=.68, high=.95)
        if score >= solid_r_score:
            rand = solid_r_sim
        elif score <= solid_d_score and score > likely_d_score:
            rand = solid_d_sim
        elif score >= likely_r_score:
            rand = likely_r_sim
        elif score <= likely_d_score and score > 0:
            rand = likely_d_sim
        else:
            rand = np.random.uniform()
        x1 = x + (u * rand)
        y1 = y + (u * (1 - rand))
        x1, y1 = moe(x1, y1, n)
        if x1 > y1:
            x_wins += 1
        else:
            y_wins += 1
    return x_wins/num_sims, y_wins/num_sims 

# https://cookpolitical.com/state-pvis
pvi = pd.read_csv('data-l0JU2.csv')
pvi['State'] = pvi['State'].str.lower()
pvi['score'] = pvi['PVI'].str.split('+').str[1].astype('float')
pvi.loc[pvi['PVI'].str.startswith("D"), 'score'] *= -1
pvi.loc[pvi['PVI'].str.startswith("E"), 'score'] = 0
pvi['norm_score'] = pvi['score'] / pvi['score'].std()
df = pd.merge(df, pvi[['State','PVI','score','norm_score']], how='inner', on = 'State')

df["Biden_avg"] = pd.to_numeric(df["Biden_avg"],errors='coerce')
df["Trump_avg"] = pd.to_numeric(df["Trump_avg"],errors='coerce')
df["undecideds"] = pd.to_numeric(df["undecideds"],errors='coerce')

lean_r = list(df[(df['norm_score'] <.25)& (df['norm_score'] >0)]['State'])
lean_d = list(df[(df['norm_score'] <0)& (df['norm_score'] > -.24)]['State'])
tossup = list(df[df['norm_score'] ==0]['State'])
solid_r_score = df[df['norm_score'] > 0]['norm_score'].quantile(.1)
solid_d_score = df[df['norm_score'] < 0]['norm_score'].quantile(.1)
likely_r_score = df[(df['norm_score'] > 0) & (df['norm_score'] < solid_r_score)]['norm_score'].min()
likely_d_score = df[(df['norm_score'] < 0) & (df['norm_score'] > solid_d_score)]['norm_score'].max()

b = df['Biden_avg'].values
t = df['Trump_avg'].values
u = df['undecideds'].values
score = df['norm_score'].values
pvi_prob = []
for x, y, a, z in zip(b,t,u,score):
    p = pvi_sim(x,y,a,z)
    pvi_prob.append(p)
df['biden_pvi_prob'] = [i[0] for i in pvi_prob]
df['trump_pvi_prob'] = [i[1] for i in pvi_prob]
df.loc[(df['cook'] == 'Solid Dem') & (df['Biden_avg'].isnull()),'biden_pvi_prob'] = 0.9999
df.loc[(df['cook'] == 'Solid Dem') & (df['Biden_avg'].isnull()),'trump_pvi_prob'] = 0.0001
df.loc[(df['cook'] == 'Solid Rep') & (df['Trump_avg'].isnull()),'biden_pvi_prob'] = 0.0001
df.loc[(df['cook'] == 'Solid Rep') & (df['Trump_avg'].isnull()),'trump_pvi_prob'] = 0.9999
df.loc[df['biden_pvi_prob'] == 1,'biden_pvi_prob'] = 0.9999
df.loc[df['biden_pvi_prob'] == 0,'biden_pvi_prob'] = 0.0001
df.loc[df['trump_pvi_prob'] == 1,'trump_pvi_prob'] = 0.9999
df.loc[df['trump_pvi_prob'] == 0,'trump_pvi_prob'] = 0.0001

for col in df.columns:
    df[col] = df[col].astype(str)
df['text'] = df['State'] + '<br>' + \
'Electoral College Votes '+ df['ec'] +  '<br>' + \
'Cook Political Report: ' + df['cook'] + '<br>' + \
'Weighted Polling: ' + df['polls'] + '<br>' + \
'Partisan Voter Index: ' + df['PVI'] + '<br>' + \
'Biden ' + df['Biden_avg'] + ' Trump ' + df['Trump_avg'] +  '<br>' +\
'Biden probability ' + df['biden_pvi_prob'] + '<br>' +\
'Trump probability ' + df['trump_pvi_prob']

fig = go.Figure(data=go.Choropleth(
    locations=df['code'],
    z=df['biden_pvi_prob'].astype(float),
    locationmode='USA-states',
    colorscale='RdBu',
    autocolorscale=False,
    text=df['text'], 
    marker_line_color='white',
    colorbar_title="Biden Probability"
))
fig.update_layout(
    title_text='State probabilities with undecided voters distributed by Partisan Voter Index<br>(Hover for breakdown)',
    geo = dict(
        scope='usa',
        projection=go.layout.geo.Projection(type = 'albers usa'),
        showlakes=False, 
        lakecolor='rgb(255, 255, 255)'),
)

fig.write_html("pvi.html")
fig.write_image('pvi_' + datetime.datetime.now().strftime("%m%d") + '.png')
df["biden_pvi_prob"] = pd.to_numeric(df["biden_pvi_prob"])
df["trump_pvi_prob"] = pd.to_numeric(df["trump_pvi_prob"])
df['ec'] = pd.to_numeric(df['ec'])
print("Trump Solid States",df[df['trump_pvi_prob'] > .9]['ec'].sum())
print("Trump Likely States",df[(df['trump_pvi_prob'] < .9) & (df['trump_pvi_prob'] > .5)]['ec'].sum())
print("Trump Solid + Likely States",df[df['trump_pvi_prob'] > .5]['ec'].sum())
print()
print("Biden Solid States",df[df['biden_pvi_prob'] > .9]['ec'].sum())
print("Biden Likely States",df[(df['biden_pvi_prob'] < .9) &(df['biden_pvi_prob'] > .5)]['ec'].sum())
print("Biden Solid + Likely States",df[df['biden_pvi_prob'] > .5]['ec'].sum())
print()
print(df[['State','ec','cook','PVI','Biden_avg','Trump_avg','undecideds']].to_markdown())
print()
bg_df = pd.read_csv('battleground_' + datetime.datetime.now().strftime("%Y%m%d") + '.csv')
bg_df = pd.merge(bg_df, pvi[['State','PVI','score','norm_score']], how='inner', on = 'State')
print(bg_df[['State','ec','cook','PVI','Biden_avg','Trump_avg','undecideds']].to_markdown())