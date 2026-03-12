from neo4j import GraphDatabase

from config.settings import settings


class Neo4jConnection:
    def __init__(self) -> None:
        self.uri = settings.NEO4J_URI
        self.user = settings.NEO4J_USER
        self.password = settings.NEO4J_PASSWORD

        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def close(self) -> None:
        self.driver.close()

    def query(self, cypher, parameters=None) -> None:
        with self.driver.session() as session:
            return session.run(cypher, parameters or {}).data()
