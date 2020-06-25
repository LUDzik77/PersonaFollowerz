from requests_oauthlib import OAuth1Session
import json
from tkinter import *
from PIL import ImageTk, Image

#my_own_module
import twitter_tools

#IMPORTANT: To run the programme you have to add your client and owner keys. 
#You can easily get them from: www.https://developer.twitter.com/en
twitter = OAuth1Session(client_key= 'YOUR KEY HERE',
                        client_secret= 'YOUR KEY HERE',
                        resource_owner_key= 'YOUR KEY HERE',
                        resource_owner_secret= 'YOUR KEY HERE')

root=Tk()
root.title('PersonaFolowerz')
root.iconbitmap('twitter_r_icon.ico')
root.configure(background = 'red')


persons=[]

def twitterdata_for_label(name, id_, description, location, followers):
    
    persons.append((Label(root, fg="white", bg="red"), Label(root, fg="white", bg="black")))
    
    persons[len(persons)-1][0]["text"] = (name + '   twitter id: ' + id_ + '\n' + description + '\n' + location)
    persons[len(persons)-1][0].grid(row = len(persons)+2, column=1)
    persons[len(persons)-1][1]["text"] = (followers + ' followers')
    persons[len(persons)-1][1].grid(row = len(persons)+2, column=2)


def scrap_to_label():
    if twitter_tools.correct_screen_name(entry_1.get(), twitter): 
        name, id_, description, location, followers=twitter_tools.t_account_data(entry_1.get(), twitter)
        #from now on i can play with data, as i have it canned
    else: text='error'
    twitterdata_for_label(name, id_, description, location, followers)


def account_to_label(screenname):
    name, id_, description, location, followers=twitter_tools.t_account_data(screenname, twitter)
    twitterdata_for_label(name, id_, description, location, followers)


Label_description =Label(root, fg="black", bg="red", font=('Helvetica', 10, 'bold'), \
                         text ="Comp@re any twitter account with the Polish Presidential election 2020 candidates accounts^^\n")
Label_description.grid(row = 2, column=1)


theframe = Frame(root, bg='red')
theframe.grid(row=1,column=1)


button1=Button(theframe, width=40, borderwidth=5, text="click & check twitter acc", command=scrap_to_label)
button1.grid(row=2,column=1)


entry_1 =Entry(theframe, width=40, borderwidth=5)
entry_1.insert(10,'            (type twitter`s account name)')
entry_1.grid (row=1, column=1)


path="twPF.png"
logo=ImageTk.PhotoImage(Image.open(path))
Logo_1 = Label(root, image=logo, bg='black')
Logo_1.grid(row=1,column=2)


account_to_label('krzysztofbosak')
account_to_label('trzaskowski_')
account_to_label('szymon_holownia')
account_to_label('andrzejduda')
account_to_label('robertbiedron')
account_to_label('Pawel_Tanajno')
account_to_label('KosiniakKamysz')
account_to_label('StanislawZoltek')
account_to_label('jakubiak_marek')
account_to_label('mir_piotrowski')
account_to_label('Witkowski_UP')


root.mainloop()