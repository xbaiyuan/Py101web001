# CH0 打开百宝箱，探索你的学习节奏

## 工欲善其事，必先利其器

### 正面

本周是课程预备周，你需完成一些基本环境配置，以便畅快创作。包括编程环境，个人教程撰写环境，并熟悉CLI基本操作。

当然，最重要的还是立即上手编程。上手时，你很容易遇到的问题是：被看似困难的任务吓倒，幻想多，实践少。如何解决这个问题？

### 反面

《WOOP心理学》的作者厄廷根做了无数实验后发现：人在幻想自己做某件事时，会真的以为自己已经做完了那件事。

电影中的程序员像武侠，一番奇遇之后，成就绝世武功。

现实中的编程更像手艺人，眼、手、心三管其下，心下安宁，才能技艺有成。

所以，降伏其中，把念头和心力都放在：

编程

编程

编程

别被环境配置困住太久，把最重要的编程任务忽略啦。



## ch0课程安排

### 正面

课程每周节奏相对固定，本周你就可以开始摸索适合自己的学习节奏。

本章课程安排如下：

* 领取任务：0wd6前解锁「启程~ch0节奏」共计4个卡包，了解本章任务。
* 自主探索：自主安排学习时间，记录探索过程和经验，教六个月前的自己学Python。
* 集体即时答疑：0wd6 学员群即时答疑、交流。
* 提交任务：1wd1前，提交本章任务到课程Github Issues，详见本章任务说明Issues。

哦对，别忘了参加 0wd4(170105) 19:42 的线上开学典礼哟。详情请见邮件通知。

### 反面

遇到疑问欢迎在Issues中交流探讨，养成良好的Issues使用习惯后，你将有能力向全世界的程序员们发起问题，收获解答。

* 疑问发布到 Issues 中，提问方式参考 Issue 提问模板
* 教练异步答疑
* 尽量不要在微信群里讨论技术问题

重温一下 [提问的智慧](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way) 吧！



### ch0课程任务

正面：演示视频

反面：

* 上手CLI基础
* GitBook 搭建 
* Python 基础语法 
* 运行 Python 程序
* pip 的安装和使用



### 上手CLI基础

正面

CLI ~ Command Line Interface命令行界面

整个互联网都建筑在CLI的基础上，此时此刻，你看着这一行字时，无数命令行在背后默默运作。熟悉命令行，是你踏入新世界大门的第一步。

早期的计算机操作系统都只有命令行操作模式，现在非常流行的“图形用户界面（GUI - Graphical User Interface）”的概念最早由施乐公司的一名工程师提出，在它提出来不久之后，乔布斯看到了GUI，把它用在了苹果电脑上。

在GUI发明以前，CLI（命令行用户界面）是用户操控计算机的唯一途径。

在命令行界面下，你可以：

* 输入一行命令（尽管可以不止一行）直接与计算机互动；
* 爽快地编辑代码、执行代码；
* 高效地管理系统；
* 大多数服务器的操作；
* …….

要想顺利的完成后期课程的任务，我们需要掌握 CLI 下的：

- 调用 Python 来执行 Python 程序；
- 创建文件、编辑文件并保存退出；
- 对文件和文件夹的内容查看、复制、粘贴和重命名等操作；
- ……

既已决定踏上编程之路，那就尽快用上CLI， 享受手指在键盘上跳舞的快乐吧。不少程序员都喜欢用键盘（而非鼠标）操控一切哦。

### 背面

每台计算机里都内置命令行界面，比如 Windows 系列的 cmd 和 PowerShell， Mac 里的 Terminal 等，也可以使用功能更为强大的第三方 CLI 工具。使用时可参考以下资料：

Windows 系列：

