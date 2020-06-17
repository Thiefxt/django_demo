"""
@Author				: xiaotao
@Email				: 18773993654@163.com
@Lost modifid		: 2020/6/17 16:45
@Filename			: consumers.py
@Description		:
@Software           : PyCharm
"""
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    """
    这是一个异步的WebSocket使用者，它接受所有连接，从其客户端接收消息，并将这些消息回显到同一客户端。目前，它不会将消息广播到同一房间中的其他客户端
    """
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

# class ChatConsumer(WebsocketConsumer):
#     """
#     这是一个同步的WebSocket使用者，它接受所有连接，从其客户端接收消息，并将这些消息回显到同一客户端。目前，它不会将消息广播到同一房间中的其他客户端
#     """
#     def connect(self):
#         # 每个使用者都有一个范围，该范围包含有关其连接的信息，尤其包括URL路由和当前经过身份验证的用户（如果有）中的任何位置或关键字参数
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#
#         # 直接从用户指定的房间名称构造通道组名称，而无需引号或转义。
#         # 组名只能包含字母，数字，连字符和句点。因此，此示例代码将在包含其他字符的房间名称上失败。
#         self.room_group_name = 'chat_%s' % self.room_name
#
#         # 加入一个小组。
#         # 需要使用async_to_sync（…）包装器，因为ChatConsumer是一个同步WebsocketConsumer，但是它正在调用异步通道层方法。（所有通道层方法都是异步的。）
#         # 组名仅限于ASCII字母数字，连字符和句点。由于此代码直接从会议室名称构造一个组名称，因此如果会议室名称包含组名称中无效的任何字符，它将失败。
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         # 接受WebSocket连接。
#         # 如果未在connect（）方法内调用accept（），则连接将被拒绝并关闭。例如，您可能想拒绝连接，因为没有授权执行请求的用户执行请求的操作。
#         # 如果您选择接受连接，建议将accept（）作为connect（）中的最后一个动作
#         self.accept()
#
#     def disconnect(self, close_code):
#         # 离开一组
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#
#         # 将事件发送到组。
#         # 事件具有一个特殊的'type'键，该键对应于应在接收该事件的使用者上调用的方法的名称。
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#
#     def chat_message(self, event):
#         message = event['message']
#
#         # Send message to WebSocket
#         self.send(text_data=json.dumps({
#             'message': message
#         }))
