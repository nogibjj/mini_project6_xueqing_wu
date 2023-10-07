"""
Transforms and Loads data into the local SQLite3 database
"""
import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


# load the csv file and insert into databricks
def load(dataset="data/split1.csv", dataset2="data/split2.csv"):
    """Transforms and Loads data into the local SQLite3 database"""
    df = pd.read_csv(dataset, delimiter=",", skiprows=1)
    df2 = pd.read_csv(dataset2, delimiter=",", skiprows=1)
    load_dotenv()
    server_h = os.getenv("SEVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    print(server_h, access_token, http_path)
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        # INSERT TAKES TOO LONG
        # c.execute("DROP TABLE IF EXISTS Birth")
        c.execute("SHOW TABLES FROM default LIKE 'birth1'")
        result = c.fetchall()
        # takes too long so not dropping anymore
        # c.execute("DROP TABLE IF EXISTS Birth1")
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS Birth1 (
                    id int,
                    Year int,
                    Month int
                )
            """
            )
            # insert
            for _, row in df.iterrows():
                convert = (_,) + tuple(row)  # add the id to the row
                c.execute(f"INSERT INTO Birth1 VALUES {convert}")
        c.execute("SHOW TABLES FROM default LIKE 'Birth2'")
        result = c.fetchall()
        # c.execute("DROP TABLE IF EXISTS Birth2")
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS Birth2 (
                    id int,
                    Day_Of_Month int,
                    Day_Of_Week int,
                    Births int
                )
                """
            )
            for _, row in df2.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO Birth2 VALUES {convert}")
        c.close()

    return "success"
