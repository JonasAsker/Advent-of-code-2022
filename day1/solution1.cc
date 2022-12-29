#include <fstream>
#include <string>
#include <sstream>
#include <iostream>
#include <list>
#include <iterator>
using namespace std;

int main() {
    std::ifstream infile("input20221.txt");
    std::string cals;
    std::list<int> elves;
    int currentElf {0};
    while (std::getline(infile, cals)){
        std::istringstream iss(cals);
        int a;
        if ((iss >> a)) {
             currentElf += a;
        }
        else{
            //std::cout << i;
            elves.push_back(currentElf);
            currentElf = 0;
        }
    }
    elves.sort();
    elves.reverse();
    int total{0};
    auto l_front = elves.begin();
    total += *l_front;
    std::advance(l_front, 1);
    total += *l_front;
    std::advance(l_front, 1);
    total += *l_front;
    std::cout << total;
    return 0;
}