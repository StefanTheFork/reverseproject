# made by penguinguy25, ported to reverse by bkgrnd/STF
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
import platform
import os
import psutil
from screeninfo import get_monitors
import subprocess

console = Console()

def get_cpu_name():
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output(["wmic", "cpu", "get", "Name"], universal_newlines=True)
            lines = [line.strip() for line in output.split("\n") if line.strip()]
            return lines[1] if len(lines) > 1 else platform.processor()
        elif platform.system() == "Linux":
            with open('/proc/cpuinfo', 'r') as f:
                for line in f:
                    if 'model name' in line:
                        return line.split(':')[1].strip()
        elif platform.system() == "Darwin":  # macOS
            output = subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"], universal_newlines=True)
            return output.strip()
    except Exception:
        pass
    return platform.processor() or "Unknown CPU"
    
def get_gpu_name():
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output(["wmic", "path", "win32_VideoController", "get", "name"], universal_newlines=True)
            lines = [line.strip() for line in output.split("\n") if line.strip()]
            return lines[1] if len(lines) > 1 else "Unknown GPU"
        elif platform.system() == "Linux":
            # Try lspci first
            try:
                output = subprocess.check_output(["lspci"], universal_newlines=True)
                for line in output.split('\n'):
                    if 'VGA compatible controller' in line or 'Display controller' in line:
                        return line.split(': ', 1)[1] if ': ' in line else line
            except:
                pass
            # Try nvidia-smi as fallback
            try:
                output = subprocess.check_output(["nvidia-smi", "--query-gpu=name", "--format=csv,noheader,nounits"], universal_newlines=True)
                return output.strip()
            except:
                pass
        elif platform.system() == "Darwin":  # macOS
            try:
                output = subprocess.check_output(["system_profiler", "SPDisplaysDataType"], universal_newlines=True)
                for line in output.split('\n'):
                    if 'Chipset Model:' in line:
                        return line.split(':')[1].strip()
            except:
                pass
    except Exception:
        pass
    return "Unknown GPU"

user_os = platform.system()
user_os_version = platform.version()
user_kernel_version = platform.release()
user_cpu = get_cpu_name()    
user_ram = round(psutil.virtual_memory().total / (1024 ** 3))
user_gpu = get_gpu_name()

# display info fallback if screeninfo fails
try:
    user_monitor = get_monitors()[0]
    width = user_monitor.width
    height = user_monitor.height
except Exception:
    width, height = "Unknown", "Unknown"

user_minifetch_specs = f"""
[#52FFBA]host OS:[/#52FFBA] {user_os}
[#52FFBA]host CPU:[/#52FFBA] {user_cpu}
[#52FFBA]host RAM (GB):[/#52FFBA] {user_ram}
[#52FFBA]host GPU:[/#52FFBA] {user_gpu}
[#52FFBA]host Display width:[/#52FFBA] {width}
[#52FFBA]host Display height:[/#52FFBA] {height}
"""

logo = r"""
[#A378C2]      
         __     
        /\ \   
       /  \ \  
      / /\ \ \ 
     / / /\ \_\
    / / /_/ / /
   / / /__\/ / 
  / / /_____/  
 / / /\ \ \    
/ / /  \ \ \   
\/_/    \_\/   
minifetch by PenguinGuy

[/#A378C2]
"""

def sysfetch():
    logo_frame = Panel.fit(logo, border_style="#A378C2")
    specs_frame = Panel.fit(user_minifetch_specs, border_style="#52FFBA")
    console.print(Columns([logo_frame, specs_frame]))

