this simple website consist only of one page that 
the i make to help me to track to position of the train instead of going to the station early and wait a long time till the train arive 

so it works by putting the trainid that i wanna to track and someone else already in the train will put the trainid and choace to volunteer with its location

and using the browser api to give the current locaion of  the person that vlounteer with this every second and send it to the server through a websocket connection 

to send it to anyone monitor that train through a websocket connection 


the server side is very simple just daphne server and behind it django asgi application that handle http and websockets and using django channels to handle groups and sending the event to groups 
