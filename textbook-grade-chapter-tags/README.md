# 教材章节整理

## 项目流程

* ~~确定各版教材章节整理录入的分工(2020.04.30前完成):~~

* ~~根据教材目录，录入各教材版本的章节信息(2020.5.7前完成);~~

* 确定各章节所对应的叶知识点(2020.5.15前完成).

## 分工：

人教版-初中 目录整理 [@dangming25](https://github.com/dangming25)

沪教版-初中 目录整理 [@dangming25](https://github.com/dangming25)

苏教版-初中 目录整理 [@dangming25](https://github.com/dangming25)

沪教版-高中 目录整理 慕容玖

人教版-高中 目录整理 暂缺

## 文件格式说明:

知识点文件以csv形式保存在``textbook-grade-chapters-full.csv``, 导入数据库后生成``chapter-nodes-leaves.csv``.

```
textbook-grade-chapter-tags/
├── textbook-grade-chapters-full.csv
├── chapter-nodes-leaves.csv
```


在``chapter-nodes-leaves.csv``文件新增一列，输入与章节对应的新知识点的ID运算.

```
% chapter-nodes-leaves.csv
ID,PATH,NAME
4,"人教版-初中->七年级上->第一章 有理数->1.1 正数和负数","1.1 正数和负数",
```
在上述两个文件新增一列，输入与该旧知识点对应的新知识点的ID.

> 注意csv文件中用英文逗号分割列数据.
> 当旧知识点与多个新知识点对应时，会涉及"且"和"或"运算，即要求同事满足两个知识点标签(且)还是只需满足其一(或), 用'and'和'or'连接两个ID.
>
> ```
> ID,PATH,NAME
> 4,"人教版-初中->七年级上->第一章 有理数->1.1 正数和负数","1.1 正数和负数",10307 and 10306
> ```


## 相关教程

* [如何使用Github进行协作编辑](http://docs.mathcrowd.cn/howtos/how_to_use_github.html)
