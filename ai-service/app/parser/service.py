from app.parser.loader import PDFLoader


class PDFService:

    def __init__(self):
        self.loader = PDFLoader()

    def load_pdf(self, file_path: str):
        return self.loader.load(file_path)