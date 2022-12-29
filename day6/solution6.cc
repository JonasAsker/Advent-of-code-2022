#include <fstream>
#include <sstream>
#include <iostream>
#include <set>
#include <tuple>
using namespace std;

int main() {
    std::ifstream infile("input20226.txt");
    std::string row;
    int subIndex{0};
    int currentIndex{-1};
    bool marker{false};
    std::getline(infile, row);
    unsigned detectionLength{14};
    while (!marker){
        currentIndex += subIndex + 1;
        std::set<char> currentWord;
        subIndex = 0;
        string current = row.substr(currentIndex, detectionLength);
        for(char& l: current){
            if (!get<1>(currentWord.insert(l))){
                subIndex = max(subIndex, int(current.find(l)));
            }
            else if (currentWord.size() == detectionLength){
                marker = true;
            }
        }
    }
    cout << currentIndex + detectionLength << '\n';
}