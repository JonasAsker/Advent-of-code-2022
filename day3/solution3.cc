#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <iterator>
using namespace std;

int main() {
    std::ifstream infile("input20223.txt");
    std::string row;
    int totalPrioriy{0};
    int normA {int('A')};
    int norma {int('a')};
    
    vector <string> threeStrings;

    while (std::getline(infile, row)){
        threeStrings.push_back(row);
        while (threeStrings.size() == 3){
            string firstElf{threeStrings[0]};
            for (auto& letter: firstElf){
                if(threeStrings[1].find(letter) != string::npos 
                    && threeStrings[2].find(letter) != string::npos){
                    if (isupper(letter))
                    {
                        totalPrioriy += int(letter) - normA + 27;
                        cout << "Upper " << (int(letter) - normA + 27) << '\n';
                    }
                    else
                    {
                        totalPrioriy += int(letter) - norma + 1;
                        cout << "Lower " << (int(letter) - norma + 1) << '\n';
                    }
                    threeStrings.clear();
                    break;
                }
            }
        }
    }
    cout << totalPrioriy << '\n';
}

void task1(){
    std::ifstream infile("input20223.txt");
    std::string row;
    int totalPrioriy{0};
    cout << int('A') << '\n';
    cout << int('a') << '\n';
    int normA {int('A')};
    int norma {int('a')};
    while (std::getline(infile, row)){
        string containerOne {row.substr(0, row.length()/2)};
        string containerTwo {row.substr(row.length()/2, row.length()/2)};
        for (auto& letter: containerOne){
            if(containerTwo.find(letter) != std::string::npos){
                if (isupper(letter))
                {
                    totalPrioriy += int(letter) - normA + 27;
                    cout << "Upper " << (int(letter) - normA + 27) << '\n';
                }
                else
                {
                    totalPrioriy += int(letter) - norma + 1;
                    cout << "Lower " << (int(letter) - norma + 1) << '\n';
                }
                break;
            }
        }
    }
    cout << totalPrioriy << '\n';
}