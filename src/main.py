#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import urllib
import random
from yattag import *
import boto3
from html.parser import HTMLParser
from bs4 import BeautifulSoup as bso
import codecs

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

def style ():
    return """
    <style type="text/css">
    html{touch-action:manipulation}body{background:#fff;color:#1c1e21;direction:ltr;line-height:1.34;margin:0;padding:0;unicode-bidi:embed}body,button,input,label,select,td,textarea{font-family:Helvetica, Arial, sans-serif;font-size:12px}h1,h2,h3,h4,h5,h6{color:#1c1e21;font-size:13px;font-weight:600;margin:0;padding:0}h1{font-size:14px}h4,h5,h6{font-size:12px}p{margin:1em 0}b,strong{font-weight:600}a{color:#385898;cursor:pointer;text-decoration:none}button{margin:0}a:hover{text-decoration:underline}img{border:0}td,td.label{text-align:left}dd{color:#000}dt{color:#606770}ul{list-style-type:none;margin:0;padding:0}abbr{border-bottom:none;text-decoration:none}hr{background:#dadde1;border-width:0;color:#dadde1;height:1px}form{margin:0;padding:0}label{color:#606770;cursor:default;font-weight:600;vertical-align:middle}label input{font-weight:normal}textarea,.inputtext,.inputpassword{border:1px solid #ccd0d5;border-radius:0;margin:0;padding:3px}textarea{max-width:100%}select{border:1px solid #ccd0d5;padding:2px}input,select,textarea{background-color:#fff;color:#1c1e21}.inputtext,.inputpassword{padding-bottom:4px}.inputtext:invalid,.inputpassword:invalid{box-shadow:none}.inputradio{margin:0 5px 0 0;padding:0;vertical-align:middle}.inputcheckbox{border:0;vertical-align:middle}.inputbutton,.inputsubmit{background-color:#4267b2;border-color:#DADDE1 #0e1f5b #0e1f5b #d9dfea;border-style:solid;border-width:1px;color:#fff;padding:2px 15px 3px 15px;text-align:center}.inputsubmit_disabled{background-color:#999;border-bottom:1px solid #000;border-right:1px solid #666;color:#fff}.inputaux{background:#ebedf0;border-color:#EBEDF0 #666 #666 #e7e7e7;color:#000}.inputaux_disabled{color:#999}.inputsearch{background:#FFFFFF url(https://static.xx.fbcdn.net/rsrc.php/v3/yV/r/IJYgcESal33.png) no-repeat left 4px;padding-left:17px}.clearfix:after{clear:both;content:'.';display:block;font-size:0;height:0;line-height:0;visibility:hidden}.clearfix{zoom:1}.datawrap{word-wrap:break-word}.word_break{display:inline-block}.flexchildwrap{min-width:0;word-wrap:break-word}.ellipsis{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.aero{opacity:.5}.column{float:left}.center{margin-left:auto;margin-right:auto}#facebook .hidden_elem{display:none !important}#facebook .invisible_elem{visibility:hidden}#facebook .accessible_elem{clip:rect(1px 1px 1px 1px);clip:rect(1px, 1px, 1px, 1px);height:1px;overflow:hidden;position:absolute;white-space:nowrap;width:1px}.direction_ltr{direction:ltr}.direction_rtl{direction:rtl}.text_align_ltr{text-align:left}.text_align_rtl{text-align:right}body{overflow-y:scroll}.mini_iframe,.serverfbml_iframe{overflow-y:visible}.auto_resize_iframe{height:auto;overflow:hidden}.pipe{color:gray;padding:0 3px}#content{margin:0;outline:none;padding:0;width:auto}.profile #content,.home #content,.search #content{min-height:600px}.UIStandardFrame_Container{margin:0 auto;padding-top:20px;width:960px}.UIStandardFrame_Content{float:left;margin:0;padding:0;width:760px}.UIStandardFrame_SidebarAds{float:right;margin:0;padding:0;width:200px;word-wrap:break-word}.UIFullPage_Container{margin:0 auto;padding:20px 12px 0;width:940px}.empty_message{background:#f5f6f7;font-size:13px;line-height:17px;padding:20px 20px 50px;text-align:center}.see_all{text-align:right}.standard_status_element{visibility:hidden}.standard_status_element.async_saving{visibility:visible}img.tracking_pixel{height:1px;position:absolute;visibility:hidden;width:1px}#globalContainer{margin:0 auto;position:relative;zoom:1}.fbx #globalContainer{width:981px}.sidebarMode #globalContainer{padding-right:205px}.fbx #tab_canvas>div{padding-top:0}.fb_content{min-height:612px;padding-bottom:20px}.fbx .fb_content{padding-bottom:0}.skipto{display:none}.home .skipto{display:block}._li._li._li{overflow:initial}._72b0{position:relative;z-index:0}._5vb_ #pageFooter{display:none}html body._5vb_ #globalContainer{width:976px}._5vb_.hasLeftCol #headerArea{margin:0;padding-top:0;width:786px}._5vb_,._5vb_ #contentCol{background-color:#e9ebee;color:#1d2129}html ._5vb_.hasLeftCol #contentCol{border-left:0;margin-left:172px;padding-left:11px;padding-top:11px}._5vb_.hasLeftCol #topNav{border-left:0;margin-left:172px;padding:11px 7px 0 11px}._5vb_.hasLeftCol #topNav~#contentCol{padding-top:0}._5vb_.hasLeftCol #leftCol{padding-left:8px;padding-top:12px;width:164px}._5vb_.hasLeftCol #mainContainer{border-right:0;margin-left:0}._5vb_.hasLeftCol #pageFooter{background:none}html ._5vb_._5vb_.hasLeftCol div#contentArea{padding-left:0;padding-right:10px;width:786px}html ._5vb_._5vb_.hasLeftCol .hasRightCol div#contentArea{width:496px}._5vb_.hasLeftCol ._5r-_ div#rightCol{padding:0 7px 0 0;width:280px}._2yq #globalContainer{width:1012px !important}._2yq #headerArea{float:none !important;padding:0 0 12px 0 !important;width:auto !important}._2yq #contentArea{margin-right:0;padding:0 !important}._2yq #leftCol,._2yq #contentCol{padding:0 !important}._2yq #rightCol{float:left;margin-top:0;padding:0 !important}._2yq .groupJumpLayout{margin-top:-12px}._2yq .loggedout_menubar_container{min-width:1014px}._4yic{margin:auto;font-size:13px}._3a_u{margin:0 auto;width:598px}._4t5n{float:left;margin-bottom:15px;position:relative;width:inherit;word-break:break-word;z-index:0}._4t5o{clear:both;color:#7f7f7f;font-size:14px;margin-bottom:20px;margin-top:10px;text-align:center}._3b0a{position:relative;z-index:100}._3b0b{background:#fff;border-radius:3px;display:flex;flex-direction:row;padding:15px}._3z-t{border-radius:50%;height:16px;padding:4px;width:16px}._3b0c{display:flex;flex-direction:column;justify-content:center;margin-left:8px}._3b0d{color:#1d2129;font-size:14px;font-weight:bold;line-height:18px;margin-bottom:3px}._3b0e{color:#90949c;font-size:14px;line-height:16px}._218o{display:flex;justify-content:space-between;margin:0 auto;width:600px}._72m4{font-size:12px;margin-top:4px}._5aj7{display:flex}._5aj7 ._4bl7{float:none}._5aj7 ._4bl9{flex:1 0 0px}._ikh ._4bl7{float:left;min-height:1px}._4bl7,._4bl9{word-wrap:break-word}._4bl9{overflow:hidden}._21dp{position:relative;z-index:301}._2t-8._2t-8{font-family:Helvetica, Arial, sans-serif}._2t-8{height:43px;min-width:100%}._2t-a{height:42px;position:relative;width:100%}._2s1y{box-sizing:border-box;height:43px}._50ti{position:fixed;top:0}.hasDemoBar ._50ti{top:60px}._33rf{min-width:981px}._2yq ._33rf,._2xk0 ._33rf{min-width:1014px}._50tj{box-sizing:border-box;padding-right:0}.sidebarMode ._50tj{padding-right:205px}._4pmj{box-sizing:border-box;padding:0 16px}._2t-d{margin:auto;padding:0 8px}._2t-a{display:flex;justify-content:space-between}._2t-e,._2t-f{display:flex}._2t-e{flex:1 1 auto;justify-content:flex-start}._2t-f{flex:0 0 auto;justify-content:flex-end;margin-left:8px}._4kny{float:left}._50tm{width:100%}._2s24{margin-left:1px;position:relative}._h2p ._2s24{margin-left:0}._2s24::before{content:'';display:block;height:18px;left:-1px;position:absolute;top:12px;width:1px}._cy6{display:inline-block;padding:0 9px;vertical-align:top}._h2p ._cy6{padding:0 5px 0 4px}._cy6:first-child{padding-left:0}._h2p ._cy6:first-child{padding:0}._cy6:last-child{padding-right:0}._cy7{margin:7px 0 8px 0}._h2p ._cy7{margin-right:1px}._2s25{background-color:transparent;color:inherit;display:inline-block;font-size:12px;font-weight:bold;height:27px;line-height:28px;padding:0 10px 1px;position:relative;text-decoration:none;vertical-align:top;white-space:nowrap}.segoe ._2s25{font-weight:600}._h2p ._2s25{padding:0 12px 1px}._h2p ._cy6 ._4kny:last-child ._2s25{padding-right:11px}._2s25:hover,._2s25:focus,._2s25:active{border-radius:2px;color:inherit;outline:none;text-decoration:none;z-index:1}.openToggler ._2s25:hover,.openToggler ._2s25:focus,.openToggler ._2s25:active{background:transparent}._4kny ._585-{margin-left:0;min-width:144px;width:100%}._4kny .__wu ._539-.roundedBox{margin-left:0}._4kny ._4962{float:none;margin:5px 0 6px 0;position:relative}._h2p ._4kny ._4962{margin:5px 0 6px}._3x1p{height:100%;overflow:hidden;position:absolute;width:100%}._63i8{display:block;left:0;opacity:0;position:absolute;top:0;transition:opacity 200ms;width:100vw;z-index:2}._4yim,._4yin{display:block;left:0;position:absolute;top:0;transform-origin:left}._4yin{transform-origin:right}._4yio,._4yip{display:inline-block;height:2px;left:0;min-width:12px;position:absolute;top:0;transform-origin:left}._4yip{transform-origin:right}._2t-8.indeterminateBarTransition.transitioning ._63i8{opacity:1}._2t-8.indeterminateBarTransition.transitioning ._4yim{animation:indeterminateBarTransitionTranslate-left 2000ms infinite;animation-timing-function:steps(20, end)}._2t-8.indeterminateBarTransition.transitioning ._4yin{animation:indeterminateBarTransitionTranslate-right 2000ms infinite;animation-timing-function:steps(20, end)}._2t-8.indeterminateBarTransition.transitioning ._4yio{animation:indeterminateBarTransitionWidth-left 2000ms infinite;animation-timing-function:steps(20, end)}._2t-8.indeterminateBarTransition.transitioning ._4yip{animation:indeterminateBarTransitionWidth-right 2000ms infinite;animation-timing-function:steps(20, end)}._2t-8.indeterminateBarTransition.finishing ._63i8{opacity:0}@keyframes indeterminateBarTransitionTranslate-left{0%{animation-timing-function:ease-in;transform:translateX(0)}25%{animation-timing-function:ease-out;transform:translateX(25vw)}50%{animation-timing-function:ease-in;transform:translateX(calc(100vw - 12px))}100%{transform:translateX(calc(100vw - 12px))}}@keyframes indeterminateBarTransitionTranslate-right{0%{transform:translateX(0)}51%{animation-timing-function:ease-in;transform:translateX(0)}75%{animation-timing-function:ease-out;transform:translateX(calc(-25vw))}100%{animation-timing-function:ease-in;transform:translateX(calc(-100vw + 12px))}}@keyframes indeterminateBarTransitionWidth-left{0%{animation-timing-function:ease-in;opacity:1;transform:scaleX(1)}25%{animation-timing-function:ease-out;transform:scaleX(50)}50%{animation-timing-function:ease-in;opacity:1;transform:scaleX(1)}51%{opacity:0}100%{opacity:0}}@keyframes indeterminateBarTransitionWidth-right{0%{opacity:0}25%{opacity:0}50%{animation-timing-function:ease-in;opacity:0;transform:scaleX(1)}51%{opacity:1}75%{animation-timing-function:ease-out;opacity:1;transform:scaleX(50)}100%{animation-timing-function:ease-in;opacity:1;transform:scaleX(1)}}._2s1x ._2s1y{background-color:#4267b2;border-bottom:1px solid #29487d;color:#fff}._2s1x ._2s24::before{background:rgba(0, 0, 0, .1)}._2s1x ._2s25:hover,._2s1x ._2s25:focus,._2s1x ._2s25:active{background:rgba(0, 0, 0, .1);color:inherit}._2s1x.transitioning ._3fju{background-image:url(https://static.xx.fbcdn.net/rsrc.php/v3/yv/r/z1PAxf53vph.gif);height:100%;width:100%}._2s1x.transitioning ._3fjv{background-image:url(https://static.xx.fbcdn.net/rsrc.php/v3/y5/r/OzkCShPcfVN.gif);height:100%;width:100%}._2s1x.transitioning ._3fjx{background-image:url(https://static.xx.fbcdn.net/rsrc.php/v3/yH/r/YIs0iw6cHAa.gif);height:100%;width:100%}._2s1x ._3b33{background:#fff;height:100%;opacity:0;position:absolute;width:100%}._2s1x.pulseTransition.transitioning ._3b33{animation:pulse-loading 800ms cubic-bezier(.455, .03, .515, .955) infinite alternate;animation-timing-function:steps(8, end)}@keyframes pulse-loading{0%{opacity:0}100%{opacity:.15}}._2s1x ._3b34{height:100%;max-width:1016px;position:absolute;width:100%}._2s1x.shimmerTransition.transitioning ._3b34{animation:shimmer-loading 1600ms cubic-bezier(.455, .03, .515, .955) infinite;animation-timing-function:steps(16, end);background:linear-gradient(to right, rgba(66, 103, 178, 0), #577fbc, rgba(66, 103, 178, 0));background-size:1016px auto}@keyframes shimmer-loading{0%{transform:translateX(-1016px)}100%{transform:translateX(calc(100vw + 1016px))}}._2s1x ._63tk{background-color:#fff}._19ea{margin:7px 0;margin-left:-2px;margin-right:5px}._19eb{display:inline-block;outline:none;padding:2px;position:relative}._7tp1{display:inline-block;height:20px;outline:none;padding:4px;position:relative}._19eb:hover,._19eb:focus,._19eb:active,._7tp1:hover,._7tp1:focus,._7tp1:active{background-color:#365899;background-color:rgba(0, 0, 0, .1);border-radius:3px}._2md{background-image:url(https://static.xx.fbcdn.net/rsrc.php/v3/yT/r/b6e5rXnhY-F.png);background-repeat:no-repeat;background-size:auto;background-position:-97px -781px;display:block;height:24px;outline:none;overflow:hidden;text-indent:-999px;white-space:nowrap;width:24px}._7tp2{background-image:url(https://static.xx.fbcdn.net/rsrc.php/v3/yT/r/b6e5rXnhY-F.png);background-repeat:no-repeat;background-size:auto;background-position:0 0;display:block}._7ql{border-radius:2px;display:inline;margin:2px 6px 2px -8px;vertical-align:inherit}._h2p ._7ql{margin-left:-10px}._1k67 ._2s25{position:relative}._1k67._d0b ._2s25{padding-right:0}._1k67 ._1vp5 .img{transform:translateY(2px)}._1k67._d0b._5-y2 ._2s25{padding-right:6px}._1k67 ._2s25:after{border:1px solid rgba(0, 0, 0, .1);border-radius:2px;box-sizing:border-box;content:'';height:24px;left:2px;position:absolute;top:2px;width:24px}._2qgu._2qgu{border-radius:50%;overflow:hidden}._2s25._2s25._606w._606w:after,._606w:after{border-radius:50%}._605a .fbxWelcomeBoxBlock:after{border-radius:50%}._1qv9{align-items:center;display:flex;flex-direction:row}._rv{height:100px;width:100px}._rw{height:50px;width:50px}._s0:only-child{display:block}._3tm9{height:14px;width:14px}._54rv{height:16px;width:16px}._3qxe{height:19px;width:19px}._1m6h{height:24px;width:24px}._3d80{height:28px;width:28px}._54ru{height:32px;width:32px}._tzw{height:40px;width:40px}._54rt{height:48px;width:48px}._54rs{height:56px;width:56px}._1m9m{height:64px;width:64px}._ry{height:24px;width:24px}._4jnw{margin:0}._3-8h{margin:4px}._3-8i{margin:8px}._3-8j{margin:12px}._3-8k{margin:16px}._3-8l{margin:20px}._2-5b{margin:24px}._1kbd{margin-bottom:0;margin-top:0}._3-8m{margin-bottom:4px;margin-top:4px}._3-8n{margin-bottom:8px;margin-top:8px}._3-8o{margin-bottom:12px;margin-top:12px}._3-8p{margin-bottom:16px;margin-top:16px}._3-8q{margin-bottom:20px;margin-top:20px}._2-ox{margin-bottom:24px;margin-top:24px}._1a4i{margin-left:0;margin-right:0}._3-8r{margin-left:4px;margin-right:4px}._3-8s{margin-left:8px;margin-right:8px}._3-8t{margin-left:12px;margin-right:12px}._3-8u{margin-left:16px;margin-right:16px}._3-8v{margin-left:20px;margin-right:20px}._6bu9{margin-left:24px;margin-right:24px}._5soe{margin-top:0}._3-8w{margin-top:4px}._3-8x{margin-top:8px}._3-8y{margin-top:12px}._3-8z{margin-top:16px}._3-8-{margin-top:20px}._4aws{margin-top:24px}._2-jz{margin-right:0}._3-8_{margin-right:4px}._3-90{margin-right:8px}._3-91{margin-right:12px}._3-92{margin-right:16px}._3-93{margin-right:20px}._y8t{margin-right:24px}._5emk{margin-bottom:0}._3-94{margin-bottom:4px}._3-95{margin-bottom:8px}._3-96{margin-bottom:12px}._3-97{margin-bottom:16px}._3-98{margin-bottom:20px}._20nr{margin-bottom:24px}._av_{margin-left:0}._3-99{margin-left:4px}._3-9a{margin-left:8px}._3-9b{margin-left:12px}._3-9c{margin-left:16px}._3-9d{margin-left:20px}._4m0t{margin-left:24px}._8tm{padding:0}._2phz{padding:4px}._2ph-{padding:8px}._2ph_{padding:12px}._2pi0{padding:16px}._2pi1{padding:20px}._40c7{padding:24px}._2o1j{padding:36px}._6buq{padding-bottom:0;padding-top:0}._2pi2{padding-bottom:4px;padding-top:4px}._2pi3{padding-bottom:8px;padding-top:8px}._2pi4{padding-bottom:12px;padding-top:12px}._2pi5{padding-bottom:16px;padding-top:16px}._2pi6{padding-bottom:20px;padding-top:20px}._2o1k{padding-bottom:24px;padding-top:24px}._2o1l{padding-bottom:36px;padding-top:36px}._6bua{padding-left:0;padding-right:0}._2pi7{padding-left:4px;padding-right:4px}._2pi8{padding-left:8px;padding-right:8px}._2pi9{padding-left:12px;padding-right:12px}._2pia{padding-left:16px;padding-right:16px}._2pib{padding-left:20px;padding-right:20px}._2o1m{padding-left:24px;padding-right:24px}._2o1n{padding-left:36px;padding-right:36px}._iky{padding-top:0}._2pic{padding-top:4px}._2pid{padding-top:8px}._2pie{padding-top:12px}._2pif{padding-top:16px}._2pig{padding-top:20px}._2owm{padding-top:24px}._div{padding-right:0}._2pih{padding-right:4px}._2pii{padding-right:8px}._2pij{padding-right:12px}._2pik{padding-right:16px}._2pil{padding-right:20px}._31wk{padding-right:24px}._2phb{padding-right:32px}._au-{padding-bottom:0}._2pim{padding-bottom:4px}._2pin{padding-bottom:8px}._2pio{padding-bottom:12px}._2pip{padding-bottom:16px}._2piq{padding-bottom:20px}._2o1p{padding-bottom:24px}._4gao{padding-bottom:32px}._1cvx{padding-left:0}._2pir{padding-left:4px}._2pis{padding-left:8px}._2pit{padding-left:12px}._2piu{padding-left:16px}._2piv{padding-left:20px}._2o1q{padding-left:24px}._2o1r{padding-left:36px}._2lej{border-radius:3px}._2lek{color:#1d2129;font-size:14px;font-weight:bold;line-height:18px}._2lel{border-bottom:1px solid #dadde1}._2lem,._2lem a{color:#8d949e;font-size:13px;line-height:16px}._2let{color:#1d2129;font-size:13px;line-height:17px}._tqp{color:gray;font-size:13px}._4mp8{font-weight:bold}._4nkx,._3ttj{font-size:14px;line-height:2;text-align:left}._4nkx tbody tr th{padding:5px 5px;text-align:left;vertical-align:top;width:150px}._2yuc{max-width:100%}._3hls{font-size:14px;font-weight:bold}._2oao{color:#90949c;font-size:13px;font-weight:bold;line-height:20px;width:100px}._23bw{font-size:13px}._6udd{word-break:break-all}.uiBoxGray{background-color:#f2f2f2;border:1px solid #ccc}.uiBoxDarkgray{color:#ccc;background-color:#333;border:1px solid #666}.uiBoxGreen{background-color:#d1e6b9;border:1px solid #629824}.uiBoxLightblue{background-color:#edeff4;border:1px solid #d8dfea}.uiBoxRed{background-color:#ffebe8;border:1px solid #dd3c10}.uiBoxWhite{background-color:#fff;border:1px solid #ccc}.uiBoxYellow{background-color:#fff9d7;border:1px solid #e2c822}.uiBoxOverlay{background:rgba(255, 255, 255, .85);border:1px solid #3b5998;border:1px solid rgba(59, 89, 153, .65);zoom:1}.noborder{border:none}.topborder{border-bottom:none;border-left:none;border-right:none}.bottomborder{border-left:none;border-right:none;border-top:none}.dashedborder{border-style:dashed}.pas{padding:5px}.pam{padding:10px}.pal{padding:20px}.pts{padding-top:5px}.ptm{padding-top:10px}.ptl{padding-top:20px}.prs{padding-right:5px}.prm{padding-right:10px}.prl{padding-right:20px}.pbs{padding-bottom:5px}.pbm{padding-bottom:10px}.pbl{padding-bottom:20px}.pls{padding-left:5px}.plm{padding-left:10px}.pll{padding-left:20px}.phs{padding-left:5px;padding-right:5px}.phm{padding-left:10px;padding-right:10px}.phl{padding-left:20px;padding-right:20px}.pvs{padding-top:5px;padding-bottom:5px}.pvm{padding-top:10px;padding-bottom:10px}.pvl{padding-top:20px;padding-bottom:20px}.mas{margin:5px}.mam{margin:10px}.mal{margin:20px}.mts{margin-top:5px}.mtm{margin-top:10px}.mtl{margin-top:20px}.mrs{margin-right:5px}.mrm{margin-right:10px}.mrl{margin-right:20px}.mbs{margin-bottom:5px}.mbm{margin-bottom:10px}.mbl{margin-bottom:20px}.mls{margin-left:5px}.mlm{margin-left:10px}.mll{margin-left:20px}.mhs{margin-left:5px;margin-right:5px}.mhm{margin-left:10px;margin-right:10px}.mhl{margin-left:20px;margin-right:20px}.mvs{margin-top:5px;margin-bottom:5px}.mvm{margin-top:10px;margin-bottom:10px}.mvl{margin-top:20px;margin-bottom:20px}._51mz{border:0;border-collapse:collapse;border-spacing:0}._5f0n{table-layout:fixed;width:100%}.uiGrid .vTop{vertical-align:top}.uiGrid .vMid{vertical-align:middle}.uiGrid .vBot{vertical-align:bottom}.uiGrid .hLeft{text-align:left}.uiGrid .hCent{text-align:center}.uiGrid .hRght{text-align:right}._51mx:first-child>._51m-{padding-top:0}._51mx:last-child>._51m-{padding-bottom:0}._51mz ._51mw{padding-right:0}._51mz ._51m-:first-child{padding-left:0}._51mz._4r9u{border-radius:50%;overflow:hidden}._37no{font-size:13px;padding-bottom:8px}._u14{color:gray;font-size:13px;padding-bottom:8px}._12gz{font-size:14px;font-weight:bold;padding-bottom:8px}._67gx{color:gray;font-size:13px}._3bki{color:#90949c;font-size:13px}
    </style>
    """

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

