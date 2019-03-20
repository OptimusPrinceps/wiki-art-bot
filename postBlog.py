import sys

from oauth2client import client
from googleapiclient import sample_tools

from constructPost import constructPost        

import config

def postBlog():

    # Authenticate and construct service.
    service, flags = sample_tools.init(
        ['blog.py'], 'blogger', 'v3', "", "blog.py",
        scope='https://www.googleapis.com/auth/blogger')

    blogId = service.blogs().listByUser(userId='self').execute()['items'][-1]['id']

    posts = service.posts()

    postNumber, postBody = constructPost()  
    print('Post number: ' + str(postNumber))

    postTitle = "Random Wikiart Post #{}".format(postNumber+1)
    body = {
        "kind": "blogger#post",
        "id": config.id,
        "title": postTitle,
        "content": postBody
    }
    insertPost = posts.insert(blogId=blogId, body=body)
    posts_doc = insertPost.execute()

postBlog()