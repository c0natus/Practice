# 테이블 생성
```
xlsx 파일을 csv 파일로 변환한 후, 테이블에 데이터를 load한다. 
```

* copy product(id, productname, supplierid, categoryid, quantityperunit, unitprice, unitsinstock, unitsonorder, reorderlevel, discontinued)
    from 'C:\Users\hks89\Desktop\production.csv' with (format csv, header);

