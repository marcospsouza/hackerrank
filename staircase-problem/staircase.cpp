#include <bits/stdc++.h>

using namespace std;

// Complete the staircase function below.
void staircase(int n) {
    if(n > 0 && n <= 100){
        for(int i=n-1; i >= 0; i--){
            for(int j=0; j < n; j++){
                if (i<=j)
                    cout << "#";
                else cout << " ";
            }
            cout << endl;
        }
    }
}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    staircase(n);

    return 0;
}
