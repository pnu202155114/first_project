# first_project
주제: 상대적 빈곤율 및 1인당 국민총소득 제시

프로젝트 내용:

국가지표체계(K-indicator)가 제공하는 국민삶의질지표 중 상대적 빈곤율(*100)과 1인당 국민총소득을 사용하여 그래프로 비교해보고자 한다. 

2011년부터 2019년까지의 상대적 빈곤율 지표를 크롤링 하여 그래프1, 1인당 실질 국민총소득(만 원)을 크롤링 하여(2010년 및 2020년 제외) 그래프2, 1인당 명목 국민총소득(만 원)을 크롤링 하여(2010년 및 2020년 제외) 그래프 3을 출력한다. matplotlib를 이용해 표기한다.



202155114 김미송 역할

크롤링 - 국가지표체계에서 제공하는 국민삶의질지표의 Beautiful Soup을 이용하여, 정보를 포함하고 있는 전체 테이블을 찾아서 반환한다.

그래프 - 박재형이 반환한 리스트를 사용하여 그래프 1번, 2번을 제작한다.



202155139 박재형 역할

크롤링 - 김미송이 찾은 전체 테이블에서 필요한 정보 제거 후 각 리스트를 만들어 이를 반환한다.

그래프 - 그래프3을 추가적으로 코딩하여 이를 시각적으로 나타낸다.



크롤링할 사이트 URL: 국가지표체계 (index.go.kr)