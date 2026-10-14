## chunking
from ingestion import load_rag_document
# This function splits the data into pieces
def documentChunking(retreived_document_data):
    rag_file_metadata = retreived_document_data["metadata"]
    rag_file_content = retreived_document_data["content"]

    # chunking the data 
    chunk_size = 100
    overlap = 20
    start_index = 0

    if chunk_size<=0 or chunk_size<=overlap or overlap <0:
       raise ValueError("Incorrect Values added")
    
    # spliting the rag file content 
    rag_file_words = rag_file_content.split()


    
    #next index formula -> next_index = start_index + chunk_size - overlap
    chunks = []
    rag_file_len = len(rag_file_words)
    while start_index<rag_file_len:
      if chunks and rag_file_len - start_index <= overlap:
        break
      else:
          end_index = start_index + chunk_size
          curr_chunk = rag_file_words[start_index:end_index]
          curr_chunk = " ".join(curr_chunk)
          start_index = start_index + chunk_size - overlap
          chunks.append({
              "content": curr_chunk,
              "metadata": rag_file_metadata
          })
    
    return chunks


temp_rag_content = load_rag_document("/home/ahmad-rauf/Documents/Projects/RAG-Forge/RAG-Forge/data/rag_file_180words.txt")
temp_chunks = documentChunking(temp_rag_content)
print(temp_chunks)