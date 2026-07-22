## 🗃️ Dataset Description

The dataset used in this project comprises real-time traffic performance data collected from the Seoul Transport Operation & Information Service ([TOPIS](https://data.seoul.go.kr)) via the Seoul Open Data Plaza. It consists of 5-minute interval road speed observations recorded across central arterial corridors in Seoul throughout April 2018.

* **Data Source:** [Seoul Open Data Plaza](https://data.seoul.go.kr)
* **Target Network:** Urban Core Network (Seoul central arterial corridors)
* **Network Scale:** 304 roadway links (`Link ID` count: 304)
* **Temporal Resolution:** 5-minute intervals across 30 days (April 1, 2018, 00:00 – April 30, 2018, 23:55; 8,640 time steps per link)
* **Dataset Attributes:**
  * **Spatial Attributes:** `Link ID`, `Sort ID`, `Center point_X`, `Center point_Y`
  * **Physical & Operational Attributes:** `Speed limit`, `Length`, `Direction`
  * **Time-Series Traffic Data:** 5-minute speed measurements from `2018/04/01 0:00` through `2018/04/30 23:55`

---

> **Note:** Below is a sample preview of the dataset.
