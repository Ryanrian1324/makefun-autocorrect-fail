"""Entry for u-zeroxfive-funniest-autocorrect-fail."""
import os

ENTRY = "Texted my landlord 'the sink is leaking' - sent as 'the sin is leaking.' He offered to pray over my kitchen. Took three texts to prove I needed a wrench, not an exorcist."

out = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
