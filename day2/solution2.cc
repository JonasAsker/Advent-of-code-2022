#include <fstream>
#include <string>
#include <sstream>
#include <iostream>
using namespace std;

void task2();

int main() {
    std::ifstream infile("test.txt");
    std::string games;
    int score {0};
    int normA {int('A') - 1};
    int normX {int('X') - 1};
    int multiplier {0};
    int outcome {0};
    while (std::getline(infile, games)){
        std::istringstream iss(games);
        char a, b;
        iss >> a; iss >> b;
        score += (int(b) - normX);
        outcome = (int(a) - normA) - (int(b) - normX);
        if (outcome == -1 || outcome == 2){
            multiplier = 2;
        }
        else if (outcome == 0){
            multiplier = 1;
        }
        score += multiplier * 3;
        multiplier = 0;
    }
    //std::cout << score << '\n';
    task2();
    return 0;
}

void task2(){
    std::ifstream infile("input20222.txt");
    std::string games;
    int score {0};
    int i{0};
    int normA {int('A') - 1};
    int normX {int('X') - 1};
    while (std::getline(infile, games)){
        std::istringstream iss(games);
        i ++;
        char a, b;
        iss >> a; iss >> b;
        int bNormed {int(b) - normX};
        int aNormed {int(a) - normA};
        if(bNormed == 3){
            score += 1 + ((aNormed) % 3);
        }
        else if(bNormed == 2){
            score += aNormed;
        }
        else{
            score += (aNormed - 1) + ((3/(aNormed))/2)*3;
        }
        score += (int(b) - (normX + 1)) * 3;
    }
    std::cout << score;
}