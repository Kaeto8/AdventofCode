#include<iostream>
#include<fstream>
#include<regex>
using namespace std;

int computer(string line)
{
    int result = 0;
    regex search = regex(R"(mul\((\d+),(\d+)\))");
    
    auto words_begin = sregex_iterator(line.begin(), line.end(), search);
    auto words_end = sregex_iterator();
    
    for(sregex_iterator i = words_begin; i != words_end; i++)
    {
        smatch m = *i;
        result += stoi(m[1].str())*stoi(m[2].str());
    }
    return result;
}

int conditionalComputer(string line)
{
    int result = 0;
    bool flag = true;
    regex search = regex(R"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))");
    
    auto words_begin = sregex_iterator(line.begin(), line.end(), search);
    auto words_end = sregex_iterator();
    
    for(sregex_iterator i = words_begin; i != words_end; i++)
    {
        smatch m = *i;
        if(m[0].str() == "do()")
            flag = true;
        else if (m[0].str() == "don't()")
            flag = false;
        else
            if(flag)
                result += stoi(m[1].str())*stoi(m[2].str());
    }
    return result;
}

int main()
{
    ifstream datafile("data3.txt");
    string line, data;
    while (getline(datafile, line))
        data += line;
    
    cout<<computer(data)<<endl;
    cout<<conditionalComputer(data)<<endl;
}
