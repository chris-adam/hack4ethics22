import numpy as np
import pandas as pd
from py2neo import Graph, Node, Relationship
from neo4j import GraphDatabase

# load graph connection instance (https://sandbox.neo4j.com/)
port      = "7687"
user      = "neo4j"
passw     = "07xLgl5sy7uUazqtWh1QvuRHSTIkkUZ_kMz5Hqg8Twc"
db_name   = "neo4j"
uri       = "neo4j+s://2abbd1fc.databases.neo4j.io"

# py2neo instance
graph   = Graph(uri, auth=(user, passw))

# list of files
SAS_url   = "https://datalake28042022.blob.core.windows.net/"
signkey   = "?sv=2020-02-10&st=2022-04-30T13%3A49%3A23Z&se=2022-05-29T13%3A49%3A00Z&sr=d&sp=racwdl&sig=JD%2BAFdAqKPT%2FZaUJad9dA%2FkhbQhzDjhIGEeJwGxPbdk%3D&sdd=1"

come_from_url = SAS_url + "datalake/silver/come_from.csv" + signkey
complete_cleaned_url = SAS_url + "datalake/silver/complete_cleaned.csv" + signkey
date_url = SAS_url + "datalake/silver/date.csv" + signkey
has_product_url = SAS_url + "datalake/silver/has_product.csv" + signkey
located_in_url = SAS_url + "datalake/silver/located_in.csv" + signkey

query = """
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM '"""+complete_cleaned_url+"""' AS line FIELDTERMINATOR ','
MERGE (co:Company {CompanyName:(line.CompanyName)})
"""
graph.run(query)

query = """
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM '"""+date_url+"""' AS line FIELDTERMINATOR ','
MERGE (pr:Product {ProductName:(line.ProductName)})
"""
graph.run(query)

query = """
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM '"""+complete_cleaned_url+"""' AS line FIELDTERMINATOR ','
MERGE (cy:Country {CountryName:(line.CountryName)})
"""
graph.run(query)

query = """
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM '"""+located_in_url+"""' AS line FIELDTERMINATOR ','
MATCH (co:Company {CompanyName:(line.CompanyName)})
MATCH (cy:Country {CountryName:(line.CountryName)})
MERGE (co)-[:LOCATED_IN]->(cy)
"""
graph.run(query)

query = """
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM '"""+has_product_url+"""' AS line FIELDTERMINATOR ','
MATCH (co:Company {CompanyName:(line.CompanyName)})
MATCH (pr:Product {ProductName:(line.ProductName)})
MERGE (co)-[:HAS_PRODUCT]->(pr)
"""
graph.run(query)

query = """
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM '"""+come_from_url+"""' AS line FIELDTERMINATOR ','
MATCH (pr:Product {ProductName:(line.ProductName)})
MATCH (cy:Country {CountryName:(line.CountryName)})
MERGE (pr)-[:COME_FROM]->(cy)
"""
graph.run(query)

