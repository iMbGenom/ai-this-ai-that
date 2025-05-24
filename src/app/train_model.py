from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
import joblib
import json
from src.config.config import GENERATED_MODEL_PATH
from src.config.config import TRAINING_DATA_PATH

# X = ["I love this!", "I hate this", "Not bad", "Terrible experience", "Best ever"]
# y = ["positive", "negative", "neutral", "negative", "positive"]

# load json file
with open(TRAINING_DATA_PATH, "r") as f:
    data = json.load(f)

# grep
texts = [item["text"] for item in data]
labels = [item["label"] for item in data]

# vectorize using pipeline
# model = Pipeline([
#     ('vectorizer', CountVectorizer()),
#     ('classifier', MultinomialNB())
# ])

# vectorize text single
X = CountVectorizer().fit_transform(texts)
# X = texts
y = labels

model = LogisticRegression()

# gotcha
model.fit(X, y)

# save pipeline & model
joblib.dump(model, GENERATED_MODEL_PATH)