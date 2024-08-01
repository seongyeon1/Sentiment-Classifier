# 네이버 리뷰 데이터를 활용한 감정 예측 모델

---

### MLOps 실습 개선
- 이전 실습(https://github.com/seongyeon1/aiffel/tree/main/MLOps/Day5) 에서는 lstm 모델을 학습한 후 저장하여 이를 이용해 예측을 진행했다.
- 이를 개선하여 bert model로 모델을 변경하였다

- model link : https://huggingface.co/seongyeon1/klue-base-finetuned-nsmc

### 추가적으로 개선 예정인 부분
- mysql을 사용하여 데이터 저장
- UI 제작

### 전체 구조
- (개선 예정)
![Screenshot 2024-08-01 at 5 57 29 PM](https://github.com/user-attachments/assets/063676e9-17b8-47eb-b579-5fadc3ff4f6f)



---
### Running the Project
Build and run the FastAPI container:

```shell
docker build -t text-classification-app -f Dockerfile.fastapi .
docker run -d -p 80:80 text-classification-app
```

### Access
Open a web browser and go to http://localhost.
