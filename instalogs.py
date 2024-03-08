import os
import json

def reformat_messages(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    reformatted_messages = []
    
    # Loop through messages in reverse order
    for message in reversed(data["messages"]):
        sender_name = message["sender_name"]
        # Check if "content" key exists
        if "content" in message:
            content = message["content"]
            if content:
                formatted_message = f"{sender_name}: {content}"
                reformatted_messages.append(formatted_message)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(reformatted_messages))

if __name__ == "__main__":
    # Get all JSON files in the same directory as the script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    json_files = [f for f in os.listdir(current_directory) if f.endswith('.json')]
    
    for json_file in json_files:
        input_file = os.path.join(current_directory, json_file)
        # Remove the ".json" extension from the file name
        output_file_name = os.path.splitext(json_file)[0]
        output_file = os.path.join(current_directory, f"Formatted Messages of {output_file_name}.txt")
        reformat_messages(input_file, output_file)
        print(f"Messages from {json_file} reformatted and saved to {output_file}")
