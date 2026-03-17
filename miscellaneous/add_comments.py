import re
import os

# To use this script, update the list of html files to process
files_to_process = [
    'index.html',
    'mobile-app.html',
    'software-dev.html'
]

# Get the directory of this script to resolve paths relative to the project root
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

for file in files_to_process:
    filepath = os.path.join(project_root, file)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()

    tokens = []
    # Match <div ...> and </div>
    for m in re.finditer(r'<div\b([^>]*)>|</div>', content, re.IGNORECASE):
        is_close = m.group(0).lower() == '</div>'
        if is_close:
            tokens.append({'type': 'close', 'start': m.start(), 'end': m.end()})
        else:
            class_match = re.search(r'class\s*=\s*(["\'])(.*?)\1', m.group(1), re.IGNORECASE)
            class_val = class_match.group(2) if class_match else ""
            tokens.append({'type': 'open', 'class': class_val})

    stack = []
    closes = []
    for t in tokens:
        if t['type'] == 'open':
            stack.append(t['class'])
        else:
            if stack:
                class_val = stack.pop()
                if class_val:
                    t['class'] = class_val
                    closes.append(t)

    content_list = list(content)
    for t in reversed(closes):
        class_val = t.get('class', '').strip()
        if class_val:
            # take the first class name if there are multiple
            first_class = class_val.split()[0]
            comment = f' <!-- .{first_class} -->'
            
            end_idx = t['end']
            
            # Check if there is already a comment
            ahead = content[end_idx:end_idx+30]
            if not re.match(r'\s*<!--', ahead):
                content_list.insert(end_idx, comment)

    new_content = "".join(content_list)
    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Processed {filepath}")
