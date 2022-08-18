# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:03:20 2021

@author: Aryanand
"""
import instaloader
#This Program will find people who don't follow back your Instagram Account
print("\t\t\t 'NOT FOLLOWING BACK' LIST MAKER\t\t")
logid=input("Your IG with @\t")
ps=input("Your Password\t")

userid=input("ID for which Follower Status to Check\t")

ig=instaloader.Instaloader()

ig.login(logid,ps)
profile = instaloader.Profile.from_username(ig.context,userid)

follow=profile.get_followers()
following=profile.get_followees()

followers=[]
followings=[]

for i in follow:
    username=i.username
    followers.append(username)

for j in following:   
    username=j.username
    followings.append(username)
    
counter=0    
outfilename="D:\\PYTHON exps\\PYTHONunfollowers\\"+userid+"_unflb.txt"
outputfile=open(outfilename,"w")


for followee in followings:
    if followee not in followers:
        counter+=1
        
        outputfile.write(followee+"\n")
outputfile.write("\n No. of Non BackFollowers=="+str(counter))        
           
outputfile.close()           
print("Completed")          
    