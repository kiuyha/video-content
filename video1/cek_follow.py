import json

#impor data dari json file
with open("following.json","r") as file:
    following = json.load(file)
with open("followers_1.json","r") as file:
    followers = json.load(file)

udah_follow= []
Gak_follow = []

#mengecek siapa saja yang telah follow
for follower in followers:
     udah_follow.append(follower['string_list_data'][0]['href'])

#mengecek siapa belum follow back
for follow in following["relationships_following"]:
    yang_kufollow = follow['string_list_data'][0]['href']
    if yang_kufollow  not in udah_follow:
        Gak_follow.append(yang_kufollow)
        print(yang_kufollow)

#menyimpan data siapa yang belum follow back dalam .txt file
with open('gakfollow.txt','w') as file:
    [file.write(f"{i}\n") for i in Gak_follow]