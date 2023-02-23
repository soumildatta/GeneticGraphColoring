from random import randint
import numpy as np

n = 1000
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
        unused_colors = n * [True]

        for neighborIndex in range(n):
            if(graph[vertexIndex][neighborIndex] == 1):
                if vertexIndex == neighborIndex:
                    # Let's not consider itself. Skip
                    continue
                else:
                    if neighborIndex in graphColors:
                        color = graphColors[neighborIndex]
                        unused_colors[color] = False
        for color, unused in enumerate(unused_colors):
            if unused:
                graphColors[vertexIndex] = color
                break
    return graphColors

def maxColoring(colorDict):
    maxColors = max(colorDict.values())
    return maxColors

def generateTestGraph():
    global graph
    result = {}

    for i in range(n):
        result[i] = []
        for j in range(n):
            if graph[i][j] == 1:
                result[i].append(j)

    return result

def testColoring(graph):
  vertices = sorted((list(graph.keys())))
  colour_graph = {}

  for vertex in vertices:
    unused_colours = len(vertices) * [True]

    for neighbor in graph[vertex]:
      if neighbor in colour_graph:
        colour = colour_graph[neighbor]
        unused_colours[colour] = False
    for colour, unused in enumerate(unused_colours):
        if unused:
            colour_graph[vertex] = colour
            break

  return colour_graph

def iterateTests(n):
    for i in range(n):
        print(f'{i}/{n}')
        createGraph()
        result = doColoring()
        maxColors = maxColoring(result)

        testGraph = generateTestGraph()
        result = testColoring(testGraph)
        maxx = maxColoring(result)

        if maxColors != maxx:
            print('ERROR IN ITERATION', i)
            break

if __name__ == '__main__':
    createGraph()
    # printGraph()
    result = doColoring()
    maxColors = maxColoring(result)
    print(maxColors)

    iterateTests(100)