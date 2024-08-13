# DOCKER

<br>


最近搞了很多有关docker的东西，有一些东西由于时效性已经失去功能，这里来算是补充

## 安装docker

docker可以直接apt install安装，但是docker-com需要本地安装。国内很多镜像源并没有docker-com

<br>

## 常用命令(只记一半的)

````
docker ps 查看所有正在进行容器进程 -a可以查看已停止的进程
docker images 查看已经构建的镜像
docker build 构建镜像
docker exec 和自己的镜像终端进行链接
docker rm 删除容器进程
docker rmi 删除镜像
````

<br>

## 镜像源问题

由于某不可抗力，国内传统镜像源大多已挂，这里贴一个最近还能用的

来源：

https://github.com/tech-shrimp/docker_installer?tab=readme-ov-file

````
{
    "registry-mirrors": [
        "https://docker.m.daocloud.io",
        "https://docker.1panel.live",
        "https://hub.rat.dev"
    ]
}
````

<br>

## ctf出题

感谢探姬helloctf，CTF-Archives的模板，提供了很多可用成品dockers供平台搭建
以下是一些模板:
````
https://github.com/CTF-Archives/ctf-docker-template/releases
````