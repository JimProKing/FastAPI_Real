# LV1
## 251231
연말에 코딩하고 있는 내 모습이 레전드..
fastapi 써보면서 뭐라도 해보자 


### 
> md 미리보기는 ```command + Shift + V``` 
___
### 브랜치 만들기
```bash
git checkout -b branch1
```
### 가상환경 만들기
```bash
mkdir todos && cd todos
python3 -m venv venv
# python3에는 기본적으로 venv 모듈 있음 (표준 라이브러리임)
# 첫 venv: 
# 두번째 venv: 가상환경으로 사용할 폴더명
```
> lib: 파이썬 인터프리터 설치
> bin: 가상환경 내에서 상호작용 필요한 파일 

### 가상환경 활성화
```
source venv/bin/activate
#비활성화: deactivate

```

### fastAPI 설치
```
pip install fastapi
```
### 현재 프로젝트 설치된 패키지 목록 파일로 저장
```
freeze > requirement.txt
```

### requirements.txt 여기 있는 것들 다 설치
```
pip install -r requirements.txt
```
### 도커 설정
> 컨테이너화 하면, 구성요소를 단일 이미지로 묶어 배포가 쉬워짐

즉, 도커 == 컨테이너를 생성하고 관리하는 도구
- Push: 도커 허브에 저장
- Pull: 다시 추출


