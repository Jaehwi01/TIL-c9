select sum(누적관객수) from movies;
select 영화이름, 누적관객수 from movies where 누적관객수= (select max(누적관객수) from movies);   
select 장르, 상영시간 from movies where 상영시간=(select min(상영시간) from movies);
select avg(누적관객수)from movies where 제작국가='한국' ;
select count(관람등급='청소년관람불가') from movies;
select count(상영시간 >= 100 and 장르 = '애니메이션') from movies;