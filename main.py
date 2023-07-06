from input import parse_cmd_line, parse_file
from graph import Graph
from algos import *


def main():
    in_file, plot_graph = parse_cmd_line()
    vertices, edges = parse_file(in_file)
    print(f"#E={len(edges)}, #V={len(vertices)}")

    #path 1 = List of consecutive vertices
    #path 2 = List of consecutive edges
    path1, path1_edges = compute_path(vertices, edges)
    print("\n")
    print("PATH FOUND")
    print(path1)

    print("\n")
    print("Total length = " + str(len(path1)))
    print("Total weight = " + str(weight(path1_edges)))

    verify = eliminate_doubles(path1_edges)

    print("Verify length = " + str(len(verify)))

    graph = Graph(vertices, edges)
    #graph1 = Graph(path1, path1_edges)
    if plot_graph:
        graph.plot()
        #graph1.plot()



if __name__ == "__main__":
    main()


