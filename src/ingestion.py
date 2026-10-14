## RAG ingestion code
from pathlib import Path



def load_rag_document(rag_file_path):
    rag_file = Path(rag_file_path)
    supported_extensions = [".txt",".md"] #add supported extentions here
    ## validating file type
    if rag_file.is_file():

    #   print("file exits")
      if rag_file.suffix.lower() in supported_extensions:
        # print("file Type is Supported ")
        '''reading from rag file'''
        ## This is the data about the file i am ingesting so 
        
        rag_file_metadata = {
          "Source" : rag_file.name
        } 
        rag_file_content = rag_file.read_text(encoding="utf-8")
        if not rag_file_content.strip():
          raise ValueError("The Document is Empty")
        return {
          "content" : rag_file_content,
          "metadata" : rag_file_metadata
        }
        
      else:
        raise ValueError("File not supported")
    else:
      #print("file does not exist")
      raise FileNotFoundError("File not Found")


## writing this temp will remove after taking reeal document
temp_rag_content = load_rag_document("/home/ahmad-rauf/Documents/Projects/RAG-Forge/RAG-Forge/data/rag_file.txt")
print(temp_rag_content)










