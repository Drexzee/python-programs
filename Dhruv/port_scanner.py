import socket

# Function to save results to a file
def save_results(results):
    with open("scan_results.txt", "a") as file:
        file.write(results + "\n")

# Function to check if port is open and save results
def scan_port_and_save(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(5)  # 5 second timeout
    result = sock.connect_ex((target, port))  # Connect to the target and port
    
    # Determine if the port is open or closed
    result_message = f"Port {port} {'open' if result == 0 else 'closed'} on {target}"
    
    # Print the result to the console
    print(result_message)
    
    # Save the result to the file
    
    save_results(result_message)
    
    sock.close()

# Main code
def main():
    try:
        # Ask the user for multiple targets (comma-separated)
        targets = input("Enter target IPs or domains (comma-separated): ").split(',')
        
        # Define the ports to scan
        ports = [22, 80, 443, 8080, 53, 21, 25, 3306]  # Add more ports as needed
        
        # Loop over each target
        for target_ip in targets:
            target_ip = target_ip.strip()  # Remove extra spaces
            if not target_ip:
                raise ValueError("No target specified")

            print(f"Scanning {target_ip}...")
            for port in ports:
                scan_port_and_save(target_ip, port)
                
        print("Scan completed. Results saved in 'scan_results.txt'.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
