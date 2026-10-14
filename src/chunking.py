## chunking

# This function splits the data into pieces
def documentChunking(retreived_document_data):
    rag_file_metadata = retreived_document_data["metadata"]
    rag_file_content = retreived_document_data["content"]

    # spliting the rag file content 
    rag_file_words = rag_file_content.split()

    # chunking the data 
    chunk_size = 100
    overlap = 20
    start_index = 0
    end_index = 100
    
    #next index formula -> next_index = start_index + chunk_size - overlap
    
    return ["chunk_data"]
