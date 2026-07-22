## 🗃️ Dataset Description

The dataset used in this project comprises real-time traffic performance data collected from the Seoul Transport Operation & Information Service ([TOPIS](https://data.seoul.go.kr)) via the Seoul Open Data Plaza. It consists of 5-minute interval road speed observations recorded over the entire month of April 2018.

* **Data Source:** [Seoul Open Data Plaza](https://data.seoul.go.kr)
* **Coverage:** Two distinct spatial configurations are utilized: **Urban Core** (central arterial corridors) and **Urban Mix** (metropolitan road networks).
* **Temporal Resolution:** 5-minute intervals across 30 days (April 1, 2018, 00:00 – April 30, 2018, 23:55; 8,640 time steps per link).

### 1. Urban Core Network
* **Network Scale:** 304 roadway links (`Link ID` count: 304)
* **Attributes:**
  * Spatial Attributes: `Link ID`, `Sort ID`, `Center point_X`, `Center point_Y`
  * Physical & Operational Attributes: `Speed limit`, `Length`, `Direction`
  * Time-Series Traffic Data: 5-minute speed intervals from `2018/04/01 0:00` through `2018/04/30 23:55`

### 2. Urban Mix Network
* **Network Scale:** 1,007 roadway links (`Link ID` count: 1,007)
* **Attributes:**
  * Spatial Attributes: `Link ID`, `Start point_X`, `Start point_Y`, `End point_X`, `End point_Y`
  * Operational Attributes: `Speed limit`
  * Time-Series Traffic Data: 5-minute speed intervals from `2018/04/01 0:00` through `2018/04/30 23:55`

---

> **Note:** Below are sample previews of both datasets.
