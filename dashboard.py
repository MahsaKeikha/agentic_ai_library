#!/usr/bin/env python3
"""Zero-dependency local web dashboard for the Agentic AI Library."""
from __future__ import annotations

import html
import json
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs

from launcher import registry, run_agent

HOST = "127.0.0.1"
PORT = 8765


def page(result: dict | None = None, selected: str = "F35", case_text: str = "{}", approve: bool = False) -> str:
    systems = registry()
    options = []
    for fid, item in systems.items():
        suffix = "external repo" if item["kind"] == "standalone" else "local runner"
        sel = " selected" if fid == selected else ""
        options.append(f'<option value="{fid}"{sel}>{fid} — {html.escape(item["name"])} ({suffix})</option>')

    rendered = ""
    if result is not None:
        rendered = f"<h2>Execution result</h2><pre>{html.escape(json.dumps(result, indent=2, ensure_ascii=False))}</pre>"

    checked = " checked" if approve else ""
    return f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agentic AI Library — F01-F170</title>
<style>
body {{ font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; max-width: 1100px; margin: 38px auto; padding: 0 20px; background:#f7f7f8; color:#161616; }}
.card {{ background:white; border:1px solid #ddd; border-radius:14px; padding:24px; margin-bottom:20px; box-shadow:0 3px 12px rgba(0,0,0,.04); }}
h1 {{ margin-bottom:6px; }} .muted {{ color:#666; }}
select, textarea {{ width:100%; box-sizing:border-box; margin-top:8px; margin-bottom:18px; padding:12px; border:1px solid #bbb; border-radius:9px; font:inherit; }}
textarea {{ min-height:210px; font-family:ui-monospace,SFMono-Regular,Menlo,monospace; }}
button {{ padding:11px 18px; border-radius:9px; border:0; background:#111; color:#fff; font-weight:600; cursor:pointer; }}
pre {{ white-space:pre-wrap; overflow-wrap:anywhere; background:#111; color:#eee; padding:18px; border-radius:10px; }}
.badge {{ display:inline-block; padding:5px 9px; border-radius:999px; background:#eee; margin-right:6px; font-size:13px; }}
</style>
</head>
<body>
<div class="card">
<h1>Agentic AI Library</h1>
<p class="muted">Unified local launcher for F01-F170. F27-F170 execute from this repository. F01-F26 point to their standalone repositories.</p>
<span class="badge">170 systems</span><span class="badge">offline-first</span><span class="badge">human-gated</span>
</div>
<div class="card">
<form method="post">
<label><strong>Select system</strong></label>
<select name="system">{''.join(options)}</select>
<label><strong>Case input (JSON)</strong></label>
<textarea name="case">{html.escape(case_text)}</textarea>
<label><input type="checkbox" name="approve" value="yes"{checked}> Record human approval for this run</label><br><br>
<button type="submit">Run selected system</button>
</form>
</div>
<div class="card">{rendered or '<p class="muted">Choose a system, optionally provide JSON evidence/context, and run it.</p>'}</div>
</body>
</html>"""


class Handler(BaseHTTPRequestHandler):
    def _send(self, body: str, status: int = 200) -> None:
        data = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:
        self._send(page())

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        form = parse_qs(self.rfile.read(length).decode("utf-8"))
        selected = form.get("system", ["F35"])[0]
        case_text = form.get("case", ["{}"])[0]
        approve = form.get("approve", [""])[0] == "yes"
        try:
            case = json.loads(case_text or "{}")
            if not isinstance(case, dict):
                raise ValueError("Case JSON must be an object/dictionary.")
            result = run_agent(selected, case, approve=approve)
            self._send(page(result, selected, case_text, approve))
        except Exception as exc:
            self._send(page({"error": str(exc)}, selected, case_text, approve), status=400)

    def log_message(self, format: str, *args) -> None:
        return


def main() -> None:
    url = f"http://{HOST}:{PORT}"
    print(f"Agentic AI dashboard running at {url}")
    print("Press Ctrl+C to stop.")
    try:
        webbrowser.open(url)
    except Exception:
        pass
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDashboard stopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
