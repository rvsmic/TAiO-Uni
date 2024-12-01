import random

def generate_random_directed_graph(vertex_count):
    graph = [[0 for _ in range(vertex_count)] for _ in range(vertex_count)]
    for i in range(vertex_count):
        for j in range(vertex_count):
            if i != j:
                graph[i][j] = random.choice([0, 1])
    return graph

def write_graph_to_file(graphs, file_path):
    with open(file_path, 'w') as file:
        file.write(f"{len(graphs)}\n")
        for graph in graphs:
            file.write(f"{len(graph)}\n")
            for row in graph:
                file.write(' '.join(map(str, row)) + '\n')
            file.write('\n')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python generate_tests.py <number_of_graphs> <number_of_vertices>")
        sys.exit(1)
    
    number_of_graphs = int(sys.argv[1])
    number_of_vertices = int(sys.argv[2])
    
    graphs = [generate_random_directed_graph(number_of_vertices) for _ in range(number_of_graphs)]
    write_graph_to_file(graphs, 'test_graphs.txt')
    print(f"Generated {number_of_graphs} random directed graphs with {number_of_vertices} vertices each, saved to 'test_graphs.txt'")
