# Hardware And Software Constraints

## 2026-03-25 - Windows Store alias was not a reliable Codex automation target

### Problem

The packaged Codex app alias under `C:\Program Files\WindowsApps\...` could not be spawned reliably from automation.

### Resolution

Use a standalone Codex CLI binary at `C:\Users\xliup\bin\codex.exe` and target it explicitly from the wrapper.

### Durable Insight

For Windows automation, prefer an explicit standalone CLI path over the Store app alias.

## 2026-03-25 - Codex Windows sandbox sometimes blocked long stage writes

### Problem

Long ARIS stages could complete logically but still fail to persist artifacts because of the local Windows sandbox behavior.

### Resolution

Add `--dangerous-bypass` as an explicit local workaround for trusted workspaces.

### Durable Insight

On this machine, artifact persistence is more important than strict sandboxing for long trusted research runs.
