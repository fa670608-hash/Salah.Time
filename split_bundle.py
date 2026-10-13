# Usage: python3 split_bundle.py salah_time_bundle.txt
# Recreates every project file from the bundle text. Then add assets/logo.png yourself.
import os, re, sys
t = open(sys.argv[1], encoding='utf-8').read()
for m in re.finditer(r'=== FILE: (.+?) ===\n(.*?)\n=== END ===', t, re.S):
    p = m.group(1)
    if os.path.dirname(p): os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(m.group(2) + '\n')
    print('wrote', p)
