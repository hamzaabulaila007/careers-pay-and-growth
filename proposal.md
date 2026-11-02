# Final Project Proposal — Which Careers Offer the Best Combination of Pay and Growth?

**Hamza Abulaila** — INFO 4617 Web Data Science

## Research Question

For my final project, I want to look into something that I think is actually important for me and
other college students, and that is figuring out which careers are worth pursuing after graduation.
While I understand that most people who choose a career take salaries into account, I feel that this
decision should take into account several more aspects, such as job opportunities and job growth in a
specific profession in the future. I am interested in finding out whether a career that provides high
earnings will also be characterized by many job opportunities, or whether a low salary will not
prevent some professions from being more in demand in the future. The question I will focus on is the
following: **Among 12 occupations that may be interesting to college students, how do median annual
wages correlate with projections of employment and annual employment openings in the United States
for 2025 to 2035?**

To investigate this problem, I plan on looking into careers from different fields, such as
technology, business, marketing, healthcare, and others that may interest me. I think I will find out
that some careers that require special knowledge and skills will be characterized by high wages, but
I believe that some careers with low wages will be associated with many openings or job growth. To be
honest, I would be very surprised if the highest paying careers will be among the best in all other
criteria.

## Data Sources and Method

For my data, I will be using two public sources from the U.S. Bureau of Labor Statistics. First, I'm
gonna take Occupational Employment and Wage Statistics tables, in which median annual wages will be
available for specific occupations. My second source of data will be the Employment Projections
database, which contains important details such as employment estimates, projected growth up to 2035,
annual job openings, and education requirements information. I'll download all tables in Excel or
text format and process them from there. I'll be matching the two datasets via occupation codes in
order to provide reliable comparisons of careers. The source of the data, its name, URL, and date of
collection will be noted for the purpose of data explanation.

I'm then gonna select 12 occupations based on my impression of their importance and relation to
student preparation for entering the workforce. I will collect each occupation's median annual wage,
percentage employment growth projection (from 2025 to 2035), and annual job openings. Education
requirements will also be collected if it is possible, since I suppose that it will be useful
information.

## Scope and Analysis

I will treat each occupation as one record in my dataset, resulting in about 12 records in total. In
order not to complicate my data collection efforts and to keep my project manageable, I will collect
data at national level. Comparing different cities or states is not required by the assignment, and
doing this will add too much complexity and effort to my work. It is also important to note that
wages I collect are indicative for people working in the occupation as a whole, thus I cannot assume
that it reflects what I, as a new graduate, am likely to earn.

Once I collect my data, I will rank occupations according to median wage, projected job growth, and
number of annual openings. My goal is to produce a scatterplot that compares median wage and
projected job growth, as well as a chart that lists occupations according to number of annual
openings. Then I will compare rankings produced above in order to identify which careers perform well
in multiple dimensions, instead of just in one of them.

If there is enough time, I will also want to produce a single composite ranking based on standardized
scores of median wage, job growth, and number of annual openings, each of those factors being equally
weighted in the final ranking. This will increase clarity of my findings since it will allow me to
highlight careers with relative success in terms of pay and opportunities, while making clear that
the ranking is dependent upon how data is scored.

## Ethics and Feasibility

I decided to use publicly available BLS datasets since I want to work with easy and reliable data
without scraping websites that may limit my automated access to the information provided. I will make
sure to comply with relevant data-use restrictions, properly cite BLS as my data source, and link to
the pages I use. Since I will be dealing with occupation-level statistics and not the characteristics
of individual employees, I don't anticipate having to deal with personally identifiable information
such as names, usernames, photographs, and so on. I also want to avoid representing projections about
future job growth as guarantees, due to the volatility of the job market.

One potential problem that might come up when I combine the two datasets is that each dataset may
label or code some occupations differently, making it impossible to match some careers. In that case,
I'll double check the occupation codes and delete the records that I cannot be confident enough in
matching. In case combining the two datasets becomes too complicated for me to accomplish, I will
reduce my sample to 8 occupations, or concentrate on comparing wages and only use one dataset. It is
more important for me to finish a small but reliable project than to force together incompatible
datasets.

In my first retrieval, I downloaded the BLS May 2025 featured wage tables from
<https://www.bls.gov/oes/2025/may/featured_data.htm>. The table I downloaded stated that the annual
mean wage is $69,770 across all occupations. I managed to download the page, but I have to verify the
HTTP status code using my own logs before submission.

All in all, I chose this project in order to find out more about the different career paths that I
might follow and base my knowledge on facts rather than assumptions about good career choices.
Hopefully, this project will be helpful not only to me but to other students as well in making better
decisions about their future.
