# Design notes — the sin is leaking

- Story: autocorrect turned "the sink is leaking" into "the sin is leaking".
- The humor escalates from a typo to a spiritual misunderstanding: the landlord
  offers prayer, and the punchline flips the resolution — wrench, not exorcist.
- Kept concrete (landlord, kitchen, three texts) so it reads like a real
  message thread, not a generic autocorrect joke.
- Entry text is 170 characters, inside the 200 limit.
- main.py stays a plain writer: entry text to $OUTPUT_DIR/entry.txt (default
  /output) so reproduce works unchanged.
