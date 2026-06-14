## 2026-06-14 - Icon-only Button Accessibility
**Learning:** Icon-only buttons (using emojis or symbols) without text labels are inaccessible to screen readers and can be ambiguous for users. Adding `aria-label` provides the necessary semantic context for assistive technologies, while `title` provides a visual tooltip for mouse users.
**Action:** Always include `aria-label` and `title` when implementing icon-only interactive elements, especially when using emojis as icons.

## 2026-06-14 - Destructive Action Consistency
**Learning:** Found an inconsistency where `deleteCli` was missing a confirmation dialog while other delete functions had one.
**Action:** Ensure all destructive actions (deletes, resets) have consistent confirmation prompts to prevent accidental data loss.
