# -*- encoding:utf-8 -*-

from kscore.session import get_session
import json

if __name__ == "__main__":
    s = get_session()
    '''
    通用产品线，不包含容器（docker）
    '''
    #ListMetrics

    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m=client.list_metrics(InstanceID="3f092bb4-7461-4dac-9ee5-c60b75eeae22",Namespace="kec",PageIndex="1",PageSize="10")
    print json.dumps(m,sort_keys=True,indent=4)



    #GetMetricStatistics
    
    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m=client.get_metric_statistics(InstanceID="227d550e-88d4-428e-8b90-a9bc2ce16fc7",Namespace="eip",MetricName="qos.bps_in",StartTime="2019-11-27T20:09:00Z",EndTime="2019-11-27T20:19:00Z",Period="60",Aggregate="Average,Max,Min,Count,Sum")
    print json.dumps(m,sort_keys=True,indent=4)
    
    #GetMetricStatisticsBatch      version=2018-11-14
    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    param={
           "Namespace": "kec",
           "StartTime": "2019-11-27T14:00:00Z",
           "EndTime": "2019-11-27T14:09:00Z",
           "Period": "180",
           "Aggregate": ["Max","Min","Avg"],
           "Metrics": [
                       {
                        "InstanceID": "3f092bb4-7461-4dac-9ee5-c60b75eeae22",
                        "MetricName":"net.if.in"
                       },
                       {
                        "InstanceID": "3f092bb4-7461-4dac-9ee5-c60b75eeae22",
                        "MetricName":"cpu.utilizition.total"
                       },
                       {
                        "InstanceID": "ee321b50-1d9b-474c-92d0-ba007f0c01f6",
                        "MetricName":"rds.qpss"
                       }
                     ]
          }
    m=client.get_metric_statistics_batch_v2(**param)
    print json.dumps(m,sort_keys=True,indent=4)
    

    '''
    只支持容器docker（kce），其余产品线不支持。
    '''
   #ListMetrics 
    paraml={
    "Action":"ListMetrics",
    "Version":"2019-08-12",
    "Namespace":"kce",
    "PageIndex":"1",
    "PageSize":"10",
    "Dimensions.0.Name":"ClusterId",
    "Dimensions.0.Value":"807a4149-b7e2-4e05-8a35-b77221ce5bb8",
    "Dimensions.1.Name":"NamespaceName",
    "Dimensions.1.Value":"kube-system",
    "Dimensions.2.Name":"WorkloadType",
    "Dimensions.2.Value":"deployment",
    "Dimensions.3.Name":"WorkloadName",
    "Dimensions.3.Value":"system-monitor",
    "Dimensions.4.Name":"PodName",
    "Dimensions.4.Value":"system-monitor-69f6d456bf-r7khs",
   # "Dimensions.5.Name":"ContainerName",
   # "Dimensions.5.Value":"ksc-metrics-pusher"
    }

    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m=client.list_metrics_v3(**paraml)
    print json.dumps(m,sort_keys=True,indent=4)



    #GetMetricStatistics
    paramg={
    "Action":"GetMetricStatistics",
    "Version":"2019-08-12",
    "Namespace":"kce",
    "MetricName":"pod.network.rx",
    "StartTime":"2019-11-26T17:09:00Z",
    "EndTime":"2019-11-26T17:19:00Z",
    "Period":"60",
    "Aggregate":"Average,Max,Min,Count,Sum",
    "Dimensions.0.Name":"ClusterId",
    "Dimensions.0.Value":"807a4149-b7e2-4e05-8a35-b77221ce5bb8",
    "Dimensions.1.Name":"NamespaceName",
    "Dimensions.1.Value":"kube-system",
    "Dimensions.2.Name":"WorkloadType",
    "Dimensions.2.Value":"deployment",
    "Dimensions.3.Name":"WorkloadName",
    "Dimensions.3.Value":"system-monitor",
    "Dimensions.4.Name":"PodName",
    "Dimensions.4.Value":"system-monitor-69f6d456bf-r7khs",
   # "Dimensions.5.Name":"ContainerName",
   # "Dimensions.5.Value":"ksc-metrics-pusher"
    }

    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m=client.get_metric_statistics_v3(**paramg)
    print json.dumps(m,sort_keys=True,indent=4)    
    
