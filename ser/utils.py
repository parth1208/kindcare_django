from django.core.mail import send_mail      # for sending mail
from django.template.loader import render_to_string    
from django.utils.html import strip_tags
from datetime import datetime, timedelta

def sendmail(subject,template,to,context):

    template_str = template+'.html' #get template from templates folder
    html_message = render_to_string(template_str, {'data': context})  
    plain_message = strip_tags(html_message)  #Tries to remove anything that looks like an   
    #HTML tag from the string, that is anything      contained within <>.
    from_email ='parthmangukiya1208@gmail.com'
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

