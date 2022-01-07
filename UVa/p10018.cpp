#include <bits/stdc++.h>
using namespace std;

int rev(int num)
{
    int re=0;
    while(num!=0)
        {
            re*=10;
            re+=(num%10);
            num/=10;
        }
        return re;
}

int main()
{
    int t, p, temp, n, sum=0, re, count(0);
    cin>>t;
    while(t--)
    {
        cin>>p;
        temp = p;
        sum = rev(temp);
        if(sum==p)
            cout<<count<<" "<<sum<<endl;
        else
        {
            p+=sum;
            count++;
        }



    }

    return 0;
}
