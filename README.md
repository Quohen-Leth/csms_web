# Web Backend for Charging Station Management System.
### Description:
REST API to manage Charging Stations. Based on Django with DRF.
Charging Stations could be connected with this [proxy](https://github.com/Quohen-Leth/csms_ocpp).
Charging Stations could be mocked with this [websockets server](https://github.com/Quohen-Leth/charging-station-mocking).

### Dev commands:
- run: `docker-compose -f docker-compose.dev.yml up --build --remove-orphans`
- manage: `docker-compose -f docker-compose.dev.yml exec web python3 src/manage.py`
