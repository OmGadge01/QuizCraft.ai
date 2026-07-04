from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


class PDFLoader:

    def load(self, file_path: Path):
        loader = PyPDFLoader(str(file_path))
        return loader.load()