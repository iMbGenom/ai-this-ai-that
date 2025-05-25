from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
import joblib
import json
from const.const import GENERATED_MODEL_PATH
from const.const import TRAINING_DATA_PATH

# # load json file
# with open(TRAINING_DATA_PATH, "r") as f:
#     data = json.load(f)
# # grep
# texts = [item["text"] for item in data]
# labels = [item["label"] for item in data]

# hard code sample dta
X = ["I love this!", "I hate this", "Not bad", "Terrible experience", "Best ever"]
y = ["positive", "negative", "neutral", "negative", "positive"]

# vectorize text using pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])
# X = texts
# y = labels

# vectorize text single
# model = LogisticRegression()
# X = CountVectorizer().fit_transform(texts)
# y = labels


# gotcha
model.fit(X, y)

# save pipeline & model
joblib.dump(model, GENERATED_MODEL_PATH)