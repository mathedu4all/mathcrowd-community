# 知识点整理

## 项目流程

* ~~讨论并确定一二级知识点(2020.04.30前完成)~~

* ~~确定各板块三级及以下知识点的分工(2020.04.30前完成):~~

* ~~讨论并确定各板块三级及以下知识点(2020.05.07前完成);~~

* 确定已有知识点与新知识点间的对应关系(2020.5.15前完成).

## 确定最终版知识点的讨论页面【已结束】：

在提交最终版知识点文件前，先将草稿发至相关issue页面进行讨论.

* 【已结束】 [一二级知识点讨论](https://github.com/mathedu4all/mathcrowd-community/issues/3) 

    负责人: 橘子老君

* 【已结束】[数与运算 知识点讨论](https://github.com/mathedu4all/mathcrowd-community/issues/9)

    负责人: 橘子老君
    
* 【已结束】[图形与几何 知识点讨论](https://github.com/mathedu4all/mathcrowd-community/issues/8)

    负责人: 橘子老君(高中) [@dangming25 (初中)](https://github.com/dangming25) 

* 【已结束】[方程与代数板 识点讨论](https://github.com/mathedu4all/mathcrowd-community/issues/6)

    负责人: 橘子老君(高中) [@dangming25 (初中)](https://github.com/dangming25) 

* 【已结束】[函数与分析 知识点讨论](https://github.com/mathedu4all/mathcrowd-community/issues/5)

    负责人: 橘子老君

* 【已结束】[应用数学与数学建模 知识点讨论](https://github.com/mathedu4all/mathcrowd-community/issues/7)

    负责人: [@52511338(高中)](https://github.com/52511338),  [@sunpingana(初中)](https://github.com/sunpingana)
    
在

## 文件格式说明:

各板块知识点文件以markdown形式保存在``knowledge-tags/``目录，文件命名如下：

```
knowledge-tags/
├── knowledge-nodes-algebra.md
├── knowledge-nodes-analysis.md
├── knowledge-nodes-application.md
├── knowledge-nodes-arithmetic.md
├── knowledge-nodes-geometry.md
├── knowledge-roots.md
```

其中知识点树状结构以无序列表嵌套的形式呈现如下:

```markdown
* 一级知识点1
  * 二级知识点1
  * 二级知识点2
* 一级知识点2
  * 二级知识点3
    * 三级知识点1
```

> 注意，每一层知识点请严格缩进两个空格，同级知识点缩进量相同.

各板块知识点确定后合并文件为``knowledge-nodes-full.md``，导入数据库后生成``knowledge-nodes-leaves.csv``

```
knowledge-tags/
├── knowledge-nodes-full.md
├── knowledge-nodes-leaves.csv
```

csv文件格式如下:

```
ID,PATH,NAME
10004,方程与代数->代数式->整式->整式的概念->字母表述数,字母表述数,4,10003
```

其中首列ID为该知识点在数据库中的编号.

现有(旧的)叶知识点被保存在以下两个文件:

```
knowledge-tags/
├── knowledge-chuzhong-nodes-old.csv
├── knowledge-gaozhong-nodes-old.csv
```

```
ID,PATH,NAME
568,初中数学->数与运算(初中)->有理数->数的整除性,数的整除性
```

在上述两个文件新增一列，输入与该旧知识点对应的新知识点的ID.

> 注意csv文件中用英文逗号分割列数据.
> 当旧知识点与多个新知识点对应时，用英文`;`分隔.
>
>```
>ID,PATH,NAME
> 568,初中数学->数与运算(初中)->有理数->数的整除性,数的整除性,10001;10002
> ```

## 相关教程

* [如何使用Github进行协作编辑](http://docs.mathcrowd.cn/howtos/how_to_use_github.html)
