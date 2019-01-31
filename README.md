# MachineLearningAction
#### 运行环境
    python3.7 
    iMAC一体机(系统macOS Mojave， 版本10.14.1)

## 遇到的问题

#### 1. pip3 install feedparser 时出现包冲突 pkg_resources.VersionConflict: (pip 18.1 (/usr/local/lib/python3.7/site-packages), Requirement.parse('pip==18.0'))
      解决方案
      第一步：重新安装 get-pip.py   在终端上执行 curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
      第二步： python3 get-pip.py
      第三步： 再次执行   pip3 install feedparser

