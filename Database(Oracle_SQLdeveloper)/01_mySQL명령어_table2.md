## 테이블 관련 명령어
- INSERT
- SELECT
- UPDATE
- DELETE
<br><br>

### 테이블에 데이터 등록하기 
<img width="531" alt="insert" src="https://github.com/minkim7704/DataScience/assets/49539711/101baebc-22f8-485f-bba9-785d29eca88c"><br>
- `INSERT INTO 테이블 이름 (필드 셋) -> value(레코드 셋)`<br><br><br><br>


### 데이터 조회하기
<img width="527" alt="select" src="https://github.com/minkim7704/DataScience/assets/49539711/16e6ade0-a1ee-486f-b5c5-9d6dc0a5f2ae">
<br>
- 데이터 조회 시 `SELECT _ FROM 테이블 이름;`
- 데이터 전체 컬럼을 조회할 땐 밑줄란에 별 (*), 특정 컬럼을 조회할 땐 특정 컬럼 이름

- `WHERE`을 이용해서 특정 데이터 내용이 들어간 데이터를 조회할 수 있다.
- 나는 이름이 '김'으로 시작하는 사람의 데이터를 조회했다.<br><br><br><br>


### 테이블 필드명 변경하기
<img width="552" alt="col rename" src="https://github.com/minkim7704/DataScience/assets/49539711/846b0a85-e553-4437-b5d0-1050f1805037"><br>
- `UPDATE` 명령어를 사용하면 테이블에 등록된 데이터를 수정할 수 있다.
- 테이블의 필드명 address를 dept로 변경했다.
- `SELECT`를 사용해 테이블의 address 필드가 dept로 변경된 것을 확인했다.<br><br><br><br>

### 데이블 데이터 수정하기
<img width="516" alt="update" src="https://github.com/minkim7704/DataScience/assets/49539711/4f257135-45e9-4aba-96a1-d4eb82dbe492"><br>
- `UPDATE` 명령어를 사용하면 테이블 내의 특정 데이터를 수정할 수 있다.
- `name = "최고봉"`인 데이터의 dept를 변경해주었다.
- `SELECT`를 사용해 "최고봉" 이름을 가진 사람의 dept가 변경된 것을 확인했다.<br><br><br><br>

### 테이블의 특정 레코드 삭제하기
<img width="475" alt="delete" src="https://github.com/minkim7704/DataScience/assets/49539711/7b10c405-bf23-42aa-aa46-497bf63948c3"><br>
- `DELETE` 명령어를 사용해 특정 레코드(데이터)를 삭제할 수 있다.
- "최고봉"의 데이터를 삭제했다.<br><br><br><br>
- `DELETE FROM 테이블이름;`
  - `DELETE` 명령어를 사용해 모든 레코드를 한 번에 삭제할 수도 있다.
  - 복구 불가능<br><br><br><br>

