
# Meeting Room Service
*Python 3.6 ve daha üzeri sürümleri destekler*


### Çalıştırma
 Sisteminizde dockerın kurulu olduğunu varsayıyorum.
  
 docker-compose Docker Desktop ile birlikte geliyor ancak windows olmayan bir sistemde kullanacaksanız ve docker-compose komutunu çalıştıramıyosanız, `apt-get install docker-compose` ile yükleyebilirsiniz


```bash
docker-compose up --build # arka planda çalışmasını isterseniz -d ekleyebilirsiniz.
docker exec -it web python manage.py createsuperuser # admin oluşturmak için
```

 ###### Not : docker-compose version 2.2 iken, depends_on üzerinden healtcheck condition eklenebiliyordu bunda beceremedim, o yüzden wait-for-it.sh kullanıyorum.

### Test

```bash 
docker exec web python manage.py test tests 
```






### Linkler
Api Default :  https://localhost:8000
Adminer Dashboard: http://localhost:8080


## API Requests & Responses

### POST /api/availablerooms
**Request**
 
```json
{
	"numberofpeople" : 10,
	"between" : ["2018-05-11 09:10:00","2018-05-11 10:10:00"]
}
```
**Response** : 
 
```json
  {
    "options" : [
      {
        "Roomid" : "Room3",
        "Between" : ["StartDate","EndDate"]
      }]
  }
```


### POST /api/bookroom
**Request**
 
```json
{
  "Roomid" : 1,
  "Numberofpeople" : 10,
  "between" : ["2018-05-11 09:10:00","2018-05-11 10:10:00"]
}
```
**Response** : 
 
```json
  {
    "success" : true
  }
```

```json
  {
    "success" : false,
    "ex" : "exception message"
  }
```