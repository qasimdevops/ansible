#!/bin/bash
service=$(systemctl is-active nginx)
if [[  "$service"  ==  "active"  ]]; then
	echo "nginx is running"
else
	echo "nginx is not running"
fi
