#include <iostream>
#include <string>
#include <fstream>
using namespace std;

// p022_names.txt - 5163 names

int main()
{
    cout << "Euler #22 - Name Scores\n\n";

    ifstream inFile;
    inFile.open("p022_names.txt");

    if (inFile.fail()) {
        cerr << "Error reading file!";
    }

    string name;
    int count1 = 0;
    char comma = ',';
    vector names;

    while(getline(inFile, name, comma)) {
        count1 ++;
        int nameLen = name.length();
        string name2 = name.substr(1,nameLen-2);

        cout << name2;
    }

    inFile.close();

    cout << endl << endl << count1;

    cout << "\n\nEnd of Program";
    return 0;
}
