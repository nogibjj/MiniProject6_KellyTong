"""
Transforms and Loads data into Azure Databricks
"""
import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


# load the csv file and insert into databricks
def load(dataset="data/grad-students.csv", dataset2="data/all-ages.csv"):
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
        # c.execute("DROP TABLE IF EXISTS grad-studentsDB")
        c.execute("SHOW TABLES FROM default LIKE 'serve*'")
        result = c.fetchall()
        # takes too long so not dropping anymore
        # c.execute("DROP TABLE IF EXISTS all-agesDB")
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS grad-studentsDB (
                    major string,
                    major_category string,
                    grad_total int,
                    grad_samples_size int,
                    Grad_employed int,
                    Grad_unemployed int,
                    Grad_median int,
                    Nongrad_total int
                )
            """
            )
            # insert
            for _, row in df.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO grad-studentsDB VALUES {convert}")
        c.execute("SHOW TABLES FROM default LIKE 'event*'")
        result = c.fetchall()
        # c.execute("DROP TABLE IF EXISTS all-agesDB")
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS all-agesDB (
                    Major string,
                    Major_category string,
                    Total int,
                    Unemployed int,
                    Median int
                )
                """
            )
            for _, row in df2.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO EventTimesDB VALUES {convert}")
        c.close()

    return "success"
