from flask import Flask, request, jsonify
import subprocess

def check_host_up(ip_address):
    # Run ping command
    result = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    
    # Check the return code
    if result.returncode == 0:
        return True
    else:
        return False

# Example usage
#ip_address = "192.168.1.1"
#if check_host_up(ip_address):
#    print(f"The host {ip_address} is up!")
#else:
#    print(f"The host {ip_address} is down.")

app = Flask(__name__)

# Function to read IPs from JSON file
def read_ips():
    with open("ips.json", "r") as f:
        ips = json.load(f)
    return ips

# Function to write IPs to JSON file
def write_ips(ips):
    with open("ips.json", "w") as f:
        json.dump(ips, f, indent=4)

# Route to get all IPs
@app.route('/ips', methods=['GET'])
def get_ips():
    ips = read_ips()
    return jsonify(ips)

# Route to add an IP
@app.route('/ips', methods=['POST'])
def add_ip():
    data = request.json
    ip = data.get('ip')
    if not ip:
        return jsonify({'error': 'IP address not provided'}), 400
    ips = read_ips()
    ips.append(ip)
    write_ips(ips)
    return jsonify({'message': 'IP added successfully'})

# Route to remove an IP
@app.route('/ips/<ip>', methods=['DELETE'])
def remove_ip(ip):
    ips = read_ips()
    if ip not in ips:
        return jsonify({'error': 'IP address not found'}), 404
    ips.remove(ip)
    write_ips(ips)
    return jsonify({'message': 'IP removed successfully'})

if __name__ == '__main__':
    app.run(debug=True)
