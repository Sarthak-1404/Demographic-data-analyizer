import pandas as pd

def calculate_demographic_data():
    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts()

    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = df[higher_education & (df['salary'] == '>50K')]
    lower_education_rich = df[~higher_education & (df['salary'] == '>50K')]

    percentage_higher_education_rich = (higher_education_rich.shape[0] / higher_education.sum()) * 100
    percentage_lower_education_rich = (lower_education_rich.shape[0] / (~higher_education).sum()) * 100

    min_work_hours = df['hours-per-week'].min()

    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

    country_earnings = df[df['salary'] == '>50K'].groupby('native-country').size()
    country_totals = df.groupby('native-country').size()
    highest_earning_country = (country_earnings / country_totals).idxmax()
    highest_earning_country_percentage = (country_earnings / country_totals).max() * 100

    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_earners['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'percentage_higher_education_rich': round(percentage_higher_education_rich, 1),
        'percentage_lower_education_rich': round(percentage_lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }
