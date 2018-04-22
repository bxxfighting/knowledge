/*
 * 快速排序的主要思想: 
 * 先指定一个元素，找出比这个元素小的放在左边;
 * 找出比这个元素大的放在右边;
 * 中间空出来一个位置就是这个元素的位置;
 * 之后将此元素两边的数据再次进行如上操作，就可以将数据排好序了
 * */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


// 第一种实现
void quick_sort(int *numbers, int left, int right)
{
    // 在排序过程中始终要有一个判断条件就是left要小于right
    if (left < right) {
        // 首先在查找开始之前要记录最初传进入的位置，在递归调用时要用到
        int start = left;
        int end = right;
        // key就是我们指定的那个元素，这里就用left位置上的值，
        // 因为key已经记录了left位置上的值，
        // 那么此时left位置就可以存放其它值了,下面就会用到
        int key = numbers[left];
        while (left < right) {
            // 我们先从右侧去查找比key小的值,
            // 如果找不到就right减1，继续查找
            while (left < right && numbers[right] > key) {
                right --;
            }
            // 当找到后，就将找到的值，赋值到原来left位置,赋值完成后，
            // 相当于当前right位置可以用来存放其它值了
            /* 这里有一个看着可能不太容易理解的问题，就是在不满足left < right的时候
             * 也会跳出循环，那为什么下面还有赋值呢？
             * 这个主要是因为如果因为不满足left < right跳出，
             * 那么必然是left == right，既然相等赋值一次是没有什么问题的，
             * 但是如果我们这里去进行判断,
             * 到底是找到了小于key的值还是left == right了才退出循环的
             * 因为这是一个循环操作，就可能增加了多次判断
             * 因此不如直接赋值一次就完事了
             * */
            numbers[left] = numbers[right];
            left ++;
            // 现在再从左侧查找比key大的值，
            // 如果找不到就left加1，继续查找
            while (left < right && numbers[left] < key) {
                left ++;
            }
            // 当找到后，就将找到的值，赋值到上次right位置，赋值完成后，
            // 相当于当前left位置可以用来存放其它值了
            numbers[right] = numbers[left];
        }
        // 当while循环结束，此时应该right和left是相等的，
        // 并且这个位置就是key应该在的位置了
        numbers[right] = key;
        // 上面key已经找到了自己的位置，并且前面是小于它的，后面是大于它的
        // 那么就把两边的数据再次进行同样的处理
        quick_sort(numbers, start, right - 1);
        quick_sort(numbers, right + 1, end);
    }
}

// 第二种实现
void quick_sort_v2(int *numbers, int left, int right)
{
    if (left < right) {
        // 把right位置上的值记录key
        int key = numbers[right];
        // 记录下左侧的位置
        int i = left;
        // 这里就从左侧开始处理，查找比key小的值，一直往左侧放
        for (int j = left; j < right; j ++) {
            if (numbers[j] <= key) {
                int tmp = numbers[i];
                numbers[i] = numbers[j];
                numbers[j] = tmp;
                i ++;
            }
        }
        // 当上面执行完成后，i位置左侧都是小于等于key的值，所以i位置存放key
        numbers[right] = numbers[i];
        numbers[i] = key;
        quick_sort_v2(numbers, left, i - 1);
        quick_sort_v2(numbers, i + 1, right);
    }
}

int main(int argc, char *argv[])
{
    int i, numbers[10] = {0};
    int len = sizeof(numbers) / sizeof(int);

    srand(time(NULL));
    for (i = 0; i < len; i ++) {
        numbers[i] = rand() % 100;
    }
    for (i = 0; i < len; i ++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    quick_sort(numbers, 0, 9);

    for (i = 0; i < len; i ++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    for (i = 0; i < len; i ++) {
        numbers[i] = rand() % 100;
    }
    for (i = 0; i < len; i ++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    quick_sort_v2(numbers, 0, 9);

    for (i = 0; i < len; i ++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    return 0;
}
