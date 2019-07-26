### 问题
python的GIL是什么

### 解决办法
[官方文档解释](https://docs.python.org/3.6/c-api/init.html?highlight=gil)  
[python3 cookbook解释](https://python3-cookbook.readthedocs.io/zh_CN/latest/c12/p09_dealing_with_gil_stop_worring_about_it.html)  

```
Here is how these functions work: 
the global interpreter lock is used to protect the pointer to the current thread state. 
When releasing the lock and saving the thread state, 
the current thread state pointer must be retrieved before the lock is  
released (since another thread could immediately acquire the lock and store its own
thread state in the global variable). 
Conversely, when acquiring the lock and restoring the thread state, 
the lock must be acquired before storing the thread state pointer.
```
> 上面的大概意思就是说，python每个线程都维护着一个线程状态，  
> 而有一个全局的指针指向当前线程的状态，为了保证这个全局指针的使用安全，  
> 在使用这个指针之前加了一个锁，只有获取了这个锁的线程，才能改变这个全局指针的指向。 
> 也就是，所有线程先竞争这个锁，谁获取到了，就将全局指针，指向自己的线程状态，  
> 然后可以利用CPU进行自己这个线程要做的事.  
> 当需要让出CPU时(让出CPU有几种情况，IO操作阻塞了/可利用CPU时间到了之类的)，  
> 先将指针的指向重置(可能就是重置为None)，然后释放之前的锁。  
> 锁没有人持有了，所有线程再开始竞争这个锁。之后往复。  

在很多网上搜索的说法中，说现在很多库可能依赖了这个GIL，所以已经不好更改了。  
我当时就想到底有什么库依赖这个了。  
我没有深究，但是我觉得可能只是python很多内建库依赖依赖了。其它第三方库应该不会。  

> 而且上面只提到了那个当前线程的指针切换使用了这个GIL，没有提到其它的  
> 我觉得应该还有很多其它全局变量上使用了GIL。于是我下载了python的源码来搜索了一下  

我基于的是python3.6.8的版本源码  
拿其中一个文件举例 ./Modules/readline.c  
```
#ifdef HAVE_RL_PRE_INPUT_HOOK
static int
#if defined(_RL_FUNCTION_TYPEDEF)
on_pre_input_hook(void)
#else
on_pre_input_hook()
#endif
{
    int r;
#ifdef WITH_THREAD
    PyGILState_STATE gilstate = PyGILState_Ensure();
#endif
    r = on_hook(readlinestate_global->pre_input_hook);
#ifdef WITH_THREAD
    PyGILState_Release(gilstate);
#endif
    return r;
}
#endif
```
其中可以很明显的看到，有如果是线程就获取GIL并且最后释放GIL的过程  

[python源码github](https://github.com/python/cpython)  
[python官方提供源码压缩包](https://www.python.org/downloads/source/)  
查找命令：
```
find  . -name "*.c" | xargs grep GIL
```
