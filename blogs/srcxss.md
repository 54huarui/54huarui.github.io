# 关于xss在src的补充

<br>

## 写在前面

<br>

好久没有再接触过xss，最近系统性地重新学了一遍，现在再做一些补充

<br>

## 分类和识别

<br>

能直接出回显的是反射型xss

能直接写入，刷新还在的是存储型xss ：常见于评论

<br>

## XSS常用payload

<br>

````
xss:
<script>alert(123);</script>
<a href="">xxx</ a>

dom xss:视情况而定

````