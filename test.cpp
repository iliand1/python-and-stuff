    #include <iostream>
    #include <string>
    using namespace std;
    
    struct klass
    {
        char name[20];
        int age;
        float grade;
    };
    
    int N, M;

    void Output(klass* new_klass) {
        cout<<"Output: "<<endl;
        
        for (int i = 0; i < N; ++i)
        { 
            cout << "Name: " << new_klass[i].name << endl;
            cout << "Age: " << new_klass[i].age << endl;
            cout << "Grade: " << new_klass[i].grade << endl;
        }
    }
    
    void Input(klass* new_klass) {
        cout<<"Enter number of students: \n";
        cin>>N;
        cin.ignore();
        for (int i = 0; i < N; i++) {
            cout<<"Name of the student: \n";
            cin.getline(new_klass[i].name, 30);
            cout<<"Age of the student: \n";
            cin>>new_klass[i].age;
            cin.ignore();
            cout<<"Grade of the student: \n";
            cin>>new_klass[i].grade;
            cin.ignore();
        }
    }

    void Add(klass* new_klass) {
        cout<<"Enter number of additional students: \n";
        cin>>M;
        cin.ignore();
        N += M;
        cout<<"Enter information about each additional student: \n"<<endl;
        for (int i = N-M; i < N; i++) { 
            cout<<"Name of the student: \n"<<endl;
            cin.getline(new_klass[i].name, 30);
            cout<<"Age of the student: \n"<<endl;
            cin>>new_klass[i].age;
            cin.ignore();
            cout<<"Grade of the student: \n"<<endl;
            cin>>new_klass[i].grade;
            cin.ignore();

        }
    }
    // массив, глобальные Н М
    // ввести, вывести, добавить и выйти из прог
    int main() {
        klass* new_klass = new klass[N];
        int B = 0;
  
           
    
    loh:
        cout<<"Press 1 if you want to add info: \n";
        cout<<"Press 2 if you want see current info: \n";
        cout<<"Press 3 if you want to add new info: \n";
        cout<<"Press 4 if you want to exit the application: \n";
        
        
        cin>>B;
            if (B==1)
            {
                Input(new_klass);
            } else if (B==2){Output(new_klass); }
            else if (B==3) {Add(new_klass);}
            else if (B==4){return 0;}
        


    
    goto loh;
        delete[]new_klass;
        return 0;
    }