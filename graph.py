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
        reg_agents = {}
        owners = {}
        links_set = set()

        for index, entity in enumerate(entity_data):
            cra = entity['comm_registered_agent']
            reg_agent = entity['registered_agent']
            owner = entity['owner']

            if cra in comm_registered_agents:
                links = comm_registered_agents[cra]
                links_set = self.find_entity_links(
                    links_set,
                    index,
                    links)
                links = links.append(index)
            elif cra is not None:
                comm_registered_agents[cra] = [index]

            if reg_agent in reg_agents:
                links = reg_agents[reg_agent]
                links_set = self.find_entity_links(
                    links_set,
                    index,
                    links)
                links = links.append(index)
            elif reg_agent is not None:
                reg_agents[reg_agent] = [index]

            if owner in owners:
                links = owners[owner]
                links_set = self.find_entity_links(
                    links_set,
                    index,
                    links)
                links = links.append(index)
            elif owner is not None:
                owners[owner] = [index]

        return [{'source': link[0], 'target': link[1]} for link in links_set]

    def find_entity_links(self, set, index, links):
        return set.union({(links, index) for links in links})

    def draw_graph(self):
        graph = self.nx_graph
        print(f"Nodes: {nx.number_of_nodes(graph)}\n"
              f"Edges: {nx.number_of_edges(graph)}\n"
              f"Connected Components: {nx.number_connected_components(graph)}")

        print(f"Saving graph to {self.name}.png...")
        plt.figure(1, figsize=(8, 8))
        conn_comps = nx.connected_component_subgraphs(graph)
        pos = graphviz_layout(graph)
        for g in conn_comps:
            node_color = [random.random()] * nx.number_of_nodes(g)
            nx.draw(g,
                    pos,
                    node_size=50,
                    node_color=node_color,
                    vmin=0.0,
                    vmax=1.0,
                    with_labels=False)

        plt.savefig(self.name)


def main():
    with open('crawler-entity-data.json', 'r') as f:
        data = json.load(f)
    graph = EntityResolutionGraph('entity-resolution-graph', data)
    graph.draw_graph()

if __name__ == '__main__':
    main()
