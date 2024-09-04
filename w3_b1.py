Vietnam ={
    'An Giang' : (10.5216,105.1259),
	'Vung Tau' : (10.5410,107.2429),
	'Bac Lieu' : (9.2954,105.7213),
	'Bac Kan'  : (22.1471,105.8348),
	'Bac Giang': (21.2730,106.1946),
	'Bac Ninh' : (21.1214,106.1110),
	'Ben Tre'  : (10.2414,106.3755),
	'Binh Dinh': (14.1665,108.9027),
	'Binh Duong': (11.1680,106.6774),
    'Binh Phuoc':(11.7570,106.7416),
	'Binh Thuan':(11.0904,108.0721),
	'Ca Mau'    :(9.1522,105.1961),
	'Can Tho'	:(10.0452,105.7469),
	"Cao Bang"  :(22.6724,106.2522),
	'Da Nang'	:(16.0544,108.2022),
    'Dak Lak':(12.7100,108.2378),
	'Dak Nong':(12.2058,107.6903),
	'Dien Bien':(21.3860,103.0232),
	'Dong Nai':	(10.9473,106.7431),
	'Dong Thap':(10.4493,105.6366),
	'Gia Lai' :(13.8079,	108.194),
	'Ha Giang' :(22.7680,	14.9410),
	'Ha Nam' :(20.5833,	105.9214),
	'Ha Noi' :(21.0285,	105.8542),
	'Ha Tinh':(18.3534,	1058877),
	'Hai Duong':(20.9381,106.3180),
	'Hai Phong':	(20.8449,	106.6881),
	'Hau Giang':(9.7840	, 105.4717),
	'Hoa Binh':	(20.6861,	15.3093),
	'Hung Yen':	(20.6466,	16.0514),
	'Khanh Hoa':(12.2584,109.1311),
	'Kien Giang':(10.0150,105.1772),
	'Kon Tum ':(14.3545,	108.076),
	'Lai Chau':(22.3687,	13.4501),
	'Lam Dong':	(11.5753,	108.1429),
	'Lang Son':(21.8528,	106.7654),
	"Lao Cai":(22.3382,104.1487),
	'Long An':(10.5358,106.455),
	'Nam Dinh':(20.4337,16.1774),
	'Nghe An':(19.2343,104.9200),
	'Ninh Binh':(20.2401,105.9745),
	'Ninh Thuan':(11.5649,	108.9886),
	'Phu Tho':	(21.3997,105.2405),
	'Phu Yen':	(13.0882,	109.0929),
	'Quang Binh':	(17.6104,	106.3487),
	'Quang Nam':	(15.5394,	108.0191),
	'Quang Ngai':	(15.1205,	108.7923),
	'Quang Ninh':	(21.0064,	107.2928),
	'Quang Tri':	(16.7685,	107.1826),
	'Soc Trang':	(9.6025,	105.9802),
	'Son La':      (21.3287,	103.9145),
	'Tay Ninh':	(11.3545,	106.1185),
	'Thai Binh':	(20.4463,	106.3362),
	'Thai Nguyen':	(21.5672,	105.8251),
	'Thanh Hoa':	(19.8072,	105.7760),
	'Hue':	(16.4637,	107.5905),
	'Tien Giang':	(10.4493,	106.3435),
	'TP Ho Chi Minh':	(10.8231,	106.6297),
	'Tra Vinh':	(9.8127,106.2993),
	'Tuyen Quang':	(21.7767,	105.2280),
	'Vinh Long':	(10.2540,	105.9593),
	'Vinh Phuc':	(21.3089,	105.6049),
	'Yen Bai':	(21.7229,104.9113),


    
}

 

