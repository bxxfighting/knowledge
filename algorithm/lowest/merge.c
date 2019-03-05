#include <stdio.h>

void print_array(int array[], int len)
{
    for (int i = 0; i < len; i ++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

int main(int argc, char *argv[])
{
    int a[] = {1, 2, 3, 5, 11, 23, 33, 45, 54, 62};
    int b[] = {2, 4, 6, 8, 13, 21, 32, 44, 45, 47};
    print_array(a, 10);
    print_array(b, 10);
    int a_len = sizeof(a) / sizeof(int);
    int b_len = sizeof(b) / sizeof(int);
    int lengths = a_len + b_len;
    int result[lengths];
    printf("%d\n", lengths);
    int a_site = 0;
    int b_site = 0;
    for (int i = 0; i < lengths; i ++) {
        if (a_site >= a_len) {
            for (int j = b_site; j < b_len; j ++) {
                result[i] = b[j];
                i ++;
            }
        }
        if (b_site >= b_len) {
            for (int j = a_site; j < a_len; j ++) {
                result[i] = a[j];
                i ++;
            }
        }
        if (a[a_site] <= b[b_site]) {
            result[i] = a[a_site];
            a_site += 1;
        } else {
            result[i] = b[b_site];
            b_site += 1;
        }
    }
    print_array(result, lengths);

    return 0;
}
