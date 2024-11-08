import instaloader

instaID=input("Enter any Instagram ID:")

insta=instaloader.Instaloader()

insta.download_profile(instaID)

print("download successfully!")