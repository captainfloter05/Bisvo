#!/usr/bin/python
# -*- coding: utf-8 -*-

import json


result_json = [{
       "target": "region1.host1.metric_name1",
                     "datapoints": [[123.2323232,1634083200]],    # value, timestamp
}]

result_data = {"timestamp":[],"host":[],"request_type":[],"value":[]}


str = result_json[0] 
print(str.items()[1][0])
gg = str.items()[0][1].split(".")
print(gg)

result_data["host"] = gg[1]
result_data["request_type"] = gg[2]

numbs = str.items()[1][1][0]

result_data["value"] = numbs[0]
result_data["timestamp"] = numbs[1]


print(result_data)