- [cmder](http://cmder.net/)
- [Bash on Ubuntu on Windows](https://msdn.microsoft.com/en-us/commandline/wsl/about)
- [Windows PowerShell Basics](https://msdn.microsoft.com/zh-cn/powershell/scripting/getting-started/fundamental/windows-powershell-basics)
- [Table of Basic PowerShell Commands](https://blogs.technet.microsoft.com/heyscriptingguy/2015/06/11/table-of-basic-powershell-commands/)

OS X 系列：

- [iTerm2](http://www.iterm2.com/)
- [Basic Linux Commands](http://www.comptechdoc.org/os/linux/usersguide/linux_ugbasics.html)

另外，你知道哪些 CLI 玩法和功能？欢迎写入Gitbook和学友们分享：D

## 在CLI管理你的Github仓库~Git

### 正面

写论文时，你是否修改了无数个版本？如果有一天，老师让你调出两星期前的版本，你能在无数个版本中找到它么？

再比如，你想和好朋友一起创作一本悬疑小说，你如何确保ta写的那部分，没有覆盖你写的？

Git版本管理系统就是为了解决这些问题应运而生的。有了它，你再也不用担心文章备份和远程协作，一切修订均有记录。

- 你可以利用 Git 无限次提交已经修改过的代码到 GitHub。
- 如果你对修改后的代码不满意，又可以回到过去的任意版本。

通过学习 Git，你就可以在命令行界面（CLI）使用 Git 的各种命令来存储及提交作业到 GitHub，这又是对工作效率的一次提升！

来玩耍折腾一下 Git 吧~

### 反面

本着 20/80 原则，大家首先要掌握的是

- 将 GitHub 仓库 Clone 到本地（git clone/git pull）
- 用 Git 提交代码到 GitHub (git commit/git push)

关于其他 Git 的用法，学有余力的同学可以自行折腾，当然，不要忘记将你折腾的整个过程分享出来哦~

以下为参考资料：

- [猴子都能懂的Git入门](http://backlogtool.com/git-guide/cn/)
- Set Up Git - User Documentation：[https://help.github.com/articles/set-up-git/](https://help.github.com/articles/set-up-git/)
- 在线 git 练习：[https://try.github.io/](https://try.github.io/)
- [廖雪峰的 Git 教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)



## 用 GitBook 发布你的思考

### 正面

为什么使用Gitbook来发布你的思考？因为Gitbook的树形结构，能让你的思路更清晰。

> MIT 认知科学家 Josh 发表在 pnas 的论文中，比较了抽象知识的不同表征结构，如星形结构、聚类结构、环形结构等等，最终发现，**人类的最佳抽象知识结构是树形结构**。只有树形结构，才是最符合人类认知特点的一种结构，从树的上一层到下一层，具备唯一通道，便于大脑将知识从记忆底层快速提取出来，符合人类大脑是个认知吝啬鬼的特点；树又是兼具横向扩展与纵向扩展能力的最优雅的结构。
>
> 所以，**儿童学习词汇时，最初是将物体进行扁平互斥的划分并对应到不同名称，当他们意识到，以树形结构来学习时，他们的认知开始大幅度发展**。这种神秘的树形结构不仅仅影响到儿童早期的认知发展，在科学界，也处处可以看到神秘之树的身影，如门捷列夫的元素周期表开创近代化学；卡尔·冯·林奈使用树形结构创立了对生物世界的基本分类法。
>
> — 阳志平

课程已为你搭好图书框架——你 Fork 的 Py103 仓库，里面已按章节创建好目录结构，你可以持续在每章 note 路径下记录相应折腾心路。

如果你有余力，可以让这些内容更像一本书：用 GitBook 把你的 Markdown 文档汇集成电子书，并生成多种格式 (pdf/epub/网页等) 。

GitBook 还可以和 GitHub 仓库关联，你更新 GitHub 仓库内容， GitBook 便可自动更新。

### 背面

往期学员撰写的 GitBook ，可从 [https://github.com/AIMinder/Py103/wiki/IdxGoodPractice](https://github.com/AIMinder/Py103/wiki/IdxGoodPractice) 了解。

GitBook 的配置，详见：

- [Introduction | GitBook Documentation](https://help.gitbook.com/)
- [Can I host my content on GitHub? · GitBook Help Center](https://help.gitbook.com/github/can-i-host-on-github.html#webhooks)

发布形式只是外在，关键是**先完成本周编程任务**哟！



## 夯实 Python 基础

### 正面

入学任务里，你已通过《Learn Python the Hard Way》的练习掌握了 Python 的基础知识，现在咱们再回过头来思考几个问题：

- 为什么选择 Python 作为我们的编程入门语言？
- 这份 [极简 Python 上手导念](http://wiki.zoomquiet.io/pythonic/MinimalistPyStart) 在说什么？
- 我需要掌握到什么程度？

### 背面

参考：

- [自虐式 Pythonic 入门记要 | Zoom.Quiet Personal Static Wiki](http://wiki.zoomquiet.io/pythonic/BePythonic)
- [The Python Tutorial - 2.7](https://docs.python.org/2/tutorial/index.html)
- [The Python Tutorial - 3.5](https://docs.python.org/3.5/tutorial/index.html)

欢迎把你的思考记录下来，告诉给六个月前的自己哟。



## 提交 ch0 任务

### 正面

`提交时限`：1wd1(170109) 11:42 前，提交本章任务到课程 GitHub Issues

`提交方式`：详见[本章任务说明 Issue ](https://github.com/AIHackers/Py101OC/blob/cards/PackPy103)（你也可以从本章任务通告邮件中找到此链接）

教练团会在以下时间给出反馈：

- `0wd6` 19:42 前，从已提交的任务中，抽 2-3 份，提供视频点评反馈 # 早提交多受益，你懂的 ;-)
- `1wd2` 19:42 前，在 GitHub 上给所有已提交 ch0 任务、个人教程的学员文字反馈

### 背面

也欢迎你多多给其他学友作品鼓励、建议，主动做那只帮别人挠痒痒的猴子~

> 主动做那只帮别人挠痒痒的猴子，让知识快速流动，形成更好的学习氛围，更能帮助自己更好地学习。 ——阳志平《[如何学习编程——来自认知科学的四个建议](http://mp.weixin.qq.com/s?__biz=MzA4ODM4ODQ3MQ==&mid=2651930555&idx=1&sn=d5535c8707dcc9bcf58fe06d73ea0dc3&chksm=8bcf79a3bcb8f0b5dfbd0e5d999f371b39d52a1e3af550303f9bd62e63509dcd92d1d028df90#rd)》