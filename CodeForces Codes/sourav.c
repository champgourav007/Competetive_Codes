#include <stdio.h>
void main()
{
    int i, j, n, k, l;
    scanf("%d", &n);
    l = 0;
    // l = 2 * n - 1;
    // while (n != 0)
    // {
    // for (k = n; k >= 1; k--)
    // {
    l = 2 * n - 1;
    int n1 = n;
    // int val = n;
    for (i = 1; i <= l; i++)
    {
        // l = 2 * n - 1;
        for (j = 1; j <= l; j++)
        {
            if ((i == 1 || i == l) || (j == 1 || j == l))
            {

                // for (k = n; k >= 1; k--)
                printf("%d", n1);
            }
            // printf("\n");
            else
                printf("%d", n - 1);
        }
        printf(" \n");
        n--;
    }
    // n--;}
    // n--;
    // }
}