# 配置学习环境

- 目标
    + 帮助同学熟悉开发环境，建立良好的学习节奏，学会提交作业

- 内容要点
    + Python 开发环境
    + IPython 开发环境
    + 在 CLI 调试
    + 如何提交代码到 GitHub
    + 如何提问


## 缩写


- CLI: Command Line Interface
- GUI: Graphical User Interface
- PM: Package Management
- PyPi: [Python Package Index](https://pypi.python.org/pypi) Python 包仓库



## 易迷惑


- Terminal(终端)
    + 电线的末端
    + Shell 的图形用户接口

- Command Line(命令行)
    + Shell 的文本接口

- Shell
    + 乌龟的壳
    + 操作系统的接口

- Console(控制台)
    + 带面板的机柜

- tty
    + 打字机
- 参考
    + [终端，Shell，“tty”和控制台（console）有什么区别？](https://www.zhihu.com/question/21711307)


## 配置

- Terminal
    + macOS
        * iterm2
    + Linux
        * terminal
    + Windows
        * cmder ( > windows xp)
        * windows powershell
        * cmd
    + cmds
        * 进入目录
            - cd <dirname>
        * 返回上一层目录
            - cd ..
        * 新建目录
            - mkdir <dirname>
        * 新建文件
            - touch <filename>
        * 文件列表
            - ls 
        * 更改文件/目录所有者
            - sudo chown
        * 更改文件/目录权限
            - sudo chmod
        * linux/unix/mac unix-like os
            - . 当前目录
            - .. 上一级目录
            - ／ 系统根目录

- Shell
    + bash
        * default shell
    + zsh
        * brew install zsh
        * chsh -s `which zsh` 
        * if output 'chsh: which zsh: non-standard shell'
        * chsh -s /bin/zsh
        * restart iterm2
        * install zsh 主题配置文件 oh-my-zsh
        * sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
        * vim ~/.zshrc
        * ZSH_THEME="avit"
        * restart iterm2
        * 参考
            - [1](http://wulfric.me/2015/08/zsh/)
            - [2](https://github.com/robbyrussell/oh-my-zsh/wiki/themes)
    + fish
    + 
- PM
    + pip
        * for Python 软件包
        * install
            - 如果 Python 2 的版本大于等于 2.7.9 或者 Python 3 的版本大于等于 3.4，则 pip 已经安装好了
            - 如果已安装了虚拟环境管理程序 virtualenv 或者 pyvenv, 则 pip 也已安装
        * cmds
            - pip install package
            - pip uninstall package
            - pip install -r requirements.txt
            - pip freeze > requirements.txt
            - 参考
                + [1](https://pip.pypa.io/en/stable/)
    + npm
        * for node 
        * 
    + homebrew
        * for macOS
        * install
            - ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
            - make some directories
            - install Command Line Tools (macOS Sierra version 10.12) for Xcode
            - ...
        * cmds
            - brew install package(安装包)
            - brew uninstall package(卸载包)
            - brew update(更新服务器包目录)
            - brew upgrade(升级包)
            - brew list(列出已安装的包)
        * 参考
            - https://laoshuterry.gitbooks.io/mac_os_setup_guide/content/2_PackageManagement.html
            - [Mac安装软件新方法：Homebrew-cask](http://www.yangzhiping.com/tech/homebrew-cask.html)
    + dpkg
    + apt
    + yum
    + 
- Python 版本管理
    + PATH
        * 一串目录路径
        * 每条路径之间以分号或冒号分隔
        * 当在终端中输入一个命令时
        * 操作系统会从左至右，搜索每一条路径
        * 直到相应路径下的目录有匹配的可执行文件与命令对应
    + virtualenv
        * install
            - [sudo] pip install virtualenv
        * cmds
            - virtualenv venv(在当前目录下创建一个名称为 venv 的虚拟环境)
            - source bin/activate(激活虚拟环境)
            - deactivate(退出虚拟环境)
        * [参考](https://virtualenv.pypa.io/en/stable/reference/)
    + pyenv
        * install(macOS)
            - brew install pyenv
        * cmds
            - 查看正在使用的 Python 版本
                + pyenv version
            - 查看系统中已安装的 Python 版本
                + pyenv versions
            - 查看当前可以安装的 Python 版本
                + pyenv install --list
            - 安装相应版本的 Python
                + pyenv install <Python 版本号>
            - 设置全局 Python 版本
                + pyenv global <Python 版本号>
            - 设置局域 Python 版本
                + cd <dir_name>
                + pyenv local <Python 版本号>
            - 卸载 Python 
                + pyenv uninstall <Python 版本号>
            - 确定当前目录使用 Python 版本
                + python -V
                + 或者
                + which python
        * 参考
            - [pyenv commands](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-shell)
            - [pyenv official site](https://github.com/pyenv/pyenv#simple-python-version-management-pyenv)
            - [pyenv Tutorial](https://amaral.northwestern.edu/resources/guides/pyenv-tutorial)
- Python
    + macOS
        * 默认安装了 Python 2.7
        * CLI
            - 
        * GUI
            - find
                + [Python.org](https://www.python.org/)
            - download
                + [download Python](https://www.python.org/downloads/release/python-361/)
                + Python 3.6.1
            - install
                + double click and next
    + Linux
        * 默认安装了 Python 2.7
        * CLI
            - 
        * GUI
            - like macOS
    + Windows
        * CLI
            - 
        * GUI
            - like macOS
- IPython
    + 参考
        * [IPython Documentation](http://ipython.readthedocs.io/en/stable/)
- Jupyter Notebook
- Git
    + 
- GitHub
    + location
    + sign up
    + sign in
    + SSH
    + GUI
    + 
- Gitbook
- Text Editor
    + sublime text 3
        * install
            - package control
            - markdown editing
            - markdown extended
            - markdown preview
        * settings
            - "translate_tabs_to_spaces": true
            - "font_face": "Monoid-Retina"
    + atom
    + vim
    + ...
- 开智APP
    + WEB
        * http://www.openmindclub.com/
    + APP
    + 


## 如何提问

- 识别问题
- 描述问题
- 解决问题


参考


