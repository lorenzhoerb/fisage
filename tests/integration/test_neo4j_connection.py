import pytest
from graph.connection import Neo4jConnection


@pytest.fixture(scope="module")
def neo4j_conn():
    """
    Fixture to provide a Neo4j connection for tests.
    Ensures proper cleanup after tests.
    """
    conn = Neo4jConnection()
    yield conn
    conn.close()


@pytest.fixture(scope="function")
def clean_test_node(neo4j_conn):
    """
    Clean up test nodes before and after each test.
    """
    # Ensure a clean slate
    neo4j_conn.query("MATCH (n:TestNode) DETACH DELETE n")
    yield
    neo4j_conn.query("MATCH (n:TestNode) DETACH DELETE n")


@pytest.mark.integration
def test_create_node(neo4j_conn, clean_test_node):
    """
    Integration test: Create a node and verify it's stored.
    """
    cypher = "CREATE (n:TestNode {name: $name}) RETURN n"
    params = {"name": "pytest_node"}

    result = neo4j_conn.query(cypher, params)
    assert len(result) == 1
    assert result[0]["n"]["name"] == "pytest_node"


@pytest.mark.integration
def test_query_node(neo4j_conn, clean_test_node):
    """
    Integration test: Query an existing node.
    """
    # Insert node
    neo4j_conn.query("CREATE (n:TestNode {name: $name})", {"name": "query_test"})

    # Query node
    result = neo4j_conn.query(
        "MATCH (n:TestNode {name: $name}) RETURN n", {"name": "query_test"}
    )
    assert len(result) == 1
    assert result[0]["n"]["name"] == "query_test"
