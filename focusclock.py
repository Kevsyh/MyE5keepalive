import time

def always_focus(minutes):
    seconds = minutes * 60
    end_time = time.time() + seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"保持专注，还有 {remaining_time // 60} 分钟 {remaining_time % 60} 秒！")
        time.sleep(1)

    print("专注时间已结束！")

# 输入您希望专注的分钟数
focus_minutes = int(input("请输入您希望专注的分钟数："))
always_focus(focus_minutes)
