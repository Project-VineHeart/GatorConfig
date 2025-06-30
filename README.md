# 🐊 Data-Gator Configuration Web App

This is a lightweight Flask-based web application for generating `config.json` files to provision **Data-Gator** devices. Developed [University of Idaho](https://www.uidaho.edu/) for the [Data-Gator](https://github.com/Data-Gator), it provides a simple, browser-based form for entering Wi-Fi credentials and selecting sensor types for analog ports. Upon submission, a valid JSON configuration file is generated and offered for download.

---

## 🚀 Features

* Static HTML form styled with Bootstrap
* Dropdowns for selecting sensors per analog port
* Accepts Wi-Fi SSID and password
* Generates and downloads a `config.json` file
* Runs in Docker with an Nginx reverse proxy

---

## 📦 How It Works

1. User opens the web form in a browser.
2. Inputs Wi-Fi SSID and password.
3. Selects sensor types for:

   * Shallow Port
   * Middle Port
   * Deep Port
   * Generic Analog Port
4. Submits the form.
5. The Flask backend:

   * Parses the input
   * Writes a temporary `config.json` file
   * Sends it to the user as a download

---

## 🛠️ Setup Instructions

### Prerequisites

* Docker
* Docker Compose

---

### 1. Clone the Repository

```bash
git clone <your-repo-url> GatorConfig
cd GatorConfig
```

---

### 2. Build and Run the Application

```bash
docker-compose up --build
```

* Flask app runs on port `5000` internally
* Nginx reverse-proxies to it on port `80`

Visit `http://localhost` or `http://<your-device-ip>` to access the web app.

> 💡 If port 80 is in use, change `docker-compose.yml` to expose another port, like `8080:80`.

---

### 3. Using the App

* Enter your Wi-Fi credentials.
* Select sensors from dropdowns.
* Click **Generate File**.
* Your browser will download a ready-to-use `config.json`.

---

## 🔐 Security Notes

* No secret key or session management is required for this app.
* It's safe to use in a trusted local network.
* For public deployment, consider adding authentication or IP-based access controls.

---

## 📁 Example Output

```json
{
  "analog_ports": {
    "port_shallow": "MIJ02LMS",
    "port_middle": "TEROS_10",
    "port_deep": "NONE",
    "port_analog": "MIJ02LMS"
  },
  "wifi_ssid": "MyNetwork",
  "wifi_passwd": "secret123"
}
```

---

## 📂 File Structure

```
GatorConfig/
├── app/                  # Flask app module
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       └── index.html
├── static/               # Optional static files (CSS, JS)
├── run.py                # App entry point
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── nginx/
    └── nginx.conf
```
