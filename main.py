import os
import sys

def main():
    # Cat's 1-star review of its human (exact, deadpan, feline voice)
    review = (
        "1/5 stars. Hairless primate stares at glowing rectangle all day "
        "instead of warming my lap. When I walked across the keyboard to save its soul, "
        "it moved me with two hands. Unacceptable service."
    )
    
    length = len(review)
    print(f"Entry length: {length}/200 characters")
    if not (1 <= length <= 200):
        print(f"Error: length {length} out of bounds!", file=sys.stderr)
        sys.exit(1)
        
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(review)
        
    print(f"Successfully wrote entry to {output_path}")

if __name__ == "__main__":
    main()
