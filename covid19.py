import COVID19Py
import time
from plyer import notification

covid19=COVID19Py.COVID19(data_source="jhu")
latest = covid19.getLatest()
    
while True:

    notification.notify(
    title="Covid 19 UPDATES",
    message=str(latest),
    app_icon="C:/Users/Anjana Anil/OneDrive/Desktop/Project/covid.ico",
    timeout=2
  )
    time.sleep(24*3600)
