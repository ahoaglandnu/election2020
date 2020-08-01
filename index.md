![data science](https://user-images.githubusercontent.com/19977/61344565-8966da00-a806-11e9-9e6c-954a42102b36.png)

# Understanding the 2020 Presidential Election Polls

Quite a lot has been written about 2016 election forecasts, polls, and the [influence](https://www.dartmouth.edu/~seanjwestwood/papers/aggregator.pdf) they may have had on voter behavior. A good friend and I were also caught up in the [hype around forecast models](https://slate.com/news-and-politics/2016/11/how-will-we-know-if-nate-silver-was-right.html) and which one would be the most accurate. We all know how that turned out. 

This project is based off of the lessons learned from the 2016 and 2018 elections. The intent is to **inform**, _not influence_, the 2020 presidential election.

# What's different?

Plain and simple, there is not a prediction for the winner. Instead, the intent is to show which states are close, which are not, and what the potential effects undecided voters can have on the outcome. The goal of data journalism is to leave the reader with a better understanding of the complex and that is precisely what we will try to do this time around.

### Sources of Polling Data

State polling data will come from [RealClearPolitics](https://www.realclearpolitics.com/epolls/2020/president/2020_elections_electoral_college_map.html) and not include their state [averages](https://en.wikipedia.org/wiki/Mean) for reasons covered in the approach section below. Not all states or districts may have polling available. In these cases, the [Cook Political Report's Electoral Scorecard](https://cookpolitical.com/) will be used to complete the picture. The states or districts not having polling data until much later in the campaign are often safe for one candidate while battleground states have polling data updated more frequently.  

# The Approach

**Weighted Averages**

Not all polls are of equal quality, but a simple average would treat them that way. Instead, I have two methods to weight the polls; by margin or error and by segment polled, specifically registered voters or likely voters. 

A registered voter is someone who is simply registered to vote, while a likely voter is a registered voter who has indicated their intention to vote in the election. Polling firms handle this determination differently, but you can read more about the segments [here](https://en.wikipedia.org/wiki/Voter_segments_in_political_polling). Since [voter turnout varies](https://www.census.gov/newsroom/blogs/random-samplings/2017/05/voting_in_america.html) from state to state, polls with likely voters are weighted 3 times higher than those with registered voters.

```
segment_weight = np.where(segment == 'LV',3,1)
```

Margin of error rises and falls depending on the population size, sample size, and confidence interval of the survey. The larger samples will have a smaller margin of error. Polls are ranked according to margin of error as the second weight used to determine average.

```
candidate_weighted_average = (polls * MoE ranks * sum(segment_weight)) / sum(MoE ranks * sum(segment_weight))
```
**Safe States, Likely States, and Leaning States**

We see these terms on a number of electoral college maps, but it may not be apparent as to why a state has such a label.

One of the major issues with the 2016 election was that strong third party candidate performance led to a number of plurality leads; instances in which no candidate had a majority of 50% or greater. The 2020 election year has a traditional two candidate race, meaning we will see majority victories. This is the foundation for the definitions of the labels below.

**Safe State** is where a candidate has a majority _beyond_ the margin of error and all undecided votes going to the opponent does not change the outcome.

**Likely State** is where a candidate has a majority _within_ the margin of error and all undecided votes going to the opponent does not change the outcome. 

**Leaning State** is where a candidate has a majority _within_ the margin of error and all undecided votes going to the opponent _can_ change the outcome.

**Toss Up** is where _no_ candidate has a majority and a _combination_ of the margin of error and undecided votes _divided between candidates_ changes the outcome.

**Margin of Error** 

We are assuming a 3% margin of error for the weighted averages. _why assume a 3% margin of error?_ The simple answer is that it comes down to sample size based upon population size.

Wyoming is the least populated state with around 600,000 residents. In 2016, there were 258,788 ballots cast for the presidential election. For a population of 250,000 likely voters, a sample size of 782 would have a margin of error of 3.5% and a sample size of 1,527 would have a margin of error of 2.5%.

A population of 100,000,000 has similar sample size requirements, 784 and 1,537 respectively. As you look at polling coming in, you see sample sizes near 1,000 or if you average all the polling sample sizes of a state it is also near 1,000, thus a 3% margin of error for the weighted average of state polls.

You can read more about sample sizes [here](https://www.research-advisors.com/tools/SampleSize.htm). The lookup table for required sample sizes is one I have used since grad school.

**Monte Carlo Simulation for Probabilities**

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

**Undecided Voters**

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

# Results

In order to inform and not influence, our next step involves an interactive component so the reader can see the impact of how undecided voters can change the outcome of state elections and ultimately, the electoral college.

### The Findings
_coming soon_

