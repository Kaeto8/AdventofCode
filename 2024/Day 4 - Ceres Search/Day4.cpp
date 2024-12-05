#include<iostream>
#include<fstream>
using namespace std;

int xmasCounter(const vector<string> data)
{
    int total = 0, linenumber = 0;
    for(auto line:data)
    {
        for(int i=0; i<line.length(); i++)
        {
            if(line[i] == 'X')
            {
                if(i-3 >= 0)
                {
                    if(line[i-1] == 'M' && line[i-2] == 'A' && line[i-3] == 'S')
                        total += 1;
                    if(linenumber-3 >= 0)
                        if(data[linenumber-1][i-1] == 'M' && data[linenumber-2][i-2] == 'A' && data[linenumber-3][i-3] == 'S')
                            total+=1;
                    if(linenumber+3 < data.size())
                        if(data[linenumber+1][i-1] == 'M' and data[linenumber+2][i-2] == 'A' and data[linenumber+3][i-3] == 'S')
                            total+=1;
                }
                
                if(i+3 < line.length())
                {
                    if(line[i+1] == 'M' && line[i+2] == 'A' && line[i+3] == 'S')
                        total+=1;
                    if(linenumber-3 >= 0)
                        if(data[linenumber-1][i+1] == 'M' && data[linenumber-2][i+2] == 'A' && data[linenumber-3][i+3] == 'S')
                            total+=1;
                    if(linenumber+3 < data.size())
                        if(data[linenumber+1][i+1] == 'M' && data[linenumber+2][i+2] == 'A' && data[linenumber+3][i+3] == 'S')
                            total+=1;
                }
                if(linenumber-3 >= 0)
                    if(data[linenumber-1][i] == 'M' && data[linenumber-2][i] == 'A' && data[linenumber-3][i] == 'S')
                        total+=1;
                
                if(linenumber+3 < data.size())
                    if(data[linenumber+1][i] == 'M' && data[linenumber+2][i] == 'A' && data[linenumber+3][i] == 'S')
                        total+=1;
            }
        }
        linenumber+=1;
    }
    return total;
}

int MASCounter(const vector<string> data)
{
    int total = 0, linenumber = 0;
    for(auto line:data)
    {
        for(int i=0; i<line.length(); i++)
        {
            if(linenumber != 0 && linenumber != data.size()-1 && i !=0 && i != line.length()-1)
                if(line[i]=='A')
                {
                    if(data[linenumber-1][i-1] == 'M' and data[linenumber-1][i+1] == 'M' and data[linenumber+1][i-1] == 'S' and data[linenumber+1][i+1] == 'S')
                        total += 1;
                    if(data[linenumber-1][i-1] == 'M' and data[linenumber-1][i+1] == 'S' and data[linenumber+1][i-1] == 'M' and data[linenumber+1][i+1] == 'S')
                        total += 1;
                    if(data[linenumber-1][i-1] == 'S' and data[linenumber-1][i+1] == 'S' and data[linenumber+1][i-1] == 'M' and data[linenumber+1][i+1] == 'M')
                        total += 1;
                    if(data[linenumber-1][i-1] == 'S' and data[linenumber-1][i+1] == 'M' and data[linenumber+1][i-1] == 'S' and data[linenumber+1][i+1] == 'M')
                        total += 1;
                }
        }
        linenumber+=1;
    }
    return total;
}

int main()
{
    ifstream datafile("data4.txt");
    string line;
    vector<string> data;
    while (getline(datafile, line))
    {
        data.push_back(line);
    }
    cout<<xmasCounter(data)<<endl;
    cout<<MASCounter(data)<<endl;
}
