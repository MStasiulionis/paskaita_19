from tkinter import *
from sklearn.linear_model import LinearRegression

langas = Tk()
langas.geometry("750x450")
langas.title("Akmuo Popierius Žirklės")


def modelio_mokymas(x, y):
    global nuspejimas
    nuspejimas.fit(X=x, y=y)


def logika(data1, data2, data3):
    global nuspejimas
    test = [[data1, data2, data3]]
    outcome = nuspejimas.predict(X=test)
    return outcome


def ivestis(data):
    global galima_ivestis
    return galima_ivestis[str(data)]


def isvestis(data):
    global galima_isvestis
    try:
        return galima_isvestis[int(data)]
    except Exception as e:
        print(f"Klaida logikoj, eilute 15, {data} netinkami duomanys. Exception: {e}")
        return galima_isvestis[1]


def pasirinkimo_taisym(user):
    global victory_dict
    return victory_dict[user]


def neaktyv_mygtukai():
    mygt_akmuo.config(state="disabled")
    mygt_popierius.config(state="disabled")
    mygt_zirkles.config(state="disabled")


def akmuo():
    global pasirinkimas_1
    global pasirinkimas_2
    global teis_komp_pasirinkimas
    global pasirinkimas_3

    zaid_pasirink = "Akmuo"

    pasirinkimas_3 = pasirinkimas_2
    pasirinkimas_2 = pasirinkimas_1
    pasirinkimas_1 = zaid_pasirink

    komp_nuspejimas = logika(ivestis(pasirinkimas_1), ivestis(pasirinkimas_2), ivestis(pasirinkimas_3))
    rezultatas1 = isvestis(komp_nuspejimas)

    teis_komp_pasirinkimas = pasirinkimo_taisym(zaid_pasirink)

    mok_listas_ivest.append([ivestis(pasirinkimas_1), ivestis(pasirinkimas_2), ivestis(pasirinkimas_3)])
    mok_listas_isvestis.append(ivestis(teis_komp_pasirinkimas))
    modelio_mokymas(mok_listas_ivest, mok_listas_isvestis)

    if rezultatas1 == "Akmuo":
        rezultatas = "Lygiosios"
    elif rezultatas1 == "Žirkės":
        rezultatas = "Laimėjai!"
    else:
        rezultatas = "Pralaimėjai!"
    rezult_label.config(text=rezultatas)
    zaid_vardas.config(text="Akmuo")
    komp_vardas.config(text=rezultatas1)
    teis_komp_pasirinkimas = pasirinkimo_taisym(zaid_pasirink)
    neaktyv_mygtukai()


def popierius():
    global pasirinkimas_1
    global pasirinkimas_2
    global teis_komp_pasirinkimas
    global pasirinkimas_3

    zaid_parinink = "Popierius"

    pasirinkimas_3 = pasirinkimas_2
    pasirinkimas_2 = pasirinkimas_1
    pasirinkimas_1 = zaid_parinink

    komp_nuspejimas = logika(ivestis(pasirinkimas_1), ivestis(pasirinkimas_2), ivestis(pasirinkimas_3))
    rezultatas1 = isvestis(komp_nuspejimas)

    teis_komp_pasirinkimas = pasirinkimo_taisym(zaid_parinink)

    mok_listas_ivest.append([ivestis(pasirinkimas_1), ivestis(pasirinkimas_2), ivestis(pasirinkimas_3)])
    mok_listas_isvestis.append(ivestis(teis_komp_pasirinkimas))
    modelio_mokymas(mok_listas_ivest, mok_listas_isvestis)

    if rezultatas1 == "Popierius":
        rezultatas = "Lygiosios"
    elif rezultatas1 == "Žirklės":
        rezultatas = "Pralaimėjai!"
    else:
        rezultatas = "Laimėjai!"
    rezult_label.config(text=rezultatas)
    zaid_vardas.config(text="Popierius")
    komp_vardas.config(text=rezultatas1)
    teis_komp_pasirinkimas = pasirinkimo_taisym(zaid_parinink)
    neaktyv_mygtukai()


