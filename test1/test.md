# 服务器性能测试

## 测试过程

使用**JMeter**测试服务器程序的并发性能

测试当线程池为5时，模拟不同并发量时的服务器性能指标

![1710688966023](image/test/1710688966023.png)

## 测试结果

数字解释

    线程数                     	平均每秒执行请求数    平均/最小/最大响应时间

**并发数为5**

![1710739661906](image/test/1710739661906.png)

**并发数为10**

![1710739761543](image/test/1710739761543.png)

**并发数为100**

![1710739812697](image/test/1710739812697.png)

**并发数为1000**

![1710739870231](image/test/1710739870231.png)

**并发数为2000**

![1710740108649](image/test/1710740108649.png)

当并发数大于2000时，电脑已出现明显卡顿。
