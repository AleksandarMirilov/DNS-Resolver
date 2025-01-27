import socket

def resolve_domains(domain_list):
    """
    Resolves a list of domain names to their corresponding IP addresses.
    """
    resolved_results = {}
    for domain in domain_list:
        try:
            ip = socket.gethostbyname(domain)
            resolved_results[domain] = ip
            print(f"{domain} -> {ip}")
        except socket.gaierror:
            resolved_results[domain] = None
            print(f"Error: Unable to resolve {domain}")
    return resolved_results

def save_results_to_file(results, filename="dns_results.txt"):
    """
    Saves the resolved domain-IP pairs to a file.
    """
    try:
        with open(filename, "w") as file:
            for domain, ip in results.items():
                if ip:
                    file.write(f"{domain} -> {ip}\n")
                else:
                    file.write(f"{domain} -> Resolution Failed\n")
        print(f"Results saved to {filename}")
    except IOError as e:
        print(f"Error: Unable to write to file: {e}")

if __name__ == "__main__":
    print("Welcome to the DNS Resolver!")
    domains = input("Enter domain names separated by commas (e.g., google.com, yahoo.com): ")
    domain_list = [d.strip() for d in domains.split(",")]

    # Resolve domains
    results = resolve_domains(domain_list)

    # Ask the user if they want to save the results
    save_option = input("Do you want to save the results to a file? (yes/no): ").lower()
    if save_option in ("yes", "y"):
        save_results_to_file(results)
    else:
        print("Results not saved. Exiting...")
