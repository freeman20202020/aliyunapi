# aliyunapi
短小精悍，你值得拥有，覆盖阿里云所有产品的API

#示例代码
ak = "your ak" # 阿里云access key
secret = "secret"  # 阿里云secret
conn = AliCloudConnection(ak, secret, "cn-beijing")  # 实例化连接，cn-beijing换成你所在的region
虚机调用示例  ecs: 产品 ecs/vpc/slb等，后面跟调用方法，去掉Request, 原方法aliyun-python-sdk-ecs下的 DescribeInstancesRequests
print(conn.ecs_describe_instances(PageSize=50)) 
