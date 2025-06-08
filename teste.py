import schedule
import time
import winotify

def notifica():
    notificação = winotify.Notification(app_id='TESTE',title='Teste1', msg='QUERO TESTAR')
    notificação.show()

schedule.every(5).sunday.do(notifica)

while True:
    schedule.run_pending()
    time.sleep(1)
    