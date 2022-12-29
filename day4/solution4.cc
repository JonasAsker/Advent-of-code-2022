#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
void task2();


int main() {
    std::ifstream infile("input20224.txt");
    std::string row;
    int overlaps{0};
    vector <int> elves;
    while (std::getline(infile, row)){
        int a{0};
        row += ',';
        for (auto& c: row){
            if (isdigit(c)){
                a = (a * 10) + c - '0';
            }
            else{
                elves.push_back(a);
                a = 0;
            }
        }
        if((elves[0] - elves[2]) * (elves[1] - elves[3]) <= 0){
            overlaps ++;
        }
        elves.clear();
    }
    task2();
}

void task2() {
    std::ifstream infile("input20224.txt");
    std::string row;
    int nonOverlaps {0};
    int overlaps{0};
    int total{0};
    vector <int> elves;
    while (std::getline(infile, row)){
        int a{0};
        row += ',';
        for (auto& c: row){
            if (isdigit(c)){
                a = (a * 10) + c - '0';
            }
            else{
                elves.push_back(a);
                a = 0;
            }
        }
        if(min(elves[0], elves[1]) > max(elves[2], elves[3]) ||
            max(elves[0], elves[1]) < min(elves[2], elves[3])){
            nonOverlaps ++;
        }
        total ++;
        elves.clear();
    }
    overlaps = total - nonOverlaps;
    std::cout << overlaps << '\n';
}