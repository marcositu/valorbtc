#!/bin/bash
valor=`curl https://www.bitstamp.net/api/v2/ticker/btcusd/ -s | awk -F ': "' '{print $5}' | cut -c1-6`
if [ $(echo "$valor<56196" | bc) == 1 ] ; then
curl "https://api.telegram.org/botxxxxx/sendMessage?chat_id=xxxxxxx&text=${valor}&parse_mode=markdown" >/dev/null 2>/dev/null
fi

