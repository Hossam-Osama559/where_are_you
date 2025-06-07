this simple website consist only of one page that 
i make to help me to track the position of the train instead of going to the station early and wait a long time till the train arive 

so it works by putting the train id that i wanna to track and someone else already in the train will put the train id and select to volunteer with its location

and using the browser api to give the current locaion of  the person that vlounteer with this every second and send it to the server through a websocket connection 

to send it to anyone monitor that train through a websocket connection 


the server side is very simple just daphne server and behind it django asgi application that handle http and websockets and using django channels to handle groups and sending the event to groups




requirements 

1--django channels 

2--daphne server or any asgi server that can handle websockets 

no data base needed i put all work and data in the client side 

------------------------------------------

run it just using python manage.py runserver

