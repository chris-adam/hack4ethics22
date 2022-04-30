import datetime
import pandas as pd
from py2neo import Graph


def get_all_products(country_name: str):
    """
    Returns all products from the database
    """
    user      = "neo4j"
    passw     = "07xLgl5sy7uUazqtWh1QvuRHSTIkkUZ_kMz5Hqg8Twc"
    uri       = "neo4j+s://2abbd1fc.databases.neo4j.io"

    graph = Graph(uri, auth=(user, passw))
    query = f"""
    MATCH (cy:Country)--(pr:Product)
    WHERE cy.CountryName = '{country_name}'
    AND pr.ProductName CONTAINS 'Bases'
    RETURN pr.ProductName
    """
    return graph.run(query).to_data_frame().to_string()


class Product():

    def __init__(self, product_name: str, decision: datetime.date, expiration_date: datetime.date):
        port      = "7687"
        user      = "neo4j"
        passw     = "07xLgl5sy7uUazqtWh1QvuRHSTIkkUZ_kMz5Hqg8Twc"
        db_name   = "neo4j"
        uri       = "neo4j+s://2abbd1fc.databases.neo4j.io"

        graph = Graph(uri, auth=(user, passw))
        query = """
        MATCH (w:Winery)-[:FROM_PROVENCE]->(p:Province)-[:PROVINCE_COUNTRY]->(c:Country)
        RETURN c.name AS Country, count(DISTINCT w) AS totalNrWineries
        ORDER BY totalNrWineries DESC LIMIT 10
        """
        graph.run(query).to_data_frame()

        self._product_name = product_name
        self._decision = decision
        self._expiration_date = expiration_date

    @property
    def product_name(self):
        return self._product_name

    @property
    def decision(self):
        return self._decision

    @property
    def expiration_date(self):
        return self._expiration_date