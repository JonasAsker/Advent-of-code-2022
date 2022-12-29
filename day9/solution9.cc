#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cmath>
using namespace std;


bool detectNeighbor(vector<int>& pos1, vector<int>& pos2){
    int deltaX = abs(pos1[0]-pos2[0]);
    int deltaY = abs(pos1[1] - pos2[1]);
    if (deltaX > 1 || deltaY > 1){
        return false;
    }
    return true;
}


vector<int> moveHead(vector<int> const& pos, char const& direction){
    map<char, vector<int>> dirs = {{'U', {0,1}}, {'D', {0,-1}}, {'R', {1,0}}, {'L', {-1,0}}};
    vector<int> move{dirs[direction]};
    vector<int> newPos = {pos[0] + move[0], pos[1] + move[1]};
    return newPos;
}


vector<int> moveKnot(vector<int> head, vector<int> tail){
    vector<int> delta = {head[0] - tail[0], head[1] - tail[1]};
    delta = {delta[0] / abs(delta[0]), delta[1] / abs(delta[1])};
    vector<int> newTail = {tail[0] + delta[0], tail[1] + delta[1]};
    return newTail;
}


vector<vector<int>> moveRope(vector<vector<int>>& rope, int ropeLen){
    for (int k{0}; k < ropeLen; k ++){
        if(!detectNeighbor(rope[k], rope[k + 1])){
            rope[k + 1] = moveKnot(rope[k], rope[k + 1]);
        }
    }
    return rope;
}


int solver(vector<char> instrL, vector<int> instrN){
    int ropeLength{10}; // 2 for task1 and 10 for task 2
    vector<vector<int>> rope(ropeLength, {0,0});
    set<vector<int>> uniquePositions;
    for (unsigned i{0}; i < instrL.size(); i++){
        for (int j{0} ; j < instrN[i]; j ++){
            vector<int> newPos = moveHead(rope[0], instrL[i]);
            rope[0] = newPos;
            rope = moveRope(rope, ropeLength - 1);
            uniquePositions.insert(rope[rope.size() - 1]);
            }
        }
    return uniquePositions.size();
}


int main() {
    std::ifstream infile("input20229.txt");
    std::string row;
    char letter;
    int number;
    vector<char> instructionLetters;
    vector<int> instructionNumbers;
    while (infile >> letter >> number){
        instructionLetters.push_back(letter);
        instructionNumbers.push_back(number);
    }
    int answer = solver(instructionLetters, instructionNumbers);
    cout << answer << '\n';
}