from pathlib import Path
import json


def main() -> int:
    status_path = Path(__file__).with_name("build_env_status.json")
    status = {"reportlab": False, "error": None}
    try:
        import reportlab  # noqa: F401
        status["reportlab"] = True
    except Exception as exc:
        status["error"] = str(exc)
    status_path.write_text(json.dumps(status, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
