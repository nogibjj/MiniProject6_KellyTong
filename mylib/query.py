"""Query the database from a db connection to Azure Databricks"""
import os
from databricks import sql
from dotenv import load_dotenv




def general_query(query):
    """runs a query a user inputs"""

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
        c.execute(query)
        result = c.fetchall()
    c.close()
    log_query(f"{query}", result)
