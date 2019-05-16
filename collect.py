from requests_oauthlib import OAuth1Session
import json
import os
import re
import urllib
import setting

twitter = OAuth1Session(setting.CONSUMER_KEY, setting.CONSUMER_SECRET, setting.ACCESS_TOKEN, setting.ACCESS_TOKEN_SECRET)
mkdir_name = "一風堂"


# 集めた画像を格納するディレクトリの作成を行う
def dir_check():
    if not os.path.isdir(mkdir_name):
        os.mkdir(mkdir_name)


def get_target_ward(word):
    url = "https://api.twitter.com/1.1/search/tweets.json"
    params = {'q':ward + ' min_faves:20　filter:images',
              'count':10,
              "include_entities":True
          }
    req = twitter.get(url, params = params)
    timeline = json.loads(req.text)
    return timeline

# 取得したツイートに画像があれば、その画像を取得する
def get_illustration(timeline):
    for tweet in timeline['statuses']:
        print(tweet["text"])
        try:
            media_list = tweet['extended_entities']['media']
            for media in media_list:
                image = media['media_url']
                with open(mkdir_name + '/' + os.path.basename(image), 'wb') as f:
                    img = urllib.request.urlopen(image).read()
                    f.write(img)
                with open(mkdir_name + '/text', mode='a') as f:
                    text = '{},{}\n'.format(os.path.basename(image), tweet["text"])
                    f.write(text)
            print("get tweet media")
        except KeyError:
            print("KeyError:画像を含んでいないツイートです")
        except:
            print("error")


if __name__ == '__main__':
    dir_name = dir_check()
    all_list = []
    ward = "一風堂"
    timeline = get_target_ward(ward)
    get_illustration(timeline)