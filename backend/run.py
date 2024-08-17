from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Function to categorize logs based on severity
def categorize_log(log):
    log_lower = log.lower()
    if any(keyword in log_lower for keyword in ["emergency", "alert", "critical", "error", "failure", "failed"]):
        return 'critical'
    elif any(keyword in log_lower for keyword in ["warning", "warn"]):
        return 'warning'
    else:
        return 'normal'

# Function to get and categorize system logs
def get_logs():
    logs_raw = subprocess.check_output(['journalctl', '-n', '100', '--no-pager']).decode('utf-8').splitlines()
    logs = [{'text': log, 'category': categorize_log(log)} for log in logs_raw]
    return logs

# Function to categorize services based on their state
def categorize_service(service):
    service_lower = service.lower()
    if 'loaded active running' in service_lower or 'loaded active exited' in service_lower:
        return 'normal'
    elif 'failed' in service_lower or 'inactive (dead)' in service_lower or 'not-found' in service_lower:
        return 'critical'
    elif 'loaded inactive' in service_lower or 'active (exited)' in service_lower:
        return 'warning'
    else:
        return 'warning'  # Default to warning for any unrecognized states

# Function to get and categorize service statuses
def get_services():
    services_raw = subprocess.check_output(['systemctl', 'list-units', '--type=service', '--all']).decode('utf-8').splitlines()
    services = [{'text': service.strip(), 'category': categorize_service(service.strip())} for service in services_raw if service and 'service' in service]
    return services

