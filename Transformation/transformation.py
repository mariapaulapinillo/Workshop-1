import pandas as pd 

def dataTransformation(df):
    
    
    df["hired"] = ((df["Code Challenge Score"] >= 7) & 
                   (df["Technical Interview Score"] >= 7)).astype(int)
    
    
    dim_candidates = df[["First Name", "Last Name", "Email"]].drop_duplicates().reset_index(drop=True)
    dim_candidates["candidate_id"] = dim_candidates.index + 1

    dim_country = df[["Country"]].drop_duplicates().reset_index(drop=True)
    dim_country["country_id"] = dim_country.index + 1

    dim_tech = df[["Technology"]].drop_duplicates().reset_index(drop=True)
    dim_tech["technology_id"] = dim_tech.index + 1
    

    dim_seniority = df[["Seniority"]].drop_duplicates().reset_index(drop=True)
    dim_seniority["seniority_id"] = dim_seniority.index + 1
    
    
    df["Application Date"] = pd.to_datetime(df["Application Date"], dayfirst=True, errors="coerce")
    dim_date = df[["Application Date"]].drop_duplicates().reset_index(drop=True)
    dim_date["date_id"] = dim_date.index + 1
    dim_date["year"] = dim_date["Application Date"].dt.year
    dim_date["month"] = dim_date["Application Date"].dt.month
    dim_date["day"] = dim_date["Application Date"].dt.day
    

    fact_candidates = df.merge(dim_candidates, on=["First Name", "Last Name", "Email"]) \
                        .merge(dim_country, on="Country") \
                        .merge(dim_tech, on="Technology") \
                        .merge(dim_seniority, on="Seniority") \
                        .merge(dim_date, on="Application Date")

    fact_candidates = fact_candidates[[
        "candidate_id", "country_id", "date_id", "technology_id", "seniority_id",
        "YOE", "Code Challenge Score", "Technical Interview Score", "hired"
    ]].reset_index(drop=True)

    fact_candidates["factcandidates_id"] = fact_candidates.index + 1


    return dim_candidates, dim_country, dim_tech, dim_seniority, dim_date, fact_candidates
    





