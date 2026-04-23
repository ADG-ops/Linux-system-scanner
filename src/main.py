import psutil
import platform

def get_system_info():
    print("--- System Information ---")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Hostname: {platform.node()}")
    
    print("\n--- CPU Usage ---")
    print(f"Load: {psutil.cpu_percent()}%")
    
    print("\n--- Memory Usage ---")
    mem = psutil.virtual_memory()
    print(f"Total: {mem.total / (1024**3):.2f} GB")
    print(f"Used: {mem.percent}%")
    
    print("\n--- Disk Usage ---")
    disk = psutil.disk_usage('/')
    print(f"Total: {disk.total / (1024**3):.2f} GB")
    print(f"Used: {disk.percent}%")

if __name__ == "__main__":
    get_system_info()
