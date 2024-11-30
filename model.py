# models.py
from langchain_ollama import OllamaLLM

class Models:
    def __init__(self):
        """Initialize the Models class."""
        self.llm = None  # Initialize llm attribute as None

    def mistral(self):
        """Create and return an instance of the Mistral LLM."""
        try:
            self.llm = OllamaLLM(base_url="http://localhost:11434", model="llama3.1", temperature=0)
            print("LLM instance created successfully.")
            return self.llm
        except Exception as e:
            print(f"An error occurred while creating the LLM instance: {e}")
            return None
