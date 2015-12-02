#include <stdio.h>
double findMedianSortedArrays(int A[], int m, int B[], int n);
int main ()
{
    int A[4] = {1,2,6,7}, B[4] = {3,4,5,8};
    int m = 4, n = 4;
    printf ("%lf\n", findMedianSortedArrays(A, m, B, n));
    return 0;
}

double findMedianSortedArrays(int A[], int m, int B[], int n) {
    int Amid = (m-1)/2, Bmid = (n-1)/2;
    if (m == 0)
    {
        if (n%2 == 1) return B[Bmid];
        else return ((double)B[Bmid] + (double)B[Bmid+1])/2;
    }
    else if (n == 0)
    {
        if (m%2 == 1) return A[Amid];
        else return ((double)A[Amid] + (double)A[Amid+1])/2;
    }
    else if (m == 1)
    {
        if (n == 1)
        {
            return ((double)A[0] + (double)B[0])/2;
        }
        else if (n % 2 == 1)
        {
            if ((A[0] >= B[Bmid-1])&&(A[0]<=B[Bmid+1])) return ((double)B[Bmid] + (double)A[0])/2;
            else if (A[0] < B[Bmid - 1]) return ((double)B[Bmid] + (double)B[Bmid - 1])/2;
            else if (A[0] > B[Bmid + 1]) return ((double)B[Bmid] + (double)B[Bmid + 1])/2;
        }
        else
        {
            if (A[0] <= B[Bmid]) return B[Bmid];
            else if (A[0] >= B[Bmid+1]) return B[Bmid+1];
            else return A[0];
         }
    }
    else if (n == 1)
    {
        if (m%2 == 1)
        {
            if ((B[0] >= A[Amid-1])&&(B[0] <= A[Amid+1])) return ((double)A[Amid] + (double)B[0])/2;
            else if (B[0] > A[Amid + 1]) return ((double)A[Amid] + (double)A[Amid + 1])/2;
            else if (B[0] < A[Amid - 1]) return ((double)A[Amid] + (double)A[Amid - 1])/2;
        }
        else
        {
            if (B[0] <= A[Amid]) return A[Amid];
            else if (B[0] >= A[Amid+1]) return A[Amid+1];
            else return B[0];
        }
    }
    else if (m == 2)
    {
        //printf("hello\n");
        if ((B[Bmid + 1] >= A[Amid+1])&&(B[Bmid] <= A[Amid])&&(n%2 ==0))
        {
            //printf("hello\n");
            return ((double)A[Amid+1] + (double)A[Amid])/2;
        }
        if (n == 2)
        {
            if ((A[Amid+1] >= B[Bmid+1])&&(A[Amid] <= B[Bmid])&&(m%2 == 0))
            {
                return ((double)B[Bmid+1] + (double)B[Bmid])/2;
            }
            else
            {
               // printf("hello\n");
                int curlength = m < n? m/2: n/2;
                if (A[Amid] < B[Bmid]) return findMedianSortedArrays(&A[curlength], m-curlength, B, n - curlength);
                else if (A[Amid] > B[Bmid]) return findMedianSortedArrays(A, m-curlength, &B[curlength], n - curlength);
            }  
        }
        else
        {
           // printf("hello\n");
            int curlength = m < n? m/2: n/2;
            if (A[Amid] < B[Bmid]) return findMedianSortedArrays(&A[curlength], m-curlength, B, n - curlength);
            else if (A[Amid] > B[Bmid]) return findMedianSortedArrays(A, m-curlength, &B[curlength], n - curlength);
        }   
    }
    else if (n == 2)
    {

        if ((A[Amid+1] >= B[Bmid+1])&&(A[Amid] <= B[Bmid])&&(m%2 == 0))
        {
            return ((double)B[Bmid+1] + (double)B[Bmid])/2;
        }
        else
        {
           // printf("hello\n");
            int curlength = m < n? m/2: n/2;
            if (A[Amid] < B[Bmid]) return findMedianSortedArrays(&A[curlength], m-curlength, B, n - curlength);
            else if (A[Amid] > B[Bmid]) return findMedianSortedArrays(A, m-curlength, &B[curlength], n - curlength);
        }
    }
    else if (A[Amid] == B[Bmid])
    {
        if ((m+n)%2 == 1) return A[Amid];
        else
        {
            if (A[Amid+1] <= B[Bmid+1]) return ((double)A[Amid+1] + (double)A[Amid])/2;
            else return ((double)B[Bmid+1] + (double)B[Bmid])/2;
        }
    }
    else
    {
        printf("1\n");
        int curlength = Amid < Bmid? Amid : Bmid ;
        printf("%d\n", curlength);
        if (A[Amid] < B[Bmid]) return findMedianSortedArrays(&A[curlength], m-curlength, B, n - curlength);
        else if (A[Amid] > B[Bmid]) return findMedianSortedArrays(A, m-curlength, &B[curlength], n - curlength);
    }
}