import pickle
from sklearn.feature_extraction.text import CountVectorizer
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfTransformer


#GET VECTOR COUNT
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(training_data.data)

#SAVE WORD VECTOR
pickle.dump(count_vect.vocabulary_, open("count_vector.pkl","wb"))

from sklearn.feature_extraction.text import TfidfTransformer

#TRANSFORM WORD VECTOR TO TF IDF
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

#SAVE TF-IDF
pickle.dump(tfidf_transformer, open("tfidf.pkl","wb"))



#TRANSFORM WORD VECTOR TO TF IDF
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

#SAVE TF-IDF
pickle.dump(tfidf_transformer, open("tfidf.pkl","wb"))

category_list = ["sport", "world", "us", "business", "health", "entertainment", "sci_tech"]
list2=[]
listval=df["info"].tolist()
for x in listval:
  y=x.lower()
  docs_new=[x.lower()]


  #LOAD MODEL
  loaded_vec = CountVectorizer(vocabulary=pickle.load(open("count_vector.pkl", "rb")))
  loaded_tfidf = pickle.load(open("tfidf.pkl","rb"))
  loaded_model = pickle.load(open("nb_model.pkl","rb"))

  X_new_counts = loaded_vec.transform(docs_new)
  X_new_tfidf = loaded_tfidf.transform(X_new_counts)
  predicted = loaded_model.predict(X_new_tfidf)
  print(category_list[predicted[0]])
 
