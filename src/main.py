#!/usr/bin/python
# -*- coding: utf-8 -*-

import facebook
import requests
import urllib
import random
from yattag import *
import codecs
import boto3
import settings

def get_posts (graph):
    data = graph.get_connections('sheffelProgramming', 'posts')
    posts = []
    while True:
        try:
            posts = posts + data['data']
            data = requests.get(data['paging']['next']).json()
        except KeyError:
            break
    return posts

def select_posts (posts):
    main_post = posts[0]
    a = b = c = 0
    while a == b or b == c or c == a:
        a = random.randint(1, len(posts) - 1)
        b = random.randint(1, len(posts) - 1)
        c = random.randint(1, len(posts) - 1)
    post_1 = posts[a]
    post_2 = posts[b]
    post_3 = posts[c]
    return main_post, post_1, post_2, post_3 

def post_url (post, graph):
    d = graph.get_object(id=post['id'], fields='permalink_url')
    return d['permalink_url']

def post_html (url):
    return '<div class="fb-post" data-href="{}" data-width="500" data-show-text="true" style="background-color:white"></div>'.format(url)
    
def google_analytics ():
    return """
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-114995406-1"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    
    gtag('config', 'UA-114995406-1');
    </script>
    """

def facebook_sdk ():
    return """<script>
    window.fbAsyncInit = function() {
    FB.init({
    appId            : '339625853196140',
    autoLogAppEvents : true,
    xfbml            : true,
    version          : 'v2.12'
    });
    };
    
    (function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));
    </script>"""

def build_html_helper(m, p1, p2, p3, graph):
    doc, tag, text = Doc().tagtext()
    with tag('html'):
        with tag('head'):
            doc.asis(google_analytics())
            doc.stag('link', rel='icon', href='https://s3.eu-central-1.amazonaws.com/programming-sheffel/favicon.png')
            doc.stag('meta', charser="UTF-8")
            doc.stag('meta', name='viewport', content='width=device-width, initial-scale=1.0')
            with tag('title'.encode('utf-8')):
                doc.asis('תכנות שפל')
        with tag('body',style="background: repeating-linear-gradient(45deg,#a146a3,#a146a3 10px,#dd91de 10px,#dd91de 20px);"):
            doc.asis(facebook_sdk())
            with tag('div', align = 'center'):
                doc.stag('img',src='mekupelet.png', style='margin:10px')
                with tag('div'):
                    doc.asis(post_html(post_url(m, graph)))
                with tag('div'):
                    doc.asis(post_html(post_url(p1, graph)))
                with tag('div'):
                    doc.asis(post_html(post_url(p2, graph)))
                with tag('div'):
                    doc.asis(post_html(post_url(p3, graph)))
    #with codecs.open("index.html", "w", "utf-8-sig") as text_file:
        #text_file.write(unicode(doc.getvalue(),'utf-8-sig'))
    return unicode(doc.getvalue(),'utf-8-sig')

def upload_file_to_s3(filename, s3, bucket):
    data = open(filename, 'rb')
    response = s3.Bucket(bucket).put_object(Key=filename, Body=data)
    print(response)

def write_to_s3(html):
    bucket = 'www.programming-sheffel.com'
    s3 = boto3.resource("s3")
    index = s3.Object(bucket, 'index.html')
    response = index.put(Body=html,
                         ContentType= 'text/html; charset=utf-8',
                         ACL='public-read',
                         CacheControl='no-cache')
    print(response)
    upload_file_to_s3('favicon.png',s3, bucket)
    upload_file_to_s3('mekupelet.png',s3, bucket)

def build_html(access_token):
    graph = facebook.GraphAPI(access_token)
    posts = get_posts(graph)
    m, p1, p2, p3 = select_posts(posts)
    return build_html_helper(m, p1, p2, p3, graph)

def build():
    access_token = "EAAE0405WF2wBACSpDvgv5jrYeCe6KnMLwWXv1VAHRUFQXFI0fUiw0uAl3ZBClglRZCrwaQi5QkiNYoOmQ3NZBGCsiOXryBQIzXYiajTdjU0ZBU1jo4T7j4HA6qy9uDVaNPYyGWxoMmQ5fAcUH8KChBqB8ZBm5UcZBQnD5WBEQnCwZDZD"
    html = build_html(access_token)
    write_to_s3(html)

#graph = facebook.GraphAPI(access_token)
