#include <iostream>
#include <fstream>

using namespace std;

int *split_nums (string s, int num_count) {
    int *nums = new int[num_count];
    int idx = 0;
    size_t position = 0;
    string token;
    while ((position = s.find(' ')) != string::npos) {
        nums[idx] = stoi(s.substr(0, position));
        s.erase(0, position + 1);
        ++idx;
    }
    nums[idx] = stoi(s);

    return nums;
}

void print_data (int ***graphs, int *vertex_counts, int graph_count) {
    for (int i = 0; i < graph_count; i++) {
        cout << "Graph " << i + 1 << ":" << endl;
        for (int j = 0; j < vertex_counts[i]; j++) {
            for (int k = 0; k < vertex_counts[i]; k++) {
                cout << graphs[i][j][k] << " ";
            }
            cout << endl;
        }
    }
}

void read_data (string filename, int ***&graphs, int *&vertex_counts, int &graph_count) {
    ifstream file;
    file.open(filename);
    if (!file.is_open()) {
        cout << "Error: file not found" << endl;
        return;
    }
    string line;
    getline(file, line);
    graph_count = stoi(line);
    graphs = new int**[graph_count];
    vertex_counts = new int[graph_count];
    for (int i = 0; i < graph_count; i++) {
        getline(file, line);
        vertex_counts[i] = stoi(line);
        graphs[i] = new int*[vertex_counts[i]];
        for (int j = 0; j < vertex_counts[i]; j++) {
            getline(file, line);
            graphs[i][j] = split_nums(line, vertex_counts[i]);
        }
        getline(file, line);
    }
    file.close();
}

int calculate_size (int **graph, int vertex_count) {
    int size = 0;
    for (int i = 0; i < vertex_count - 1; i++) {
        for (int j = i + 1; j < vertex_count; j++) {
            if (graph[i][j] != 0) {
                ++size;
            }
        }
    }
    return size;
}

int main () {
    int ***graphs, *vertex_counts, graph_count;
    read_data("sample_data.txt", graphs, vertex_counts, graph_count);

    for (int i = 0; i < graph_count; i++) {
        int graph_size = calculate_size(graphs[i], vertex_counts[i]);
        cout << "Graph " << i + 1 << endl;
        cout << " -> size: " << graph_size << endl;
    }

    for (int i = 0; i < graph_count; i++) {
        for (int j = 0; j < vertex_counts[i]; j++) {
            delete[] graphs[i][j];
        }
        delete[] graphs[i];
    }
    delete[] vertex_counts;
    return 0;
}