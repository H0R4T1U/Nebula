from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from githubUpdater import github

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(github.update_github_data, 'interval', seconds=30)
    scheduler.start()