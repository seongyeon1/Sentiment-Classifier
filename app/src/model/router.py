from fastapi import APIRouter
from .textclassifier import TextClassifier
from .schemas import TextRequest, TextResponse

router = APIRouter()
classifier = TextClassifier()

@router.post("/predict", response_model=TextResponse)
def predict(request: TextRequest):
    prediction = classifier.predict(request.text)[0]
    index_to_tag = {"LABEL_0": "부정", "LABEL_1": "긍정"}
    label = index_to_tag[prediction['label']]
    return TextResponse(label=label, score=prediction['score'])
