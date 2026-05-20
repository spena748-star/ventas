## 2026-05-20 - Non-semantic interactive elements accessibility
**Learning:** Non-semantic interactive elements (e.g., <span> badges or <div> nav items used as buttons) must include role="button", tabindex="0", and keyboard event listeners for 'Enter' and 'Space' keys to be accessible to keyboard and screen reader users.
**Action:** Always include these attributes and a global or local keyboard listener when using non-button elements for interactions.
