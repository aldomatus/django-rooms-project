from events.models import Event


def room_with_same_date(data):
    return len(Event.objects.filter(event_date__year=data["event_date"][:4],
                                    event_date__month=data["event_date"][5:7],
                                    event_date__day=data["event_date"][8:10],
                                    room_id=data["room"]))


def room_has_events(room_id):
    return Event.objects.filter(room_id=room_id).first()


def is_public_event(event_id):
    event = Event.objects.filter(event_id=event_id).first()
    return event.is_public


def get_room_id_by_event_id(event_id):
    event = Event.objects.filter(event_id=event_id).first()
    return event.room.room_id


def get_all_public_events():
    return Event.objects.filter(is_public=1).all()
