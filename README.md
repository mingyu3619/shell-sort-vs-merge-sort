# shell-sort-vs-merge-sort

# 목차

1. Space –time trade off

2. Shell sort
-Selection sort
- Shell sort
- Code

3. Merge sort
- Merge sort(extra array)
- Merge sort(in-place)


4. 성능 비교
- 시간 복잡도
- 공간 복잡도
- 결론

# Space -time tradeof

컴퓨터 분야에서 space–timetradeof란
-	큰 메모리로 적은 시간의 문제를 품
-	작은 메모리로 큰 시간의 문제를 품  의 상관 관계를 의미함

# Shell sort

python file 폴더의 
selction_sort.py  shell_sort.py 를 통해 구현

# merge sort

 merge_sort.py를 통해 추가메모리를 사용하는 merge sort 구현
 
 merge_sort2.py를 통해 in-place한 merge sort 구현
 
 # 결과


![image](https://user-images.githubusercontent.com/86222639/146517493-6e7e65f2-10fa-41f2-aaaa-ccb379614120.png)
 
-𝑂(𝑛1.5)인 shel sort가 가장 느린 모습을 보인다
-	같은 시간 복잡도인 mergesort는 비슷한 시간 소요를 보인다


![image](https://user-images.githubusercontent.com/86222639/146517528-d57af9a3-690f-4bce-958b-64078d0bbf6e.png)

-	같은 시간 복잡도인 O(nlogn)
-	In-place인 mergesort 2 가 조금 느린 모습 (마지막 배열 복사 과정)



![image](https://user-images.githubusercontent.com/86222639/146517549-11d7d08f-ac4a-46de-8254-c598bb7523fe.png)

-	공간복잡도는 shel sort – O(1) / mergesort – O(n)
-	실제로는 추가 배열이 필요한 merge1은 더 많은 메모리 사용량
을 보임



![제목 없음](https://user-images.githubusercontent.com/86222639/146517415-77646226-e6cc-4abc-8fde-86f4ffeae28b.png)

-시간 복잡도:
shell>merge2(in-place)>=merge1

-공간복잡도:
merge1>=merge2(in-place)>shell

→적당히 작은 n에서 merge,shell sort  는 space –time trade-off 가 존재함을  보여준다.

