# 高级分布式系统线上作业题

作业在头歌([educoder](https://www.educoder.net/))平台完成, 这里是个人兴趣使然把题目扒下来, 使用 [Docker](https://docs.docker.com/engine/install/) 构建本地的运行测试环境。

本次作业一共有两个题目, 第一个是实现 **Paxos** 算法, 第二个实现分布式缓存一致性的 **写穿** 算法。

## 一些说明

1. 出于个人习惯, 对某些文件中的字符格式进行了修改, 不一定与线上测试平台匹配。提交线上作业检测时请复制 **所需的代码块**, <font color=#FF0000>切勿全部复制!!!</font>
2. 题目的描述详尽, 要求实现的代码逻辑较为简单。第一个题目在编译时存在一些 `警告`, 已在本仓库代码中进行修正, 但不影响答题的代码块; 第二个题目的设计和实现略显粗糙, 功能逻辑的实现不唯一。
3. 课程完全<font color=#FF0000>结束</font>后, 更新代码和报告。

## 镜像

创建

```shell
docker build -t ads:2022 .
```

`ads` 是高级分布式系统 (Advanced Distributed Systems) 的缩写, Tag 为 `2022` 年的线上作业

<font color=#FF0000>删除</font>

```shell
docker rmi ads:2022
```

## 容器

启动

```shell
docker run --name "ads2022" -di ads:2022
```

连接

```shell
docker exec -it ads2022 bash
```

停止

```shell
docker stop ads2022
```

<font color=#FF0000>删除</font>

```shell
docker rm ads2022
```

## 注意

工作目录为 `/root/ads`

在 `VSCode` 中, 可以使用 `Docker` 插件, 对容器进行 `Attach`
