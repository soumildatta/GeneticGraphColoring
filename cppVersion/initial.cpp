#include <iostream>
using std::cout;
using std::endl;
#include <cstdlib>
using std::rand;

#define n 20
#define index uint

int graph[n][n];
auto maxNumColors{0u};

void createGraph()
{
    // Populate with random numbers
    for (auto i{0u}; i < n; ++i)
    {
        for (auto j{i}; j < n; ++j)
        {   
            if(j == i)
            {
                graph[i][j] = 0;
                continue;
            }
            auto genInt = rand() % 2;
            graph[i][j] = genInt;
            graph[j][i] = genInt; 
        }
    }
}

void printGraph()
{
    cout << "Graph:" << endl;
    for (auto i{0u}; i < n; ++i)
    {
        for (auto j{0u}; j < n; ++j)
            cout << graph[i][j] << " ";
        cout << endl;
    }
}

void getMaxColors()
{
    for (auto i{0u}; i < n; ++i)
    {
        auto rowsum{0u};
        for (auto j{0u}; j < n; ++j)
        {
            rowsum += graph[i][j];
        }
        if (rowsum > maxNumColors)
        {
            maxNumColors = rowsum;
        } 
    }
}

int *createChromosome()
{
    // Represents an individual solution
    // Ultimately must contain the answer - minimum num colors of each vertex
    int *individual = (int *)malloc(sizeof(int) * n);
    for (auto i{0u}; i < n; ++i)
    {
        // Assign number of colors randomly
        individual[i] = (rand() % maxNumColors) + 1;
    }
    return individual;
}

int **createPopulation()
{
    int **population = new int *[200];
    for (auto i{0u}; i < 200; ++i)
    {
        population[i] = new int[n];
        for (auto j{0u}; j < n; ++j)
        {
            int *individual = createChromosome();
            population[i][j] = individual[j];
        }
    }

    return population;
}

struct CrossoverChildren
{
    int *child1;
    int *child2;
};

void printChromosome(int *chromosome)
{
    for (auto i{0u}; i < n; ++i)
    {
        cout << chromosome[i] << " ";
    }
    cout << endl;
}

CrossoverChildren twoPointCross(int *parent1, int *parent2)
{
    CrossoverChildren children;
    children.child1 = parent1;
    children.child2 = parent2;

    // Select first split point
    // 2 2 2 2 2
    index firstPoint = 1 + (rand() % (n - 3));
    // Select second split point
    index secondPoint = (rand() % (n - firstPoint - 1)) + firstPoint + 1;

    cout << firstPoint << " " << secondPoint << endl;

    cout << "parent1: ";
    // printChromosome(parent1);
    cout << "parent2: ";
    // printChromosome(parent2);

    int *child1 = (int *)malloc(n * sizeof(int));
    int *child2 = (int *)malloc(n * sizeof(int));

    // 3 loops for 3 parts of the parent individual
    for (auto i{0u}; i < firstPoint; ++i)
    {
        // cout << parent1[i] << " ";
        child1[i] = parent1[i];
        child2[i] = parent2[i];
    }
    cout << endl;
    for (auto i{firstPoint}; i < secondPoint; ++i)
    {
        // cout << parent1[i] << " ";
        child1[i] = parent2[i];
        child2[i] = parent1[i];
    }
    cout << endl;
    for (auto i{secondPoint}; i < n; ++i)
    {
        // cout << parent1[i] << " ";
        child1[i] = parent1[i];
        child2[i] = parent2[i];
    }

    cout << "After crossover" << endl;
    cout << "child1: ";
    // printChromosome(child1);
    cout << "child2: ";
    // printChromosome(child2);

    return children;
}

void mutation()
{

}

int main(int argc, char *argv[])
{
    srand((unsigned int)time(NULL));

    // Initialize important info
    createGraph();
    getMaxColors();
    printGraph();

    CrossoverChildren result = twoPointCross(createChromosome(), createChromosome());

    // for (auto i{0u}; i < n; ++i)
    // {
    //     cout << result.child1[i] << endl;
    // }

    // cout << maxNumColors << endl;
    return 0;
}
