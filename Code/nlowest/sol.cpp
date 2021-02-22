#include <bits/stdc++.h> 

using namespace std;

void PrintNLowestNumbers(int arr[], unsigned int length, unsigned short nLowest)
{
    int i;
    int cnt=1;
    //make a copy of the array
    std::vector<int> copy_arr(arr, arr + length); 

    //sort vector
    sort(copy_arr.begin(), copy_arr.begin() + length); 
    
    for (auto it = copy_arr.begin(); it != copy_arr.end(); ++it) {
        std::cout << *it << ' ';
        if (cnt++ >= nLowest) break;
    }
    
}

int main()
{
	char input[0x100];
	int integerList[0x100];
	unsigned int length;
	unsigned short nLowest;
	std::cin >> nLowest;
	std::cin >> length;
	for (int i=0;i<length;i++)
		 std::cin >> integerList[i];
	PrintNLowestNumbers(integerList, length, nLowest);
}
