#include<iostream>
using namespace std;

int main()
{
    int arr[5];
    cout << "Enter array :\n";
    for (int i = 0 ; i < 5 ; i++)
    {
        cin >> arr[i];
    }
    int small = arr[0];
    for (int i = 0 ; i < 5 ; i++)
    {
        small = min(small, arr[i]);
    }
    cout << "smallest is " << small;
    
}
