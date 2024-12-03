#include<iostream> 
#include<fstream> 
using namespace std;

int main ()
{
    ifstream datafile("data1.txt");
    string line;
    vector<int> left, right;

    while(getline(datafile, line))
    {
        int count = 0;
        string a = line. substr(0, line.find(' '));
        left.push_back(stoi(a));
        for(int i=0; i<line.length(); i++)
        {
            count = 0;
            if(line[i]=' ')
                count += 1;
        }
        string b = line.substr(a.length()+count, line.length());
        right.push_back(stoi(b));
    }

    sort(left.begin(), left.end()); 
    sort(right.begin(), right.end());

    long int total = 0;
    for(int i=0; i<left.size(); i++)
        total += abs (left[i]-right[i]);
    cout<<total<<endl;

    //........Part2................
    long int total2 = 0;

    for(int i=0; i<left.size(); i++)
        total2 += left[i] * count (right.begin(), right.end(), left[i]);
    cout<<total2<<endl;
}
