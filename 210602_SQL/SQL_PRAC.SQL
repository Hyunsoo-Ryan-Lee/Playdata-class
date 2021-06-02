-- 6.subQuery.sql
-- select문 내에 포함된 또 다른 select문 작성 방법
-- 참고 : join 또는 subquery로 동일한 결과값 검색. 상황에 따라 어떤 문장으로 검색할지는 그때그때 다름.

-- 문법 : 비교 연산자(대소비교, 동등비교) 오른쪽에 () 안에 select문 작성 
--	   : create 및 insert 에도 사용 가능
--	   : tip - 개발시 다수의 test 위해서 원본이 아닌 복사본 table활용 권장 
-- 실행순서 : sub query가 main 쿼리 이전에 실행

--** Table 생성 - create table emp01 as select * from emp;
--** purge recyclebin; - DB 자체가 자동 생성해주는, 사용자에게 의미없는 table들을 삭제





-- SMITH 사원 부서 번호 검색 후 해당 번호에 일치되는 부서테이블의 
-- 부서 번호와 일치되는 부서명 검색

select deptno, dname 
from dept 
where deptno = (select deptno from emp where ename = 'SMITH');



--3. SMITH와 급여가 동일하거나 더 많은(>=) 사원명과 급여 검색
-- SMITH 제외해서 검색하기

select ename, sal 
from emp 
where sal >= (select sal from emp where ename = 'SMITH')
and ename != 'SMITH';


--4. DALLAS에 근무하는 사원의 이름, 부서 번호 검색

select ename, deptno 
from emp
where deptno = (select deptno from dept where loc = 'DALLAS');


--2. SMITH와 동일한 직급(job)을 가진 사원들의 모든 정보 검색(SMITH 포함)

select * from emp 
where job = (select job from emp where ename = 'SMITH');

select * from emp 
where job = (select job from emp where ename = 'SMITH')
and ename != 'SMITH';

--3. SMITH와 급여가 동일하거나 더 많은(>=) 사원명과 급여 검색
-- SMITH 제외해서 검색하기
select ename, sal 
from emp 
where sal >= (select sal from emp where ename = 'SMITH')
and ename != 'SMITH';

--4. DALLAS에 근무하는 사원의 이름, 부서 번호 검색
select ename, deptno 
from emp 
where deptno = (select deptno from dept where loc = 'DALLAS');


--5. 평균 급여보다 더 많이 받는(>) 사원만 검색
select ename from emp 
where sal > (select avg(sal) from emp);


--6.급여가 3000이상 사원이 소속된 부서에 속한  사원이름, 급여 검색
	--급여가 3000이상 사원의 부서 번호

select ename,deptno, sal from emp 
where deptno in (select deptno from emp where sal >= 3000);


--7. in 연산자를 이용하여 부서별로 가장 급여를 많이 받는 사원의 정보
--(사번, 사원명, 급여, 부서번호) 검색

select empno, ename, sal, deptno
from emp 
where sal in (select max(sal) from emp group by deptno);



--8. 직급(job)이 MANAGER인 사람이 속한 부서의 부서 번호와 부서명(dname)과 지역검색(loc)

select deptno, dname, loc 
from dept 
where deptno in (select deptno from emp where job = 'MANAGER');




--******************************************************************************************
/*
Table 생성 명령
create table 테이블명(
	name varchar2(20),
	age number(2)
);
*/
-- 완전 새로운 Table
create table camera(
    brand varchar(20),
    name varchar(20),
    price number(5),
    format number(5)
);

-- 기존에 있는 table에서 특정 data들만 가져와서 table 생성
create table new as select empno, ename, job, sal
from emp;

create table new1 as select empno, ename, job, sal 
from emp where deptno = 10;

-- 기존에 있는 table에서 data들을 제외하고 포맷만 가져오고 싶을 때
create table new01 as select * from dept where 1=2;

-- table의 컬럼 추가 / 정보 수정
alter table new add(loc varchar(10));
alter table new modify (loc varchar(20));

-- table의 컬럼 삭제
alter table new drop column job;

-- 조건에 부합하는 data 삭제
delete from new where ename = 'KING';

-- Insert 
insert into camera values ('Nikon','FM2',40,35);
insert into camera values ('Canon','NEW F-1',50,35);
insert INTO camera values ('Minolta','X-700',20,35);
insert INTO camera values ('Pentax','pentax645',30,120);
insert INTO camera values ('Hasselblad','503cx',200,120);
insert INTO camera values ('contax','T3',150,35);
insert INTO camera values ('Olympus','OM10',15,35);
insert INTO camera values ('Rollei','Rolleiflex',90,120);


insert into camera (brand, price) values ('Canon',50);
insert into camera (name, format) values ('NEW F-1',35);

-- Update - update 테이블명 set 바꿀조건;
update friends set deptno=100;

update cameras set price = 35 where brand='Nikon';


-- new table의 모든 사원의 급여를 10%(sal*1.1) 인상하기
update new set sal = sal*1.1;

-- 테이블명 변경 >> ALTER TABLE 기존테이블명 RENAME TO 변경할테이블명;
-- 컬럼명 변경 >> ALTER TABLE명 RENAME COLUMN 변경할 컬럼명 TO 변경될 컬럼명;


-- *** merge[병합] ***
/*
merge into 병합받을table명 별칭
using 이미data보유한table명 별칭
on 조건식(병합받을table.컬럼 = 이미data보유한table.컬럼)
when matched then 
	조건식 (True일 경우 실행)
when not matched then 
	조건식 (False인 경우 실행)
*/

create table cams as select * from camera where 1=2;

insert into cams values('Nikon','FE2',50,35);
insert into cams values('Minolta','X-300',15,35);



merge into cams f 
using camera c
on (f.brand = c.brand)
when not matched THEN
    insert values(c.brand,c.name,c.price,c.format);
    
-- when matched then
--     update set f.price = f.price + c.price