class Command:
    def execute(self):
        raise NotImplementedError()

# публікувати роботу  
class PublishArtWorkCommand(Command):
    def __init__(self, artwork):
        self.artwork = artwork

    def execute(self):
        self.artwork.status = 'published'
        self.artwork.save()

# продана робота
class MarkAsSoldCommand(Command):
    def __init__(self,artwork):
        self.artwork = artwork

    def execute(self):
        self.artwork.status = 'sold'
        self.artwork.save()

# приховати
class SetDraftCommand(Command):
    def __init__(self, artwork):
        self.artwork = artwork

    def execute(self):
        self.artwork.status = 'draft'
        self.artwork.save()