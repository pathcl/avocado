from pyVim.connect import SmartConnectNoSSL
from pyVmomi import vim
from jinja2 import Template
from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates')

host = os.environ.get("VSPHERE_VCENTER")
user = os.environ.get("VSPHERE_USER")
pswd = os.environ.get("VSPHERE_PASSWORD")

@app.route('/')
def index():
    si = SmartConnectNoSSL(host=host, user=user,
                           pwd=pswd, port=443)
    content = si.RetrieveContent()

    dc = content.viewManager.CreateContainerView(content.rootFolder,
            [vim.Datacenter], True)

    counter = 0
    datacenters = list(dc.view)
    events = []
    for dc in datacenters:
        alarms = dc.triggeredAlarmState
        for alarm in alarms:
            counter += 1
            events.append((alarm.entity.name, alarm.alarm.info.description, alarm.entity.overallStatus, str(alarm.time)))
    
    if counter >= 1:
        color = 'red'
    else:
        color = 'green'
    return render_template('index.html',color=color, counter=counter, events=events)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