def zirkles():
    global pasirinkimas_1
    global pasirinkimas_2
    global teis_komp_pasirinkimas
    global pasirinkimas_3

    zaid_parinink = "Žirklės"

    pasirinkimas_3 = pasirinkimas_2
    pasirinkimas_2 = pasirinkimas_1
    pasirinkimas_1 = zaid_parinink

    komp_nuspejimas = logika(ivestis(pasirinkimas_1), ivestis(pasirinkimas_2), ivestis(pasirinkimas_3))
    rezultatas1 = isvestis(komp_nuspejimas)

    teis_komp_pasirinkimas = pasirinkimo_taisym(zaid_parinink)

    mok_listas_ivest.append([ivestis(pasirinkimas_1), ivestis(pasirinkimas_2), ivestis(pasirinkimas_3)])
    mok_listas_isvestis.append(ivestis(teis_komp_pasirinkimas))
    modelio_mokymas(mok_listas_ivest, mok_listas_isvestis)

    if rezultatas1 == "Akmuo":
        rezultatas = "Pralaimėjai!"
    elif rezultatas1 == "Žirklės":
        rezultatas = "Lygiosios"
    else:
        rezultatas = "Laimėjai!"
    rezult_label.config(text=rezultatas)
    zaid_vardas.config(text="Žirklės")
    komp_vardas.config(text=rezultatas1)
    teis_komp_pasirinkimas = pasirinkimo_taisym(zaid_parinink)
    neaktyv_mygtukai()


def mygt_atstat():
    mygt_akmuo.config(state="active")
    mygt_popierius.config(state="active")
    mygt_zirkles.config(state="active")
    zaid_vardas.config(text="Žaidėjas")
    komp_vardas.config(text="Kompiuteris")
    rezult_label.config(text="")


lango_remas = LabelFrame(langas, text="Akmuo Popierius Žirklės", font='Century 20 bold', labelanchor="n", bd=5,
                         bg="#FFFAF0", width=600, height=450, cursor="target")
lango_remas.pack(expand=True, fill=BOTH)

# sukuriami užrašai naudojami žaidimo lange
zaid_vardas = Label(lango_remas, text="Žaidėjas", font='Helvetica 18 bold', bg='#FFFAF0')
zaid_vardas.place(relx=.18, rely=.1)
vs_label = Label(lango_remas, text="VS", font='Helvetica 18 bold', bg="#FFFAF0")
vs_label.place(relx=.45, rely=.1)
komp_vardas = Label(lango_remas, text="Kompiuteris", font='Helvetica 18 bold', bg='#FFFAF0')
komp_vardas.place(relx=.65, rely=.1)
rezult_label = Label(lango_remas, text="", font=('Coveat', 25, 'bold'), bg="#FFFAF0")
rezult_label.pack(pady=150)

# sukuriami mygtukai
mygt_akmuo = Button(lango_remas, text="Akmuo", font=10, width=7, command=akmuo)
mygt_akmuo.place(relx=.25, rely=.62)
mygt_popierius = Button(lango_remas, text="Popierius", font=10, width=7, command=popierius)
mygt_popierius.place(relx=.41, rely=.62)
mygt_zirkles = Button(lango_remas, text="Žirkės", font=10, width=7, command=zirkles)
mygt_zirkles.place(relx=.58, rely=.62)
reset = Button(lango_remas, text="Reset", bg="OrangeRed3", fg="white", width=7, font=10, command=mygt_atstat)
reset.place(relx=.8, rely=.62)

# mokymo kintamieji kurie naudojami funkcijose
mok_listas_ivest = []
mok_listas_isvestis = []
galima_ivestis = {"Akmuo": 1, "Popierius": 2, "Žirklės": 3}
galima_isvestis = {1: "Akmuo", 2: "Popierius", 3: "Žirklės"}
pasirinkimas_1 = "Akmuo"
pasirinkimas_2 = "Akmuo"
pasirinkimas_3 = "Akmuo"
teis_komp_pasirinkimas = "Popierius"
victory_dict = {"Akmuo": "Popierius", "Popierius": "Žirklės", "Žirklės": "Akmuo"}
nuspejimas = LinearRegression(n_jobs=-1)

mok_listas_ivest.append(
    [ivestis(pasirinkimas_1), ivestis(pasirinkimas_2), ivestis(pasirinkimas_3)])
mok_listas_isvestis.append(ivestis(teis_komp_pasirinkimas))
modelio_mokymas(mok_listas_ivest, mok_listas_isvestis)

langas.mainloop()
