#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t, n, i, k;
    cin>>t;
    for(int j=1; j<=t; j++)
    {
        int max =0;
        cin>>n;
        int ar[n];
        for(i=0; i<n; i++)
            cin>>ar[i];
        for( k=0; k<n; k++)
            if(max<ar[k])
            max = ar[k];

        cout<<"Case "<<j<<": "<<max<<endl;
    }

    return 0;
}
