import os
from googleapiclient.discovery import build
from supabase import create_client, Client

# 🎯 YouTube API Configuration
YOUTUBE_API_KEY = "YOUTUBE_API_KEY"
VIDEO_IDS = [
    "---AOnslvBo",
    "---Hnqef64k",
    "---JLbBz6Ls",
    "---KIj04zPQ",
    "---XjA38-uo",
    "---eDafFBhg",
    "---k1vFBbWw",
    "---kL8ZiM7g",
    "---n0WDScf8",
    "--01APk266U",
    "--02D71FV0g",
    "--0FinuLhug",
    "--0PHPuKyVU",
    "--0TYFEyz0c",
    "--0bCF-iK2E",
    "--0r21x1q1g",
    "--10rdVLy1U",
    "--11m37rCFQ",
    "--14w5SOEUs",
    "--1AXfq-Nl0",
    "--1GL5dLrYI",
    "--1IpIrEU1k",
    "--1PlF2VNP4",
    "--1eOrPughU",
    "--1kZDOLC9Q",
    "--1lSmtuyUg",
    "--1tPAtBOmM",
    "--1yBpF537M",
    "--28BBjBQLU",
    "--2N2QdRVs0",
    "--2SnbjKklM",
    "--2TdkJFZ2A",
    "--2VKlyOXGw",
    "--2YkuFG3b4",
    "--2eG2F7LHI",
    "--2oRD1ifBs",
    "--2pJasAQFY",
    "--2r8Pn0jT8",
    "--3-beh8d9Q",
    "--300uf_82g",
    "--35JjRdKv8",
    "--3B0KgX-Ug",
    "--3Hn6OK9EE",
]

# 🎯 Supabase Configuration
SUPABASE_URL = "https://kzneblpfsvyuvbslltou.supabase.co"
SUPABASE_SERVICE_KEY = "SUPABASE_SERVICE_KEY"

# ✅ Initialize Supabase Client
supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# ✅ Initialize YouTube API Client
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)


def fetch_video_details(video_id):
    """📌 Fetches video details including the thumbnail URL."""
    request = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    )
    response = request.execute()

    if not response.get("items"):
        print(f"⚠ No data found for Video ID: {video_id}")
        return None, None

    video_data = response["items"][0]
    snippet = video_data["snippet"]
    statistics = video_data["statistics"]

    # Extract thumbnail URL (high resolution)
    thumbnail_url = snippet["thumbnails"]["high"]["url"] if "high" in snippet["thumbnails"] else None

    video_info = {
        "video_id": video_id,
        "channel_id": snippet["channelId"],
        "title": snippet["title"],
        "description": snippet["description"],
        "published_at": snippet["publishedAt"],
        "views": int(statistics.get("viewCount", 0)),
        "likes": int(statistics.get("likeCount", 0)),
        "comments": int(statistics.get("commentCount", 0)),
        "thumbnail_url": thumbnail_url
    }

    return video_info, snippet["channelId"]


def fetch_channel_details(channel_id):
    """📊 Fetches channel details."""
    request = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id
    )
    response = request.execute()

    if not response.get("items"):
        print(f"⚠ No data found for Channel ID: {channel_id}")
        return None

    channel_data = response["items"][0]
    snippet = channel_data["snippet"]
    statistics = channel_data["statistics"]

    channel_info = {
        "channel_id": channel_id,
        "channel_name": snippet["title"],
        "description": snippet["description"],
        "subscribers": int(statistics.get("subscriberCount", 0)),
        "total_views": int(statistics.get("viewCount", 0)),
        "total_videos": int(statistics.get("videoCount", 0))
    }

    return channel_info


def insert_video_data(video_info):
    """📌 Inserts video data into Supabase."""
    if not video_info:
        return

    # Check if video already exists
    existing = supabase.table("youtube_videos").select("video_id").eq("video_id", video_info["video_id"]).execute()
    if existing.data:
        print(f"⚠ Skipping duplicate Video: {video_info['title']}")
    else:
        supabase.table("youtube_videos").insert(video_info).execute()
        print(f"✅ Inserted Video: {video_info['title']}")


def insert_channel_data(channel_info):
    """📌 Inserts channel data into Supabase."""
    if not channel_info:
        return

    # Check if channel already exists
    existing = supabase.table("youtube_channels").select("channel_id").eq("channel_id", channel_info["channel_id"]).execute()
    if existing.data:
        print(f"⚠ Skipping duplicate Channel: {channel_info['channel_name']}")
    else:
        supabase.table("youtube_channels").insert(channel_info).execute()
        print(f"✅ Inserted Channel: {channel_info['channel_name']}")


if __name__ == "__main__":
    processed_channels = set()

    for video_id in VIDEO_IDS:
        video_info, channel_id = fetch_video_details(video_id)
        insert_video_data(video_info)

        if channel_id and channel_id not in processed_channels:
            channel_info = fetch_channel_details(channel_id)
            insert_channel_data(channel_info)
            processed_channels.add(channel_id)

    print("🚀 Data successfully inserted into Supabase!")
