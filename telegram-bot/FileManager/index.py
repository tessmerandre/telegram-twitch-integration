import csv

def save_user(telegram_id, twitch_username, bypass):
    with open('../users.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([telegram_id, twitch_username, bypass])
        
