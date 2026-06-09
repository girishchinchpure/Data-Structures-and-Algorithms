#include<iostream>
using namespace std;

int linearSearch(int arr[], int size, int target)
{
    for(int i = 0 ; i < size ; i++)
    {
        if (arr[i] == target)
        {
            return i; //found
        }
    }
    return -1; // not found
}
int main()
{
    int arr[] = {87, 25, 56,-90,89,0,10,6,90};
    int size = 9;
    int target = 10;
    cout << "Target element's Index = " << linearSearch(arr, size, target) << endl;
}
