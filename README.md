# SpellingCorrect_GUI

#### 介绍
自然语言处理（NLP）- 一个英文拼写纠错系统；
功能：给出拼写错误的单词，返回一个正确的单词，或者返回一个与输入单词最接近的单词；
IDE：pycharm；python3.5；PYQT做界面；
数据：
使用big.txt作为语料库。

[博客链接](https://blog.csdn.net/bensonrachel/article/details/85128735)
[编辑距离博客](https://blog.csdn.net/bensonrachel/article/details/78387389)

![输入图片说明](https://images.gitee.com/uploads/images/2021/0314/213725_c4efe2d4_8773742.png "屏幕截图.png")


![输入图片说明](https://images.gitee.com/uploads/images/2021/0314/213743_5341f85a_8773742.png "屏幕截图.png")


效果如图

![avatar](https://img-blog.csdnimg.cn/201812201729553.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JlbnNvbnJhY2hlbA==,size_16,color_FFFFFF,t_70)



#### 软件架构
软件架构说明


主要算法原理：

 

编辑距离（这里使用的是替换操作算一次开销的版本，跟插入和删除等价）：

这里的东西请看我的博客算法里的编辑距离问题，这里不在详细说明。

编辑距离

具体处理方法：

把big.txt的全部单词变成小写，并且计算他们出现的次数，再除以单词总数（字典长度）作为该词的频率，对输入的单词在词典里进行匹配，至少0次编辑，最多2次编辑。找出编辑距离最小的，当编辑距离为最小的不只一个时，找出所有单词里的概率最大的作为输出。



#### 总结：

一般来说，对于错误单词，大多错误字母数在1-2范围内，所以只需找到编辑距离为1-2的，就会有相应的正确单词出现。
编辑距离算法时间复杂度比较高且需要对字典进行搜索匹配，所以总体开销比较大。
概率方面使用的朴素贝叶斯的方法，本系统是小型的英文单词纠错系统，若是百度谷歌微软的纠错系统则更为复杂。

