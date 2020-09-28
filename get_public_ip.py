from requests import get

def get_ip():
	ip = get("https://api.ipify.org").text
	return ip

def main():
	print("Your public IP is: " + get_ip())
	input("Press any button to close...")

if __name__ == "__main__":
	main()