## 2025-05-14 - Restoring Keyboard Focus Visibility
**Learning:** In applications where `outline: none` is used extensively for aesthetics, keyboard users are left without navigation cues. Using `:focus-visible` with `!important` is a safe way to restore accessibility without impacting the visual design for mouse users.
**Action:** Always audit for `outline: none` and implement a `:focus-visible` ring using theme-consistent colors.
