#include <iostream>
#include <string.h>
#include <fstream>
using namespace std;
 
int main()
{
    string before, after;
    ifstream input_file;
    ofstream output_file;
    input_file.open("input.txt");
    cout << "Please wait...\n"; getline(input_file, before);
    
    bool p = false;
    for (int i = 0, size = before.size(); i < size; ++i) {
        if (before[i] == ' ') {
            if (p) continue;
            else {
                after += ' ';
                p = true; continue;
            }
        } else
            p = false;
        after += before[i];
    }
    output_file.open("output.txt");
    output_file<<after;
    cout << "All done!";
    output_file.close();
    return 0;
}