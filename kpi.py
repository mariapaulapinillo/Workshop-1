import pandas as pd
import sqlite3

def HiresByTechnology(dbName):
    try:
        conn = sqlite3.connect(dbName)
        
        query = '''
            SELECT t.Technology AS technology,
            COUNT(*) AS total_hires
            FROM fact_candidates f
            JOIN dim_tech t
            ON f.technology_id = t.technology_id
            WHERE f.hired = 1
            GROUP BY t.Technology
            ORDER BY total_hires DESC;

        '''
        
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        return df
    
    except Exception as e:
        return str(e)
    

def HiresByYear(dbName):
    try:
        conn = sqlite3.connect(dbName)
        
        query = '''
            SELECT d.year,
            COUNT(*) AS total_hires
            FROM fact_candidates f
            JOIN dim_date d
            ON f.date_id = d.date_id
            WHERE f.hired = 1
            GROUP BY d.year
            ORDER BY d.year;
        '''
        
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        return df
    
    except Exception as e:
        return str(e)
    
def HiresBySeniority(dbName):
    try:
        conn = sqlite3.connect(dbName)
        
        query = '''
            SELECT s.Seniority AS seniority,
            COUNT(*) AS total_hires
            FROM fact_candidates f
            JOIN dim_seniority s
            ON f.seniority_id = s.seniority_id
            WHERE f.hired = 1
            GROUP BY s.Seniority
            ORDER BY total_hires DESC;

        '''
        
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        return df
    
    except Exception as e:
        return str(e)

def HiresByCountryOverYears(dbName):
    try:
        conn = sqlite3.connect(dbName)
        
        query = '''
            SELECT c.Country AS country,
            d.year,
            COUNT(*) AS total_hires
            FROM fact_candidates f
            JOIN dim_country c
            ON f.country_id = c.country_id
            JOIN dim_date d
            ON f.date_id = d.date_id
            WHERE f.hired = 1
            AND c.Country IN ('United States of America', 'Brazil', 'Colombia', 'Ecuador')
            GROUP BY c.Country, d.year
            ORDER BY c.Country, d.year;

        '''
        
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        return df
    
    except Exception as e:
        return str(e)

def HiresByExperienceRange(dbName):
    try:
        conn = sqlite3.connect(dbName)
        
        query = '''
            SELECT 
                CASE
                    WHEN f.yoe BETWEEN 0 AND 2 THEN 'Years (0-2)'
                    WHEN f.yoe BETWEEN 3 AND 5 THEN 'Years (3-5)'
                    WHEN f.yoe BETWEEN 6 AND 10 THEN 'Years (6-10)'
                    ELSE 'Years (10+)' 
                END AS experience_range,
                COUNT(*) AS total_hires
            FROM fact_candidates f
            WHERE f.hired = 1
            GROUP BY experience_range
            ORDER BY total_hires DESC
        '''
        
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        return df
    
    except Exception as e:
        return str(e)
    
def AverageScores(dbName):
    try:
        conn = sqlite3.connect(dbName)
        
        query = '''
            SELECT 
            ROUND(AVG(f."Code Challenge Score"), 2) AS avg_code_score,
            ROUND(AVG(f."Technical Interview Score"), 2) AS avg_interview_score
            FROM fact_candidates f;

        '''
        
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    
    except Exception as e:
        return str(e)


