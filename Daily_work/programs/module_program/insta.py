import instaloader

data=instaloader.Instaloader()

user=input("enter profile name:")

data.download_profile(user,profile_pic_only=True)