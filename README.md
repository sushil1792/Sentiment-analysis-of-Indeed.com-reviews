**Overview:**

Indeed.com was founded in 2004 and currently is the highest traffic job website in the United States. It received about 380 million website visits in October 2018. The user on average spends about 6 mins 20 secs and visits 9 pages per visit. Indeed.com currently has more than 4 million employer reviews and it adds more than 55,000 reviews every week.

Employee ratings in employee reviews have become quite crucial for employers since poor rated companies tend to overpay on salaries by 10%. So, undertaken study has two key objectives, first: to improve the way in which ratings are reflected for each employer and second: to add Pros and Cons for each employer so that user can get better insights without reading all the reviews.

Here's the video explaining our analysis:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=2Ay8LZMy-ec
" target="_blank"><img src="http://img.youtube.com/vi/2Ay8LZMy-ec/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>



We selected top 4 US airline companies for our analysis, which collectively hold a market share of about 65%. Employee reviews data of about 10,000 reviews was scraped for these companies from Indeed utilizing beautiful soup in Python. A sentiment rating was generated for each review by using natural language processing techniques. Vader lexicon from the NLTK library was used for these purposes. The sentiment rating was scaled on a range of 1 to 5, and then aggregate rating was generated for every employer.

The analysis showed that many of the employer reviews have differing user and scaled sentiment rating. Extreme examples were found where even though the review content suggested sharply negative sentiment about the company, but the user rating was 5 and vice versa.



To test that this Sentiment Rating which is generated through user reviews- is different than user rating or not we did a 2-sided t-test and found that the difference between the two ratings is statistically significant as the p-value is very small. Also, the null hypothesis was rejected with 95% confidence level.

On the basis of above analysis, we recommend following actions to Indeed.com. Firstly, to add an additional feature highlighting sentiment rating score, along with already existing user-rating for each company. This sentiment rating would be the average of the score generated from each review. Most important advantage would be that this would provide additional metrics of evaluation for the user i.e. prospective employee. This feature would also differentiate Indeed.com against its competitors such as Glassdoor.com or Monsterjobs.com. This feature would also provide enhanced protection against fake reviews.  Secondly, recommendation would be to display, for each company, a list of pros and cons generated from all user reviews of that company (by using term frequency matrix). This feature would help prospective employees to associate with the culture of the company and make the right move.

The underlying objective of implementing these recommendations would be to improve the overall user experience, which will generate web traffic, increase user engagement hence increased duration per visit, and more job ads listing by employer because of the job seeker&#39;s trust in the platform.
