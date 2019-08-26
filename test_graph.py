from graph import EntityResolutionGraph
import networkx as nx


def test_no_connections():
    test_entity_1 = {
        'comm_registered_entity': "Test1",
        'registered_agent': None,
        'owner': "Test1"
    }
    test_entity_2 = {
        'comm_registered_entity': "Test2",
        'registered_agent': None,
        'owner': "Test2"
    }
    test_data = [test_entity_1, test_entity_2]
    graph = EntityResolutionGraph(name='test-graph', data=test_data)

    assert nx.number_of_nodes(graph.nx_graph) == 2
    assert nx.number_of_edges(graph.nx_graph) == 0
    assert nx.number_connected_components(graph.nx_graph) == 2


def test_all_connections():
    pass


def test_all_connections_different_elements():
    pass


def test_one_connection():
    pass
