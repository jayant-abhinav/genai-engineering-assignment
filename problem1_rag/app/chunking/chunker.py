from uuid import uuid4
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from problem1_rag.app.models.document import Document
from problem1_rag.app.models.chunk import DocumentChunk
from problem1_rag.app.core.config import CHUNK_SIZE
from problem1_rag.app.core.config import CHUNK_OVERLAP

class Chunker:

    # Splits documents into overlapping chunks.
    def __init__(self, chunk_size: int = CHUNK_SIZE, chunk_overlap: int = CHUNK_OVERLAP,):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ],
        )

    def chunk_document(self, document: Document,) -> List[DocumentChunk]:

        pieces = self.splitter.split_text(document.text)
        chunks = []

        for index, piece in enumerate(pieces):

            chunks.append(
                DocumentChunk(
                    chunk_id=str(uuid4()),
                    source=document.source,
                    file_type=document.file_type,
                    text=piece,
                    chunk_index=index,
                    metadata=document.metadata.copy(),
                )
            )
        return chunks

    def chunk_documents(self, documents: List[Document],) -> List[DocumentChunk]:

        all_chunks = []

        for document in documents:
            all_chunks.extend(
                self.chunk_document(document)
            )
        return all_chunks