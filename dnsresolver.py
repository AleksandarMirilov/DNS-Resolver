import socket

def resolve_domains(domain_list):
    for domain in domain_list:
        try:
            ip = socket.gethostbyname(domain)
            print(f"{domain} -> {ip}")
        except socket.gaierror:
            print(f"Failed to resolve {domain}")

if __name__ == "__main__":
    domains = input("Enter domains separated by commas (e.g., google.com, yahoo.com): ")
    domain_list = [d.strip() for d in domains.split(",")]
    resolve_domains(domain_list)
