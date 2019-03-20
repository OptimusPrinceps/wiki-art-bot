import json
import wikipedia 
import sys


def getWikiSummary(title):
    try:
        return '<p><i>From Wikipedia:</i> {}</p>'.format(wikipedia.summary(title + ' (painting)'))
    except wikipedia.exceptions.PageError: 
        return ''
    

def updateNumberOfPaintingsPosted(paintingsToPost):
    with open('logfile.txt', 'r') as f:
        contents = [int(x) for x in f.read().split(',')]
        nPosts, nPaintings = contents
    with open('logfile.txt', 'w') as f:    
        strout = "%d,%d" % (nPosts+1, nPaintings + paintingsToPost)
        f.write(strout)
        
        return nPosts, nPaintings


def constructPost():

    with open('allPaintings.json', 'r') as f:
        allPaintings = json.loads(f.read())['allPaintings']

    totalPaintings = len(allPaintings)

    # keys:
    # ['id', 'title', 'year', 'width', 'height', 'artistName', 'image', 'map', 'paintingUrl', 'artistUrl', 'albums', 'flags', 'images']

    nPaintingsToPost = 3
    nPosts, numberOfPaintingsPosted = updateNumberOfPaintingsPosted(nPaintingsToPost)
    if(numberOfPaintingsPosted+5 > totalPaintings):
        print('No more paintings to post')
        sys.exit()

    postBody = "<div>"
    for i in range(nPaintingsToPost):    
        p = allPaintings[i+numberOfPaintingsPosted]
        p_id, title, year, artistName, image, = p['id'], p['title'], p['year'], p['artistName'], p['image']
        titleHtml = '<h3>{}</h3>'.format(title)
        attributionHtml = "<h4>{}, {}.<h4>".format(artistName, year)
        imageHtml = '<div><img src="{}" alt="Artwork"></img></div>'.format(image)
        wikiSummaryHtml = getWikiSummary(title)
        postBody += '<div> {} <hr></hr> </div> '.format(titleHtml+attributionHtml+imageHtml) #+wikiSummaryHtml)
    
    print(i+numberOfPaintingsPosted)

    postBody += "</div>"

    return nPosts, postBody