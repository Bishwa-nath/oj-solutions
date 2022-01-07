#include <bits/stdc++.h>
using namespace std;

int main()
{
    int i,num, n, high=0, low=0;
    cin>>n;
    for(int j=1; j<=n; j++)
    {
        cin>>num;
        int ar[num];
        for(i=0; i<num; i++){
            cin>>ar[i];
        }
        for(i=0; i<num-1; i++){
            if(ar[i]>ar[i+1])
            low++;
            if(ar[i]<ar[i+1])
            high++;
        }
        cout<<"Case "<<j<<": "<<high<<" "<<low<<endl;
        high=0;
        low=0;
    }

    return 0;
}
