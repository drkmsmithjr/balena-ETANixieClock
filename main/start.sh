#!/usr/bin/bash



#start wifi-connect.  This will start an access point if none is found
export DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket

#Is there an active WiFi connection?
iwgetid -r

if [ $? -eq 0 ]; then
    printf 'Skipping WiFi Connect\n'
else
    printf 'Starting WiFi Connect\n'
    # wifi connect will timeout after 5 minutes.   Giving lots of time 
    ./wifi-connect --portal-ssid="ETANixieClock Connect" --activity-timeout=300
fi

#./wifi-connect --portal-ssid="ETANixieClock Connect" --activity-timeout=300



# Default to UTC if no TIMEZONE env variable is set
echo "Setting time zone to ${TIMEZONE=America/Los_Angeles}"
# This only works on Debian-based images
echo "${TIMEZONE}" > /etc/timezone
# for this container, we also need to remove local time if it exists
if [ -f /etc/localtime ]; then
    rm /etc/localtime
fi
dpkg-reconfigure tzdata

# GoogleKey will be passed from Resin
# the MQTTUSER - username and MQTTPW-password will also be passed the ETAclock if available. 
if [ "${RUNETACLOCK="True"}" == "True" ]; then  
    printf 'Starting ETAClock\n'
    python /app/ETAclock.py ${GOOGLEKEY} ${MQTTUSER} ${MQTTPW} ${MQTTBROKER}
else
    printf 'Skipping Clock Run\n'
    while :
    do
        echo "Press [CTRL+C] to stop.."
        sleep 1
    done
fi
# python /app/DummyStart.py

#while :
#do
#   echo "Press [CTRL+C] to stop.."
#   sleep 1
#done
