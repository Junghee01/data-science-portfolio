사용 데이터는 서울시 실시간 도로 소통 정보 데이터로, 서울특별시 TOPIS(서울교통정보시스템)에서 2018년 4월에 수집된 1달 동안의 5분간격의 교통 속도 데이터입니다.

원 출처: [서울열린데이터광장](https://data.seoul.go.kr)

- 2개의 데이터 셋을 활용했으며, 도시중심부도로(Urban Core)와 도심 도로(Urban Mix)에서의 도로 소통 정보 데이터를 활용하였습니다.
- 도시중심부도로의 칼럼명은 Link ID,	Sort ID,	Center point_X,	Center point_Y,	Speed limit,	Length,	Direction,	2018/04/01 0:00,	2018/04/01 0:05,	2018/04/01 0:10, ..., 2018/04/30 23:55 가 있습니다.
- 도심도로의 칼럼명은 Link ID	Start point_X	Start point_Y	End point_X	End point_Y	Speed limit, 2018/04/01 0:00,	2018/04/01 0:05,	2018/04/01 0:10, ..., 2018/04/30 23:55 가 있습니다.
- Link ID 수는 304 개(도시중심부도로-Urban Core),  1007개(도심 도로 - Urban Mix) 입니다.
- 아래는 두 데이터셋 일부입니다.
#### (Urban Core Dataset)
![image](https://github.com/user-attachments/assets/1ef025f5-00b3-4004-82a7-6b7a690d7b89)
#### (Urban Mix Dataset)
![image](https://github.com/user-attachments/assets/7256e32c-cc5c-4f75-8730-b73b75dded3a)
