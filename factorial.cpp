#include <iostream>
using namespace std;
int main(){
  int n, i, res;
  cout<<"Enter your number: ";
  cin >> n;
  res = 1;
  for (i = 1; i <= n; i++) {
	res = res * i;
  }
  cout << "your result is: "<< res;
return 0;
}