#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

vector<vector<int>> mapBuilder() {
    std::ifstream infile("input202212.txt");
    std::string row;
    vector<vector<int>> heightMap;
    vector<int> heightRow;
    int rowNum{0};
    int colNum{0};
    vector<int> startPos{0,0};
    vector<int> endPos{0,0};
    while (std::getline(infile, row)){
        colNum = 0;
        for (char height : row){
            if (height == 'S'){
                startPos[0] = rowNum;
                startPos[1] = colNum;
                height = 'a';
            }
            else if (height == 'E'){
                endPos[0] = rowNum;
                endPos[1] = colNum;
                height = 'z';
            }
            int heightInt{height};
            heightRow.push_back(heightInt);
            colNum ++;
        }
        rowNum ++;
        heightMap.push_back(heightRow);
        heightRow.clear();
    }
    heightMap.push_back(startPos);
    heightMap.push_back(endPos);
    return heightMap;
}


vector<vector<int>> getNeighbors(vector<vector<int>> const&  grid, vector<int> pos){
    vector <vector<int>> directions {{1,0}, {-1,0}, {0,1}, {0,-1}};
    vector<vector<int>> neighbors;
    for (vector<int> direction: directions){
        vector<int> next {pos[0] + direction[0], pos[1] + direction[1]};
        try{
            grid.at(next[0]);
            grid[next[0]].at(next[1]);
        }
        catch (std::out_of_range const& exc) {
            continue;
        }
        if (grid[next[0]][next[1]] == grid[pos[0]][pos[1]] ||
            grid[next[0]][next[1]] >= grid[pos[0]][pos[1]] - 1){
            neighbors.push_back(next);
        }
    }
    return neighbors;
}


int breadthFirstSearchAlgo(vector< vector<int> > grid, vector<int> startPos, vector<int> endPos){
    queue<vector<int>> frontier;
    frontier.push(startPos);
    map<vector<int>, vector<int>> cameFrom;
    cameFrom[startPos] = startPos; // problem?
    vector<int> current{0,0};
    // creates a map representing the shortest path from the 
    // start to all other nodes.
    while (!frontier.empty()){
       current = frontier.front();
       if (grid[current[0]][current[1]] == int('a')){
            break;
       }
       frontier.pop();
       vector<vector<int>> neighbors{getNeighbors(grid, current)};
       //cout << neighbors.size()<< endl;
       for (vector<int> next : neighbors){
            if (cameFrom.find(next) == cameFrom.end()){
                frontier.push(next);
                cameFrom[next] = current;
                }
       }  
    }
    // go backwards from the end node to find how long the 
    // shortest path is.
    int steps{0};
    cout << current[0] << " " << current[1] << endl;
    cout << grid[current[0]][current[1]] << endl;
    while (current != startPos){
        steps++;
        current = cameFrom[current];
    }
    return steps;
}


int main(){
    vector<vector<int>> heightGrid {mapBuilder()};
    vector<int> startPos {heightGrid[heightGrid.size() - 2]};
    vector<int> endPos {heightGrid[heightGrid.size() - 1]};
    cout << breadthFirstSearchAlgo(heightGrid, endPos, startPos) << endl;
}