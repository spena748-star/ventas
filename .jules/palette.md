## 2026-06-16 - [Accessibility & Feedback Consolidation]
**Learning:** The application consistently utilized icon-only buttons without ARIA labels and labels without 'for' attributes across multiple panels. Additionally, destructive actions (deletion) lacked consistent confirmation prompts, creating a risk of accidental data loss.
**Action:** Always verify 'for'/'id' associations in dynamically generated forms (like the Edit modal) and ensure all CRUD tables include confirmation dialogs and descriptive ARIA labels for icon buttons.
