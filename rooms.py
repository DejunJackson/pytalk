"""Room and User objects"""


class Room:
    def __init__(self, name):
        self.name = name
        self.room = {}

    def show_users(self):
        return self.room

    def show_num_users(self):
        return len(self.room)

    def join_room(self, name, sock):
        self.room[name] = sock

    def broadcast(self, message):
        for client in self.room:
            self.room[client].send(message.encode('utf-8'))

    def leave_room(self, name, sock):
        if sock == self.room[name]:
            del self.room[name]
        else:
            self.room[name].send(
                "You can't make another player leave the room!".encode('utf-8'))


class User:
    def __init__(self, name, sock, current_room_name, current_room):
        self.name = name
        self.sock = sock
        self.current_room_name = current_room_name
        self.current_room = current_room
