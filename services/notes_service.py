

class NotesService:

    def __init__(self, agent_service):
        self.agent_service = agent_service
        self.notes = {}  # K:V, note_id : notes
        self.counter = 1

    def create_note(self, note: str):
        self.notes[self.counter] = note
        self.counter += 1
        return self.counter - 1

    def summarize_note(self, note_id: int):
        return self.agent_service.summarize_note(self.notes[note_id])
