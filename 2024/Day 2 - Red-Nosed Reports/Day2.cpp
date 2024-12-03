#include<iostream>
#include<fstream>
#include<sstream>
using namespace std;

int Analyzer(const vector<int> &report)
{
    int good = 0;
    bool safe = false;
    for(int i=0; i<report.size()-1; i++)
    {
        if(report[0]>report[1] && report[i]>report[i+1] && report[i]-report[i+1]<=3)
            safe = true;
        else if (report[0]<report[1] && report[i]<report[i+1] && report[i+1]-report[i]<=3)
            safe = true;
        else
        {
            safe = false;
            break;
        }
    }
    if(safe == true)
        good = 1;
    return good;
}

int SecondAnalyzer(const vector<int> &report)
{
    int secondgood = 0;
    if(!(Analyzer(report) == 1))
    {
        for(int i=0; i<report.size(); i++)
        {
            vector<int> newline = report;
            newline.erase(newline.begin()+i);
            if(Analyzer(newline) == 1)
            {
                secondgood = 1;
                break;
            }
        }
    }
    return secondgood;
}

int main()
{
    ifstream datafile("data2.txt");
    string line;
    vector<vector<int>> fullreport;
    int result = 0;
    int result2 = 0;
    
    while(getline(datafile, line))
    {
        stringstream s(line);
        vector<int> report;
        int level;
        while(s>>level)
        {
            report.push_back(level);
        }
        fullreport.push_back(report);
    }
    
    for(auto report:fullreport)
    {
        result += Analyzer(report);
        result2 += SecondAnalyzer(report);
    }
    cout<< result <<endl;
    cout<< result + result2 <<endl;
}
