#include <iostream>
using namespace std;

int power(int x, long long p)
{
    if (p == 0)
        return 1;
    long long temp = power(x, p / 2);
    if (p % 2)
    {
        return temp * temp * x;
    }
    else
    {
        return temp * temp;
    }
}

int main()
{
    long long x1, p1, x2, p2;
    int t;
    cin >> t;
    while (t--)
    {
        cin >> x1 >> p1;
        cin >> x2 >> p2;
        long long val1 = x1 * power(10, p1);
        long long val2 = x2 * power(10, p2);
        if (val1 > val2)
        {
            cout << ">"<<endl;
        }
        else if (val1 < val2)
        {
            cout << "<"<<endl;
        }
        else
        {
            cout << "="<<endl;
        }
    }
}