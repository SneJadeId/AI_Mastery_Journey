from langchain_text_splitters import RecursiveCharacterTextSplitter

##########################################################
# Read File
##########################################################

with open("sample_document.txt", "r", encoding="utf-8") as file:
    text = file.read()

##########################################################
# Create Text Splitter
##########################################################

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

##########################################################
# Validate Overlap
##########################################################

def validate_overlap(chunk1, chunk2, overlap_size=50):

    end_text = chunk1[-overlap_size:]
    start_text = chunk2[:overlap_size]

    if end_text == start_text:
        return end_text
    else:
        return None


##########################################################
# Print Results
##########################################################

print("=" * 80)
print("SMART SPLITTER PROOF")
print("=" * 80)

print(f"\nTotal Chunks Created : {len(chunks)}\n")

for i in range(len(chunks) - 1):

    print("=" * 80)
    print(f"Chunk {i+1}")
    print("=" * 80)
    print(chunks[i])

    print("\n")

    print("=" * 80)
    print(f"Chunk {i+2}")
    print("=" * 80)
    print(chunks[i+1])

    overlap = validate_overlap(chunks[i], chunks[i+1])

    print("\n")

    print("=" * 80)
    print("Extracted Overlap")
    print("=" * 80)

    if overlap:
        print(overlap)
    else:
        print("Overlap Not Found")

    print("\n\n")