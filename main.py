from fastapi import FastAPI
from clients.ollama_client import OllamaClient
from services.agent_service import AgentService
from services.notes_service import NotesService
from pydantic import BaseModel


class Note(BaseModel):
    note: str


app = FastAPI()

ollama = OllamaClient()
agent = AgentService(ollama)
notes = NotesService(agent)


@app.get("/notes")
def get_notes():
    return notes.notes


@app.post("/notes")
def create_note(note: Note):
    id = notes.create_note(note.note)
    return {
        "id": id,
        "note": note.note
    }


@app.post("/notes/{note_id}/summarize")
def summarize_note(note_id: int):
    return {
        "summary": notes.summarize_note(note_id)
    }
