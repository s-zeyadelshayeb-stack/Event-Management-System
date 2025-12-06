class Event:
    def __init__(self, event_id, title, description, date):
        self.event_id = event_id
        self.title = title
        self.description = description
        self.date = date


    def to_dict(self):
        return {
            "event_id": self.event_id,
            "title": self.title,
            "description": self.description,
            "date": self.date,
        }
    
    