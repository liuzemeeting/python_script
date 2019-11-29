一、docker与传统虚拟机对比
传统虚拟化技术是在硬件的基础上虚拟出多个操作系统
docker技术则是在操作系统的基础上通过操作系统的复用实现虚拟化，因此docker相比于传统虚拟化技术，
资源占用更少，效率更高
docker的优势
1.提供一致的运行环境，容易迁移
2.使用分层和镜像的概念，容易维护、扩展
3.虚拟机需要完整的操作系统，资源消耗大，docker只是一个进程
1、如何批量删除或者停止运行的容器？
docker kill/rm docker ps -aq
2、如何查看镜像支持的环境变量？
使用sudo docker run IMAGE env
3、本地的镜像文件都存放在哪里
Docker相关的本地资源存放在/var/lib/docker/目录下，其中container目录存放容器信息，graph目录存放镜像信息，aufs目录下存放具体的镜像底层文件。
4、容器退出后，通过docker ps 命令查看不到，数据会丢失么？
容器退出后会处于终止（exited）状态，此时可以通过 docker ps -a 查看，其中数据不会丢失，还可以通过docker start 来启动，只有删除容器才会清除数据。