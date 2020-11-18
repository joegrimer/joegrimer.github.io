#include <iostream>
#include <math.h>
using namespace std;

int d(int a);

int main()
{
    cout << "Euler #21 - Amicable Numbers\n\n";

    int ceiling=10000;
    int total=0;

    int a;
    for(a=0;a<=ceiling;a++) {
//        cout << a;
        int b = d(a);
        int db = d(b);

        if (a!=b && db==a) {
            total+=a;
            cout << "dSum of ";
            cout << a;
            cout << " is ";
            cout << b;
            cout << " and ";
            cout << db;
            cout << "\n";
        }

    }
    cout << "\n\ntotal is >";
    cout << total;
    cout << "<";

    cout << "\n\nEnd of Program";
    return 0;
}

int d(int a) {

    // find divisors
    int dSum = 0;
    int rtA = sqrt(a);
    int i1;
    for(i1=1;i1<=rtA;i1++) {

        if (a % i1 == 0) {
            dSum += i1;
            if (a/i1 != i1) dSum += a/i1;
//            cout << dSum;
//            cout << "\n";
        }
    }

    return dSum-a;
}
