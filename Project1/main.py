from MyDatabase import MyDatabase

from twitter import TwitterAPI
from twitter import StreamListener



def main() :



    #INFORMATIONS SUR LA BDD
    TwiDatabase = "twitterdatabase"
    user = {                                        #description des colonnes
        "idUser"    : "VARCHAR(50) PRIMARY KEY",
        "pseudo"    : "VARCHAR(50)",
        "location"  : "VARCHAR(30)",
        "time_zone" : "VARCHAR(30)"
    }
    tweet = {
        "idTweet"      : "VARCHAR(50) PRIMARY KEY",
        "created_date" : "VARCHAR(30)",
        "content"      : "VARCHAR(280)",
        "hashtags"     : "VARCHAR(30)",
        "geo"          : "VARCHAR(30)",
        "coords"       : "VARCHAR(20)",
        "place"        : "VARCHAR(30)",
        "lang"         : "VARCHAR(20)"
    }

    # DONNEES A INSERER
    #SIMPLE
    userData = {
        "idUser"   : 55545256,
        "pseudo"   : "Kikoo",
        "location" : "France"
    }

    #Partie liée à la base de donnée qu'on a pas utilisée car c'est inutile dans notre cas

    # db = MyDatabase("localhost", "root", "", "3306")

    #CREATION ET CONNECTION A LA BDD
    #db.connectToMySQL()
    #db.createDatabase(TwiDatabase)
    #db.connectToDB(TwiDatabase)

    #OPERATION SUR LA BDD
    # db.createTable("user", user)
    # db.createTable("tweet", tweet)
    # db.insert("user", userData)

    #On créé une instance de l'API Twitter
    twitterAPI = TwitterAPI()

    #On crée une instance du stream listener
    streamListener = StreamListener()

    #On l'initialise
    streamListener.init()

    # [-5.48,43.19,6.19,50.07] : France
    # [5.662662,45.127587,5.80823,45.236484] : Grenoble
    # [1.6128,48.4654,3.0849,49.2604] : Paris

    # C'est bounding box qui entoure la France
    location = [-5.48,43.19,6.19,50.07]

    #On écoute le stream par rapport à une localisation
    streamListener.useStreamByLocation(twitterAPI, location)

if __name__ == '__main__':
    main()


