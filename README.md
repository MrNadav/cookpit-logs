#  Cockpit Logs

## Overview

Custom Cockpit Dashboard is a web application designed to monitor system logs and services in real-time. It consists of a React-based frontend that provides a clean and responsive interface, and a Flask backend that serves API data by interacting with the system. The project is configured to run as a service on Linux using systemd, ensuring that the backend starts automatically on system boot.

## Features

- **Real-time Monitoring**: View and filter system logs and service statuses.
- **Responsive Design**: The interface adjusts seamlessly across various screen sizes.
- **Interactive Dashboard**: Clickable count boxes to filter logs and services by category (normal, warning, critical).
- **Expandable Sections**: Logs and services sections can be toggled open or closed for better visibility.
- **Systemd Integration**: The backend runs as a systemd service, ensuring automatic startup on boot.

