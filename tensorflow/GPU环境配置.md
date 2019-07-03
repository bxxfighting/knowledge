### 问题:
安装不同版本的tensorflow需要的显卡驱动、cuda、cudnn版本不同
因此需要在安装时安装正确版本

### 解决办法:
1. 先根据自己使用的tensorflow-gpu版本在官方的测试配置列表中查找对应的依赖版本  
官方测试配置列表：https://tensorflow.google.cn/install/source#linux  
2. NVIDIA驱动安装  
下载地址：https://www.nvidia.cn/Download/index.aspx?lang=cn  
3. CUDA安装  
下载地址：https://developer.nvidia.com/cuda-toolkit-archive  
4. cuDNN安装  
下载地址: https://developer.nvidia.com/rdp/cudnn-archive  

#### 示例:
现在我要使用tensorflow-gpu==1.8.0  
1. 查看测试配置列表，对应配置如下：  
```
版本	                Python 版本	    编译器	    编译工具	    cuDNN	CUDA
tensorflow_gpu-1.8.0	2.7、3.3-3.6	GCC 4.8	    Bazel 0.10.0	7	    9
```

2. 下载驱动  
我这里显卡是Tesla M40，选择对应的驱动、操作系统及对应的CUDA版本  
因为配置列表中说让用9，那就严格下载9的，不要下载9.1的  

3. 下载CUDA  
选择了CUDA Toolkit 9.0 -> Linux -> x86_64 -> Ubuntu -> 16.04 -> runfile(local)  
然后下载，并执行安装命令  
```
sudo sh cuda_9.0.176_384.81_linux.run
```

> 这个命令在下载处会有提示  
> 在安装过程中，会问你是否安装驱动，因为我们安装过了，所以这个选择no，其它都默认安装并且位置直接默认就可以  
> 安装完成后，会有提示，说要把安装的路径的bin目录加到PATH，并且把lib64目录加到LD_LIBRARY_PATH  
> 我一般都是写到/etc/bash.bashrc中，如下：  
> ```
> export PATH=/usr/local/cuda/bin:$PATH
> export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
> ```
> 这里的路径不用cuda-9.0，是因为cuda就是cuda-9.0目录的软件链接，效果是一样的，  
> 而且如果你要升级到9.1的话，只需要更改cuda这个软件链接的指向就够了，  
> 不用修改bash.bashrc文件内容  

4. 下载cuDNN  
我下载了与cuda9相匹配的cuDNN v7.0.5 for CUDA 9.0  
> 其实7.0以上也有和CUDA9.0相匹配的，但是官方测试配置就是7的，因此我没有下载更高版本  
> 下载完成后，具体安装直接看和下载同一目录的cuDNN Install Guide，介绍的很详细  
