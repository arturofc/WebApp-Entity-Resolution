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
    test_entity_1 = {
        'comm_registered_entity': "Test",
        'registered_agent': 'Test',
        'owner': "Test"
    }
    test_entity_2 = {
        'comm_registered_entity': "Test",
        'registered_agent': 'Test',
        'owner': "Test"
    }
    test_data = [test_entity_1, test_entity_2]
    graph = EntityResolutionGraph(name='test-graph', data=test_data)

    assert nx.number_of_nodes(graph.nx_graph) == 2
    assert nx.number_of_edges(graph.nx_graph) == 1
    assert nx.number_connected_components(graph.nx_graph) == 1


def test_all_connections_different_elements():
    test_entity_1 = {
        'comm_registered_entity': "Test",
        'registered_agent': 'Test1',
        'owner': "Test"
    }
    test_entity_2 = {
        'comm_registered_entity': "Test",
        'registered_agent': 'Test',
        'owner': "Test2"
    }
    test_entity_3 = {
        'comm_registered_entity': "Test3",
        'registered_agent': 'Test',
        'owner': "Test"
    }
    test_data = [test_entity_1, test_entity_2, test_entity_3]
    graph = EntityResolutionGraph(name='test-graph', data=test_data)

    assert nx.number_of_nodes(graph.nx_graph) == 3
    assert nx.number_of_edges(graph.nx_graph) == 3
    assert nx.number_connected_components(graph.nx_graph) == 1


def test_connector_node():
    test_entity_1 = {
        'comm_registered_entity': "Test",
        'registered_agent': 'Test1',
        'owner': "Test"
    }
    test_entity_2 = {
        'comm_registered_entity': "Test",
        'registered_agent': 'Test',
        'owner': None
    }
    test_entity_3 = {
        'comm_registered_entity': "Test3",
        'registered_agent': 'Test',
        'owner': None
    }
    test_data = [test_entity_1, test_entity_2, test_entity_3]
    graph = EntityResolutionGraph(name='test-graph', data=test_data)

    assert nx.number_of_nodes(graph.nx_graph) == 3
    assert nx.number_of_edges(graph.nx_graph) == 2
    assert nx.number_connected_components(graph.nx_graph) == 1
