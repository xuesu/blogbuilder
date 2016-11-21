#Blog Builder
##by xuesu
##Version 0.0.1
###功能说明
Blog Builder是一个简单,轻量的静态博客生成工具,它无需任何数据库,其初步功能有

2. 将.md文件通过网页模板转化为网页
1. 按照用户文件目录树建立博客网站,请参照[http://xuesu.github.io](http://xuesu.github.io)
2. 用户可自定义模板元素
###使用说明
- python main.py execute &lt;blog文件所在位置&gt; 可以生成静态网站
- blog所在文件夹需如此布置:
	- &lt;blog文件所在位置&gt;文件夹下
		- _layout文件夹
			- default.html
				- 具体博客模板
				- 可选元素:
					- {{content}}代表.md文件转化后的html
					- {{title}}代表文件名称
			- defaultIndex.html
				- 主页模板
				- 可选元素:
					- {{category}}文件目录
		- _posts文件夹
			- 放入.md博客文件以及其他博客文件
			
### Attention
.md中不能出现\g符号，必须用\\g代替（因为re.sub）
