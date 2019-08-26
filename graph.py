import json
import networkx as nx
from networkx.readwrite import json_graph
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt
import pydot
import random
import warnings

warnings.filterwarnings("ignore", category=UserWarning)


class EntityResolutionGraph():
    def __init__(self, name, data):
        entity_links = self.generate_node_links(data)
        node_link_data = {'nodes': data, 'links': entity_links}

        self.name = name
        self.nx_graph = json_graph.node_link_graph(node_link_data)

    def generate_node_links(self, entity_data):
        comm_registered_agents = {}
        links_set = set()

        for index, entity in enumerate(entity_data):
            # TODO: fix data to be comm_registered_agent!
            cra = entity['comm_registered_entity']
            if cra in comm_registered_agents:
                associates = comm_registered_agents[cra]
                links_set = self.find_entity_links(
                    links_set,
                    index,
                    associates)
                associates = associates.append(index)
            elif cra is not None:
                comm_registered_agents[cra] = [index]

        return [{'source': link[0], 'target': link[1]} for link in links_set]

    def find_entity_links(self, links, index, associates):
        return links.union({(associate, index) for associate in associates})
