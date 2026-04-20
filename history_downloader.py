import wikipediaapi
import os

# 1. The "Big" History List (Long-form articles only)
history_topics = [
    "Muhammad",  # The Seerah / Foundation
    "History of Islam",
    "Rashidun Caliphate",
    "Umayyad Caliphate",
    "Abbasid Caliphate",
    "Islamic Golden Age",
    "Ottoman Empire",
    "Mamluk Sultanate (Cairo)",
    "Al-Andalus",
    "Fatimid Caliphate",
    "Ayyubid dynasty"
]

def download_history():
    # 2. Initialize with a User Agent (Wikipedia requires this in 2026)
    wiki = wikipediaapi.Wikipedia(
        user_agent="IslamicHistoryBot/1.0 (contact@example.com)",
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    folder = "./history_pages"
    os.makedirs(folder, exist_ok=True)
    
    print(f"🚀 Downloading {len(history_topics)} major history articles...")

    for topic in history_topics:
        try:
            # IMPORTANT: Use wiki.page() not wikipedia.page()
            page = wiki.page(topic)
            
            if page.exists():
                filename = topic.replace(" ", "_") + ".txt"
                path = os.path.join(folder, filename)
                
                # Save the text
                with open(path, "w", encoding="utf-8") as f:
                    f.write(page.text)
                
                print(f"✅ Saved: {topic} ({len(page.text.split())} words)")
            else:
                print(f"⚠️ Page not found: {topic}")
                
        except Exception as e:
            print(f"❌ Error with {topic}: {e}")

if __name__ == "__main__":
    download_history()