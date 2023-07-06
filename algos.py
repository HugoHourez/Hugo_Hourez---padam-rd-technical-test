import math
from math import *

# The algorithm that computes the path

def compute_path(vertices, edges):
    """

    Parameters
    ----------
    vertices: list of vertices
    edges: list of edges

    Returns
    -------
    path: list of consecutive vertices in the computed path

    """

    # Step 1 : Generate a primal solution
    path, path_edges = generate_path(vertices, edges, 0)

    return path, path_edges


def generate_path(vertices, edges, startID):
    """
    This function generates a first solution to the problem.

    At each vertice, it chooses the next edge prioritizing the unused ones and the heaviest ones.
    If every edge is used, it tries finding the lightest lenght 1 path to another unused edge.
    If not found, it tries going closer and closer to



    Parameters
    ----------
    vertices: list of vertices
    edges: list of edges

    Returns
    -------
    solution: the generated path

    """

    # Keeps track of each used edge
    used_edges = []
    used_edges_count = 0

    # List of consecutive vertices in the generated path
    solution = [startID]
    list_of_edges = []

    total_edge_count = len(edges)

    #No stuck decisions (stage 3)
    no_loop_list = []
    flag = False

    # Loop repeats at each new choice until every edge is crossed
    while used_edges_count < total_edge_count:

        current_vertice = solution[-1]

        # Search every unsused or lightest path
        heaviest_unused_edge = None

        for i in range(len(edges)):

            if edges[i][0] == current_vertice or edges[i][1] == current_vertice:

                # Find heaviest unused edge

                if heaviest_unused_edge == None and edges[i] not in used_edges:
                    heaviest_unused_edge = edges[i]

                # compare to find the heaviest unused edge
                if edges[i] not in used_edges and edges[i][2] > heaviest_unused_edge[2]:
                    heaviest_unused_edge = edges[i]

        # TAKING THE DECISION

        # if unused edge available, take the heaviest one
        if heaviest_unused_edge != None:
            used_edges.append(heaviest_unused_edge)
            used_edges_count += 1
            list_of_edges.append(heaviest_unused_edge)
            if heaviest_unused_edge[0] == current_vertice:
                solution.append(heaviest_unused_edge[1])
            else:
                solution.append(heaviest_unused_edge[0])

            print("Crossed edges : " + str(used_edges_count))

            no_loop_list = []

            continue

        # if not, problems !!!!

        #Approach 1
        #Look in the direct surroundings if there is an unused edge
        #Choose the lightest one

        # Search lightest path that goes to unused edge
        lightest_promising_edge = None

        for i in range(len(edges)):

            if edges[i][0] == current_vertice:

                # Find lightest edge that goes to free edge

                if lightest_promising_edge == None and find_free_edges(edges[i][1], used_edges, edges) == True:
                    lightest_promising_edge = edges[i]

                    #Stop search once a minimal length edge has been found
                    if lightest_promising_edge[2] == 1:
                        break

                # compare to find the lightest edge respecting criteria
                if find_free_edges(edges[i][1], used_edges, edges) == True and edges[i][2] < lightest_promising_edge[2]:
                    lightest_promising_edge = edges[i]

                    # Stop search once a minimal length edge has been found
                    if lightest_promising_edge[2] == 1:
                        break

            #alternative case

            if edges[i][1] == current_vertice:

                if lightest_promising_edge == None and find_free_edges(edges[i][0], used_edges, edges) == True:
                    lightest_promising_edge = edges[i]

                    # Stop search once a minimal length edge has been found
                    if lightest_promising_edge[2] == 1:
                        break

                # compare to find the lightest edge respecting criteria
                if find_free_edges(edges[i][0], used_edges, edges) == True and edges[i][2] < lightest_promising_edge[2]:
                    lightest_promising_edge = edges[i]

                    # Stop search once a minimal length edge has been found
                    if lightest_promising_edge[2] == 1:
                        break


        # TAKING THE DECISION (SECOND TIME)

        # if unused edge available after distance 1, take the lightest one
        if lightest_promising_edge != None:
            list_of_edges.append(lightest_promising_edge)
            if lightest_promising_edge[0] == current_vertice:
                solution.append(lightest_promising_edge[1])
            else:
                solution.append(lightest_promising_edge[0])

            no_loop_list = []
            continue

        #if not : BIGGER PROBLEMS

        # Approach 2 :

        # Lists every possible target points, at which a vertice is unused
        # Goes the vertice that is the closest to one of them

        #STEP 1 : FIND ALL UNUSED EDGES

        unused_edges = []

        for i in range(len(edges)):
            if edges[i] not in used_edges:
                unused_edges.append(edges[i])

        # STEP 2 : FIND CLOSEST TARGET VERTICE

        target = None
        target_dist = 0

        for i in range(len(unused_edges)):
            if target == None:
                target = unused_edges[0][0]
                target_dist = distance(vertices,target,current_vertice)

            if distance(vertices,unused_edges[i][0],current_vertice) < target_dist:
                target = unused_edges[i][0]
                target_dist = distance(vertices,unused_edges[i][0],current_vertice)

            if distance(vertices,unused_edges[i][1],current_vertice) < target_dist and unused_edges[i][1] not in no_loop_list:
                target = unused_edges[i][1]
                target_dist = distance(vertices,unused_edges[i][1],current_vertice)

        #STEP 3 : FIND THE EDGE THAT GOES THE CLOSEST

        closest_edge = None
        closest_dist = 0

        for i in range(len(edges)):

            if edges[i][0] == current_vertice:

                # Find minimal distance edge

                if closest_edge == None and edges[i][1] not in no_loop_list:
                    closest_edge = edges[i]
                    closest_dist = distance(vertices,target,edges[i][1])

                # compare to find the minimal distance to target edge
                if distance(vertices,target,edges[i][1]) < closest_dist and edges[i][1] not in no_loop_list:
                    closest_edge = edges[i]
                    closest_dist = distance(vertices,target,edges[i][1])

            # alternative case

            if edges[i][1] == current_vertice:

                # Find minimal distance edge

                if closest_edge == None and edges[i][0] not in no_loop_list:
                    closest_edge = edges[i]
                    closest_dist = distance(vertices, target, edges[i][0])

                # compare to find the minimal distance to target edge
                if distance(vertices, target, edges[i][0]) < closest_dist and edges[i][0] not in no_loop_list:
                    closest_edge = edges[i]
                    closest_dist = distance(vertices, target, edges[i][0])

        # PICK THE CLOSEST ONE

        if closest_edge != None:

            list_of_edges.append(closest_edge)

            if current_vertice == closest_edge[0]:
                solution.append(closest_edge[1])
            else:
                solution.append(closest_edge[0])

            print("Hard decision :" + str(current_vertice))
            no_loop_list.append(current_vertice)

            continue

        flag = True
        print("No solution found")
        break




    return solution, list_of_edges


def distance(vertices,ID1,ID2):

    return math.sqrt(((vertices[ID1][0]-vertices[ID2][0])**2)+((vertices[ID1][1]-vertices[ID2][1])**2))



def find_free_edges(ID, used_edges, edges):
    """

    Parameters
    ----------
    ID: Vertice at which we are looking for unused edges
    used_edges: List of every used edge
    vertices: list of vertices
    edges: list of edges

    Returns
    -------


    """

    for i in range(len(edges)):
        if edges[i] not in used_edges and edges[i][0] == ID:
            return True
        if edges[i] not in used_edges and edges[i][1] == ID:
            return True

    return False



def weight(path_edges):

    sum = 0
    for i in range(len(path_edges)):
        sum += path_edges[i][2]

    return sum


def eliminate_doubles(original_path_edges):

    path_edges = original_path_edges[:]

    for i in range(len(path_edges)-2):
        for j in range(i+1, len(path_edges)-1):
            if path_edges[i] == path_edges[j]:
                path_edges.pop(i)

    return path_edges