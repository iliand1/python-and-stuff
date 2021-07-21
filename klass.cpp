#include <iostream>
#include <string>
#include <fstream>
using namespace std;

struct klass
{
    char name[20];
    int age;
    float grade;
};
ifstream input_file("input.txt");
ofstream output_file("output.txt");
int N, M;

void Output(klass *new_klass) // Outputs Info to terminal
{
    cout << "Output: " << endl;

    for (int i = 0; i < N; ++i)
    {
        cout << "Name: " << new_klass[i].name << endl;
        cout << "Age: " << new_klass[i].age << endl;
        cout << "Grade: " << new_klass[i].grade << endl;
    }
}

void Input(klass *new_klass) // First input in the program
{
    cout << "Enter number of students: \n";
    cin >> N;
    cin.ignore();
    for (int i = 0; i < N; i++)
    {
        cout << "Name of the student: \n";
        cin.getline(new_klass[i].name, 30);
        cout << "Age of the student: \n";
        cin >> new_klass[i].age;
        cin.ignore();
        cout << "Grade of the student: \n";
        cin >> new_klass[i].grade;
        cin.ignore();
    }
}

void Add(klass *new_klass) // Second and etc. inputs in the program
{
    cout << "Enter number of additional students: \n";
    cin >> M;
    cin.ignore();
    N += M;
    cout << "Enter information about each additional student: \n"
         << endl;
    for (int i = N - M; i < N; i++)
    {
        cout << "Name of the student: \n"
             << endl;
        cin.getline(new_klass[i].name, 30);
        cout << "Age of the student: \n"
             << endl;
        cin >> new_klass[i].age;
        cin.ignore();
        cout << "Grade of the student: \n"
             << endl;
        cin >> new_klass[i].grade;
        cin.ignore();
    }
}
void Input_file(klass *new_klass){
 for ( int i=0; i<N; i++ )
  {
    input_file>>new_klass[i].name>>new_klass[i].age>>new_klass[i].grade;
   
  }
  input_file.clear();
}
void Output_file(klass *new_klass){
for (int i = 0; i<N; i++){
    output_file<< new_klass[i].name<<" "<<new_klass[i].age<<" "<<new_klass[i].grade<<"\n";
    output_file.clear();
}
}

int main()
{
    klass *new_klass = new klass[N]; //init the place where data is stored
    int B = 0;

loh:
    cout << "Press 1 for first input: \n";
    cout << "Press 2 for additional input: \n";
    cout << "Press 3 for output: \n";
    cout << "Press 4 for file input: \n";
    cout << "Press 5 for file output \n";
    cout << "Press 6 for exit: \n";
    cin >> B;
    if (B == 1)
    {
        Input(new_klass);
    }
    else if (B == 3)
    {
        Output(new_klass);
    }
    else if (B == 2)
    {
        Add(new_klass);
    }
    else if (B == 6)
    {
        return 0;
    }
    else if (B == 4)
    {
        Input_file(new_klass);
    }
    else if (B == 5)
    {
        Output_file(new_klass);
    }

    goto loh;
    delete[] new_klass; // deletes the data
    output_file.close();
    return 0;
}