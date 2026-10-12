## RAG ingestion code
from pathlib import Path

rag_file = Path("rag_file.txt")
if rag_file.is_file():
    print("file exits")
else:
    print("file does not exist")

## validating file type


supported_extensions = [".txt",".md"] #add supported extentions here

if rag_file.suffix.lower() in supported_extensions:
    print("file Type is Supported ")
else:
    print("file is not supported")

