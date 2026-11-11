import re

date = "2026-03-03"
hostname = "SW-Core-01"
level = "CRITICAL"
message = "%LINK-3-UPDOWN: Interface GigabitEthernet0/2, changed state to up"

# 正则，两个捕获分组：group1=接口名，group2=状态
pattern = r"Interface (\S+), changed state to (\S+)"
result = re.search(pattern, message)

if result:
    intf_name = result.group(1)
    state = result.group(2)
    print(f"日期 : {date}")
    print(f"设备 : {hostname}")
    print(f"等级 : {level}")
    print(f"接口 : {intf_name}")
    print(f"状态 : {state}")

