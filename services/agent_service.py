

class AgentService:

    def __init__(self, client):
        self.client = client

    def summarize_note(self, note: str):
        prompt = f"""
            Summarize the following note clearly and concisely, avoid
            being too wordy. Use bullet points and section headers,
            limit to at most 5 bullet points:
            {note}
        """

        return self.client.generate(prompt)
