import os
import json
import importlib
from aliyunsdkcore.client import AcsClient


class AliCloudConnection(AcsClient):

    def __getattr__(self, item):
        def handler(**kwargs):
            # 方法拼接类名： ecs_describe_instances -> ecs产品下的 DescribeInstancesRequest
            names = str(item).split("_")  # 产品 资源方法类
            cls_name = "".join(map(lambda x: str(x).lower().capitalize(), names[1:])) + "Request"  # 类名
            package = importlib.import_module(f"aliyunsdk{names[0]}.request")  # request包
            module = [n for n in os.listdir(package.__path__[0]) if str(n)[1:].isdigit()][0]  # 当前版本的模块名          
            cls_path = f"aliyunsdk{names[0]}.request.{module}.{cls_name}"  # 类的全路径          
            req = getattr(importlib.import_module(cls_path), cls_name)
            if not req:
                raise ECSException(f'get AliYun method failed: {item}')
            request = req()
            request.set_accept_format('json')
            list(map(lambda kv: getattr(request, f'set_{kv[0]}')(kv[1]), kwargs.items()))
            result = self.do_action_with_exception(request)
            return json.loads(result)

        return handler
ak = "your ak"
secret = "secret"
conn = AliCloudConnection(ak, secret, "cn-beijing")
print(conn.ecs_describe_instances(PageSize=50))  # 虚机
