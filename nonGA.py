from random import randint
import numpy as np

n = 40
graph = np.empty([n, n])

def createGraph():
    global graph
    graph = np.random.randint(0, 2, size=(n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
                continue
            graph[i][j] = graph[j][i]

    return graph

def printGraph():
    for row in graph:
        for item in row:
            print(item, end = " ")
        print()

def doColoring():
    global graph
    # Key - index of vertex
    graphColors = {}

    for vertexIndex in range(n):
        unusedColors = n * [True]

        for neighborIndex in range(n):
            if(graph[vertexIndex][neighborIndex] == 1):
                if vertexIndex == neighborIndex:
                    # Let's not consider itself. Skip
                    continue
                else:
                    if neighborIndex in graphColors:
                        color = graphColors[neighborIndex]
                        unusedColors[color] = False
        for color, unused in enumerate(unusedColors):
            if unused:
                graphColors[vertexIndex] = color
                break
    return graphColors

def maxColoring(colorDict):
    maxColors = max(colorDict.values())
    return maxColors

if __name__ == '__main__':
    createGraph()
    # printGraph()
    result = doColoring()
    maxColors = maxColoring(result)
    print(maxColors)