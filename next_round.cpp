#include<iostream>
#include<vector>
#include<string>
#include<cmath>

using namespace std;

int main()
{
    vector <int> tnt;
    vector <int> numbers;
    vector <int> slt;

    string input1;
   getline(cin,input1);
    for(int i=0; i< input1.size(); ++i)
     {
        if (!isspace(input1[i]))
        {
            if(!isspace(input1[i-1]) && i != 0)
                {
                    string passer;
                    string temp;
                    temp = input1[i];
                    int n = tnt.size();
                    passer = tnt[n-1];
                    tnt[n-1] = (tnt[n-1] * (pow(10,(passer.size())))) + stoi(temp);
                    continue;
                 }
            string temp;
            temp = input1[i];
            int itemp = stoi(temp);
            tnt.push_back(itemp);
        }
        
     }
     
     string input2;
     getline(cin,input2);

    for(int i=0; i< input2.size(); ++i)
     {
        if (!isspace(input2[i]))
        {
            if(!isspace(input2[i-1]) && i != 0)
                {
                    string passer;
                    string temp;
                    temp = input2[i];
                    int n = numbers.size();
                    passer = numbers[n-1];
                    numbers[n-1] = (numbers[n-1] * (pow(10,(passer.size())))) + stoi(temp);
                    continue;
                 }
            string temp;
            temp = input2[i];
            int itemp = stoi(temp);
            numbers.push_back(itemp);
        }
        
     }

     int j = tnt[1] - 1;
    for(int i = 0; i<numbers.size(); ++i)
     {
        if(numbers[i] >= numbers[j] && numbers[i]!= 0)
        {
            slt.push_back(numbers[i]);
        }
     }

    cout<<slt.size();

 return 0;   
} 