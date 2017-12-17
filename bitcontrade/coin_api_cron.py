from crontab import CronTab

my_cron = CronTab(user='Tora')
job = my_cron.new(command='python /home/Tora/api_call_gcs.py')
job.minute.every(60)

my_cron.write()