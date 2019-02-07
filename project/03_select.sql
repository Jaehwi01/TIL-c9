select*from movies where 상영시간 >= 150;
select 영화코드, 영화이름 from movies where 장르 ='애니메이션';
select 영화이름 from movies where 제작국가='덴마크' and 장르='애니메이션';
select 영화이름, 누적관객수 from movies where 누적관객수>=1000000 and 관람등급='청소년관람불가'; 
select*from movies where 개봉연도 >= 20000101 and 개봉연도 < 20091231;
select DISTINCT*장르 FROM movies;