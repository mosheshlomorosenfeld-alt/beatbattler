# Loop Packs (Download + Zip)

Binary files are not committed to git.

To fetch free loop files and create ZIPs for each battle, run:

```bash
python assets/loop-packs/download_free_loops.py
```

This script downloads free loop files and creates:
# Loop Packs (Source-Only in Repo)

Binary files are intentionally excluded from git.

To generate downloadable `.zip` loop packs locally, run:

```bash
python assets/loop-packs/generate_loop_packs.py
```

This creates:
- `soul_flip_42.zip`
- `drum_surgery_18.zip`
- `ambient_trap_09.zip`

If any URL expires, replace it directly in `download_free_loops.py`.
Each pack includes WAV loops and a README with BPM/key/license metadata.
