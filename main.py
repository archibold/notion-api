# Notion API
from dotenv import load_dotenv
import os
from notion import Notion
load_dotenv()

NOTION_API_KEY = os.getenv('NOTION_API_KEY')


def getNotionDatabases():
    notion = Notion(NOTION_API_KEY)
    notion.databases()


if __name__ == '__main__':
    getNotionDatabases()
