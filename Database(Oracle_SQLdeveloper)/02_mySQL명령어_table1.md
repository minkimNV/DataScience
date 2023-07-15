<img width="552" alt="mysql_db생성선택" src="https://github.com/minkim7704/DataScience/assets/49539711/761a1298-8947-47a0-9e48-ae96a8fc77aa"><br>
사용할 데이터베이스인 `addr_db`을 만들고, 사용할 DB로 선택했다.<br><br><br>

## 테이블 관련 명령어
- CREATE
- DESC / DESCRIBE
- ALTER
- RENAME
- DROP
<br><br>

### 테이블 생성
<img width="552" alt="mysql_테이블생성" src="https://github.com/minkim7704/DataScience/assets/49539711/8e063142-a7b1-4bdb-94f6-7b0bfb4d1575"><br>
- 사용할 데이터베이스 `addr_db`에서 새로운 테이블 `member_tbl`을 만들었다.<br>
```int = 정수형```<br>
```varchar(x) = x-byte의 문자열형 (x에는 정수가 들어간다)```
- `show table;`을 통해 테이블 목록을 확인했다.<br><br><br><br>

### 테이블 구조 확인
<img width="487" alt="desc_describe table" src="https://github.com/minkim7704/DataScience/assets/49539711/0a98246e-691d-47ab-91d6-ef6830991491"><br>
- 테이블 구조를 확인할 때는 `desc` `describe` 둘 다 사용 가능하다.<br><br><br><br>

### 테이블에 새로운 필드 추가하기
<img width="501" alt="alter add col" src="https://github.com/minkim7704/DataScience/assets/49539711/ed991551-ebf6-4772-9d6d-ec04014c53a3"><br>
- 테이블 변경하고 싶을 때 `ALTER` 명령어를 사용한다.<br><br><br><br>

### 기존 필드 삭제하기
<img width="504" alt="alter drop col" src="https://github.com/minkim7704/DataScience/assets/49539711/e1dd39ba-3598-438f-905d-940ae9f2fa03"><br>
- `ALTER` 명령어를 사용해서 추가했던 `age` 필드를 삭제했다.<br><br><br><br>

### 테이블 이름 변경하기
<img width="477" alt="rename" src="https://github.com/minkim7704/DataScience/assets/49539711/f906baca-1180-403e-bb3d-5f809831eec7">
<br>

- `RENAME` 명령어를 사용해서 `member_tbl`테이블의 이름을 `student_tbl`로 변경했다.
- 테이블 목록을 확인하는 `SHOW TABLES;` 명령어를 통해 변경된 테이블 이름을 확인했다. <br><br><br><br>


### 테이블 삭제하기
- `DROP TABLE 테이블명;`
- 데이터베이스 또는 테이블을 삭제할 때 사용하는 명령어 `DROP`
- 데이터베이스를 삭제하게 되면 그 안에 들어있는 모든 테이블도 삭제됨.
- DROP 명령어로 데이터베이스 또는 특정 테이블을 삭제하게 되면 다시 복구할 수 없다.