@app.route('/api/data')
def get_data():
    logs = get_logs()
    services = get_services()
    
    normal_count = sum(1 for item in logs + services if item['category'] == 'normal')
    warning_count = sum(1 for item in logs + services if item['category'] == 'warning')
    critical_count = sum(1 for item in logs + services if item['category'] == 'critical')
    total_alerts_count = warning_count + critical_count
    
    return jsonify({
        'logs': logs,
        'services': services,
        'counts': {
            'normal': normal_count,
            'warning': warning_count,
            'critical': critical_count,
            'total_alerts': total_alerts_count
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

# Function to categorize logs based on severity
def categorize_log(log):
    log_lower = log.lower()
    if any(keyword in log_lower for keyword in ["emergency", "alert", "critical", "error", "failure", "failed"]):
        return 'critical'
    elif any(keyword in log_lower for keyword in ["warning", "warn"]):
        return 'warning'
    else:
        return 'normal'

# Function to get and categorize system logs
def get_logs():
    logs_raw = subprocess.check_output(['journalctl', '-n', '100', '--no-pager']).decode('utf-8').splitlines()
    logs = [{'text': log, 'category': categorize_log(log)} for log in logs_raw]
    return logs

# Function to categorize services based on their state
def categorize_service(service):
    service_lower = service.lower()
    if 'loaded active running' in service_lower or 'loaded active exited' in service_lower:
        return 'normal'
    elif 'failed' in service_lower or 'inactive (dead)' in service_lower or 'not-found' in service_lower:
        return 'critical'
    elif 'loaded inactive' in service_lower or 'active (exited)' in service_lower:
        return 'warning'
    else:
        return 'warning'  # Default to warning for any unrecognized states

# Function to get and categorize service statuses
def get_services():
    services_raw = subprocess.check_output(['systemctl', 'list-units', '--type=service', '--all']).decode('utf-8').splitlines()
    services = [{'text': service.strip(), 'category': categorize_service(service.strip())} for service in services_raw if service and 'service' in service]
    return services

@app.route('/api/data')
def get_data():
    logs = get_logs()
    services = get_services()
    
    normal_count = sum(1 for item in logs + services if item['category'] == 'normal')
    warning_count = sum(1 for item in logs + services if item['category'] == 'warning')
    critical_count = sum(1 for item in logs + services if item['category'] == 'critical')
    total_alerts_count = warning_count + critical_count
    
    return jsonify({
        'logs': logs,
        'services': services,
        'counts': {
            'normal': normal_count,
            'warning': warning_count,
            'critical': critical_count,
            'total_alerts': total_alerts_count
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Function to categorize logs based on severity
def categorize_log(log):
    log_lower = log.lower()
    if any(keyword in log_lower for keyword in ["emergency", "alert", "critical", "error", "failure", "failed"]):
        return 'critical'
    elif any(keyword in log_lower for keyword in ["warning", "warn"]):
        return 'warning'
    else:
        return 'normal'

# Function to get and categorize system logs
def get_logs():
    logs_raw = subprocess.check_output(['journalctl', '-n', '100', '--no-pager']).decode('utf-8').splitlines()
    logs = [{'text': log, 'category': categorize_log(log)} for log in logs_raw]
    return logs

# Function to categorize services based on their state
def categorize_service(service):
    service_lower = service.lower()
    if 'loaded active running' in service_lower or 'loaded active exited' in service_lower:
        return 'normal'
    elif 'failed' in service_lower or 'inactive (dead)' in service_lower or 'not-found' in service_lower:
        return 'critical'
    elif 'loaded inactive' in service_lower or 'active (exited)' in service_lower:
        return 'warning'
    else:
        return 'warning'  # Default to warning for any unrecognized states

# Function to get and categorize service statuses
def get_services():
    services_raw = subprocess.check_output(['systemctl', 'list-units', '--type=service', '--all']).decode('utf-8').splitlines()
    services = [{'text': service.strip(), 'category': categorize_service(service.strip())} for service in services_raw if service and 'service' in service]
    return services

@app.route('/api/data')
def get_data():
    logs = get_logs()
    services = get_services()
    
    normal_count = sum(1 for item in logs + services if item['category'] == 'normal')
    warning_count = sum(1 for item in logs + services if item['category'] == 'warning')
    critical_count = sum(1 for item in logs + services if item['category'] == 'critical')
    total_alerts_count = warning_count + critical_count
    
    return jsonify({
        'logs': logs,
        'services': services,
        'counts': {
            'normal': normal_count,
            'warning': warning_count,
            'critical': critical_count,
            'total_alerts': total_alerts_count
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

# Function to categorize logs based on severity
def categorize_log(log):
    log_lower = log.lower()
    if any(keyword in log_lower for keyword in ["emergency", "alert", "critical", "error", "failure", "failed"]):
        return 'critical'
    elif any(keyword in log_lower for keyword in ["warning", "warn"]):
        return 'warning'
    else:
        return 'normal'

# Function to get and categorize system logs
def get_logs():
    logs_raw = subprocess.check_output(['journalctl', '-n', '100', '--no-pager']).decode('utf-8').splitlines()
    logs = [{'text': log, 'category': categorize_log(log)} for log in logs_raw]
    return logs

# Function to categorize services based on their state
def categorize_service(service):
    service_lower = service.lower()
    if 'loaded active running' in service_lower or 'loaded active exited' in service_lower:
        return 'normal'
    elif 'failed' in service_lower or 'inactive (dead)' in service_lower or 'not-found' in service_lower:
        return 'critical'
    elif 'loaded inactive' in service_lower or 'active (exited)' in service_lower:
        return 'warning'
    else:
        return 'warning'  # Default to warning for any unrecognized states

# Function to get and categorize service statuses
def get_services():
    services_raw = subprocess.check_output(['systemctl', 'list-units', '--type=service', '--all']).decode('utf-8').splitlines()
    services = [{'text': service.strip(), 'category': categorize_service(service.strip())} for service in services_raw if service and 'service' in service]
    return services

@app.route('/api/data')
def get_data():
    logs = get_logs()
    services = get_services()
    
    normal_count = sum(1 for item in logs + services if item['category'] == 'normal')
    warning_count = sum(1 for item in logs + services if item['category'] == 'warning')
    critical_count = sum(1 for item in logs + services if item['category'] == 'critical')
    total_alerts_count = warning_count + critical_count
    
    return jsonify({
        'logs': logs,
        'services': services,
        'counts': {
            'normal': normal_count,
            'warning': warning_count,
            'critical': critical_count,
            'total_alerts': total_alerts_count
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
