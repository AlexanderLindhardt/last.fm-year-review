from createAlbumCollage import *
from createArtistCollage import *
from topXAlbums import *
from getTopXArtists import *
from getTotalPlaytime import *
import tkinter as tk
from tkinter.ttk import *
from getTopXSongs import *

user = 'DEFAULT'


def main():
    layout = (5, 5)
    start = "31/12/2019"
    end = "31/12/2020"

    root = tk.Tk()
    root.title("Last.fm yearly review")
    root.geometry('1600x700')
    label1 = tk.Label(root, text="Welcome to your last.fm 2020 review!", font=("Arial Bold", 20))
    label1.place(x=0, y=0)

    label_username = tk.Label(root, text="Please enter your username", font=("Arial Bold", 10))
    label_username.place(x=0, y=40)

    txt_username = tk.Entry(root, width=20)
    txt_username.place(x=200, y=40)

    label_success_user = tk.Label(root, text='', font=('helvetica', 12, 'bold'))
    label_success_user.place(x=375, y=40)

    label_top_artists = tk.Label(root, text='', font=('helvetica', 12, 'bold'), justify='left')
    label_top_artists.place(x=550, y=160)

    label_top_albums = tk.Label(root, text='', font=('helvetica', 12, 'bold'),  justify='left')
    label_top_albums.place(x=550, y=260)

    label_top_songs = tk.Label(root, text='', font=('helvetica', 12, 'bold'), justify='left')
    label_top_songs.place(x=550, y=360)

    def show_album_collage(lyt):
        createAlbumCollage(topXAlbums(user, lyt[0] * lyt[1]), lyt[0], lyt[1]).show()

    def artist_collage():
        createArtistCollage(getTopXArtists(user, 10), 5, 2, user)

    def show_top_stats(X=3):
        top_artists = getTopXArtists(user, X)
        top_albums = topXAlbums(user, X)
        top_songs = getTopXSongs(user, X)

        total_plays = getTotalScrobbles(user, start,end)
        text_artist = 'Top ' + str(X) + ' Artists:\n '
        text_album = 'Top ' + str(X) + ' Albums:\n '
        text_song = 'Top ' + str(X) + ' Songs:\n '
        for i in range(X):
            text_artist += str(i+1) + '. ' +top_artists['Artist'][i] + ' - ' + top_artists['Playcount'][i] + ' plays' + ' (' + str(round(100 * (int(top_artists['Playcount'][i]) / total_plays), 2)) + '%)' + '\n '
            text_album += str(i + 1) + '. ' + top_albums['Album'][i] + ' - ' + top_albums['Playcount'][
                i] + ' plays' + ' (' + str(
                round(100 * (int(top_albums['Playcount'][i]) / total_plays), 2)) + '%)' + '\n '
            text_song += str(i + 1) + '. ' + top_songs['Track'][i] + ' - ' + top_songs['Playcount'][
                i] + ' plays' + ' (' + str(
                round(100 * (int(top_songs['Playcount'][i]) / total_plays), 2)) + '%)' + '\n '

        label_top_artists.configure(text=text_artist)
        label_top_artists.place(x=550, y=160)
        label_top_albums.configure(text=text_album)
        label_top_albums.place(x=550, y=160 + 25 + (X*25))
        label_top_songs.configure(text=text_song)
        label_top_songs.place(x=550, y=160 + 25*2 + 2*(X*25))

    def album_collage_layout():
        label_album_collage_layout = tk.Label(root,
                                              text='Please choose how many albums you want and your desired layout',
                                              font=('helvetica', 10))
        label_album_collage_layout.place(x=0, y=170)

        button_3x3 = tk.Button(root, text='3x3', command=lambda: show_album_collage((3, 3)),
                               bg='brown',
                               fg='white')
        button_3x3.place(x=20, y=200)

        button_5x5 = tk.Button(root, text='5x5', command=lambda: show_album_collage((5, 5)),
                               bg='brown',
                               fg='white')
        button_5x5.place(x=70, y=200)

        button_10x10 = tk.Button(root, text='10x10', command=lambda: show_album_collage((10, 10)),
                                 bg='brown',
                                 fg='white')
        button_10x10.place(x=123, y=200)

        label_customized = tk.Label(root, text='Customized layout \n (rows, columns)', font=('helvetica', 10))
        label_customized.place(x=185, y=193)

        combo1 = Combobox(root, width=5)
        combo1['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        combo1.place(x=310, y=200)

        combo2 = Combobox(root, width=5)
        combo2['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        combo2.place(x=370, y=200)

        button_apply_layout = tk.Button(root, text='Apply',
                                        command=lambda: show_album_collage((int(combo1.get()), int(combo2.get()))),
                                        bg='brown',
                                        fg='white')
        button_apply_layout.place(x=435, y=200)

    def set_username(new_user):
        global user
        user = new_user
        label_success_user.configure(text='Success!', fg='green')
        try:
            getTopXArtists(user, 1)
        except Exception as e:
            label_success_user.configure(text='No such user exists, try again', fg='red')
            return

        button_playtime = tk.Button(root, text='Calculate playtime',
                                    command=lambda: get_playtime(),
                                    bg='brown',
                                    fg='white')
        button_playtime.place(x=1250, y=100)
        label_playtime = tk.Label(root, text='This might take a few minutes...',
                                  font=('helvetica', 8))
        label_playtime.place(x=1230, y=130)

        label_album_collage = tk.Label(root, text='Press this button to make a collage of your favorite albums',
                                       font=('helvetica', 10))
        label_album_collage.place(x=0, y=100)

        button_album_collage = tk.Button(root, text='Album collage', command=lambda: album_collage_layout(), bg='brown',
                                         fg='white')
        button_album_collage.place(x=100, y=130)

        label_artist_collage = tk.Label(root,
                                        text='Press this button to make a collage of your top 10 artists with stats',
                                        font=('helvetica', 10))
        label_artist_collage.place(x=0, y=300)
        label_artist_time = tk.Label(root, text='This might take a few minutes...',
                                  font=('helvetica', 8))
        label_artist_time.place(x=70, y=360)

        button_artist_collage = tk.Button(root, text='Artist collage', command=lambda: artist_collage(),
                                          bg='brown',
                                          fg='white')
        button_artist_collage.place(x=100, y=330)

        label_top_stats = tk.Label(root,
                                   text='Press to show your top artists, albums and songs',
                                   font=('helvetica', 10))
        label_top_stats.place(x=600, y=100)
        label_top_combo = tk.Label(root,
                                   text='You can choose how many you want to show',
                                   font=('helvetica', 10))
        label_top_combo.place(x=600, y=130)
        combo_stats = Combobox(root, width=3)
        combo_stats['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        combo_stats.place(x=550, y=130)
        combo_stats.current(2)
        button_top_stats = tk.Button(root, text='Show', command=lambda: show_top_stats(X=int(combo_stats.get())),
                                     bg='brown',
                                     fg='white')
        button_top_stats.place(x=550, y=100)


    label_playtime = tk.Label(root, text='', font=('helvetica', 12, 'bold'))
    label_playtime.place(x=1130, y=160)

    button_username = tk.Button(root, text='Apply', command=lambda: set_username(txt_username.get()), bg='brown',
                                fg='white')
    button_username.place(x=330, y=38)

    def get_playtime():
        avg, total, total_scrobbles = getTotalPlaytime(user, start, end)
        label_playtime.configure(text='Total playtime for user ' + user + ' in 2020 was:\n ' + str(
            round(total)) + ' minutes or\n ' + str(int(total / (60 * 24))) + ' days and ' + str(
            round(total / 60) % 24) + ' hours.\n \n' + 'With a total playcount of ' + str(
            total_scrobbles) + ' songs \n \n' 'and average song length was ' + str(round(avg, 2)) + ' minutes. \n \n' +
                                      'An average of ' + str(round(total_scrobbles / 365)) + ' songs or ' + str(
            round(total / (60 * 365), 2)) + ' hours each day')

    root.mainloop()
    # end = "31/12/2020"
    # print(getTotalPlaytime(user,start,end))
    # createAlbumCollage(topXAlbums(user, 10), 5, 2).show()
    # print(getTopXArtists(user, 10)['Image'][0])
    # createArtistCollage(getTopXArtists(user, 10), 5, 2)


if __name__ == '__main__':
    main()
