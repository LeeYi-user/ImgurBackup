import os
import re
import sys
import requests

# 確認是否有提供參數
if len(sys.argv) != 2:
    print("請提供一個參數")
    sys.exit()

# 設定Markdown檔案的路徑
markdown_file_path = sys.argv[1]

# 設定下載的圖片儲存位置
image_folder_path = "imgur/"

# 獲取Markdown檔案中的所有圖片連結
with open(markdown_file_path, "r", encoding = "utf-8") as f:
    markdown_content = f.read()
image_links = re.findall(r"!\[.*\]\((http[s]?://i.imgur.com/.*?)\)", markdown_content)

# 下載所有圖片，並儲存到本地端
for link in image_links:
    response = requests.get(link)
    image_path = os.path.join(image_folder_path, link.split("/")[-1])
    with open(image_path, "wb") as f:
        f.write(response.content)

    # 更新Markdown檔案中的圖片連結
    markdown_content = markdown_content.replace(link, image_path)

# 將更新後的Markdown內容寫回原Markdown檔案中
with open(markdown_file_path, "w", encoding = "utf-8") as f:
    f.write(markdown_content)
