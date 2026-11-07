"""Mirror the public FRAME library of this repository into the FRAME Maintainers SharePoint library (one way).

The master of the library is this repository (the website links to it). The SharePoint copy is read-only for the
Maintainers: files are added or replaced, never deleted, and every target folder gets a _MIRROR.txt that says where
the files come from. Run it after the library changed, then upload the target folders to SharePoint (or point it at
the OneDrive-synchronised library).

usage: python tools/mirror_library.py <SharePoint General folder> [--apply]
"""
import sys, os, shutil, subprocess, datetime
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dest_root = sys.argv[1]; APPLY = '--apply' in sys.argv
LIB, LEG, PUB = '10_Inputs/FRAME Library', '10_Inputs/Legacy Repository/Tools', '40_Published/Tool Releases/v5.1.1'
RULES = [  # (prefix in the repository, target folder); the first match wins, the rest of the path is kept
    ('docs/assets/docs/articles/', f'{LIB}/Articles'),
    ('docs/assets/docs/brochures/', f'{LIB}/Brochures'),
    ('docs/assets/docs/reports/', f'{LIB}/Reports'),
    ('docs/assets/docs/deliverables/', f'{LIB}/Deliverables'),
    ('docs/assets/docs/manuals/', f'{LEG}/Manuals'),
    ('docs/assets/docs/FRAME-Seminar', f'{LIB}/Seminars and Workshops'),
    ('docs/assets/docs/FRAME-Workshop', f'{LIB}/Seminars and Workshops'),
    ('docs/assets/tools/FRAME_Architecture_Tool_V5.1.1', PUB),
    ('docs/assets/tools/FRAME Toolbox_V1.0', PUB),
    ('docs/assets/tools/', LEG),
]
files = subprocess.run(['git', '-C', root, 'ls-files', '-z', 'docs/assets/docs', 'docs/assets/tools'], capture_output=True, check=True).stdout.decode().split('\0')
commit = subprocess.run(['git', '-C', root, 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
done, skipped, unmapped, targets = [], 0, [], set()
for f in filter(None, files):
    for pre, tgt in RULES:
        if f.startswith(pre):
            rest = f[len(pre):] if pre.endswith('/') else os.path.basename(f)
            d = os.path.join(dest_root, tgt, rest); targets.add(tgt); break
    else:
        unmapped.append(f); continue
    src = os.path.join(root, f)
    if os.path.exists(d) and os.path.getsize(d) == os.path.getsize(src):
        skipped += 1; continue
    done.append((f, os.path.relpath(d, dest_root)))
    if APPLY:
        os.makedirs(os.path.dirname(d), exist_ok=True); shutil.copy2(src, d)
if APPLY:
    for t in targets:
        with open(os.path.join(dest_root, t, '_MIRROR.txt'), 'w', encoding='utf-8') as fh:
            fh.write(f'Mirror of github.com/FRAME-ITS/FRAME-online (commit {commit}, {datetime.date.today()}).\n'
                     'Do not edit or add files here: the master is the repository. Changes go through a pull request.\n')
for f, d in done: print(f'{"copied" if APPLY else "to copy"}: {d}')
print(f'{len(done)} {"copied" if APPLY else "to copy"}, {skipped} unchanged, {len(unmapped)} not mapped')
for f in unmapped: print('not mapped:', f)
