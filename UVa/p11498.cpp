#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, x, y, px, py;
    cin>>n;
    while(n!=0)
    {
            cin>>px>>py;
            while(n--)
            {
                cin>>x>>y;
                if(x==px || y==py)
                    cout<<"divisa"<<endl;
                else if(x>px && y>py)
                    cout<<"NE"<<endl;
                else if(x<px && y>py)
                    cout<<"NO"<<endl;
                else if(x>px && y<py)
                    cout<<"SE"<<endl;
                else
                    cout<<"SO"<<endl;
            }
            cin>>n;
    }

    return 0;
}
