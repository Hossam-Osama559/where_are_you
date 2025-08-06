import json
from channels.generic.websocket import AsyncWebsocketConsumer


from asgiref.sync import sync_to_async


class handle_new_client(AsyncWebsocketConsumer):



    def __init__(self, *args, **kwargs):



        super().__init__(*args, **kwargs)


    async def connect(self):

        print("new client")

        self.group_name=""

        await self.accept()
    
    async def disconnect(self, close_code):
        print("disconnect")
    
        if self.group_name:
            await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "unregister_volunteer"
            }
        )
            await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )


             
    

    async def receive(self,text_data):

        print(" new msg ")

        obj=json.loads(text_data)

        if obj["msg_type"]=="1":

            # sending the location to all users that monitoring the same train
            print(obj["x"], "  ",obj["last_x"])

            self.group_name=obj['trainid']

            await self.channel_layer.group_send(
                f"{obj['trainid']}",

                {

                    "type":"updating_location",

                    "last_x":obj["last_x"],

                    "last_y":obj["last_y"],

                    "x":obj["x"],

                    "y":obj["y"]
                }
            )
        

        elif obj["msg_type"]=="2":
            # register the user into the group of that train
            self.group_name=obj["trainid"]
            
            await self.channel_layer.group_add(

                f"{obj['trainid']}",
                self.channel_name
            )

        

        elif obj["msg_type"]=="3":

            # tell the users that exist in a specific group the volunteer stoped his giving 
            self.group_name=""
            await self.channel_layer.group_send(

                f"{obj['trainid']}",

                {

                    "type":"unregister_volunteer",
                }
            )





    async def updating_location(self,event):

        
        await self.send(

            text_data=json.dumps(
                {

                "type":"1",

                "last_x":event["last_x"],

                "last_y":event["last_y"],

                "x":event["x"],

                "y":event["y"]
                }
            )
        )
    

    async def unregister_volunteer(self,event):


        await self.send(

            text_data=json.dumps(

                {

                    "type":"2",

                }
            )
        )

            

