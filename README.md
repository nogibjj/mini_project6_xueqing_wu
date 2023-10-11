[![CI](https://github.com/nogibjj/mini_project6_xueqing_wu/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/mini_project6_xueqing_wu/actions/workflows/cicd.yml)

## Purpose
The goal of this project is to create a database and query the data on the cloud using Azure Databricks. Create data pipelin (ETL) and write query (including join, aggregation, and sorting).

Dataset source: Birth data from github (https://github.com/fivethirtyeight/data)

Birth data: https://github.com/fivethirtyeight/data/blob/master/births/US_births_2000-2014_SSA.csv?raw=true

The data is splitted into 2 datasets by splitting the column in order to join the datasets later

## Items Included
1. external data (birth data, split1 & split2)
1. mylib
    1. extract.py
    1. transform_load.py
    1. query.py
1. main.py, test_main.py

## Steps
1. Find the data on Github
1. Connect Github with Databricks
    1. Connect Azure Databricks with Github with authentication (server hostname, http path, and access token). Those 3 secret variables need to be hidden from the public by adding new repository to secrets and variables
        1. adding server hostname, http path, and access token to .env file
        1. add each repository secrets to secrets and variables on Github
1. Upload data to Databricks
1. ETL process:
    1. Extract: import the data in extract.py 
    1. Transform and load: clean and load the data by creating a database and a table
    1. Query: getting the top 10 days that have the most number of births (using join, aggregate, and sort)
1. Update the Makefile 
1. Update yml file by adding "set up environment variables"

## Workflow
<img width="981" alt="Workflow" src="https://github.com/nogibjj/mini_project6_xueqing_wu/assets/47194238/8075d9ea-c034-4b25-a12b-76f2c982b43d">

## Tests
<img width="952" alt="Test" src="https://github.com/nogibjj/mini_project6_xueqing_wu/assets/47194238/13d3dfc8-a0ca-4540-afef-cfa7f1207bee">