graph = {
    'Ha Giang' : ['Lao cai','Cao Bang','Tuyen Quang','Yen Bai'],
    'Lao Cai'  : ['Ha Giang','Yen Bai','Lai Chau'],
    'Lai Chau' : ['Lao Cai','Dien Bien','Yen Bai','Son La'],
    'Cao Bang' : ['Ha Giang','Tuyen Quang','Bac Kan','Lang Son'],
    'Tuyen Quang' :['Ha Giang','Yen Bai','Bac Kan','Thai Nguyen','Vinh Phuc','Phu Tho','Cao Bang'],
    'Bac Kan'  : ['Cao Bang','Tuyen Quang','Lang Son','Thai Nguyen',],
    'Lang Son' : ['Cao Bang','Bac Kan','Thai Nguyen','Bac Giang','Quang Ninh'],
    'Yen Bai'  : ['Lao Cai','Lai Chau','Ha Giang','Tuyen Quang','Phu Tho','Son La'],
    'Son La'   : ['Dien Bien','Lai Chau','Yen Bai','Phu Tho','Hoa Binh','Thanh Hoa'],
    'Dien Bien': ['Lai Chau','Son La'],
    'Phu Tho'  : ['Son La','Yen Bai','Tuyen Quang','Vinh Phuc','Ha Noi','Hoa Binh'],
    'Thai Nguyen' : ['Tuyen Quang','Bac Kan','Bac Giang','Ha Noi','Vinh Phuc','Lang Son'],
    'Vinh Phuc': ['Thai Nguyen','Ha Noi','Phu Tho','Tuyen Quang'],
    'Bac Giang': ['Thai Nguyen','Lang Son','Bac Ninh','Ha Noi','Hai Duong','Quang Ninh'],
    'Quang Ninh': ['Lang Son','Bac Giang','Hai Duong','Hai Phong'],
    'Hai Phong': ['Quang Ninh','Hai Duong','Thai Binh'],
    'Hai Duong': ['Hai Phong','Quang Ninh','Bac Giang','Bac Ninh','Hung Yen','Thai Binh'],
    'Bac Ninh' : ['Bac Giang','Ha Noi','Hung Yen','Hai Duong'],
    'Hung Yen' : ['Bac Ninh','Ha Noi','Hai Duong','Thai Binh','Ha Nam'],
    'Ha Noi'   : ['Thai Nguyen','Bac Ninh','Bac Giang','Vinh Phuc','Hung Yen','Phu Tho','Hoa Binh','Ha Nam'],
    'Hoa Binh' : ['Son La','Ha Noi','Ha Nam','Ninh Binh','Thanh Hoa','Phu Tho'],
    'Ha Nam'   : ['Ha Noi','Hung Yen','Hoa Binh','Thai Binh','Nam Dinh','Ninh Binh'],
    'Thai Binh': ['Ha Nam','Nam Dinh','Hung Yen','Hai Duong','Hai Phong'],
    'Nam Dinh' : ['Thai Binh','Ha Nam','Ninh Binh'],
    'Ninh Binh': ['Nam Dinh','Ha Nam','Hoa Binh','Thanh Hoa'],
    'Thanh Hoa': ['Ninh Binh','Hoa Binh','Son La','Nghe An'],
    'Nghe An'  : ['Thanh Hoa','Ha Tinh'],
    'Ha Tinh'  : ['Nghe An','Quang Binh'],
    'Quang Binh'  : ['Ha Tinh','Quang Tri'],
    'Quang Tri': ['Quang Binh','Hue'],
    'Hue'      : ['Quang Tri','Da Nang','Quang Nam'],
    'Da Nang'  : ['Hue','Quang Nam'],    
    'Quang Nam': ['Da Nang','Hue','Quang Ngai','Kon Tum'],
    'Kon Tum'  : ['Quang Nam','Quang Ngai','Gia Lai'],
    'Quang Ngai':['Kon Tum','Quang Nam','Binh Dinh','Gia Lai'],
    'Binh Dinh': ['Gia Lai','Quang Ngai','Phu Yen'],
    'Gia Lai'  : ['Kon Tum','Quang Ngai','Binh Dinh','Dak Lak'],
    'Dak Lak'  : ['Gia Lai','Phu Yen','Khanh Hoa','Lam Dong','Dak Nong'],
    'Phu Yen'  : ['Binh Dinh','Gia Lai','Dak Lak','Khanh Hoa'],
    'Khanh Hoa': ['Phu Yen','Dak Lak','Lam Dong','Ninh Thuan'],
    'Ninh Thuan':['Khanh Hoa','Lam Dong','Binh Thuan'],
    'Lam Dong' : ['Dak Lak','Dak Nong','Binh Phuoc','Ninh Thuan','Binh Thuan','Dong Nai','Khanh Hoa'],
    'Dak Nong' : ['Dak Lak','Lam Dong','Binh Phuoc'],
    'Binh Phuoc':['Dak Nong','Lam Dong','Dong Nai','Binh Duong','Tay Ninh'],
    'Tay Ninh'  :['Binh Phuoc','Binh Duong','Long An'],
    'Binh Duong':['Tay Ninh','TP Ho Chi Minh','Dong Nai','Binh Phuoc'],
    'Dong Nai' : ['Binh Phuoc','Lam Dong','Binh Thuan','Vung Tau','TP Ho Chi Minh','Binh Duong'],
    'Binh Thuan':['Dong Nai','Ninh Thuan','Lam Dong','Vung Tau'],
    'Vung Tau' : ['Binh Thuan','Dong Nai','TP Ho Chi Minh'],
    'TP Ho Chi Minh' : ['Vung Tau','Dong Nai','Binh Duong','Tay Ninh','Long An','Tien Giang'],
    'Long An'  : ['TP Ho Chi Minh','Tay Ninh','Tien Giang','Dong Thap'],
    'Dong Thap': ['Long An','Tien Giang','Vinh Long','An Giang'],
    'Tien Giang':['Dong Thap','TP Ho Chi Minh','Ben Tre','Long An','Vinh Long'],
    'Ben Tre'  : ['Tien Giang','Vinh Long','Tra Vinh'],
    'Tra Vinh' : ['Ben Tre','Vinh Long','Soc Trang'],
    'Vinh Long': ['Ben Tre','Tien Giang','Dong Thap','Can Tho','Hau Giang','Soc Trang','Tra Vinh'],
    'Can Tho'  : ['Vinh Long','Dong Thap','An Giang','Kien Giang','Hau Giang'],
    'An Giang' : ['Can Tho','Kien Giang','Dong Thap'],
    'Hau Giang': ['Can Tho','Kien Giang','Bac Lieu','Soc Trang','Vinh Long'],
    'Soc Trang': ['Tra Vinh','Vinh Long','Hau Giang','Bac Lieu'],
    'Kien Giang':['An Giang','Can Tho''Hau Giang','Bac Lieu','Ca Mau'],
    'Bac Lieu' : ['Kien Giang','Hau Giang','Soc Trang','Ca Mau'],
    'Ca Mau'   : ['Bac Lieu','Kien Giang'],
    }
