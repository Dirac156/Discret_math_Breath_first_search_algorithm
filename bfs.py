import time


#define nodes

vertices = {"A" : ["C", "D"], "B" : "E", "Dirac" : {"CS": [1, 2, 3], "LC" : 1}}
visited = []

lst = list(vertices.keys())

def get_edges(visited, vertices, first):
    if (isinstance(vertices, dict)):
        if first in vertices.keys():
            print(f"start at {first}")
            print("===")
            print("===")
            visited.append(first)
            time.sleep(1)
        new_vertices = list(vertices.keys())

    elif (isinstance(vertices, list)):
        new_vertices = vertices

    elif len(vertices) != 0:
        return vertices

    for vertice in new_vertices:
        if vertice not in visited:
            visited.append(vertice)
            print(f"move to {vertice}")
            print("===")
            print("===")
            time.sleep(1)

    if isinstance(vertices, dict):
        for vertice in visited:
            if vertice in new_vertices:
                if isinstance(vertices[vertice], dict):
                    print(vertice)
                    get_edges(visited, vertices[vertice], "")
                elif isinstance(vertices[vertice], list):
                    get_edges(visited, vertices[vertice], "")

                elif isinstance(vertices[vertice], str):
                    if len(vertices[vertice]) != 0:
                        visited.append(vertices[vertice])
                        print(f"move to {vertices[vertice]}")
                        print("===")
                        print("===")
                        time.sleep(1)
                elif isinstance(vertices[vertice], int):
                    visited.append(vertices[vertice])
                    print(f"move to {vertices[vertice]}")
                    print("===")
                    print("===")
                    time.sleep(1)

get_edges(visited, vertices, "A")
print("End")
print("The walk followed is", end=": ")
print(visited)
