![coder farmer](https://raw.githubusercontent.com/llsw/sgoly/dev/doc/sk/img/xixi.gif "0. 0")
#  分割日志工具
## 使用方法
### linux:
#### 1.将需割的日志放入rawLogs文件夹，可一次性放多个
#### 2.打开 终端 cd进入splitLog目录执行：
```Bash  
python splitLog.py
```
#### 3.解压后的日志文件在slicesLogs文件夹下

### windows:
#### 1.将需割的日志放入rawLogs文件夹，可一次性放多个
#### 2.打开 cmd cd进入logTool目录执行：
```Bash  
python splitLog.py
```
#### 3.解压后的日志文件在slicesLogs文件夹下


## 参数说明  
	python spliteLog.py [options]
	-m size, 以 size MB的大小分割日志，默认是10  
	-i path, 指定所需分割日志所在的目录，默认是./rawLogs  
	-o path, 指定分割后日保存的目录,默认是./slicesLogs  
## 中文乱码  
	如果分割后的日志文件用Sublime打开出现中文乱码，可以调整编码格式为UTF-8。  
	步骤如下(Sublime Text):  
	File --> Reopen with Encoding --> UTF-8