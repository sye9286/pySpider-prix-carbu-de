# pySpider-prix-carbu-de
A Python spider for fetching the fuel price of a station in Kehl


crontab -e
*/5 8-21 * * * /usr/bin/python3 /home/sye/node_app/pySpider/prix-carbu-de.py >> /home/sye/node_app/pySpider/log.log 2>&1 &

every 5 mins of 8h-21h

log in "log.log"
data in "data.json"