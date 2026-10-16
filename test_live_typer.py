#!/usr/bin/env python3
"""Live typing commits only words two consecutive live transcripts agree on."""

from whisper_dictate import LiveTyper

nw = LiveTyper.new_words
# trailing word is never committed, even if stable
assert nw(["Hey", "do"], ["Hey", "do"], []) == ["Hey"]
# cut-off last word ("g" -> "go") stays out
assert nw(["Okay,", "let's", "g"], ["Okay,", "let's", "go", "now"], []) == ["Okay,", "let's"]
# punctuation/case flips still count as agreement (the 11:13 test typed nothing)
assert nw(["Hey.", "do"], ["Hey,", "do", "you"], []) == ["Hey,", "do"]
assert nw(["Hey,", "do", "you", "hear", "what?"],
          ["Hey", "do", "you", "hear", "what", "I'm"], ["Hey,"]) == ["do", "you", "hear", "what"]
# only words beyond what's already typed
assert nw(["Hey", "do", "you"], ["Hey", "do", "you", "hear"], ["Hey"]) == ["do", "you"]
# shrinking result: nothing new, nothing re-typed
assert nw(["Hey", "do", "you", "hear"], ["Hey", "do"], ["Hey"]) == []
# typed prefix no longer matches: wait for the final transcript
assert nw(["Hi", "there", "you"], ["Hi", "there", "you"], ["Okay"]) == []
print("ok")
