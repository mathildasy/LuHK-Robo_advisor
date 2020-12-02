# README

## 1 Introduction

To deal with the problem of clients’ being unable to subscribe iBond, our LuHK Robo-Advisor gives clients investment suggestions to help them allocate their money. Since user data is not available, we apply the mock data method. After that, we use CART to get a parameter which represents the user’s risk-return preference. 

 

In the fund-of-fund portfolio management part, we use technical analysis to capture risk-return features of each fund. Classical standards we use include: Sharpe Ratio, Information Ratio and Jensen Alpha. Besides, we construct another risk-return indicator by using the fund manager and company’s information. 

 

After the feature of each fund is captured, we add market conditions to our analysis. We collect data on each fund’s benchmark index, CPI, PPI, etc. Then, we use strategic & tactic asset allocation methods to decide the optimal weight of each asset category. 

 

An overall consideration of asset allocation and each fund’s risk-return characteristic can now give a ranking to the funds. We select the top 6 funds, use the user parameter to detect each fund’s weight, and advise the fund-of-fund portfolio to help them make investment decisions.



## Data

## 2.1 User Data

See `customerData.csv`

### 2.1.1 User Portrait

Financial platform can easily get various information from the clients. It's feasible for us to consider, and actually, list them in the form of a table. Generally, we separate them into four parts:

(1) registered information,
which includes name, contact details, demographic data (e.g. gender, birth date, nationality, national ID number/passport) and basic financial (background) information. These are obtained when the client register in the platform;

(2) risk preference questionnaire,
which can include more detailed personal demographic information (e.g. educational level, job) and financial (background) information (e.g. individual/family income level, debt situation, scale of wealth available for investment), plus that personal investing mode/experience level and risk preference/tolerance. That is often asked under a detailed specific scene and is able to intuitively reveal the client's preference. Usually the risk preference questionnaires are designed in vivid versions and are finally able to give a rough and concise evaluation of the risk preference level (e.g. conservative, robust, balanced, growing, aggressive) to better guide the clients doing their investment;

(3) interaction records,
which can be categorized by long-term/short-term performance, behavior/transaction information. Behavior information consists of records of app using, such as searching/browsing/visiting/favorite records(content, staying time, clicking frequency) and app using mode(active location/time/section). Transaction information consists of the detailed records of investment, redemption and transferring;

(4) outside information,
which is the information the platform obtain outside the app. Platform can possibly find resources like credit report, past transaction records and preference captured by other agencies.

Since the data of the last two terms are difficult to mock, and our method mainly relies on the risk preference parameter, which can be related only to the first two terms, we merely mock the data from the registered information and risk preference questionnaire.



### 2.1.2 Dimension Design

To determine which set of dimensions to select as our data, we design a questionnaire. It mainly covers detailed demographic information, financial situation and risky choices. The questionnaire is attached in the following lines:

01、Name
02、Gender
	A、Male
	B、Female
03、Hometown/Country
04、Age	
	A、<18
	B、19——25
	C、26——51
	D、51——64
	E、>64
05、Educational Level	
	A、Junior high school and below
	B、Senior high
	C、Junior college
	D、Undergraduate
	E、Master and above
06、Income (HKD/year)	
	A、<5w
	B、5——20w
	C、21——50w
	D、51——100w
	E、>100w
07、Investing Experience (1——5、no——rich)	
	A、1
	B、2
	C、3
	D、4
	E、5
08、Longest Acceptable Investing Period	
	A、<1y
	B、1——3y
	C、3——8y
	D、>8y
	E、No Specific Requirement
09、Maximum Acceptable Drawdown	
	A、<1%
	B、<5%
	C、<10%
	D、<40%
	E、>40%
10、Debt Situation	
	A、Absolutely no
	B、Only small amount
	C、Short-term credit debts (e.g. credit card installment and consumer credit)
	D、Long-term debts (e.g. mortgages and car loans)
	E、Other Personal Debts
11、Risk Preference (prefer which kind of uncertain return)	
	A、100% * 1k
	B、50% * 5w
	C、25% * 50w
	D、10% * 100w
	E、5% * 500w
12、Investing Attitude	
	A、Do not expect any investing risk
	B、Strongly risk averse, expect secure principal, regardless of low return rate
	C、Relatively conservative, but willing to take small amount of risk
	D、Risk-taking, willing to take some loss in principal
	E、Expect high return and growth rate, willing to take great loss in principal

They can be simply represented by the following list, each of them corresponds to a word or a number between 1 and 5:
Name, Gender, Hometown, Age, Education, Income, Experience, Period, Drawdown, Debt, Risk, Attitude.



### 2.1.3 Mocking Process

We post the questionnaire and (due to time and resource limit) get nearly 20 real samples that is suitable for the target group with generally risk averse preference.

One simple method to mock the required data is to randomly generate the first few factors that shall have little correlation with each other (i.e. name, gender), hometown, age and educational level. For other factors, to each one we assume that it is absolutely determined by some or all of the previous factors, represented in linear expressions. Therefore, this sequence of factors can be arranged in a layer-by-layer order. The next layer relies on the layers before. In each layer, we test and adjust the coefficients of each related factor in the linear expression according to those only real samples we have. Finally, by classification, we determine the corresponding score level.

Another method is to put random normal disturbing into the small initial data set, which maintains the general characteristics of the real data but magnifies the scale of the data set. We add a random variable with normal distribution in the range of -2 to 2 to each of the factors of the initial set of data.

For the three kinds of data in our mocking database, the initial real data set is the least in amount and the method of linear correlation takes about 30% of the whole data set, the method of random normal disturbing takes about 70% of the whole data set. Generally, the data set still holds the characteristic of risk averse and can be used for our further analyzing simulation.