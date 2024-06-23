import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men_data = df[df['sex'] == 'Male']
    daverage_age_men = men_data['age'].mean()
    average_age_men=round(daverage_age_men,1)

    # What is the percentage of people who have a Bachelor's degree?
    total_count = len(df)
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    
    dpercentage_bachelors = (bachelors_count / total_count) * 100
    percentage_bachelors=round(dpercentage_bachelors,1)

   
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    dhigher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    rich_higher_education = dhigher_education[dhigher_education['salary'] == '>50K']

    total_higher_education = len(dhigher_education)

    rich_count = len(rich_higher_education)

    if total_higher_education > 0:
         higher_education  = (rich_count / total_higher_education) * 100
    else:
          higher_education  = 0.0
   
    le = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    count_le = len(le)

    lower_rich = le[le['salary'] == '>50K']
    count_lower_rich = len(lower_rich)

    if count_le > 0:
         percentage_lower_rich = (count_lower_rich / count_le) * 100
    else:
         percentage_lower_rich = 0.0
         
         
         
    

    # percentage with salary >50K
    higher_education_rich = round(higher_education,1)
    lower_education_rich = round(percentage_lower_rich,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_workers = df[df['hours-per-week'] == min_work_hours]
    num_min_hours_rich = len(min_hours_workers[min_hours_workers['salary'] == '>50K'])
    num_min_workers = len(min_hours_workers)
    if num_min_workers > 0:
        rich_percentage = (num_min_hours_rich / num_min_workers) * 100
    else:
        rich_percentage = 0.0
    
    

    

    # What country has the highest percentage of people that earn >50K?
    country_stats = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)

    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    high_income_india = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_IN_occupation = high_income_india['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
