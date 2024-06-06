import os
import subprocess

# Define a function to filter out non-printable characters
def filter_non_printable(text):
    return ''.join(char for char in text if char.isprintable() or char.isspace())

# Define a function to generate the directory tree with formatting
def generate_directory_tree(root_dir, prefix=""):
    tree_output = ""
    items = os.listdir(root_dir)
    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        if item == "node_modules" or item == ".git" or item == ".vscode":
            continue  # Exclude specified directories
        path = os.path.join(root_dir, item)
        if os.path.isdir(path):
            tree_output += f"{prefix}├── {item}/\n"
            if not is_last:
                next_prefix = f"{prefix}│   "
            else:
                next_prefix = f"{prefix}    "
            tree_output += generate_directory_tree(path, next_prefix)
        else:
            tree_output += f"{prefix}├── {item}\n"
    return tree_output

# Specify the root directory to start the tree
root_directory = "./"  # Change this to the desired root directory

# Generate the directory tree
directory_tree = generate_directory_tree(root_directory)

# Filter the output to remove non-printable characters
filtered_output = filter_non_printable(directory_tree)

# Save the filtered output to a Markdown file
output_path = "./docs/directory_tree.md"  # Change this to your desired output path
with open(output_path, "w") as file:
    file.write("```bash\n")
    file.write(filtered_output)
    file.write("\n```")

print(f"Directory tree saved to {output_path}")
