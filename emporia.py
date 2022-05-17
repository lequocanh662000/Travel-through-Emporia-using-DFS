import sys
import numpy
from collections import defaultdict
import math
import os
import random
import re

# This class represents a directed graph
# using adjacency list representation


class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'.
	visited[] keeps track of vertices in current path.
	path[] stores actual vertices and path_index is current
	index in path[]'''

    def printAllPathsUtil(self, u, d, visited, path, result):
        # print(self.graph)
        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If(current vertex is same as destination && pass all vertices), then print
        # current path[]
        if(u == d):
            if(len(path) == self.V):
                result[0] += 1
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path, self.result)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'

    def printAllPaths(self, s, d):

        # Mark all the vertices as not visited
        # plus 2 because cell starts at 2
        visited = [False]*(self.V+2)

        # Create an array to store paths
        path = []

        # result declaration
        self.result = [0]

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path, self.result)
        print(self.result[0])

# Create a Graph from user input


def createGraph():
    ############# Take Matrix from STDIN ###############
    first_multiple_input = input().rstrip().split()

    R = int(first_multiple_input[0])

    C = int(first_multiple_input[1])

    matrix = []
    for _ in range(R):
        matrix.append(list(map(int, input().rstrip().split())))

########################### Tranform Matrix to a directed Graph #######################
    replace = 4
    vertice_total = 2
    for row in range(R):
        for col in range(C):
            if matrix[row][col] == 0:
                matrix[row][col] = replace
                replace += 1
                vertice_total += 1

    #vertice_ignored = R*C - vertice_total
    # print(matrix)
    # print(vertice_total)
###################### convert Matrix -> Graph #########################
    # Declare a graph
    g = Graph(vertice_total)
    for row in range(R):
        for col in range(C):
            if matrix[row][col] == 1 or matrix[row][col] == 3:
                continue
            elif matrix[row][col] == 2:
                # Maybe: vertice '2' next to '3'(haven't considered)
                # not add vertice '1'
                # add up_cell
                if row-1 >= 0 and matrix[row-1][col] != 1:
                    g.addEdge(2, matrix[row-1][col])
                # add down_cell
                if row+1 < R and matrix[row+1][col] != 1:
                    g.addEdge(2, matrix[row+1][col])
                # add right
                if col+1 < C and matrix[row][col+1] != 1:
                    g.addEdge(2, matrix[row][col+1])
                # add left
                if col-1 >= 0 and matrix[row][col-1] != 1:
                    g.addEdge(2, matrix[row][col-1])
            else:
                # Remember not addEdge with vertivces '2' and '1'
                current_vertice = matrix[row][col]
                # add front
                if row-1 >= 0 and matrix[row-1][col] != 2 and matrix[row-1][col] != 1:
                    g.addEdge(current_vertice, matrix[row-1][col])
                # add below
                if row+1 < R and matrix[row+1][col] != 2 and matrix[row+1][col] != 1:
                    g.addEdge(current_vertice, matrix[row+1][col])
                # add right
                if col+1 < C and matrix[row][col+1] != 2 and matrix[row][col+1] != 1:
                    g.addEdge(current_vertice, matrix[row][col+1])
                # add left
                if col-1 >= 0 and matrix[row][col-1] != 2 and matrix[row][col-1] != 1:
                    g.addEdge(current_vertice, matrix[row][col-1])
    # have not done yet
    return g


#######################  MAIN  ############################
s = 2
d = 3
# Create Graph
g = createGraph()
g.printAllPaths(s, d)
