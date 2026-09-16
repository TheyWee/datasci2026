from notion_client import Client
from datetime import datetime
import os

NOTION_TOKEN = "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"
DATABASE_ID = "3dde8c45add0808b8d59e2a41ea4dc4b"
notion = Client(auth=NOTION_TOKEN)

def submit_grade(name: str, lab_name: str, grade: float, comment: str = ""):
    notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Name": {
                "title": [{"text": {"content": name}}]
            },
            "Lab": {
                "rich_text": [{"text": {"content": lab_name}}]
            },            
            "Grade": {
                "number": grade
            },
            "Date": {
                "date": {"start": datetime.now().isoformat()}
            },
            "Comment": {
                "rich_text": [{"text": {"content": comment}}]
            },            
        }
    )
    #print("Дані успішно відправлено в Notion!")