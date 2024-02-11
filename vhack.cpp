#include <bits/stdc++.h>

using namespace std;

int n, m, k, z;
int lines[2005];
int products[2005];
int reductions[5005][2];

int main()
{
  cin >> n >> m >> k;
  for (int i = 0; i < k; i++)
  {
    int x, y;
    cin >> x >> y;
    products[x - 1]++;
    lines[y - 1]++;
  }
  for (int i = 0; i < m; i++)
  {
    cin >> lines[i];
  }
  cin >> z;
  for (int i = 0; i < z; i++)
  {
    cin >> reductions[i][0] >> reductions[i][1];
  }
  int ans = 0;
  for (int i = 0; i < z; i++)
  {
    int r = reductions[i][0] - 1;
    int p = reductions[i][1];
    int temp = 0;
    lines[r] -= p;
    int tempArray[m+1];
    for(int i = 0; i <= m; i++)
    {
      tempArray[i] = lines[i];
    }
    for (int j = 0; j < n; j++)
    {
      if (tempArray[j] > 0)
      {
        temp++;
        tempArray[j] -= 1;
      }
    }
    // ans = max (ans, temp);
    cout << temp << endl;
  }
  return 0;
}