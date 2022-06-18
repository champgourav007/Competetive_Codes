#include <bits/stdc++.h>
using namespace std;

int main()
{
  int n, c;
  cin >> n >> c;
  vector<int> clg(c);
  for (int i = 0; i < c; i++)
  {
    cin >> clg[i];
  }
  map<string, vector<string>> st;
  for (int i = 0; i < n; i++)
  {
    string s;
    cin >> s;
    vector<string> v;
    for (int j = 0; j < c; j++)
    {
      string t;
      cin >> t;
      v.push_back(t);
    }
    st[s] = v;
  }
  map<string, vector<string>> result;
  for (auto i : st)
  {
    for (auto j : i.second)
    {
      int clg_no = stoi(j.substr(2));
      if (clg[clg_no - 1] != 0)
      {
        clg[clg_no - 1]--;
        result[i.first] = j;
        break;
      }
    }
  }
  for (auto i : result)
  {
    cout << i.first << " " << i.second << endl;
  }
  return 0;
}