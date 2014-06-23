#!/usr/bin/python3
import sh
import re
xinputstring = str(sh.xinput(list=True))
ids = re.findall('USB\sLaser\sGame\sMouse\s+id=[0-9]+', xinputstring)
for mouseid in ids:
    avariable = re.search('id=[0-9]+', mouseid).group()[3::]
    listofproperties = str(sh.xinput("list-props", avariable))
    if re.search('Device\sAccel\sProfile', listofproperties):
        sh.xinput("set-prop", avariable, 'Device Accel Profile', "-1")
        sh.xinput("set-prop", avariable, 'Device Accel Velocity Scaling', "1")
        sh.xinput("set-prop", avariable, 'Device Accel Constant Deceleration', "7")
