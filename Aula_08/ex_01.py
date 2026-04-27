from datetime import datetime
from zoneinfo import ZoneInfo

data = datetime.now(ZoneInfo("America/Sao_Paulo"))
print(data)
print(data.date())
print(data.time())
