import folium

import re

import os

from collections import Counter

class MapFolium:

    #Liste des stop words
    stopWords = ['a','à','â','abord','afin','ah','ai','aie','ainsi','allaient','allo','allô','allons','après','assez','attendu','au','aucun','aucune','aujourd','auquel','aura','auront','aussi','autre','autres','aux','auxquelles','auxquels','avaient','avais','avait','avant','avec','avoir','ayant','b','bah','beaucoup','bien','bigre','boum','bravo','brrr','c','ça','car','ce','ceci','cela','celle','celle-ci','celle-là','celles','celles-ci','celles-là','celui','celui-ci','celui-là','cent','cependant','certain','certaine','certaines','certains','certes','ces','cet','cette','ceux','ceux-ci','ceux-là','chacun','chaque','cher','chère','chères','chers','chez','chiche','chut','ci','cinq','cinquantaine','cinquante','cinquantième','cinquième','clac','clic','combien','comme','comment','compris','concernant','contre','couic','crac','d','da','dans','de','debout','dedans','dehors','delà','depuis','derrière','des','dès','désormais','desquelles','desquels','dessous','dessus','deux','deuxième','deuxièmement','devant','devers','devra','différent','différente','différentes','différents','dire','divers','diverse','diverses','dix','dix-huit','dixième','dix-neuf','dix-sept','doit','doivent','donc','dont','douze','douzième','dring','du','duquel','durant','e','effet','eh','elle','elle-même','elles','elles-mêmes','en','encore','entre','envers','environ','es','ès','est','et','etant','étaient','étais','était','étant','etc','été','etre','être','eu','euh','eux','eux-mêmes','excepté','f','façon','fais','faisaient','faisant','fait','feront','fi','flac','floc','font','g','gens','h','ha','hé','hein','hélas','hem','hep','hi','ho','holà','hop','hormis','hors','hou','houp','hue','hui','huit','huitième','hum','hurrah','i','il','ils','importe','j','je','jusqu','jusque','k','l','la','là','laquelle','las','le','lequel','les','lès','lesquelles','lesquels','leur','leurs','longtemps','lorsque','lui','lui-même','m','ma','maint','mais','malgré','me','même','mêmes','merci','mes','mien','mienne','miennes','miens','mille','mince','moi','moi-même','moins','mon','moyennant','n','na','ne','néanmoins','neuf','neuvième','ni','nombreuses','nombreux','non','nos','notre','nôtre','nôtres','nous','nous-mêmes','nul','o','o|','ô','oh','ohé','olé','ollé','on','ont','onze','onzième','ore','ou','où','ouf','ouias','oust','ouste','outre','p','paf','pan','par','parmi','partant','particulier','particulière','particulièrement','pas','passé','pendant','personne','peu','peut','peuvent','peux','pff','pfft','pfut','pif','plein','plouf','plus','plusieurs','plutôt','pouah','pour','pourquoi','premier','première','premièrement','près','proche','psitt','puisque','q','qu','quand','quant','quanta','quant-à-soi','quarante','quatorze','quatre','quatre-vingt','quatrième','quatrièmement','que','quel','quelconque','quelle','quelles','quelque','quelques','quels','qui','quiconque','quinze','quoi','quoique','r','revoici','revoilà','rien','s','sa','sacrebleu','sans','sapristi','sauf','se','seize','selon','sept','septième','sera','seront','ses','si','sien','sienne','siennes','siens','sinon','six','sixième','soi','soi-même','soit','soixante','son','sont','sous','stop','suis','suivant','sur','surtout','t','ta','tac','tant','te','té','tel','telle','tellement','telles','tels','tenant','tes','tic','tien','tienne','tiennes','tiens','toc','toi','toi-même','ton','touchant','toujours','tous','tout','toute','toutes','treize','trente','très','trois','troisième','troisièmement','trop','tsoin','tsouin','tu','u','un','une','unes','uns','v','va','vais','vas','vé','vers','via','vif','vifs','vingt','vivat','vive','vives','vlan','voici','voilà','vont','vos','votre','vôtre','vôtres','vous','vous-mêmes','vu','w','x','y','z','zut']

    def __init__(self):

        #Liste des mots extraient des tweets
        self.words = []

    def init(self):

        #On efface le fichier pour visualiser la recherche car il contient les anciennes données
        exists = os.path.isfile('index.html')
        if exists:
            os.remove('index.html')

        #On créée la carte Folium
        m = folium.Map(
            location=[48.8567, 2.3508],
            zoom_start=5,
            tiles='Stamen Toner'
        )

        self.m = m


    #Methode pour sauvgarder la carte
    def saveMap(self):
        #On utilise un counter pour compter les mots les plus tweetés
        counter = Counter(self.words)
        most_occur = counter.most_common(10)

        stringToPut = ""

        #On format les 10 mots les plus utilisé en format HTML
        string = "<p>----------------------------------<br>"
        for strr in most_occur:
            #string += "<p>"
            string += "<br>"
            stringToPut = re.sub("[\'\)\(]", "", str(strr))
            stringToPut = re.sub("[,]", " --> ", str(stringToPut))
            string += str(stringToPut)
            #string += "</p>"
        string += "<br>----------------------------------</p>"

        #On ajoute le marqueur en plein milieu de Paris avec les 10 mots les plus tweetés
        self.addMarker([48.8567, 2.3508], string)

        #On sauvgarde la carte dans un fichier HTML
        self.m.save('index.html')

    #
    def addMarker(self, location, popUpString):

        tooltip = 'Click me to reveal the most used words!'
        folium.marker(location, popup=popUpString, tooltip=tooltip).add_to(self.m)

    #Ajoute le mot au dictionnaire
    def addWordsToTheMap(self, words):

        for w in words:
            if w != '':
                if w.lower() not in MapFolium.stopWords:
                    self.words.append(w.lower())