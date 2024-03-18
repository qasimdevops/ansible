#!/bin/bash
service_status=$(systemctl is-active sshd)
if [[ "$service_status" == "active" ]]; then
        echo "ssh is running!!!"
else
        echo "ssh is not running!!!"
fi

