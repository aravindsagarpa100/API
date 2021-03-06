# Name: RunDll32 with .inf Callback
# rta: rundll32_inf_callback.py
# ATT&CK: T1105
# Description: Loads RunDll32 with a suspicious .inf file that makes a local http GET

import time
import common

INF_FILE = common.get_path("bin", "script_launch.inf")


@common.dependencies(INF_FILE)
def main():
    # http server will terminate on main thread exit
    # if daemon is True
    common.log("RunDLL32 with Script Object and Network Callback")
    server, ip, port = common.serve_web()
    callback = "http://%s:%d" % (ip, port)
    common.clear_web_cache()

    common.patch_regex(INF_FILE, common.CALLBACK_REGEX, callback)

    rundll32 = "rundll32.exe"
    dll_entrypoint = "setupapi.dll,InstallHinfSection"
    common.execute([rundll32, dll_entrypoint, "DefaultInstall", "128", INF_FILE], shell=False)

    time.sleep(1)
    common.log("Cleanup", log_type="-")
    common.execute("taskkill /f /im notepad.exe")
    server.shutdown()


if __name__ == "__main__":
    exit(main())
