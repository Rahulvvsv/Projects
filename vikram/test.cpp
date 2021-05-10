#include <iostream>
#include<fstream>
using namespace std;

int main()
{
    ofstream abc;
    abc.open("item.txt");
    abc<<"usa";
    abc<<"\nuk";
    abc.close();
    ofstream xyz;
    xyz.open("item 2.txt");
    xyz<<"washington";
    xyz<<"\nlondon";
    xyz.close();
    char line[100];
    char ch;
    ifstream a;
    a.open("item.txt",ios::in);
    cout<<"\n item contents:\n";
    while(!a.eof() )
    
    {
        a.get(ch);
        // cout<<"hi";
        // cout<<a.tellp()<<endl;
        cout<<ch;
    }
    a.close();
    ifstream b;
    b.open("item 2");
    cout<<"\n item 2 contents:\n";
    while(!b.eof())
    
    {
        b.get(ch);
        cout<<ch;
    }   
    return 0;
}