#include <iostream>
#include <vector>

void factors(int num){
    std::vector<int>x;
    for(int i = 1; i < num / 2 + 1; i++){
        if(num % i == 0){
            x.push_back(i);
        }
    }

    x.push_back(num);
    
    for(auto i = x.begin(); i != x.end(); i++){
        std::cout<<*i<<std::endl;
    }
}

int main(){
    int num;
    std::cout<<"number: ";
    std::cin>>num;
    factors(num);
    return 0;
}

