#!/bin/bash

if ps -ef | grep -e "/bin/bash ./parser.sh" 1> /dev/null ; then
	echo -e "parser OK"
else
	echo -e "parser ERROR"
fi

if ps -ef | grep -e "SCREEN python3 binance_api.py" 1> /dev/null ; then
        echo -e "binance_api OK"
else
        echo -e "binance_api ERROR"
fi

if ps -ef | grep -e "SCREEN python3 report_check.py" 1> /dev/null ; then
        echo -e "report_check OK"
else
        echo -e "report_check ERROR"
fi

if ps -ef | grep -e "python3 ./an2linuxserver.py" 1> /dev/null ; then
        echo -e "an2linuxserver OK"
else
        echo -e "an2linuxserver ERROR"
fi
