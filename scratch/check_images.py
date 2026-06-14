import re, os
root = r'C:\Users\hp\OneDrive\Desktop\TinkeresLab'
with open(os.path.join(root, 'technical-innovation.html'), encoding='utf-8') as f:
    content = f.read()
refs = sorted(set(re.findall(r'src="image/([^"]+)"', content)))
missing = [r for r in refs if not os.path.exists(os.path.join(root, 'image', r))]
print('Total refs:', len(refs))
print('Missing:', len(missing))
for m in missing:
    print('  MISSING:', m)
print('---')
print('Existing image dirs:')
for item in sorted(os.listdir(os.path.join(root, 'image'))):
    p = os.path.join(root, 'image', item)
    if os.path.isdir(p):
        print('  DIR:', item, '-', len(os.listdir(p)), 'files')
print('---')
print('extracted images:')
for item in sorted(os.listdir(os.path.join(root, 'image'))):
    if item.startswith('extracted_'):
        print(' ', item)
