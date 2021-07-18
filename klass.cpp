#include <iostream>
#include <string>
using namespace std;
/*
https://ru.stackoverflow.com/questions/642331/%D0%9A%D0%B0%D0%BA-%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D1%82%D1%8C-%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D1%83-%D0%B8%D0%B7-%D1%84%D0%B0%D0%B9%D0%BB%D0%B0
*/
struct klass
{
    char name[20];
    int age;
    float grade;
};

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

void Add(klass *new_klass) // Second ant etc. inputs in the program
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
int main()
{
    klass *new_klass = new klass[N]; //init the place where data is stored
    int B = 0;

loh:
    cout << "Press 1 for first input: \n";
    cout << "Press 2 for additional input: \n";
    cout << "Press 3 for output \n";
    cout << "Press 4 for exit: \n";

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
    else if (B == 4)
    {
        return 0;
    }

    goto loh;
    delete[] new_klass; // deletes the data
    return 0;
}