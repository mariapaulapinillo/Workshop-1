import pandas as pd
from kpi import (
    HiresByTechnology,
    HiresByYear,
    HiresBySeniority,
    HiresByCountryOverYears,
    HiresByExperienceRange,
    AverageScores
)

DB_NAME = "Transformation/candidates.db"

def main():
    
    df_tech = HiresByTechnology(DB_NAME)
    print("KPI #1")
    print(df_tech if isinstance(df_tech, str) else df_tech.to_string(index=False))

    
    df_year = HiresByYear(DB_NAME)
    print("KPI #2")
    print(df_year if isinstance(df_year, str) else df_year.to_string(index=False))

    
    df_seniority = HiresBySeniority(DB_NAME)
    print("KPI #3")
    print(df_seniority if isinstance(df_seniority, str) else df_seniority.to_string(index=False))

    
    df_country = HiresByCountryOverYears(DB_NAME)
    print("KPI #4")
    print(df_country if isinstance(df_country, str) else df_country.to_string(index=False))

    
    df_experience = HiresByExperienceRange(DB_NAME)
    print("KPI #5")
    print(df_experience if isinstance(df_experience, str) else df_experience.to_string(index=False))

    
    df_avg_scores = AverageScores(DB_NAME)
    print("KPI #6")
    print(df_avg_scores if isinstance(df_avg_scores, str) else df_avg_scores.to_string(index=False))


if __name__ == "__main__":
    main()

