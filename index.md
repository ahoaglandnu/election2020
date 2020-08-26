# Understanding the 2020 Presidential Election Polls

![candidates](https://raw.githubusercontent.com/ahoaglandnu/election2020/master/graphics/election2020.png)

**Last updated**: August 20, 2020

## TL;DR Scenarios

**States with a weighted polling average of 50% or higher**

| Candidate      | Strong     | Likely     |   Total     |
|:---------------|:-----------|:-----------|------------:|
| Biden          | 189        | 57         |        246  | 
| Trump          | 61         | 44         |        105  | 



**If _ALL_ undecided voters in every state vote for Trump**

| Candidate      | Strong     | Likely     |   Total     |
|:---------------|:-----------|:-----------|------------:|
| Biden          | 193        | 24         |        217  | 
| Trump          | 256        | 65         |        **321**  | 



**Randomized distribution of undecided voters in every state**

| Candidate      | Strong     | Likely     |   Total     |
|:---------------|:-----------|:-----------|------------:|
| Biden          | 246        | 91         |        **337**  | 
| Trump          | 111        | 90         |        201  |



**_NEW_**   
**Undecided voters distributed by Partisan Voter Index**

| Candidate      | Strong     | Likely     |   Total     |
|:---------------|:-----------|:-----------|------------:|
| Biden          | 217        | 91         |        **308**  | 
| Trump          | 212        | 18         |        230  |

## Update

I added a fourth scenario to demonstrate how undecided voters can change the outcome of the election. This one uses the Cook Political Report's [Partisan Voter Index](https://cookpolitical.com/state-pvis) to weight how to distribute undecided voters. Keep in mind that an electoral college tally of 270 and above is a win so when a scenario has a winner, that total will be in **bold**.

## Strong and Likely States

In the two graphics below, we have states that are considered strong or likely states for the two candidates. The probability is based upon the weighted average polling for each state and if a candidate can win the state without the support of any undecided voters. Safe states without polling as designated by the Cook Political Report are assigned a probabilty of 1 for the favored candidate and 0 for the opponent.

### Biden

Biden Solid States 189  
Biden Likely States 57   
Biden Solid + Likely States 246   

**Link to Interactive graphic**  
[Biden Solid and Likely States](https://ahoaglandnu.github.io/biden_no_undecideds.html)

![biden](https://raw.githubusercontent.com/ahoaglandnu/election2020/gh-pages/images/biden_0820.png)




### Trump

Trump Solid States 61   
Trump Likely States 44   
Trump Solid + Likely States 105      

**Link to Interactive graphic**  
[Trump Solid and Likely States](https://ahoaglandnu.github.io/trump_no_undecideds.html)

![trump](https://raw.githubusercontent.com/ahoaglandnu/election2020/gh-pages/images/trump_0820.png)




## States where undecided voters are most likely to determine the outcome

The table below can be considered the "path to victory" states as both campaigns will pursue several combinations of these states to pass 270 electoral college votes.


|    | State          |   ec | cook       | PVI   |   Biden_avg |   Trump_avg |   undecideds |
|---:|:---------------|-----:|:-----------|:------|------------:|------------:|-------------:|
|  0 | arizona        |   11 | Toss Up    | R+5   |        46.2 |        44.9 |          8.9 |
|  1 | florida        |   29 | Toss Up    | R+2   |        50.2 |        44.5 |          5.4 |
|  2 | georgia        |   16 | Toss Up    | R+5   |        45.1 |        47.3 |          7.7 |
|  3 | iowa           |    6 | Lean Rep   | R+3   |        44.5 |        46   |          9.5 |
|  4 | michigan       |   16 | Lean Dem   | D+1   |        49.1 |        41.9 |          9   |
|  5 | minnesota      |   10 | Lean Dem   | D+1   |        47.9 |        45.5 |          6.6 |
|  6 | nevada         |    6 | Likely Dem | D+1   |        48   |        43.7 |          8.3 |
|  7 | north carolina |   15 | Toss Up    | R+3   |        46.5 |        47.4 |          6.1 |
|  8 | ohio           |   18 | Lean Rep   | R+3   |        47.8 |        45   |          7.2 |
|  9 | pennsylvania   |   20 | Lean Dem   | EVEN  |        49.5 |        43.6 |          6.9 |
| 10 | utah           |    6 | Likely Rep | R+20  |        38.5 |        46.9 |         14.6 |
| 11 | wisconsin      |   10 | Lean Dem   | EVEN  |        47.8 |        43.2 |          9   |




## If all undecided voters are shy Trump supporters

The graphic below assumes **all** undecided voters will vote for Trump. This scenario is the "hidden Trump vote" or "shy Trump supporter" in polling. 

Trump Solid States 256   
Trump Likely States 65  
Trump Solid + Likely States **321**     

Biden Solid States 193  
Biden Likely States 24  
Biden Solid + Likely States 217   


**Link to Interactive graphic**  
[Hidden Trump Vote Scenario](https://ahoaglandnu.github.io/hidden_trump.html)   

![hidden](https://raw.githubusercontent.com/ahoaglandnu/election2020/gh-pages/images/hidden_0820.png)




## Random distribution of undecided voters

The graphic below randomly distributed undecided voters for each state in 20,000 simulations per state.

Trump Solid States 111   
Trump Likely States 90   
Trump Solid + Likely States 201   

Biden Solid States 246   
Biden Likely States 91   
Biden Solid + Likely States **337**  

**Link to Interactive graphic**   
[Randomized undecided voters](https://ahoaglandnu.github.io/random_undecided.html)  

![random](https://raw.githubusercontent.com/ahoaglandnu/election2020/gh-pages/images/random_0820.png)




## Partisan Voter Index distribution of undecided voters

The graphic below uses the PVI to determine how to distribute undecided voters for each state in 20,000 simulations per state. This is the equivalent of a _Polls Plus_ model.

Trump Solid States 212   
Trump Likely States 18   
Trump Solid + Likely States 230   

Biden Solid States 217   
Biden Likely States 91   
Biden Solid + Likely States **308**   

**Link to Interactive graphic**   
[PVI undecided voters](https://ahoaglandnu.github.io/pvi.html)

![pvi](https://raw.githubusercontent.com/ahoaglandnu/election2020/gh-pages/images/pvi_0820.png)

## Updated Weighted Polls, Cook Political Report Assessment, and Partisan Voter Index


|    | State                |   ec | cook       | PVI   |   Biden_avg |   Trump_avg |   undecideds |
|---:|:---------------------|-----:|:-----------|:------|------------:|------------:|-------------:|
|  0 | alabama              |    9 | Solid Rep  | R+14  |        38   |        58   |          4   |
|  1 | alaska               |    3 | Likely Rep | R+9   |        45   |        48   |          7   |
|  2 | arizona              |   11 | Toss Up    | R+5   |        46.2 |        44.9 |          8.9 |
|  3 | arkansas             |    6 | Solid Rep  | R+15  |        45   |        47   |          8   |
|  4 | california           |   55 | Solid Dem  | D+12  |        62.4 |        29.6 |          8   |
|  5 | colorado             |    9 | Likely Dem | D+1   |        55   |        45   |          0   |
|  6 | connecticut          |    7 | Solid Dem  | D+6   |        50.9 |        33.9 |         15.2 |
|  7 | delaware             |    3 | Solid Dem  | D+6   |        56   |        40   |          4   |
|  8 | florida              |   29 | Toss Up    | R+2   |        50.2 |        44.5 |          5.4 |
|  9 | georgia              |   16 | Toss Up    | R+5   |        45.1 |        47.3 |          7.7 |
| 10 | indiana              |   11 | Solid Rep  | R+9   |        39   |        52   |          9   |
| 11 | iowa                 |    6 | Lean Rep   | R+3   |        44.5 |        46   |          9.5 |
| 12 | kansas               |    6 | Solid Rep  | R+13  |        40.6 |        49.6 |          9.8 |
| 13 | kentucky             |    8 | Solid Rep  | R+15  |        39.7 |        53.3 |          7   |
| 14 | maine                |    4 | Likely Dem | D+3   |        51.6 |        39.2 |          9.1 |
| 15 | massachusetts        |   11 | Solid Dem  | D+12  |        62.9 |        29.4 |          7.6 |
| 16 | michigan             |   16 | Lean Dem   | D+1   |        49.1 |        41.9 |          9   |
| 17 | minnesota            |   10 | Lean Dem   | D+1   |        47.9 |        45.5 |          6.6 |
| 18 | mississippi          |    6 | Solid Rep  | R+9   |        41   |        56   |          3   |
| 19 | missouri             |   10 | Solid Rep  | R+9   |        43.2 |        50.2 |          6.7 |
| 20 | montana              |    3 | Likely Rep | R+11  |        42   |        52.2 |          5.8 |
| 21 | nevada               |    6 | Likely Dem | D+1   |        48   |        43.7 |          8.3 |
| 22 | new hampshire        |    4 | Lean Dem   | EVEN  |        52.5 |        40.8 |          6.7 |
| 23 | new jersey           |   14 | Solid Dem  | D+7   |        55   |        34.5 |         10.5 |
| 24 | new mexico           |    5 | Solid Dem  | D+3   |        53.7 |        43.7 |          2.7 |
| 25 | new york             |   29 | Solid Dem  | D+11  |        55.7 |        32   |         12.4 |
| 26 | north carolina       |   15 | Toss Up    | R+3   |        46.5 |        47.4 |          6.1 |
| 27 | ohio                 |   18 | Lean Rep   | R+3   |        47.8 |        45   |          7.2 |
| 28 | pennsylvania         |   20 | Lean Dem   | EVEN  |        49.5 |        43.6 |          6.9 |
| 29 | south carolina       |    9 | Likely Rep | R+8   |        43.3 |        50.2 |          6.4 |
| 30 | tennessee            |   11 | Solid Rep  | R+14  |        39   |        52.7 |          8.3 |
| 31 | texas                |   38 | Lean Rep   | R+8   |        43.5 |        47.7 |          8.8 |
| 32 | utah                 |    6 | Likely Rep | R+20  |        38.5 |        46.9 |         14.6 |
| 33 | virginia             |   13 | Likely Dem | D+1   |        50.7 |        39   |         10.3 |
| 34 | washington           |   12 | Solid Dem  | D+7   |        59.5 |        30.2 |         10.3 |
| 35 | wisconsin            |   10 | Lean Dem   | EVEN  |        47.8 |        43.2 |          9   |
| 36 | district of columbia |    3 | Solid Dem  | D+43  |       nan   |       nan   |        nan   |
| 37 | hawaii               |    4 | Solid Dem  | D+18  |       nan   |       nan   |        nan   |
| 38 | idaho                |    4 | Solid Rep  | R+19  |       nan   |       nan   |        nan   |
| 39 | illinois             |   20 | Solid Dem  | D+7   |       nan   |       nan   |        nan   |
| 40 | louisiana            |    8 | Solid Rep  | R+11  |       nan   |       nan   |        nan   |
| 41 | maryland             |   10 | Solid Dem  | D+12  |       nan   |       nan   |        nan   |
| 42 | nebraska             |    5 | Solid Rep  | R+14  |       nan   |       nan   |        nan   |
| 43 | north dakota         |    3 | Solid Rep  | R+17  |       nan   |       nan   |        nan   |
| 44 | oklahoma             |    7 | Solid Rep  | R+20  |       nan   |       nan   |        nan   |
| 45 | oregon               |    7 | Solid Dem  | D+5   |       nan   |       nan   |        nan   |
| 46 | rhode island         |    4 | Solid Dem  | D+10  |       nan   |       nan   |        nan   |
| 47 | south dakota         |    3 | Solid Rep  | R+14  |       nan   |       nan   |        nan   |
| 48 | vermont              |    3 | Solid Dem  | D+15  |       nan   |       nan   |        nan   |
| 49 | west virginia        |    5 | Solid Rep  | R+19  |       nan   |       nan   |        nan   |
| 50 | wyoming              |    3 | Solid Rep  | R+25  |       nan   |       nan   |        nan   |


# About this Project 

Quite a lot has been written about 2016 election forecasts, polls, and the [influence](https://www.dartmouth.edu/~seanjwestwood/papers/aggregator.pdf) they may have had on voter behavior. A good friend and I were also caught up in the [hype around forecast models](https://slate.com/news-and-politics/2016/11/how-will-we-know-if-nate-silver-was-right.html) and which one would be the most accurate. We all know how that turned out. 

![data science](https://user-images.githubusercontent.com/19977/61344565-8966da00-a806-11e9-9e6c-954a42102b36.png)

This project is based off of the lessons learned from the 2016 and 2018 elections. The intent is to **inform**, _not influence_, the 2020 presidential election.

# What's different?

Plain and simple, there is not a prediction for the winner. Instead, the intent is to show which states are close, which are not, and what the potential effects undecided voters can have on the outcome. The goal of data journalism is to leave the reader with a better understanding of the complex and that is precisely what we will try to do this time around.

### Sources of Polling Data

State polling data will come from [RealClearPolitics](https://www.realclearpolitics.com/epolls/2020/president/2020_elections_electoral_college_map.html) and not include their state [averages](https://en.wikipedia.org/wiki/Mean) for reasons covered in the approach section below. Not all states or districts may have polling available. In these cases, the [Cook Political Report's Electoral Scorecard](https://cookpolitical.com/) will be used to complete the picture. The states or districts not having polling data until much later in the campaign are often safe for one candidate while battleground states have polling data updated more frequently.

# The Approach

### Weighted Averages

Not all polls are of equal quality, but a simple average would treat them that way. Instead, I have two methods to weight the polls; by margin or error and by segment polled, specifically registered voters or likely voters. 

A registered voter is someone who is simply registered to vote, while a likely voter is a registered voter who has indicated their intention to vote in the election. Polling firms handle this determination differently, but you can read more about the segments [here](https://en.wikipedia.org/wiki/Voter_segments_in_political_polling). Since [voter turnout varies](https://www.census.gov/newsroom/blogs/random-samplings/2017/05/voting_in_america.html) from state to state, polls with likely voters are weighted 3 times higher than those with registered voters.

```
segment_weight = np.where(segment == 'LV',3,1)
```

Margin of error rises and falls depending on the population size, sample size, and confidence interval of the survey. The larger samples will have a smaller margin of error. Polls are ranked according to margin of error as the second weight used to determine average.

```
candidate_weighted_average = (polls * MoE ranks * sum(segment_weight)) / sum(MoE ranks * sum(segment_weight))
```
### Safe States, Likely States, and Leaning States

We see these terms on a number of electoral college maps, but it may not be apparent as to why a state has such a label.

One of the major issues with the 2016 election was that strong third party candidate performance led to a number of plurality leads; instances in which no candidate had a majority of 50% or greater. The 2020 election year has a traditional two candidate race, meaning we will see majority victories. This is the foundation for the definitions of the labels below.

**Safe State** is where a candidate has a majority _beyond_ the margin of error and all undecided votes going to the opponent does not change the outcome.

**Likely State** is where a candidate has a majority _within_ the margin of error and all undecided votes going to the opponent does not change the outcome. 

**Leaning State** is where a candidate has a majority _within_ the margin of error and all undecided votes going to the opponent _can_ change the outcome.

**Toss Up** is where _no_ candidate has a majority and a _combination_ of the margin of error and undecided votes _divided between candidates_ changes the outcome.

### Margin of Error

We are assuming a 3% margin of error for the weighted averages. _why assume a 3% margin of error?_ The simple answer is that it comes down to sample size based upon population size.

Wyoming is the least populated state with around 600,000 residents. In 2016, there were 258,788 ballots cast for the presidential election. For a population of 250,000 likely voters, a sample size of 782 would have a margin of error of 3.5% and a sample size of 1,527 would have a margin of error of 2.5%.

A population of 100,000,000 has similar sample size requirements, 784 and 1,537 respectively. As you look at polling coming in, you see sample sizes near 1,000 or if you average all the polling sample sizes of a state it is also near 1,000, thus a 3% margin of error for the weighted average of state polls.

You can read more about sample sizes [here](https://www.research-advisors.com/tools/SampleSize.htm). The lookup table for required sample sizes is one I have used since grad school.

### Monte Carlo Simulation for Probabilities

I know upfront I said we are not forecasting a winner and that is still the case. In order to make the state labels easier to understand, we use the weighted averages and 3% margin of error to determine the probability a candidate can win a state _without_ any undecided voter support. 

The margin of error gives us a range of what the actual number could be. For example, let's say a candidate is polling at 50% with a 4% margin of error. That means the actual number would be within this range below.

![range of poll](https://raw.githubusercontent.com/ahoaglandnu/election/master/images/ex1.png)

When we do the same for the competitor, then we can see who may be winning the race.
A **Safe State** for a candidate would look like this

![safe](https://raw.githubusercontent.com/ahoaglandnu/election/master/images/ex12.png)

Unfortunately, there are a number of races where the margin of error will overlap. 
**Likely and Leaning States** are where we have our first potential area for misinterpretation

![confusion](https://raw.githubusercontent.com/ahoaglandnu/election/master/images/ex7.png)

This is why we introduce random error within the range. Using a random number generator for each candidate, we can get a result from a simulation that looks like this below.

![single sim](https://raw.githubusercontent.com/ahoaglandnu/election/master/images/ex8.png)

That is one random outcome. What we need to do is figure out how often we can see one candidate ahead of another. 

To do a single monte carlo simulation, we would input the respective weighted averages of the candidates and the margin of error and assume normal distribution of the errors.
```
def moe(x, y, n):
    min_x = x - n
    max_x = x + n
    std_x = (max_x - min_x) / 4
    min_y = y - n
    max_y = y + n
    std_y = (max_y - min_y) / 4
    return round(random.gauss(x, std_x),1), round(random.gauss(y, std_y),1)
```

Running a simulation one time may lead to an outcome that does not have either candidate with a majority or a sum of votes that does not equal 100% of votes cast.

### Undecided Voters

Whenever a round of a simulation does not end up with a total of 100%, we capture that as our undecided voters. The reason this number is important is because undecided voters determine the winner of close races.

```
def undecided(x,y,n):
    cand1, cand2 = moe(x, y, n)
    u = round((100 - cand1 - cand2),1)
    return round(cand1,1),round(cand2,1),round(u,1)
```

Now we can run the simulation multiple times in order to generate a probability of how often a candidate can win a majority without any undecided voter support.

```
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
```

This gives us a much better perspective on the state of the election race as we can now identify which states are likely to be determined by undecided voters.

Another challenge in interpreting the data remains as the label for *Leaning* states often gives the false impression that the state will be awarded to that candidate. We saw this scenario play out in the 2016 election as unaccounted for undecided voters tipped several states and the electoral college.
