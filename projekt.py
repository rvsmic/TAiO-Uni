import sys
import networkx as nx

def read_file(file_path):
    with open(file_path, 'r') as file:
        graph_count = int(file.readline())
        graphs = [None] * graph_count
        for gr_idx in range(graph_count):
            numbers = [int(x) for x in file.readline().split()]
            if len(numbers) > 1:
                graph_size = graph_count
                graph_count = 1
                graphs = [[[None] * graph_size] * graph_size]
                graphs[gr_idx][0] = numbers
                for row_idx in range(1, graph_size):
                    numbers = [int(x) for x in file.readline().split()]
                    graphs[gr_idx][row_idx] = numbers
                return graphs
            graph_size = numbers[0]
            graphs[gr_idx] = [[None] * graph_size] * graph_size
            for row_idx in range(graph_size):
                numbers = [int(x) for x in file.readline().split()]
                graphs[gr_idx][row_idx] = numbers
            file.readline()
    return graphs

def print_graphs(graphs):
    for g_idx, graph in enumerate(graphs):
        print(f'Graph {g_idx + 1}:')
        for row in graph:
            for cell in row:
                print(cell, end=' ')
            print()
        print()

def calculate_size(graph):
    return sum([sum(row) for row in graph])

def find_max_cycles(graph):
    g = nx.DiGraph()
    for row_idx, row in enumerate(graph):
        for col_idx, cell in enumerate(row):
            if cell == 1:
                g.add_edge(row_idx, col_idx)
    cycles = list(nx.simple_cycles(g))
    max_cycle_len = max([len(cycle) for cycle in cycles]) if cycles else 0
    max_cycles = [cycle for cycle in cycles if len(cycle) == max_cycle_len]
    return max_cycle_len, max_cycles

def s_metric(graph):
    g = nx.DiGraph()
    for row_idx, row in enumerate(graph):
        for col_idx, cell in enumerate(row):
            if cell == 1:
                g.add_edge(row_idx, col_idx)
    return nx.s_metric(g)

def density(graph):
    g = nx.DiGraph()
    for row_idx, row in enumerate(graph):
        for col_idx, cell in enumerate(row):
            if cell == 1:
                g.add_edge(row_idx, col_idx)
    return nx.density(g)

    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python projekt.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    graphs = read_file(file_path)
    print('\n -----------------\n')
    for g_idx, graph in enumerate(graphs):
        print(f'Graph {g_idx + 1}')
        print(f' -> Nodes: {len(graph)}')
        print(f' -> Size: {calculate_size(graph)}')
        print(' -> Density: %5.2f' % density(graph))
        print(' -> S-metric: %5.2f' % s_metric(graph))
        max_cycle_len, max_cycles = find_max_cycles(graph)
        print(f' -> Max cycle length: {max_cycle_len}')
        print(f' -> Max cycle count: {len(max_cycles)}')
        print('\n ----------------- \n')
