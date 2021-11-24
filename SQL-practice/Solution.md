# 테이블 생성 및 데이터 load
```
xlsx 파일을 csv 파일로 변환한 후, 테이블에 데이터를 load한다. 
```

* copy product(id, productname, supplierid, categoryid, quantityperunit, unitprice, unitsinstock, unitsonorder, reorderlevel, discontinued)    from 'C:\Users\hks89\Desktop\production.csv' with (format csv, header);

* create table Product    
(    
	id int PRIMARY KEY,    
	ProductName varchar(100),    
	SupplierId int,    
	CategoryId int,    
	QuantityPerUnit varchar(100),    
	UnitPrice int,    
	UnitsInStock int,    
	UnitsOnOrder int,    
	ReorderLevel int,    
	Discontinued int    
);
