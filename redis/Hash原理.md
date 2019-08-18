### 问题
在redis中是如何存储hash值

### 解决办法
1. 其实redis中的hash类型，就是我们一般据说的dict或者map。只是底层实现时，使用了hashtable。  
在dict结构中，存在一个dictht的数组ht[2]，数组大小为2，也就是两个hashtable。  
还存在是一个标志rehashidx，-1时代表没有在进行rehash。  
```
typedef struct dict {
    dictType *type;
    void *privdata;
    dictht ht[2];
    long rehashidx; /* rehashing not in progress if rehashidx == -1 */
    unsigned long iterators; /* number of iterators currently running */
} dict;
```

2. 在dictht中size记录hashtable的大小，而sizemask记录size的一个掩码，这里是一个技巧。  
我们在使用hashtable的时候，一般都是生成hash值后，对hashtable的size取余，  
但是这里size的取值都是2的指数，将sizemask = size - 1，  
这样就可以通过将生成的hash值与sizemask进行与运算就可以获取到余数，比取余运算要快。  
这里如果不理解可以自己手动计算一下，size = 8 = 0b1000, sizemask = 7 = 0b111，  
0b111 & 0b101 = 0b101, 0b111 & 0b10111101 = 0b101。  
```
typedef struct dictht {
    dictEntry **table;
    unsigned long size;
    unsigned long sizemask;
    unsigned long used;
} dictht;
```
在dictht中还有一个字段是used，代表当前已经使用的大小。  
初始时，会分配DICT_HT_INITIAL_SIZE大小， 这个值为4。  
在使用过程中，需要扩展大小时，一般先used * 2，再取第一个大于此值的2的指数。  
```
static unsigned long _dictNextPower(unsigned long size)
{
    unsigned long i = DICT_HT_INITIAL_SIZE;

    if (size >= LONG_MAX) return LONG_MAX + 1LU;
    while(1) {
        if (i >= size)
            return i;
        i *= 2;
    }
}
```
> 这里LONG_MAX是长整数的最大值，+ 1LU后变成无符号整数  

3. 原本数据是在ht[0]上，当需要扩展大小时，也就是进行rehash操作。  
会在ht[1]上新建一个hashtable，之后新加入的数据都往这个hashtable上加。  
也就是新的数据操作，需要先在ht[0]上看有没有，如果没有，就加到ht[1]上去。  
redis在设计时，并没有直接将原来的数据一次性的弄到ht[1]上，而是一点点弄的，  
这个一点点是什么意思呢，就是不论在进行增加删改查时，都会帮忙rehash一下。  
开始rehash时，rehashidx就设置为0，然后进行一次rehash就加1。  
直到最后ht[0]上的used为0时，就把ht[0]再指向ht[1]，把ht[1]原来指向的hashtable释放。  

4. 其它就是正常的hash存储方式了，dictht中的**table就是指向指针数组的指针
```
typedef struct dictEntry {
    void *key;
    union {
        void *val;
        uint64_t u64;
        int64_t s64;
        double d;
    } v;
    struct dictEntry *next;
} dictEntry;
```
