import os
import zipfile

pptx_path = r"c:\Users\hp\OneDrive\Desktop\TinkeresLab\image\DAY 1.pptx"
extract_dir = r"c:\Users\hp\OneDrive\Desktop\TinkeresLab\image"

os.makedirs(extract_dir, exist_ok=True)

with zipfile.ZipFile(pptx_path, 'r') as z:
    for name in z.namelist():
        if name.startswith("ppt/media/"):
            basename = os.path.basename(name)
            # Prefix them to make them clear
            out_name = f"extracted_{basename}"
            out_path = os.path.join(extract_dir, out_name)
            with open(out_path, 'wb') as f_out:
                f_out.write(z.read(name))
            print(f"Extracted {name} to {out_path}")
