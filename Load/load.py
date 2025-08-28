import sqlite3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Transformation.transformation import dataTransformation
from Extraction.extraction import extract_data   


def loadToSQLite(dim_candidates, dim_country, dim_tech, dim_seniority, dim_date, fact_candidates, db_path="Transformation/candidates.db"):
    conn = sqlite3.connect(db_path)

    dim_candidates.to_sql("dim_candidates", conn, if_exists="replace", index=False)
    dim_country.to_sql("dim_country", conn, if_exists="replace", index=False)
    dim_tech.to_sql("dim_tech", conn, if_exists="replace", index=False)
    dim_seniority.to_sql("dim_seniority", conn, if_exists="replace", index=False)
    dim_date.to_sql("dim_date", conn, if_exists="replace", index=False)
    fact_candidates.to_sql("fact_candidates", conn, if_exists="replace", index=False)

    conn.close()
    


if __name__ == "__main__":
    try:
        
        df = extract_data()   

        dim_candidates, dim_country, dim_tech, dim_seniority, dim_date, fact_candidates = dataTransformation(df) 
    
        try:
            
            loadToSQLite(dim_candidates, dim_country, dim_tech, dim_seniority, dim_date, fact_candidates)
            print(" Carga completada con éxito en candidates.db")
        except Exception as e:
            print(f"Error en la carga: {e}")

    except Exception as e:
        print(f" Error en la transformación: {e}")