from asyncio.windows_events import NULL
import math
from os import path
from turtle import distance

def haversine(Vietnam1, Vietnam2):
    # Radius of Earth in kilometers
    R = 6371.0
    
    lat1, lon1 = math.radians(Vietnam1[0]), math.radians(Vietnam1[1])
    lat2, lon2 = math.radians(Vietnam2[0]), math.radians(Vietnam2[1])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    return R * c

def get_coordinates(province_name):
    # Duyệt qua danh sách để tìm tỉnh thành cần lấy tọa độ
    for province in Vietnam:
        if Vietnam[province] == province_name:
            return province[0], province[1]
    return None  # Trả về None nếu không tìm thấy

province = input("Nhap tinh thanh bat dau : ")
coordinates = get_coordinates(province)
eprovince = input("Nhap diem ket thuc : ")
coordinates1 = get_coordinates(eprovince)


import heapq

def beam_seach(graph,Vietnam,province,eprovince,beam_width):
  
    queue = [(haversine(Vietnam[province],Vietnam[eprovince]),[province])]

    
    while queue:
        canidate = heapq.nsmallest(beam_width,queue)
        queue=[]
        
        for cost,path in canidate:
            current_node = path[-1]
            if current_node == eprovince:
                return path
            for neighbor in graph[current_node]:
                new_path = path + [neighbor]
                distance_to_neighbor = haversine(Vietnam[current_node],Vietnam[neighbor])
                total_cost = cost + distance_to_neighbor + haversine(Vietnam[neighbor],Vietnam[eprovince])
                heapq.heappush(queue, (total_cost,new_path))
    print(f"Khoang cach {distance_to_neighbor : .2f}")    
    return None
    
    
    
        

beam_width = 1
path = beam_seach(graph,Vietnam,province,eprovince,beam_width)
print("Hanh trinh tu dau den dich ",path)


#distance = haversine(coordinates[0],coordinates[1],coordinates1[0],coordinates1[1])
#print(f"Khoang cach giua {province} va {eprovince} la : {distance : .2f} km ")
