from rooms.models import Room


def get_room_by_id(id):
    return Room.objects.filter(room_id=id).first()

