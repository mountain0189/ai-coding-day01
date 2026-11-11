version_raw = "  Cisco IOS XE Software, Version 17.03.04  "
version_stripped=version_raw.strip()
print("去掉空格：" + version_stripped)
print("转大写：  " + version_stripped.upper())
print("替换版本：" + version_stripped.replace("17.03.04", "17.06.01"))
