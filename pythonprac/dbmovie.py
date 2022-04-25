from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.5hfjn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

movie = db.movies.find_one({'title':'가버나움'})
print(movie['star'])

star = movie['star']
all_movies = list(db.movies.find({'star':star},{'_id':False}))
for movies in all_movies:
    print(movies['title'])

db.movies.update_one({'title':'아일라'},{'$set':{'star':'0'}})