import json

with open('/tmp/config.json') as f:
    try:
        res = json.load(f)
    except ValueError as ex:
        print(ex)
        res = {}

print(res)

''' config.json should contain:
{
  "os": {"type":"windows", "version":"7"}.
  "browser": {"type":"firefox", "version":"35"}
}
'''