def read_posts_file():
    s3 = boto3.resource('s3')
    obj = s3.Object("www.programming-sheffel.com","posts/posts_1.html")
    return obj.get()['Body'].read().decode('utf-8')

def random_posts(html):
    soup = bso(html, "lxml")
    posts = list(soup.findAll(attrs={"role" : "main"})[0].children)
    result = []
    for i in range(3):
        result.append(str(posts[random.randint(0, len(posts))]))
    return result

def build_html(posts):
    doc, tag, text = Doc().tagtext()
    with tag('html'):
        with tag('head'):
            doc.asis(google_analytics())
            doc.asis(style())
            doc.stag('link', rel='icon', href='https://s3.eu-central-1.amazonaws.com/programming-sheffel/favicon.png')
            doc.stag('meta', charser="UTF-8")
            doc.stag('meta', name='viewport', content='width=device-width, initial-scale=1.0')
            with tag('title'.encode('utf-8')):
                doc.asis('תכנות שפל')
        with tag('body',style="background: repeating-linear-gradient(45deg,#a146a3,#a146a3 10px,#dd91de 10px,#dd91de 20px);"):
            with tag('div', align = 'center'):
                doc.stag('img',src='mekupelet.png', style='margin:10px')
                with tag('div'):
                    doc.asis(posts[0])
                with tag('div'):
                    doc.asis(posts[1])
                with tag('div'):
                    doc.asis(posts[2])
    v = doc.getvalue()
    return v.encode('utf-8-sig')

def build():
    f = read_posts_file()
    posts = random_posts(f)
    html = build_html(posts)
    write_to_s3(html)