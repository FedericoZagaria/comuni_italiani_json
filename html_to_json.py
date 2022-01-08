from html.parser import HTMLParser
import json

switch = False
tempDictionary: dict
listDictionary = []

def newTownDictionary ():
    emptyTownDictionary = { 'nr':'','descrizione comune':'','sigla':'','codice elettorale':'','codice istat':'','codice Belfiore':''}
    return emptyTownDictionary

def fillTownDictionary(argument):
    global tempDictionary
    if not(tempDictionary['nr']):
        tempDictionary['nr']=argument
    elif not(tempDictionary['descrizione comune']):
        tempDictionary['descrizione comune']=argument
    elif not(tempDictionary['sigla']):
        tempDictionary['sigla']=argument
    elif not(tempDictionary['codice elettorale']):
        tempDictionary['codice elettorale']=argument
    elif not(tempDictionary['codice istat']):
        tempDictionary['codice istat']=argument
    elif not(tempDictionary['codice Belfiore']):
        tempDictionary['codice Belfiore']=argument



class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global switch
        global tempDictionary
        if (tag == 'tr'):
            switch = True
            tempDictionary = newTownDictionary()
        
    def handle_endtag(self, tag):
        global switch
        global listDictionary
        global tempDictionary
        if (tag == 'tr'):
            switch = False
            listDictionary.append(tempDictionary)
        elif (tag == 'table'):
            HTMLParser.close
         

    def handle_data(self, data):
        global switch
        if (switch == True):
            fillTownDictionary(data)

parser = MyHTMLParser()
filehtml = open('D:\Dipartimento_per_gli_Affari_Interni_e_Territoriali.html','r')
parser.feed(filehtml.read())
with open("D:\codici_comuni_italiani.json", "w") as outfile:
    json.dump(listDictionary, outfile, indent=4, )

