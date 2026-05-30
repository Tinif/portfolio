import os
import json

def update_certificates():
    cert_dir = 'assets/certificates_and_achievements'
    data_file = 'data.js'
    
    # Check if directory exists
    if not os.path.exists(cert_dir):
        os.makedirs(cert_dir)
        
    valid_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.webp'}
    certificates = []
    
    for filename in os.listdir(cert_dir):
        ext = os.path.splitext(filename)[1].lower()
        if ext in valid_extensions:
            # Name without extension is the caption
            caption = os.path.splitext(filename)[0]
            # Replace underscores or hyphens with spaces for better readability
            caption = caption.replace('_', ' ').replace('-', ' ')
            
            certificates.append({
                "src": f"{cert_dir}/{filename}",
                "caption": caption
            })
            
    # Write to data.js
    with open(data_file, 'r') as f:
        content = f.read()
        
    # We will just rewrite the file, but keep other stuff if it exists.
    # Actually, let's just overwrite data.js or replace the specific variable.
    
    # Safe overwrite:
    js_content = f"const certificatesData = {json.dumps(certificates, indent=4)};\n"
    
    with open(data_file, 'w') as f:
        f.write(js_content)
        
    print(f"Successfully updated data.js with {len(certificates)} certificates.")

if __name__ == '__main__':
    update_certificates()
