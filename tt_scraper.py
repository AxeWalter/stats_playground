import asyncio
from twscrape import API
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

tt_username1 = os.getenv("TT_USERNAME1")
tt_password1 = os.getenv("TT_PASSWORD1")
email1 = os.getenv("EMAIL1")
email_password1 = os.getenv("EMAIL_PASSWORD1")

tt_username2 = os.getenv("TT_USERNAME2")
tt_password2 = os.getenv("TT_PASSWORD2")
email2 = os.getenv("EMAIL2")
email_password2 = os.getenv("EMAIL_PASSWORD2")

tt_username3 = os.getenv("TT_USERNAME3")
tt_password3 = os.getenv("TT_PASSWORD3")
email3 = os.getenv("EMAIL3")
email_password3 = os.getenv("EMAIL_PASSWORD3")

async def main():
    api = API()

    # https://github.com/vladkens/twscrape/issues/214
    await api.pool.add_account(tt_username1, tt_password1,email1, email_password1)

    await api.pool.add_account(tt_username2, tt_password2, email2, email_password2)

    await api.pool.add_account(tt_username3, tt_password3, email3, email_password3)
    await api.pool.login_all()


async def dirty_scrape():
    api = API()

    tweets_data = []
    index = 1

    async for tweet in api.search("rony lang:pt", limit=1000):
        tweets_data.append({
            "id": index,
            "Username": tweet.user.username,
            "Date": tweet.date,
            "Text": tweet.rawContent
        })
        index += 1

    df = pd.DataFrame(tweets_data)
    df.to_csv("tweets_rony2.csv", index=False)

if __name__ == "__main__":
    asyncio.run(main())
    #asyncio.run(dirty_scrape())
