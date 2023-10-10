"""
Transforms and Loads data into Azure Databricks
"""
import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


# load the csv file and insert into databricks
def load(dataset="data/grad_students.csv", dataset2="data/all_ages.csv"):
    """Transforms and Loads data into the local databricks database"""
    df = pd.read_csv(dataset, delimiter=",", skiprows=1)
    df2 = pd.read_csv(dataset2, delimiter=",", skiprows=1)
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        # INSERT TAKES TOO LONG
        # c.execute("DROP TABLE IF EXISTS grad_studentsDB")
        c.execute("SHOW TABLES FROM default LIKE 'serve*'")
        result = c.fetchall()
        # takes too long so not dropping anymore
        # c.execute("DROP TABLE IF EXISTS all_agesDB")
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS grad_studentsDB (
                    Major_code int,
                    Major string,
                    Major_category string,
                    Grad_total int,
                    Grad_sample_size int,
                    Grad_employed int,
                    Grad_full_time_year_round int, 
                    Grad_unemployed int,
                    Grad_unemployment_rate int, 
                    Grad_median int,
                    Grad_P25 int,
                    Grad_P75 int, 
                    Nongrad_total int,
                    Nongrad_employed int,
                    Nongrad_full_time_year_round int, 
                    Nongrad_unemployed int, 
                    Nongrad_unemployment_rate int, 
                    Nongrad_median int, 
                    Nongrad_P25 int, 
                    Nongrad_P75 int, 
                    Grad_share int, 
                    Grad_premium int
                )
            """
            )
            # insert
            for _, row in df.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO grad_studentsDB VALUES {convert}")
        c.execute("SHOW TABLES FROM default LIKE 'event*'")
        result = c.fetchall()
        # c.execute("DROP TABLE IF EXISTS all_agesDB")
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS all_agesDB (
                    Major_code int,
                    Major string,
                    Major_category string,
                    Total int,
                    Employed int, 
                    Employed_full_time_year_round int, 
                    Unemployed int,
                    Unemployment_rate int, 
                    Median int, 
                    P25th int, 
                    P75th int
                )
                """
            )
            for _, row in df2.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO all_agesDB VALUES {convert}")
        c.close()

    return "success"
