#!/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import json
import os
user = os.environ.get('USER')
jsof="main.json"
window = tk.Tk()
window.geometry("600x400")
window.configure(background='black')
# window grids
toolbar = tk.Frame(window, background="black", height=40)
main = tk.PanedWindow(window, background="black")
toolbar.pack(side="top", fill="x")
main.pack(side="top", fill="both", expand=True)
left_pane = tk.Frame(main, background="black", width=100)
right_pane = tk.PanedWindow(main, background="black", width=200)
main.add(left_pane)
main.add(right_pane)
# toolbar
tbutton3=tk.Button(toolbar, text="x")
tbutton3.pack( side = tk.RIGHT)

tbutton2=tk.Button(toolbar, text="edit")
tbutton2.pack(side=tk.RIGHT)

# add to invintory + button
def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = tk.Toplevel(window)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")
    newWindow.configure(background="black")

    def callback(selection):
       print(selection)
       if selection == "pc":
           drop.pack_forget()
           top = tk.Frame(newWindow, background="black", height=40)
           main = tk.PanedWindow(newWindow, background="black")

           top.pack(side="top", fill="x")
           main.pack(side="top", fill="both", expand=True)
           left_pane = tk.Frame(main, background="black", width=300)
           right_pane = tk.PanedWindow(main, background="black", width=300)
           main.add(left_pane)
           main.add(right_pane)
           left = tk.Label(top,text="pc")
           left.pack()

           # turn input into json
           def submit():
               pcb=cbrandrv.get()
               pcm=cmodelv.get()
               pco=corev.get()
               pig=igpuv.get()
               pt=threadv.get()
               pso=socketv.get()
               pch=chipsetv.get()
               pcl=clockv.get()
               pgb=gbrandv.get()
               pgr=gramv.get()
               ppv=pciv.get()
               pd=dpv.get()
               ph=hdmiv.get()
               pse=serialv.get()
               po=otherpv.get()
               pgt=gtypev.get()
               pgm=gmodelv.get()
               pra=ramtv.get()
               pec=eccv.get()
               prm=ramv.get()
               prs=ramslotsv.get()
               psa=satav.get()
               ppi=pci16v.get()
               pu=usbpv.get()
               pa=amountv.get()
               pma=mramv.get()
               pnv=nvmev.get()
               r={}
               r['cpu_model']= pcm
               r['cpu_core']= pco
               r['igpu']= pig
               r['ram']= prm
               r['ram_slots']= prs
               r['ddr']= pra
               r['sata']=psa
               r['max_ram']= pma
               r['nvme']= pnv
               r['csocket']= pso
               r['cthread']= pt
               r['gpu_model']= pgm
               r['usb_ports']= pu
               r['cpu_brand']= pcb
               r['cpu_chipset']= pch
               r['gbrand']= pgb
               r['pcie_gen']= ppv
               r['cpu_clock']= pcl
               r['vram']= pgr
               r['ecc']= pec
               r['display_ports']= pd
               r['other_ports'] = po
               r['hdmi_ports'] = ph
               r['serial']= pse
               r['gmem_type'] = pgt
               r['pcie16'] = ppi
               r['amount'] = pa


               print(json.dumps(r))
               def write_json(new_data, filename=jsof):
                 with open(filename,'r+') as file:
                # First we load existing data into a dict.
                    file_data = json.load(file)
        # Join new_data with file_data inside emp_details
                    file_data["pc"].append(new_data)
        # Sets file's current position at offset.
                    file.seek(0)
        # convert back to json.
                    json.dump(file_data, file, indent = 4)
               write_json(r)
               newWindow.destroy()
           sub_btn=tk.Button(top,text="submit",command=submit)
           sub_btn.pack()

           # max ram nvme

           # labels
           cbrand=tk.Label(left_pane,text="cpu brand")
           cbrand.pack(fill = tk.BOTH, expand = True)
           cmodel=tk.Label(left_pane,text="cpu model")
           cmodel.pack(fill = tk.BOTH, expand = True)
           core = tk.Label(left_pane,text="cpu cores")
           core.pack(fill = tk.BOTH, expand = True)
           igpu=tk.Label(left_pane,text="intergrated graphics")
           igpu.pack(fill = tk.BOTH, expand = True)
           thread=tk.Label(left_pane,text="cpu threads")
           thread.pack(fill = tk.BOTH, expand = True)
           socket=tk.Label(left_pane,text="cpu socket")
           socket.pack(fill = tk.BOTH, expand = True)
           chipset=tk.Label(left_pane,text="cpu chipset")
           chipset.pack(fill = tk.BOTH, expand = True)
           clock=tk.Label(left_pane,text="cpu base clock")
           clock.pack(fill = tk.BOTH, expand = True)
           gbrand=tk.Label(left_pane,text="gpu brand")
           gbrand.pack(fill = tk.BOTH, expand = True)
           gram=tk.Label(left_pane,text="gpu vram")
           gram.pack(fill = tk.BOTH, expand = True)
           pci=tk.Label(left_pane,text="pci gen")
           pci.pack(fill = tk.BOTH, expand = True)
           dp=tk.Label(left_pane,text="display ports")
           dp.pack(fill = tk.BOTH, expand = True)
           hdmi=tk.Label(left_pane,text="hdmi ports")
           hdmi.pack(fill = tk.BOTH, expand = True)
           serial=tk.Label(left_pane,text="serial ports")
           serial.pack(fill = tk.BOTH, expand = True)
           otherp=tk.Label(left_pane,text="other ports")
           otherp.pack(fill = tk.BOTH, expand = True)
           gtype=tk.Label(left_pane,text="gpu mem type")
           gtype.pack(fill = tk.BOTH, expand = True)
           gmodel=tk.Label(left_pane,text="gpu model")
           gmodel.pack(fill = tk.BOTH, expand = True)
           ramt=tk.Label(left_pane,text="ddr type")
           ramt.pack(fill = tk.BOTH, expand = True)
           ecc=tk.Label(left_pane,text="ecc ram")
           ecc.pack(fill = tk.BOTH, expand = True)
           ram=tk.Label(left_pane,text="ram amount")
           ram.pack(fill = tk.BOTH, expand = True)
           mram=tk.Label(left_pane,text="max ram support")
           mram.pack(fill = tk.BOTH, expand = True)
           nvme=tk.Label(left_pane,text="nvme slots")
           nvme.pack(fill = tk.BOTH, expand = True)
           ramslots=tk.Label(left_pane,text="ram slots")
           ramslots.pack(fill = tk.BOTH, expand = True)
           sata=tk.Label(left_pane,text="sata ports")
           sata.pack(fill = tk.BOTH, expand = True)
           pci16=tk.Label(left_pane,text="pci 16x")
           pci16.pack(fill = tk.BOTH, expand = True)
           usbp=tk.Label(left_pane,text="usb ports")
           usbp.pack(fill = tk.BOTH, expand = True)
           amount=tk.Label(left_pane,text="amount")
           amount.pack(fill = tk.BOTH, expand = True)

           # input vars
           cmodelv=tk.StringVar();
           socketv=tk.StringVar();
           cbrandrv=tk.StringVar();
           threadv=tk.StringVar();
           corev=tk.StringVar();
           igpuv=tk.StringVar();
           mramv=tk.StringVar()
           nvmev=tk.StringVar()
           chipsetv=tk.StringVar();
           clockv=tk.StringVar();
           gbrandv=tk.StringVar();
           gramv=tk.StringVar();
           pciv=tk.StringVar();
           dpv=tk.StringVar();
           hdmiv=tk.StringVar();
           serialv=tk.StringVar();
           otherpv=tk.StringVar();
           gtypev=tk.StringVar();
           gmodelv=tk.StringVar();
           ramtv=tk.StringVar();
           eccv=tk.StringVar();
           ramv=tk.StringVar();
           ramslotsv=tk.StringVar();
           satav=tk.StringVar();
           pci16v=tk.StringVar();
           usbpv=tk.StringVar();
           amountv=tk.StringVar();

           # input
           cbrandrv.set("Choose one")
           brand = tk.OptionMenu(right_pane,cbrandrv,"powerpc","intel","amd")
           brand.pack(fill= tk.BOTH, expand=True)
           cmodele = tk.Entry(right_pane,textvariable=cmodelv)
           cmodele.pack(fill = tk.BOTH, expand = True)
           threade=tk.Entry(right_pane,textvariable=threadv)
           threade.pack(fill = tk.BOTH, expand = True)
           coree=tk.Entry(right_pane,textvariable=corev)
           coree.pack(fill = tk.BOTH, expand = True)
           igpue=tk.Entry(right_pane,textvariable=igpuv)
           igpue.pack(fill = tk.BOTH, expand = True)
           sockete=tk.Entry(right_pane,textvariable=socketv)
           sockete.pack(fill = tk.BOTH, expand = True)
           chipsete=tk.Entry(right_pane,textvariable=chipsetv)
           chipsete.pack(fill = tk.BOTH, expand = True)
           clocke=tk.Entry(right_pane,textvariable=clockv)
           clocke.pack(fill = tk.BOTH, expand = True)
           gbrandv.set("Choose one")
           gbrande=tk.OptionMenu(right_pane,gbrandv,"msi","nvidia","amd","evga","asus","gigabyte","sapphiretech")
           gbrande.pack(fill = tk.BOTH, expand = True)
           grame=tk.Entry(right_pane,textvariable=gramv)
           grame.pack(fill = tk.BOTH, expand = True)
           pcie=tk.Entry(right_pane,textvariable=pciv)
           pcie.pack(fill = tk.BOTH, expand = True)
           dpe=tk.Entry(right_pane,textvariable=dpv)
           dpe.pack(fill = tk.BOTH, expand = True)
           hdmie=tk.Entry(right_pane,textvariable=hdmiv)
           hdmie.pack(fill = tk.BOTH, expand = True)
           seriale=tk.Entry(right_pane,textvariable=serialv)
           seriale.pack(fill = tk.BOTH, expand = True)
           otherpe=tk.Entry(right_pane,textvariable=otherpv)
           otherpe.pack(fill = tk.BOTH, expand = True)
           gtypee=tk.Entry(right_pane,textvariable=gtypev)
           gtypee.pack(fill = tk.BOTH, expand = True)
           gmodele=tk.Entry(right_pane,textvariable=gmodelv)
           gmodele.pack(fill = tk.BOTH, expand = True)
           ramte=tk.Entry(right_pane,textvariable=ramtv)
           ramte.pack(fill = tk.BOTH, expand = True)
           nvmee=tk.Entry(right_pane,textvariable=nvmev)
           nvmee.pack(fill = tk.BOTH, expand = True)
           mrame=tk.Entry(right_pane,textvariable=mramv)
           mrame.pack(fill = tk.BOTH, expand = True)
           ecce=tk.Entry(right_pane,textvariable=eccv)
           ecce.pack(fill = tk.BOTH, expand = True)
           rame=tk.Entry(right_pane,textvariable=ramv)
           rame.pack(fill = tk.BOTH, expand = True)
           ramslotse=tk.Entry(right_pane,textvariable=ramslotsv)
           ramslotse.pack(fill = tk.BOTH, expand = True)
           satae=tk.Entry(right_pane,textvariable=satav)
           satae.pack(fill = tk.BOTH, expand = True)
           pci16e = tk.Entry(right_pane,textvariable=pci16v)
           pci16e.pack(fill = tk.BOTH, expand = True)
           usbpe=tk.Entry(right_pane,textvariable=usbpv)
           usbpe.pack(fill = tk.BOTH, expand = True)
           amounte=tk.Entry(right_pane,textvariable=amountv)
           amounte.pack(fill = tk.BOTH, expand = True)
       elif selection=="cables":
           drop.pack_forget()
           top = tk.Frame(newWindow, background="black", height=40)
           main = tk.PanedWindow(newWindow, background="black")

           top.pack(side="top", fill="x")
           main.pack(side="top", fill="both", expand=True)
           left_pane = tk.Frame(main, background="black", width=300)
           right_pane = tk.PanedWindow(main, background="black", width=300)
           main.add(left_pane)
           main.add(right_pane)
           left = tk.Label(top,text="cables")
           left.pack()

           def submit():
               cta = ctypev.get()
               cr1 =cp1v.get()
               cr2 = cp2v.get()
               cr3 = cp3v.get()
               ctl = lengthv.get()
               ctc = ccatv.get()
               ctm = amountv.get()
               w={}
               w['cable_gender']= cta
               w['cp1']= cr1
               w['cp2']= cr2
               w['cp3']= cr3
               w['caterogory']= ctc
               w['length']=ctl
               w['amount']=ctm
               print(json.dumps(w))
               def write_json(new_data, filename=jsof):
                 with open(filename,'r+') as file:
                # First we load existing data into a dict.
                    file_data = json.load(file)
        # Join new_data with file_data inside emp_details
                    file_data["cable"].append(new_data)
        # Sets file's current position at offset.
                    file.seek(0)
        # convert back to json.
                    json.dump(file_data, file, indent = 4)
               write_json(w)
               newWindow.destroy()
           sub_btn=tk.Button(top,text="submit",command=submit)
           sub_btn.pack()

           # labels
           length=tk.Label(left_pane,text="cable length")
           length.pack(fill = tk.BOTH, expand = True)
           ctype=tk.Label(left_pane,text="cable gender")
           ctype.pack(fill = tk.BOTH, expand = True)
           cp1=tk.Label(left_pane,text="cable port 1")
           cp1.pack(fill = tk.BOTH, expand = True)
           cp2=tk.Label(left_pane,text="cable port 2")
           cp2.pack(fill = tk.BOTH, expand = True)
           cp3=tk.Label(left_pane,text="cable port 3")
           cp3.pack(fill = tk.BOTH, expand = True)
           ccat=tk.Label(left_pane,text="cable caterogory")
           ccat.pack(fill = tk.BOTH, expand = True)
           amount=tk.Label(left_pane,text="amount")
           amount.pack(fill = tk.BOTH, expand = True)

           lengthv=tk.StringVar()
           ctypev=tk.StringVar()
           cp1v=tk.StringVar()
           cp2v=tk.StringVar()
           ccatv=tk.StringVar()
           cp3v=tk.StringVar()
           amountv=tk.StringVar()

           lengthe=tk.Entry(right_pane,textvariable=lengthv)
           lengthe.pack(fill = tk.BOTH, expand = True)
           ctypee=tk.Entry(right_pane,textvariable=ctypev)
           ctypee.pack(fill = tk.BOTH, expand = True)
           cp1e=tk.Entry(right_pane,textvariable=cp1v)
           cp1e.pack(fill = tk.BOTH, expand = True)
           cp2e=tk.Entry(right_pane,textvariable=cp2v)
           cp2e.pack(fill = tk.BOTH, expand = True)
           cp3e=tk.Entry(right_pane,textvariable=cp3v)
           cp3e.pack(fill = tk.BOTH, expand = True)
           ccate=tk.Entry(right_pane,textvariable=ccatv)
           ccate.pack(fill= tk.BOTH,expand=True)
           amounte=tk.Entry(right_pane,textvariable=amountv)
           amounte.pack(fill = tk.BOTH, expand = True)
       elif selection == "books":
           drop.pack_forget()
           top = tk.Frame(newWindow, background="black", height=40)
           main = tk.PanedWindow(newWindow, background="black")

           top.pack(side="top", fill="x")
           main.pack(side="top", fill="both", expand=True)
           left_pane = tk.Frame(main, background="black", width=300)
           right_pane = tk.PanedWindow(main, background="black", width=300)
           main.add(left_pane)
           main.add(right_pane)
           left = tk.Label(top,text="books")
           left.pack()

           def submit():
               ba=namev.get()
               bu=authorv.get()
               bd=datev.get()
               bo=onlinev.get()
               d={}
               d['name']= ba
               d['author']= bu
               d['date']= bd
               d['online']= bo
               print(json.dumps(d))
               def write_json(new_data, filename=jsof):
                 with open(filename,'r+') as file:
                # First we load existing data into a dict.
                    file_data = json.load(file)
        # Join new_data with file_data inside emp_details
                    file_data["book"].append(new_data)
        # Sets file's current position at offset.
                    file.seek(0)
        # convert back to json.
                    json.dump(file_data, file, indent = 4)
               write_json(d)

               newWindow.destroy()
           sub_btn=tk.Button(top,text="submit",command=submit)
           sub_btn.pack()
           # labels
           name=tk.Label(left_pane,text="book name")
           name.pack(fill = tk.BOTH, expand = True)
           author=tk.Label(left_pane,text="author")
           author.pack(fill = tk.BOTH, expand = True)
           date=tk.Label(left_pane,text="date")
           date.pack(fill = tk.BOTH, expand = True)
           online=tk.Label(left_pane,text="online book")
           online.pack(fill = tk.BOTH, expand = True)

           namev=tk.StringVar()
           authorv=tk.StringVar()
           datev=tk.StringVar()
           onlinev=tk.StringVar()

           namee=tk.Entry(right_pane,textvariable=namev)
           namee.pack(fill = tk.BOTH, expand = True)
           authore=tk.Entry(right_pane,textvariable=authorv)
           authore.pack(fill = tk.BOTH, expand = True)
           datee=tk.Entry(right_pane,textvariable=datev)
           datee.pack(fill = tk.BOTH, expand = True)
           onlinee=tk.Entry(right_pane,textvariable=onlinev)
           onlinee.pack(fill = tk.BOTH, expand = True)
       elif selection == "games":
           drop.pack_forget()
           top = tk.Frame(newWindow, background="black", height=40)
           main = tk.PanedWindow(newWindow, background="black")

           top.pack(side="top", fill="x")
           main.pack(side="top", fill="both", expand=True)
           left_pane = tk.Frame(main, background="black", width=300)
           right_pane = tk.PanedWindow(main, background="black", width=300)
           main.add(left_pane)
           main.add(right_pane)
           left = tk.Label(top,text="games")
           left.pack()

           def submit():
               gn=namelv.get()
               gp=platformv.get()
               gs=studiov.get()
               go=onlinelv.get()
               # dataa={"name":" + gn + ","platform":" + gp + ","studio":" + gs + ","online":" + go + "}
               d = {}
               d['name'] = gn
               d['platform'] = gp
               d['studio'] = gs
               d['online'] = go
               print(json.dumps(d))
               def write_json(new_data, filename=jsof):
                 with open(filename,'r+') as file:
                # First we load existing data into a dict.
                    file_data = json.load(file)
        # Join new_data with file_data inside emp_details
                    file_data["game"].append(new_data)
        # Sets file's current position at offset.
                    file.seek(0)
        # convert back to json.
                    json.dump(file_data, file, indent = 4)
               write_json(d)
               newWindow.destroy()
           sub_btn=tk.Button(top,text="submit",command=submit)
           sub_btn.pack()
           # labels
           namel=tk.Label(left_pane,text="name")
           namel.pack(fill = tk.BOTH, expand = True)
           platform=tk.Label(left_pane,text="platfrorm")
           platform.pack(fill = tk.BOTH, expand = True)
           studio=tk.Label(left_pane,text="studio")
           studio.pack(fill = tk.BOTH, expand = True)
           onlinel=tk.Label(left_pane,text="online")
           onlinel.pack(fill = tk.BOTH, expand = True)

           # input

           namelv=tk.StringVar()
           platformv=tk.StringVar()
           studiov=tk.StringVar()
           onlinelv=tk.StringVar()

           namee=tk.Entry(right_pane,textvariable=namelv)
           namee.pack(fill = tk.BOTH, expand = True)
           platforme=tk.Entry(right_pane,textvariable=platformv)
           platforme.pack(fill = tk.BOTH, expand = True)
           studioe=tk.Entry(right_pane,textvariable=studiov)
           studioe.pack(fill = tk.BOTH, expand = True)
           onlinele=tk.Entry(right_pane,textvariable=onlinelv)
           onlinele.pack(fill = tk.BOTH, expand = True)


       elif selection == "pc_parts":
           drop.pack_forget()
           top = tk.Frame(newWindow, background="black", height=40)
           main = tk.PanedWindow(newWindow, background="black")

           top.pack(side="top", fill="x")
           main.pack(side="top", fill="both", expand=True)
           left_pane = tk.Frame(main, background="black", width=300)
           right_pane = tk.PanedWindow(main, background="black", width=300)
           main.add(left_pane)
           main.add(right_pane)
           left = tk.Label(top,text="pc parts")
           left.pack()

           def choose1():
               inp=pi.get()
               if inp == "ram":
                   sub_btn.destroy()
                   co.destroy()

                   def submit():
                       rn=namev.get()
                       rd=ddrv.get()
                       rs=speedv.get()
                       rf=formv.get()
                       ri=dimmv.get()
                       rb=brandv.get()
                       rm=modelv.get()
                       rct=catv.get()
                       rcp=capv.get()
                       d={}
                       d['name']=rn
                       d['cap_total']=rct
                       d['cap_per']=rcp
                       d['ddr']=rd
                       d['dimm']=ri
                       d['model']=rm
                       d['speed']=rs
                       d['brand']=rb
                       d['form']=rf
                       def write_json(new_data, filename=jsof):
                        with open(filename,'r+') as file:
                            file_data = json.load(file)
                            file_data["ram"].append(new_data)
                            file.seek(0)
                # First we load existing data into a dict.
        # Join new_data with file_data inside emp_details
        # Sets file's current position at offset.
        # convert back to json.
                            json.dump(file_data, file, indent = 4)
                       write_json(d)
                       newWindow.destroy()
                   btn=tk.Button(top,text="submit",command=submit)
                   btn.pack()
                   # labels
                   ddr=tk.Label(left_pane,text="Type of Memory (ddr)")
                   ddr.pack(fill = tk.BOTH, expand = True)
                   speed=tk.Label(left_pane,text="speed")
                   speed.pack(fill = tk.BOTH, expand = True)
                   form=tk.Label(left_pane,text="Form Factor")
                   form.pack(fill = tk.BOTH, expand = True)
                   dimm=tk.Label(left_pane,text="Memory Format (dimm)")
                   dimm.pack(fill = tk.BOTH, expand = True)
                   brand=tk.Label(left_pane,text="brand")
                   brand.pack(fill = tk.BOTH, expand = True)
                   model=tk.Label(left_pane,text="model number")
                   model.pack(fill = tk.BOTH, expand = True)
                   cat=tk.Label(left_pane,text="Memory Capacity (total)")
                   cat.pack(fill = tk.BOTH, expand = True)
                   cap=tk.Label(left_pane,text="Memory Capacity (per Module)")
                   cap.pack(fill = tk.BOTH, expand = True)
                   name=tk.Label(left_pane,text="product name")
                   name.pack(fill = tk.BOTH, expand = True)

                   namev=tk.StringVar()
                   ddrv=tk.StringVar()
                   speedv=tk.StringVar()
                   formv=tk.StringVar()
                   dimmv=tk.StringVar()
                   brandv=tk.StringVar()
                   modelv=tk.StringVar()
                   catv=tk.StringVar()
                   capv=tk.StringVar()

                   ddre=tk.Entry(right_pane,textvariable=ddrv)
                   ddre.pack(fill = tk.BOTH, expand = True)
                   speede=tk.Entry(right_pane,textvariable=speedv)
                   speede.pack(fill = tk.BOTH, expand = True)
                   forme=tk.Entry(right_pane,textvariable=formv)
                   forme.pack(fill = tk.BOTH, expand = True)
                   dimme=tk.Entry(right_pane,textvariable=dimmv)
                   dimme.pack(fill = tk.BOTH, expand = True)
                   brande=tk.Entry(right_pane,textvariable=brandv)
                   brande.pack(fill = tk.BOTH, expand = True)
                   modele=tk.Entry(right_pane,textvariable=modelv)
                   modele.pack(fill = tk.BOTH, expand = True)
                   cate=tk.Entry(right_pane,textvariable=catv)
                   cate.pack(fill = tk.BOTH, expand = True)
                   cape=tk.Entry(right_pane,textvariable=capv)
                   cape.pack(fill = tk.BOTH, expand = True)
                   namee=tk.Entry(right_pane,textvariable=namev)
                   namee.pack(fill = tk.BOTH, expand = True)
               if inp == "gpu":
                   sub_btn.destroy()
                   co.destroy()

                   def submit():
                       gm=namev.get()
                       gs=sizev.get()
                       gcl=cclockv.get()
                       gbr=brandv.get()
                       gbb=bbrandv.get()
                       gcu=cudav.get()
                       gmc=mclockv.get()
                       gmt=mtypev.get()
                       gcb=cbusv.get()
                       gh=hieghtv.get()
                       gw=widthv.get()
                       gl=lengthv.get()
                       go=outputv.get()
                       gp=powerv.get()
                       gwa=wattv.get()
                       gmo=modelv.get()
                       d={}
                       d['name']=gm
                       d['size']=gs
                       d['core_clock']=gcl
                       d['brand']=gbr
                       d['model']=gmo
                       d['mem_type']=gmt
                       d['output']=go
                       d['base_brand']=gbb
                       d['cuda']=gcu
                       d['mem_clock']=gmc
                       d['card_bus']=gcb
                       d['hieght']=gh
                       d['width']=gw
                       d['length']=gl
                       d['power']=gp
                       d['watt']=gwa
                       def write_json(new_data, filename=jsof):
                        with open(filename,'r+') as file:
                            file_data = json.load(file)
                            file_data["gpu"].append(new_data)
                            file.seek(0)
                # First we load existing data into a dict.
        # Join new_data with file_data inside emp_details
        # Sets file's current position at offset.
        # convert back to json.
                            json.dump(file_data, file, indent = 4)
                       write_json(d)
                       newWindow.destroy()
                   btn=tk.Button(top,text="submit",command=submit)
                   btn.pack()
                   name=tk.Label(left_pane,text="name")
                   name.pack(fill = tk.BOTH, expand = True)
                   size=tk.Label(left_pane,text="Capacity")
                   size.pack(fill = tk.BOTH, expand = True)
                   cclock=tk.Label(left_pane,text="core clock")
                   cclock.pack(fill = tk.BOTH, expand = True)
                   brand=tk.Label(left_pane,text="brand")
                   brand.pack(fill = tk.BOTH, expand = True)
                   bbrand=tk.Label(left_pane,text="base brand (amd)")
                   bbrand.pack(fill = tk.BOTH, expand = True)
                   model=tk.Label(left_pane,text="model number")
                   model.pack(fill = tk.BOTH, expand = True)
                   cuda=tk.Label(left_pane,text="cuda cores")
                   cuda.pack(fill = tk.BOTH, expand = True)
                   mclock=tk.Label(left_pane,text="Memory clock")
                   mclock.pack(fill = tk.BOTH, expand = True)
                   mtype=tk.Label(left_pane,text="Memory type (gddr)")
                   mtype.pack(fill = tk.BOTH, expand = True)
                   cbus=tk.Label(left_pane,text="card bus")
                   cbus.pack(fill = tk.BOTH, expand = True)
                   hieght=tk.Label(left_pane,text="hieght")
                   hieght.pack(fill = tk.BOTH, expand = True)
                   width=tk.Label(left_pane,text="width")
                   width.pack(fill = tk.BOTH, expand = True)
                   length=tk.Label(left_pane,text="length")
                   length.pack(fill = tk.BOTH, expand = True)
                   output=tk.Label(left_pane,text="video outputs")
                   output.pack(fill = tk.BOTH, expand = True)
                   power=tk.Label(left_pane,text="power connectors")
                   power.pack(fill = tk.BOTH, expand = True)
                   watt=tk.Label(left_pane,text="watts")
                   watt.pack(fill = tk.BOTH, expand = True)

                   namev=tk.StringVar()
                   sizev=tk.StringVar()
                   cclockv=tk.StringVar()
                   brandv=tk.StringVar()
                   bbrandv=tk.StringVar()
                   cudav=tk.StringVar()
                   mclockv=tk.StringVar()
                   mtypev=tk.StringVar()
                   cbusv=tk.StringVar()
                   hieghtv=tk.StringVar()
                   widthv=tk.StringVar()
                   modelv=tk.StringVar()
                   lengthv=tk.StringVar()
                   outputv=tk.StringVar()
                   powerv=tk.StringVar()
                   wattv=tk.StringVar()

                   namee=tk.Entry(right_pane,textvariable=namev)
                   namee.pack(fill = tk.BOTH, expand = True)
                   modele=tk.Entry(right_pane,textvariable=modelv)
                   modele.pack(fill = tk.BOTH, expand = True)
                   sizee=tk.Entry(right_pane,textvariable=sizev)
                   sizee.pack(fill = tk.BOTH, expand = True)
                   cclocke=tk.Entry(right_pane,textvariable=cclockv)
                   cclocke.pack(fill = tk.BOTH, expand = True)
                   brande=tk.Entry(right_pane,textvariable=brandv)
                   brande.pack(fill = tk.BOTH, expand = True)
                   bbrande=tk.Entry(right_pane,textvariable=bbrandv)
                   bbrande.pack(fill = tk.BOTH, expand = True)
                   cudae=tk.Entry(right_pane,textvariable=cudav)
                   cudae.pack(fill = tk.BOTH, expand = True)
                   mclocke=tk.Entry(right_pane,textvariable=mclockv)
                   mclocke.pack(fill = tk.BOTH, expand = True)
                   mtypee=tk.Entry(right_pane,textvariable=mtypev)
                   mtypee.pack(fill = tk.BOTH, expand = True)
                   cbuse=tk.Entry(right_pane,textvariable=cbusv)
                   cbuse.pack(fill = tk.BOTH, expand = True)
                   hieghte=tk.Entry(right_pane,textvariable=hieghtv)
                   hieghte.pack(fill = tk.BOTH, expand = True)
                   widthe=tk.Entry(right_pane,textvariable=widthv)
                   widthe.pack(fill = tk.BOTH, expand = True)
                   lengthe=tk.Entry(right_pane,textvariable=lengthv)
                   lengthe.pack(fill = tk.BOTH, expand = True)
                   outpute=tk.Entry(right_pane,textvariable=outputv)
                   outpute.pack(fill = tk.BOTH, expand = True)
                   powere=tk.Entry(right_pane,textvariable=powerv)
                   powere.pack(fill = tk.BOTH, expand = True)
                   watte=tk.Entry(right_pane,textvariable=wattv)
                   watte.pack(fill = tk.BOTH, expand = True)
               if inp == "case":
                   sub_btn.destroy()
                   co.destroy()

                   def submit():
                       cb=brandv.get()
                       cml=modelv.get()
                       cn=namev.get()
                       cs=seriesv.get()
                       cc=ctypev.get()
                       cmo=mothersupv.get()
                       cwi=windowv.get()
                       ct=tdrivev.get()
                       cwd=wdrivev.get()
                       cfp=fportsv.get()
                       cp=pciev.get()
                       cfo=fanv.get()
                       cmgp=mgpuv.get()
                       cmgh=mgpuhv.get()
                       cmp=mpsuv.get()
                       cmu=mcpuv.get()
                       d={}
                       d['name']=cn
                       d['model']=cml
                       d['mobo_supp']=cmo
                       d['case_type']=cc
                       d['3drive_bays']=ct
                       d['2drive_bays']=cwd
                       d['pcie']=cp
                       d['ports']=cfp
                       d['gpu-l']=cmgp
                       d['gpu-h']=cmgh
                       d['brand']=cb
                       d['cpu-h']=cmu
                       d['window']=cwi
                       d['series']=cs
                       d['fan']=cfo
                       d['psu-l']=cmp
                       def write_json(new_data, filename=jsof):
                        with open(filename,'r+') as file:
                            file_data = json.load(file)
                            file_data["case"].append(new_data)
                            file.seek(0)
                # First we load existing data into a dict.
        # Join new_data with file_data inside emp_details
        # Sets file's current position at offset.
        # convert back to json.
                            json.dump(file_data, file, indent = 4)
                       write_json(d)
                       newWindow.destroy()
                   btn=tk.Button(top,text="submit",command=submit)
                   btn.pack()
                   name=tk.Label(left_pane,text="name")
                   name.pack(fill = tk.BOTH, expand = True)
                   brand=tk.Label(left_pane,text="brand")
                   brand.pack(fill = tk.BOTH, expand = True)
                   model=tk.Label(left_pane,text="model")
                   model.pack(fill = tk.BOTH, expand = True)
                   series=tk.Label(left_pane,text="series")
                   series.pack(fill = tk.BOTH, expand = True)
                   ctype=tk.Label(left_pane,text="case type (atx)")
                   ctype.pack(fill = tk.BOTH, expand = True)
                   mothersup=tk.Label(left_pane,text="motherboard size support")
                   mothersup.pack(fill = tk.BOTH, expand = True)
                   window=tk.Label(left_pane,text="side window")
                   window.pack(fill = tk.BOTH, expand = True)
                   tdrive=tk.Label(left_pane,text="3.5 drive bays")
                   tdrive.pack(fill = tk.BOTH, expand = True)
                   wdrive=tk.Label(left_pane,text="2.5 drive bays")
                   wdrive.pack(fill = tk.BOTH, expand = True)
                   fports=tk.Label(left_pane,text="front ports")
                   fports.pack(fill = tk.BOTH, expand = True)
                   pcie=tk.Label(left_pane,text="pcie slots")
                   pcie.pack(fill = tk.BOTH, expand = True)
                   fan=tk.Label(left_pane,text="fans")
                   fan.pack(fill = tk.BOTH, expand = True)
                   mgpu=tk.Label(left_pane,text="max gpu length")
                   mgpu.pack(fill = tk.BOTH, expand = True)
                   mgpuh=tk.Label(left_pane,text="max gpu hieght")
                   mgpuh.pack(fill = tk.BOTH, expand = True)
                   mpsu=tk.Label(left_pane,text="max psu length")
                   mpsu.pack(fill = tk.BOTH, expand = True)
                   mcpu=tk.Label(left_pane,text="max cpu hieght")
                   mcpu.pack(fill = tk.BOTH, expand = True)

                   namev=tk.StringVar()
                   brandv=tk.StringVar()
                   modelv=tk.StringVar()
                   seriesv=tk.StringVar()
                   ctypev=tk.StringVar()
                   mothersupv=tk.StringVar()
                   windowv=tk.StringVar()
                   tdrivev=tk.StringVar()
                   wdrivev=tk.StringVar()
                   fportsv=tk.StringVar()
                   pciev=tk.StringVar()
                   fanv=tk.StringVar()
                   mgpuv=tk.StringVar()
                   mgpuhv=tk.StringVar()
                   mpsuv=tk.StringVar()
                   mcpuv=tk.StringVar()

                   namee=tk.Entry(right_pane,textvariable=namev)
                   namee.pack(fill = tk.BOTH, expand = True)
                   brande=tk.Entry(right_pane,textvariable=brandv)
                   brande.pack(fill = tk.BOTH, expand = True)
                   modele=tk.Entry(right_pane,textvariable=modelv)
                   modele.pack(fill = tk.BOTH, expand = True)
                   seriese=tk.Entry(right_pane,textvariable=seriesv)
                   seriese.pack(fill = tk.BOTH, expand = True)
                   ctypee=tk.Entry(right_pane,textvariable=ctypev)
                   ctypee.pack(fill = tk.BOTH, expand = True)
                   mothersupe=tk.Entry(right_pane,textvariable=mothersupv)
                   mothersupe.pack(fill = tk.BOTH, expand = True)
                   windowe=tk.Entry(right_pane,textvariable=windowv)
                   windowe.pack(fill = tk.BOTH, expand = True)
                   tdrivee=tk.Entry(right_pane,textvariable=tdrivev)
                   tdrivee.pack(fill = tk.BOTH, expand = True)
                   wdrivee=tk.Entry(right_pane,textvariable=wdrivev)
                   wdrivee.pack(fill = tk.BOTH, expand = True)
                   fportse=tk.Entry(right_pane,textvariable=fportsv)
                   fportse.pack(fill = tk.BOTH, expand = True)
                   pciee=tk.Entry(right_pane,textvariable=pciev)
                   pciee.pack(fill = tk.BOTH, expand = True)
                   fane=tk.Entry(right_pane,textvariable=fanv)
                   fane.pack(fill = tk.BOTH, expand = True)
                   mgpue=tk.Entry(right_pane,textvariable=mgpuv)
                   mgpue.pack(fill = tk.BOTH, expand = True)
                   mgpuhe=tk.Entry(right_pane,textvariable=mgpuhv)
                   mgpuhe.pack(fill = tk.BOTH, expand = True)
                   mpsue=tk.Entry(right_pane,textvariable=mpsuv)
                   mpsue.pack(fill = tk.BOTH, expand = True)
                   mcpue=tk.Entry(right_pane,textvariable=mcpuv)
                   mcpue.pack(fill = tk.BOTH, expand = True)
               if inp == "storage":
                   sub_btn.destroy()
                   co.destroy()

                   def submit():
                       sn=namev.get()
                       sb=brandv.get()
                       sm=modelv.get()
                       ss=sizev.get()
                       sd=dtypev.get()
                       sf=formv.get()
                       sr=rpmv.get()
                       sw=writev.get()
                       sif=interfacev.get()
                       sin=internalv.get()
                       sre=readv.get()
                       d={}
                       d['name']=sn
                       d['brand']=sb
                       d['size']=ss
                       d['type']=sd
                       d['form']=sf
                       d['interface']=sif
                       d['internal']=sin
                       d['model']=sm
                       d['rpm']=sr
                       d['read']=sre
                       d['write']=sw

                       def write_json(new_data, filename=jsof):
                        with open(filename,'r+') as file:
                            file_data = json.load(file)
                            file_data["storage"].append(new_data)
                            file.seek(0)
                # First we load existing data into a dict.
        # Join new_data with file_data inside emp_details
        # Sets file's current position at offset.
        # convert back to json.
                            json.dump(file_data, file, indent = 4)
                       write_json(d)
                       newWindow.destroy()
                   btn=tk.Button(top,text="submit",command=submit)
                   btn.pack()

                   # labal
                   name=tk.Label(left_pane,text="product name")
                   name.pack(fill = tk.BOTH, expand = True)
                   brand=tk.Label(left_pane,text="brand")
                   brand.pack(fill = tk.BOTH, expand = True)
                   model=tk.Label(left_pane,text="model number")
                   model.pack(fill = tk.BOTH, expand = True)
                   size=tk.Label(left_pane,text="drive space")
                   size.pack(fill = tk.BOTH, expand = True)
                   dtype=tk.Label(left_pane,text="disk type")
                   dtype.pack(fill = tk.BOTH, expand = True)
                   form=tk.Label(left_pane,text="form factor")
                   form.pack(fill = tk.BOTH, expand = True)
                   rpm=tk.Label(left_pane,text="rpm")
                   rpm.pack(fill = tk.BOTH, expand = True)
                   read=tk.Label(left_pane,text="read speed")
                   read.pack(fill = tk.BOTH, expand = True)
                   write=tk.Label(left_pane,text="write speed")
                   write.pack(fill = tk.BOTH, expand = True)
                   interface=tk.Label(left_pane,text="interface")
                   interface.pack(fill = tk.BOTH, expand = True)
                   internal=tk.Label(left_pane,text="internal")
                   internal.pack(fill = tk.BOTH, expand = True)

                   namev=tk.StringVar()
                   brandv=tk.StringVar()
                   modelv=tk.StringVar()
                   sizev=tk.StringVar()
                   dtypev=tk.StringVar()
                   formv=tk.StringVar()
                   rpmv=tk.StringVar()
                   readv=tk.StringVar()
                   writev=tk.StringVar()
                   interfacev=tk.StringVar()
                   internalv=tk.StringVar()

                   namee=tk.Entry(right_pane,textvariable=namev)
                   namee.pack(fill = tk.BOTH, expand = True)
                   brande=tk.Entry(right_pane,textvariable=brandv)
                   brande.pack(fill = tk.BOTH, expand = True)
                   modele=tk.Entry(right_pane,textvariable=modelv)
                   modele.pack(fill = tk.BOTH, expand = True)
                   sizee=tk.Entry(right_pane,textvariable=sizev)
                   sizee.pack(fill = tk.BOTH, expand = True)
                   dtypee=tk.Entry(right_pane,textvariable=dtypev)
                   dtypee.pack(fill = tk.BOTH, expand = True)
                   forme=tk.Entry(right_pane,textvariable=formv)
                   forme.pack(fill = tk.BOTH, expand = True)
                   rpme=tk.Entry(right_pane,textvariable=rpmv)
                   rpme.pack(fill = tk.BOTH, expand = True)
                   reade=tk.Entry(right_pane,textvariable=readv)
                   reade.pack(fill = tk.BOTH, expand = True)
                   writee=tk.Entry(right_pane,textvariable=writev)
                   writee.pack(fill = tk.BOTH, expand = True)
                   interfacee=tk.Entry(right_pane,textvariable=interfacev)
                   interfacee.pack(fill = tk.BOTH, expand = True)
                   internale=tk.Entry(right_pane,textvariable=internalv)
                   internale.pack(fill = tk.BOTH, expand = True)

               if inp == "cpu_cooler":
                   sub_btn.destroy()
                   co.destroy()


                   def submit():
                       cb=brandv.get()
                       cn=namev.get()
                       cm=modelv.get()
                       cf=fansizev.get()
                       cr=rpmv.get()
                       co=colorv.get()
                       cp=cpu_coolerv.get()
                       cv=mcpuhv.get()
                       data='{"name":"' + cn + '","brand":"' + cb + '","model":"' + cm + '","max_cpu_height":"' + cv + '","rpm":"' + cr + '","fansize":"' + cf + '","fan_mount":"' + cp + '","color":"' + co + '"}'
                       print(data)
                       newWindow.destroy()


                   btn=tk.Button(top,text="submit",command=submit)
                   btn.pack()

                   brand=tk.Label(left_pane,text="brand")
                   brand.pack(fill = tk.BOTH, expand = True)
                   name=tk.Label(left_pane,text="name")
                   name.pack(fill = tk.BOTH, expand = True)
                   model=tk.Label(left_pane,text="model")
                   model.pack(fill = tk.BOTH, expand = True)
                   fansize=tk.Label(left_pane,text="fansize")
                   fansize.pack(fill = tk.BOTH, expand = True)
                   rpm=tk.Label(left_pane,text="rpm")
                   rpm.pack(fill = tk.BOTH, expand = True)
                   color=tk.Label(left_pane,text="color")
                   color.pack(fill = tk.BOTH, expand = True)
                   cpu_cooler=tk.Label(left_pane,text="fan mounting")
                   cpu_cooler.pack(fill = tk.BOTH, expand = True)
                   mcpuh=tk.Label(left_pane,text="max cpu height")
                   mcpuh.pack(fill = tk.BOTH, expand = True)


                   brandv=tk.StringVar()
                   namev=tk.StringVar()
                   modelv=tk.StringVar()
                   fansizev=tk.StringVar()
                   rpmv=tk.StringVar()
                   colorv=tk.StringVar()
                   cpu_coolerv=tk.StringVar()
                   mcpuhv=tk.StringVar()


                   brande=tk.Entry(right_pane,textvariable=brandv)
                   brande.pack(fill = tk.BOTH, expand = True)
                   namee=tk.Entry(right_pane,textvariable=namev)
                   namee.pack(fill = tk.BOTH, expand = True)
                   modele=tk.Entry(right_pane,textvariable=modelv)
                   modele.pack(fill = tk.BOTH, expand = True)
                   fansizee=tk.Entry(right_pane,textvariable=fansizev)
                   fansizee.pack(fill = tk.BOTH, expand = True)
                   rpme=tk.Entry(right_pane,textvariable=rpmv)
                   rpme.pack(fill = tk.BOTH, expand = True)
                   colore=tk.Entry(right_pane,textvariable=colorv)
                   colore.pack(fill = tk.BOTH, expand = True)
                   cpu_coolere=tk.Entry(right_pane,textvariable=cpu_coolerv)
                   cpu_coolere.pack(fill = tk.BOTH, expand = True)
                   mcpuhe=tk.Entry(right_pane,textvariable=mcpuhv)
                   mcpuhe.pack(fill = tk.BOTH, expand = True)
               if inp == "motherboard":
                   sub_btn.destroy()
                   co.destroy()


                   def submit():
                       mna=namev.get()
                       mch=chipsetv.get()
                       mr=ramslotsv.get()
                       mm=maxramv.get()
                       me=eccramv.get()
                       mcp=cpusocketv.get()
                       mcps=cpuseriesv.get()
                       mgr=graphicsv.get()
                       mpg=pciegenv.get()
                       mps=pcie16v.get()
                       mse=seriesv.get()
                       mv=vrmv.get()
                       mis=ioshieldv.get()
                       mia=iaudiov.get()
                       mpv=pciev.get()
                       mav=nvmeav.get()
                       msa=satav.get()
                       msp=sataspeedv.get()
                       mnv=nvme_pciev.get()
                       me=ethernetv.get()
                       mbr=brandv.get()
                       mmd=modelv.get()
                       mw=wifiv.get()
                       mbl=bluetoothv.get()
                       muc=usbcv.get()
                       muv=usbv.get()
                       mpo=portsv.get()
                       mmo=motherboardportsv.get()
                       mf=formfactorv.get()
                       md=ddrv.get()
                       mso=sodimmv.get()
                       data='{"name":"' + mna + '","model":"' + mmd + '","cpu_socket":"' + mcp + '","chipset":"' + mch + '","sata":"' + msa + '","ddr":"' + md + '","usbc":"' + muc + '","usb":"' + muv + '","ports":"' + mpo + '","form_factor":"' + mf + '","brand":"' + mbr + '","max_ram":"' + mm + '","series":"' + mse + '","motherboard_ports":"' + mmo + '","sodimm":"' + mso + '","pcie16":"' + mps + '","ram_slots":"' + mr + '","nvme":"' + mav + '","pcie_gen":"' + mpg + '","ethernet":"' + me + '","nvme_pcie":"' + mnv + '","wifi":"' + mw + '","bluetooth":"' + mbl + '","sata_speed":"' + msp + '","vrm":"' + mv + '","cpu_series":"' + mcps + '","graphics":"' + mgr + '","iaudio":"' + mia + '","pcie":"' + mpv + '","ioshield":"' + mis + '"}'
                       print(data)
                       newWindow.destroy()


                   btn=tk.Button(top,text="submit",command=submit)
                   btn.pack()

                   name=tk.Label(left_pane,text="name")
                   name.pack(fill = tk.BOTH, expand = True)
                   chipset=tk.Label(left_pane,text="cpu chipset")
                   chipset.pack(fill = tk.BOTH, expand = True)
                   ramslots=tk.Label(left_pane,text="ram slots")
                   ramslots.pack(fill = tk.BOTH, expand = True)
                   maxram=tk.Label(left_pane,text="max ram support")
                   maxram.pack(fill = tk.BOTH, expand = True)
                   eccram=tk.Label(left_pane,text="ecc ram support")
                   eccram.pack(fill = tk.BOTH, expand = True)
                   cpusocket=tk.Label(left_pane,text="cpu socket")
                   cpusocket.pack(fill = tk.BOTH, expand = True)
                   cpuseries=tk.Label(left_pane,text="cpu series")
                   cpuseries.pack(fill = tk.BOTH, expand = True)
                   series=tk.Label(left_pane,text="motherboard series")
                   series.pack(fill = tk.BOTH, expand = True)
                   vrm=tk.Label(left_pane,text="vrm")
                   vrm.pack(fill = tk.BOTH, expand = True)
                   ioshield=tk.Label(left_pane,text="io shield")
                   ioshield.pack(fill = tk.BOTH, expand = True)
                   iaudio=tk.Label(left_pane,text="intergrated audio")
                   iaudio.pack(fill = tk.BOTH, expand = True)
                   graphics=tk.Label(left_pane,text="graphics ports")
                   graphics.pack(fill = tk.BOTH, expand = True)
                   pciegen=tk.Label(left_pane,text="pcie gen")
                   pciegen.pack(fill = tk.BOTH, expand = True)
                   pcie16=tk.Label(left_pane,text="pcie 16x slots")
                   pcie16.pack(fill = tk.BOTH, expand = True)
                   pcie=tk.Label(left_pane,text="pcie 4 slots")
                   pcie.pack(fill = tk.BOTH, expand = True)
                   nvmea=tk.Label(left_pane,text="nvme slots")
                   nvmea.pack(fill = tk.BOTH, expand = True)
                   sata=tk.Label(left_pane,text="sata ports")
                   sata.pack(fill = tk.BOTH, expand = True)
                   sataspeed=tk.Label(left_pane,text="sata speed")
                   sataspeed.pack(fill = tk.BOTH, expand = True)
                   nvme_pcie=tk.Label(left_pane,text="nvme pcie gen")
                   nvme_pcie.pack(fill = tk.BOTH, expand = True)
                   ethernet=tk.Label(left_pane,text="ethernet speed")
                   ethernet.pack(fill = tk.BOTH, expand = True)
                   brand=tk.Label(left_pane,text="brand")
                   brand.pack(fill = tk.BOTH, expand = True)
                   model=tk.Label(left_pane,text="model")
                   model.pack(fill = tk.BOTH, expand = True)
                   wifi=tk.Label(left_pane,text="wifi type")
                   wifi.pack(fill = tk.BOTH, expand = True)
                   bluetooth=tk.Label(left_pane,text="bluetooth")
                   bluetooth.pack(fill = tk.BOTH, expand = True)
                   usbc=tk.Label(left_pane,text="usbc ports")
                   usbc.pack(fill = tk.BOTH, expand = True)
                   usb=tk.Label(left_pane,text="usb ports")
                   usb.pack(fill = tk.BOTH, expand = True)
                   ports=tk.Label(left_pane,text="ports")
                   ports.pack(fill = tk.BOTH, expand = True)
                   motherboardports=tk.Label(left_pane,text="motherboard ports")
                   motherboardports.pack(fill = tk.BOTH, expand = True)
                   formfactor=tk.Label(left_pane,text="form factor")
                   formfactor.pack(fill = tk.BOTH, expand = True)
                   ddr=tk.Label(left_pane,text="ddr gen")
                   ddr.pack(fill = tk.BOTH, expand = True)
                   sodimm=tk.Label(left_pane,text="sodimm ram")
                   sodimm.pack(fill = tk.BOTH, expand = True)



                   namev=tk.StringVar()
                   chipsetv=tk.StringVar()
                   ramslotsv=tk.StringVar()
                   maxramv=tk.StringVar()
                   eccramv=tk.StringVar()
                   cpusocketv=tk.StringVar()
                   cpuseriesv=tk.StringVar()
                   graphicsv=tk.StringVar()
                   pciegenv=tk.StringVar()
                   pcie16v=tk.StringVar()
                   seriesv=tk.StringVar()
                   vrmv=tk.StringVar()
                   ioshieldv=tk.StringVar()
                   iaudiov=tk.StringVar()
                   pciev=tk.StringVar()
                   nvmeav=tk.StringVar()
                   satav=tk.StringVar()
                   sataspeedv=tk.StringVar()
                   nvme_pciev=tk.StringVar()
                   ethernetv=tk.StringVar()
                   brandv=tk.StringVar()
                   modelv=tk.StringVar()
                   wifiv=tk.StringVar()
                   bluetoothv=tk.StringVar()
                   usbcv=tk.StringVar()
                   usbv=tk.StringVar()
                   portsv=tk.StringVar()
                   motherboardportsv=tk.StringVar()
                   formfactorv=tk.StringVar()
                   ddrv=tk.StringVar()
                   sodimmv=tk.StringVar()


                   namee=tk.Entry(right_pane,textvariable=namev)
                   namee.pack(fill = tk.BOTH, expand = True)
                   chipsete=tk.Entry(right_pane,textvariable=chipsetv)
                   chipsete.pack(fill = tk.BOTH, expand = True)
                   ramslotse=tk.Entry(right_pane,textvariable=ramslotsv)
                   ramslotse.pack(fill = tk.BOTH, expand = True)
                   maxrame=tk.Entry(right_pane,textvariable=maxramv)
                   maxrame.pack(fill = tk.BOTH, expand = True)
                   eccrame=tk.Entry(right_pane,textvariable=eccramv)
                   eccrame.pack(fill = tk.BOTH, expand = True)
                   cpusockete=tk.Entry(right_pane,textvariable=cpusocketv)
                   cpusockete.pack(fill = tk.BOTH, expand = True)
                   cpuseriese=tk.Entry(right_pane,textvariable=cpuseriesv)
                   cpuseriese.pack(fill = tk.BOTH, expand = True)
                   graphicse=tk.Entry(right_pane,textvariable=graphicsv)
                   graphicse.pack(fill = tk.BOTH, expand = True)
                   pciegene=tk.Entry(right_pane,textvariable=pciegenv)
                   pciegene.pack(fill = tk.BOTH, expand = True)
                   pcie16e=tk.Entry(right_pane,textvariable=pcie16v)
                   pcie16e.pack(fill = tk.BOTH, expand = True)
                   pciee=tk.Entry(right_pane,textvariable=pciev)
                   pciee.pack(fill = tk.BOTH, expand = True)
                   nvmeae=tk.Entry(right_pane,textvariable=nvmeav)
                   nvmeae.pack(fill = tk.BOTH, expand = True)
                   seriese=tk.Entry(right_pane,textvariable=seriesv)
                   seriese.pack(fill = tk.BOTH, expand = True)
                   vrme=tk.Entry(right_pane,textvariable=vrmv)
                   vrme.pack(fill = tk.BOTH, expand = True)
                   ioshielde=tk.Entry(right_pane,textvariable=ioshieldv)
                   ioshielde.pack(fill = tk.BOTH, expand = True)
                   iaudioe=tk.Entry(right_pane,textvariable=iaudiov)
                   iaudioe.pack(fill = tk.BOTH, expand = True)
                   satae=tk.Entry(right_pane,textvariable=satav)
                   satae.pack(fill = tk.BOTH, expand = True)
                   sataspeede=tk.Entry(right_pane,textvariable=sataspeedv)
                   sataspeede.pack(fill = tk.BOTH, expand = True)
                   nvme_pciee=tk.Entry(right_pane,textvariable=nvme_pciev)
                   nvme_pciee.pack(fill = tk.BOTH, expand = True)
                   ethernete=tk.Entry(right_pane,textvariable=ethernetv)
                   ethernete.pack(fill = tk.BOTH, expand = True)
                   brande=tk.Entry(right_pane,textvariable=brandv)
                   brande.pack(fill = tk.BOTH, expand = True)
                   modele=tk.Entry(right_pane,textvariable=modelv)
                   modele.pack(fill = tk.BOTH, expand = True)
                   wifie=tk.Entry(right_pane,textvariable=wifiv)
                   wifie.pack(fill = tk.BOTH, expand = True)
                   bluetoothe=tk.Entry(right_pane,textvariable=bluetoothv)
                   bluetoothe.pack(fill = tk.BOTH, expand = True)
                   usbce=tk.Entry(right_pane,textvariable=usbcv)
                   usbce.pack(fill = tk.BOTH, expand = True)
                   usbe=tk.Entry(right_pane,textvariable=usbv)
                   usbe.pack(fill = tk.BOTH, expand = True)
                   portse=tk.Entry(right_pane,textvariable=portsv)
                   portse.pack(fill = tk.BOTH, expand = True)
                   motherboardportse=tk.Entry(right_pane,textvariable=motherboardportsv)
                   motherboardportse.pack(fill = tk.BOTH, expand = True)
                   formfactore=tk.Entry(right_pane,textvariable=formfactorv)
                   formfactore.pack(fill = tk.BOTH, expand = True)
                   ddre=tk.Entry(right_pane,textvariable=ddrv)
                   ddre.pack(fill = tk.BOTH, expand = True)
                   sodimme=tk.Entry(right_pane,textvariable=sodimmv)
                   sodimme.pack(fill = tk.BOTH, expand = True)
               if inp == "psu":
                   sub_btn.destroy()
                   co.destroy()


                   def submit():
                       pb=brandv.get()
                       pn=namev.get()
                       pmo=modularv.get()
                       pt=typeav.get()
                       pma=maxpowerv.get()
                       mo=modelv.get()
                       pe=efficietv.get()
                       pmp=mpsulv.get()
                       pc=connectersv.get()
                       d={}
                       d['name']=pn
                       d['watt']=pma
                       d['rating']=pe
                       d['brand']=pb
                       d['model']=mo
                       d['modular']=pmo
                       d['type']=pt
                       d['connectors']=pc
                       d['max_psu_l']=pmp

                       def write_json(new_data, filename=jsof):
                        with open(filename,'r+') as file:
                            file_data = json.load(file)
                            file_data["psu"].append(new_data)
                            file.seek(0)
                # First we load existing data into a dict.
        # Join new_data with file_data inside emp_details
        # Sets file's current position at offset.
        # convert back to json.
                            json.dump(file_data, file, indent = 4)
                       write_json(d)
                       newWindow.destroy()


                   btn=tk.Button(top,text="submit",command=submit)
                   btn.pack()

                   brand=tk.Label(left_pane,text="brand")
                   brand.pack(fill = tk.BOTH, expand = True)
                   name=tk.Label(left_pane,text="name")
                   name.pack(fill = tk.BOTH, expand = True)
                   model=tk.Label(left_pane,text="model")
                   model.pack(fill = tk.BOTH, expand = True)
                   typea=tk.Label(left_pane,text="type (atx)")
                   typea.pack(fill = tk.BOTH, expand = True)
                   maxpower=tk.Label(left_pane,text="max power")
                   maxpower.pack(fill = tk.BOTH, expand = True)
                   modular=tk.Label(left_pane,text="moduar")
                   modular.pack(fill = tk.BOTH, expand = True)
                   efficiet=tk.Label(left_pane,text="Energy-Efficient")
                   efficiet.pack(fill = tk.BOTH, expand = True)
                   mpsul=tk.Label(left_pane,text="max psu length")
                   mpsul.pack(fill = tk.BOTH, expand = True)
                   connecters=tk.Label(left_pane,text="connecters")
                   connecters.pack(fill = tk.BOTH, expand = True)

                   brandv=tk.StringVar()
                   namev=tk.StringVar()
                   modelv=tk.StringVar()
                   typeav=tk.StringVar()
                   maxpowerv=tk.StringVar()
                   modularv=tk.StringVar()
                   efficietv=tk.StringVar()
                   mpsulv=tk.StringVar()
                   connectersv=tk.StringVar()

                   brande=tk.Entry(right_pane,textvariable=brandv)
                   brande.pack(fill = tk.BOTH, expand = True)
                   namee=tk.Entry(right_pane,textvariable=namev)
                   namee.pack(fill = tk.BOTH, expand = True)
                   modele=tk.Entry(right_pane,textvariable=modelv)
                   modele.pack(fill = tk.BOTH, expand = True)
                   typeae=tk.Entry(right_pane,textvariable=typeav)
                   typeae.pack(fill = tk.BOTH, expand = True)
                   maxpowere=tk.Entry(right_pane,textvariable=maxpowerv)
                   maxpowere.pack(fill = tk.BOTH, expand = True)
                   modulare=tk.Entry(right_pane,textvariable=modularv)
                   modulare.pack(fill = tk.BOTH, expand = True)
                   efficiete=tk.Entry(right_pane,textvariable=efficietv)
                   efficiete.pack(fill = tk.BOTH, expand = True)
                   mpsule=tk.Entry(right_pane,textvariable=mpsulv)
                   mpsule.pack(fill = tk.BOTH, expand = True)
                   connecterse=tk.Entry(right_pane,textvariable=connectersv)
                   connecterse.pack(fill = tk.BOTH, expand = True)
               if inp == "cpu":
                   sub_btn.destroy()
                   co.destroy()


                   def submit():
                       pv=corev.get()
                       pt=threadv.get()
                       pbt=basetv.get()
                       pbf=basefv.get()
                       pu=unlockv.get()
                       ps=socketv.get()
                       pa=cachev.get()
                       pi=igpuv.get()
                       pn=namev.get()
                       pbv=brandv.get()
                       pm=modelv.get()
                       py=yearv.get()
                       d={}
                       d['name']=pn
                       d['core']=pv
                       d['thread']=pt
                       d['socket']=ps
                       d['model']=pm
                       d['base_freq']=pbf
                       d['turbo-freq']=pbt
                       d['igpu']=pi
                       d['brand']=pbv
                       d['cache']=pa
                       d['unlocked']=pu
                       d['year']=py
                       def write_json(new_data, filename=jsof):
                        with open(filename,'r+') as file:
                            file_data = json.load(file)
                            file_data["cpu"].append(new_data)
                            file.seek(0)
                # First we load existing data into a dict.
        # Join new_data with file_data inside emp_details
        # Sets file's current position at offset.
        # convert back to json.
                            json.dump(file_data, file, indent = 4)
                       write_json(d)
                       newWindow.destroy()


                   btn=tk.Button(top,text="submit",command=submit)
                   btn.pack()
                   # label
                   core=tk.Label(left_pane,text="cpu cores")
                   core.pack(fill = tk.BOTH, expand = True)
                   thread=tk.Label(left_pane,text="threads")
                   thread.pack(fill = tk.BOTH, expand = True)
                   basef=tk.Label(left_pane,text="Processor Base Frequency")
                   basef.pack(fill = tk.BOTH, expand = True)
                   baset=tk.Label(left_pane,text="Processor Turbo Frequency")
                   baset.pack(fill = tk.BOTH, expand = True)
                   unlock=tk.Label(left_pane,text="Unlocked cpu")
                   unlock.pack(fill = tk.BOTH, expand = True)
                   socket=tk.Label(left_pane,text="cpu socket")
                   socket.pack(fill = tk.BOTH, expand = True)
                   cache=tk.Label(left_pane,text="l3 cache")
                   cache.pack(fill = tk.BOTH, expand = True)
                   igpu=tk.Label(left_pane,text="intergrated graphics")
                   igpu.pack(fill = tk.BOTH, expand = True)
                   name=tk.Label(left_pane,text="product name")
                   name.pack(fill = tk.BOTH, expand = True)
                   brand=tk.Label(left_pane,text="brand")
                   brand.pack(fill = tk.BOTH, expand = True)
                   model=tk.Label(left_pane,text="model number")
                   model.pack(fill = tk.BOTH, expand = True)
                   year=tk.Label(left_pane,text="year of launch")
                   year.pack(fill = tk.BOTH, expand = True)

                   corev=tk.StringVar()
                   threadv=tk.StringVar()
                   basetv=tk.StringVar()
                   basefv=tk.StringVar()
                   unlockv=tk.StringVar()
                   socketv=tk.StringVar()
                   cachev=tk.StringVar()
                   igpuv=tk.StringVar()
                   namev=tk.StringVar()
                   brandv=tk.StringVar()
                   modelv=tk.StringVar()
                   yearv=tk.StringVar()

                   coree=tk.Entry(right_pane,textvariable=corev)
                   coree.pack(fill = tk.BOTH, expand = True)
                   threade=tk.Entry(right_pane,textvariable=threadv)
                   threade.pack(fill = tk.BOTH, expand = True)
                   basete=tk.Entry(right_pane,textvariable=basetv)
                   basete.pack(fill = tk.BOTH, expand = True)
                   basefe=tk.Entry(right_pane,textvariable=basefv)
                   basefe.pack(fill = tk.BOTH, expand = True)
                   unlocke=tk.Entry(right_pane,textvariable=unlockv)
                   unlocke.pack(fill = tk.BOTH, expand = True)
                   sockete=tk.Entry(right_pane,textvariable=socketv)
                   sockete.pack(fill = tk.BOTH, expand = True)
                   cachee=tk.Entry(right_pane,textvariable=cachev)
                   cachee.pack(fill = tk.BOTH, expand = True)
                   igpue=tk.Entry(right_pane,textvariable=igpuv)
                   igpue.pack(fill = tk.BOTH, expand = True)
                   namee=tk.Entry(right_pane,textvariable=namev)
                   namee.pack(fill = tk.BOTH, expand = True)
                   brande=tk.Entry(right_pane,textvariable=brandv)
                   brande.pack(fill = tk.BOTH, expand = True)
                   modele=tk.Entry(right_pane,textvariable=modelv)
                   modele.pack(fill = tk.BOTH, expand = True)
                   yeare=tk.Entry(right_pane,textvariable=yearv)
                   yeare.pack(fill = tk.BOTH, expand = True)

           sub_btn=tk.Button(top,text="submit",command=choose1)
           sub_btn.pack()


           pi=tk.StringVar()
           pi.set("choose one")

           co= tk.OptionMenu(right_pane,pi,"ram","gpu","case","cpu","storage","psu","motherboard","cpu_cooler")
           co.pack()

       elif selection == "monitors":
           print(selection)
           drop.pack_forget()
           top = tk.Frame(newWindow, background="black", height=40)
           main = tk.PanedWindow(newWindow, background="black")

           top.pack(side="top", fill="x")
           main.pack(side="top", fill="both", expand=True)
           left_pane = tk.Frame(main, background="black", width=300)
           right_pane = tk.PanedWindow(main, background="black", width=300)
           main.add(left_pane)
           main.add(right_pane)
           left = tk.Label(top,text="networking")
           left.pack()

           def submit():
               mb=brandv.get()
               mmo=modelv.get()
               mss=ssizev.get()
               mw=widescreenv.get()
               mg=glaresv.get()
               ml=ledv.get()
               mp=panelv.get()
               md=displaytv.get()
               ma=astv.get()
               mma=maxresv.get()
               mre=aspectratv.get()
               mcr=constrast_ratiov.get()
               mrt=resp_timev.get()
               mrv=refresh_ratev.get()
               mi=ivcv.get()
               mco=connectersv.get()
               mvi=videov.get()
               mu=usbv.get()
               mve=vesav.get()
               n={}
               n['brand']= mb
               n['model']=mmo
               n['screen_size']=mss
               n['connecters']=mco
               n['video']=mvi
               n['usb']=mu
               n['vesa']=mve
               n['resolution']=mma
               n['refresh_rate']=mrv
               n['widescreen']=mw
               n['glare_screen']=mg
               n['panel']=mp
               n['led_backlight']=ml
               n['display_type']=md
               n['constrast_ratio']=mcr
               n['aspect_ratio']=mre
               n['response_time']=mrt
               n['adaptive_sync_tech']=ma
               n['input_video']=mi
               print(json.dumps(n))
               def write_json(new_data, filename=jsof):
                 with open(filename,'r+') as file:
                # First we load existing data into a dict.
                    file_data = json.load(file)
        # Join new_data with file_data inside emp_details
                    file_data["monitor"].append(new_data)
        # Sets file's current position at offset.
                    file.seek(0)
        # convert back to json.
                    json.dump(file_data, file, indent = 4)
               write_json(n)
               newWindow.destroy()
           sub_btn=tk.Button(top,text="submit",command=submit)
           sub_btn.pack()

           brand=tk.Label(left_pane,text="brand")
           brand.pack(fill = tk.BOTH, expand = True)
           model=tk.Label(left_pane,text="model")
           model.pack(fill = tk.BOTH, expand = True)
           ssize=tk.Label(left_pane,text="screen size")
           ssize.pack(fill = tk.BOTH, expand = True)
           widescreen=tk.Label(left_pane,text="widescreen")
           widescreen.pack(fill = tk.BOTH, expand = True)
           glares=tk.Label(left_pane,text="glare screen")
           glares.pack(fill = tk.BOTH, expand = True)
           led=tk.Label(left_pane,text="led backlight")
           led.pack(fill = tk.BOTH, expand = True)
           panel=tk.Label(left_pane,text="panel")
           panel.pack(fill = tk.BOTH, expand = True)
           displayt=tk.Label(left_pane,text="display type")
           displayt.pack(fill = tk.BOTH, expand = True)
           ast=tk.Label(left_pane,text="adaptive sync tech")
           ast.pack(fill = tk.BOTH, expand = True)
           maxres=tk.Label(left_pane,text="Resolution")
           maxres.pack(fill = tk.BOTH, expand = True)
           aspectrat=tk.Label(left_pane,text="aspect ratio")
           aspectrat.pack(fill = tk.BOTH, expand = True)
           constrast_ratio=tk.Label(left_pane,text="constrast ratio")
           constrast_ratio.pack(fill = tk.BOTH, expand = True)
           resp_time=tk.Label(left_pane,text="response time")
           resp_time.pack(fill = tk.BOTH, expand = True)
           refresh_rate=tk.Label(left_pane,text="refresh rate")
           refresh_rate.pack(fill = tk.BOTH, expand = True)
           ivc=tk.Label(left_pane,text="input video compatiblitty")
           ivc.pack(fill = tk.BOTH, expand = True)
           connecters=tk.Label(left_pane,text="connecters")
           connecters.pack(fill = tk.BOTH, expand = True)
           video=tk.Label(left_pane,text="video ports")
           video.pack(fill = tk.BOTH, expand = True)
           usb=tk.Label(left_pane,text="usb ports")
           usb.pack(fill = tk.BOTH, expand = True)
           vesa=tk.Label(left_pane,text="vesa support")
           vesa.pack(fill = tk.BOTH, expand = True)


           brandv=tk.StringVar()
           modelv=tk.StringVar()
           ssizev=tk.StringVar()
           widescreenv=tk.StringVar()
           glaresv=tk.StringVar()
           ledv=tk.StringVar()
           panelv=tk.StringVar()
           displaytv=tk.StringVar()
           astv=tk.StringVar()
           maxresv=tk.StringVar()
           aspectratv=tk.StringVar()
           constrast_ratiov=tk.StringVar()
           resp_timev=tk.StringVar()
           refresh_ratev=tk.StringVar()
           ivcv=tk.StringVar()
           connectersv=tk.StringVar()
           videov=tk.StringVar()
           usbv=tk.StringVar()
           vesav=tk.StringVar()


           brande=tk.Entry(right_pane,textvariable=brandv)
           brande.pack(fill = tk.BOTH, expand = True)
           modele=tk.Entry(right_pane,textvariable=modelv)
           modele.pack(fill = tk.BOTH, expand = True)
           ssizee=tk.Entry(right_pane,textvariable=ssizev)
           ssizee.pack(fill = tk.BOTH, expand = True)
           widescreene=tk.Entry(right_pane,textvariable=widescreenv)
           widescreene.pack(fill = tk.BOTH, expand = True)
           glarese=tk.Entry(right_pane,textvariable=glaresv)
           glarese.pack(fill = tk.BOTH, expand = True)
           lede=tk.Entry(right_pane,textvariable=ledv)
           lede.pack(fill = tk.BOTH, expand = True)
           panele=tk.Entry(right_pane,textvariable=panelv)
           panele.pack(fill = tk.BOTH, expand = True)
           displayte=tk.Entry(right_pane,textvariable=displaytv)
           displayte.pack(fill = tk.BOTH, expand = True)
           aste=tk.Entry(right_pane,textvariable=astv)
           aste.pack(fill = tk.BOTH, expand = True)
           maxrese=tk.Entry(right_pane,textvariable=maxresv)
           maxrese.pack(fill = tk.BOTH, expand = True)
           aspectrate=tk.Entry(right_pane,textvariable=aspectratv)
           aspectrate.pack(fill = tk.BOTH, expand = True)
           constrast_ratioe=tk.Entry(right_pane,textvariable=constrast_ratiov)
           constrast_ratioe.pack(fill = tk.BOTH, expand = True)
           resp_timee=tk.Entry(right_pane,textvariable=resp_timev)
           resp_timee.pack(fill = tk.BOTH, expand = True)
           refresh_ratee=tk.Entry(right_pane,textvariable=refresh_ratev)
           refresh_ratee.pack(fill = tk.BOTH, expand = True)
           ivce=tk.Entry(right_pane,textvariable=ivcv)
           ivce.pack(fill = tk.BOTH, expand = True)
           connecterse=tk.Entry(right_pane,textvariable=connectersv)
           connecterse.pack(fill = tk.BOTH, expand = True)
           videoe=tk.Entry(right_pane,textvariable=videov)
           videoe.pack(fill = tk.BOTH, expand = True)
           usbe=tk.Entry(right_pane,textvariable=usbv)
           usbe.pack(fill = tk.BOTH, expand = True)
           vesae=tk.Entry(right_pane,textvariable=vesav)
           vesae.pack(fill = tk.BOTH, expand = True)
       elif selection == "adapters":
           print(selection)
           drop.pack_forget()
           top = tk.Frame(newWindow, background="black", height=40)
           main = tk.PanedWindow(newWindow, background="black")

           top.pack(side="top", fill="x")
           main.pack(side="top", fill="both", expand=True)
           left_pane = tk.Frame(main, background="black", width=300)
           right_pane = tk.PanedWindow(main, background="black", width=300)
           main.add(left_pane)
           main.add(right_pane)
           left = tk.Label(top,text="networking")
           left.pack()

           def submit():
               nc1=cend1v.get()
               nc2=cend2v.get()
               ng1=gend1v.get()
               ng2=gend2v.get()
               nca=catv.get()
               nl=lengthv.get()
               n={}
               n["port1"] = nc1
               n["ports2"] = nc2
               n["port_gender1"] = ng1
               n["port_gender2"] = ng2
               n["caterogory"] = nca
               n["length"] = nl
               print(json.dumps(n))
               def write_json(new_data, filename=jsof):
                 with open(filename,'r+') as file:
                # First we load existing data into a dict.
                    file_data = json.load(file)
        # Join new_data with file_data inside emp_details
                    file_data["adapter"].append(new_data)
        # Sets file's current position at offset.
                    file.seek(0)
        # convert back to json.
                    json.dump(file_data, file, indent = 4)
               write_json(n)
               newWindow.destroy()
           sub_btn=tk.Button(top,text="submit",command=submit)
           sub_btn.pack()

           cend1=tk.Label(left_pane,text="connecter type (end 1)")
           cend1.pack(fill = tk.BOTH, expand = True)
           cend2=tk.Label(left_pane,text="connecters (end 2)")
           cend2.pack(fill = tk.BOTH, expand = True)
           gend1=tk.Label(left_pane,text="gender (end 1)")
           gend1.pack(fill = tk.BOTH, expand = True)
           gend2=tk.Label(left_pane,text="gender (end 2)")
           gend2.pack(fill = tk.BOTH, expand = True)
           cat=tk.Label(left_pane,text="caterogory")
           cat.pack(fill = tk.BOTH, expand = True)
           length=tk.Label(left_pane,text="length")
           length.pack(fill = tk.BOTH, expand = True)


           cend1v=tk.StringVar()
           cend2v=tk.StringVar()
           gend1v=tk.StringVar()
           gend2v=tk.StringVar()
           catv=tk.StringVar()
           lengthv=tk.StringVar()

           cend1e=tk.Entry(right_pane,textvariable=cend1v)
           cend1e.pack(fill = tk.BOTH, expand = True)
           cend2e=tk.Entry(right_pane,textvariable=cend2v)
           cend2e.pack(fill = tk.BOTH, expand = True)
           gend1e=tk.Entry(right_pane,textvariable=gend1v)
           gend1e.pack(fill = tk.BOTH, expand = True)
           gend2e=tk.Entry(right_pane,textvariable=gend2v)
           gend2e.pack(fill = tk.BOTH, expand = True)
           cate=tk.Entry(right_pane,textvariable=catv)
           cate.pack(fill = tk.BOTH, expand = True)
           lengthe=tk.Entry(right_pane,textvariable=lengthv)
           lengthe.pack(fill = tk.BOTH, expand = True)
       elif selection == "laptop":

           print(selection)
           drop.pack_forget()
           top = tk.Frame(newWindow, background="black", height=40)
           main = tk.PanedWindow(newWindow, background="black")

           top.pack(side="top", fill="x")
           main.pack(side="top", fill="both", expand=True)
           left_pane = tk.Frame(main, background="black", width=300)
           right_pane = tk.PanedWindow(main, background="black", width=300)
           main.add(left_pane)
           main.add(right_pane)
           left = tk.Label(top,text="networking")
           left.pack()

           def submit():
               mbr=brandv.get()
               mmo=modelv.get()
               mse=seriesv.get()
               mcm=cmodelv.get()
               mcc=ccorev.get()
               mcb=cbrandv.get()
               mct=cthreadv.get()
               mcf=cfreqv.get()
               mss=ssizev.get()
               mto=touchscreenv.get()
               mdt=dtypev.get()
               mre=resolutionv.get()
               mpa=panelv.get()
               mig=igpuv.get()
               mgp=gpuv.get()
               mgr=gvramv.get()
               mir=ivramv.get()
               mso=sodimmv.get()
               mrs=ram_slotsv.get()
               mmr=maxramv.get()
               mrv=ramv.get()
               mrt=ramtv.get()
               msd=ssdv.get()
               mnv=nvmev.get()
               mh=hddv.get()
               mdv=dvdv.get()
               mbl=bluetoothv.get()
               mwi=wifigenv.get()
               mwe=webcamv.get()
               mic=micv.get()
               mle=ledkeyv.get()
               mk=keyboardv.get()
               mnp=numpadv.get()
               mca=cardrev.get()
               mvv=videov.get()
               mu=usbv.get()
               mch=chargerv.get()
               ma=audiov.get()
               mbw=battrywav.get()
               mth=thunderboltv.get()
               met=ethernetv.get()
               l={}
               l["brand"]=mbr
               l["model"]=mmo
               l["cpu_core"]=mcc
               l["series"]=mse
               l["cpu_model"]=mcm
               l["ram_slots"]=mrs
               l["ram"]=mrv
               l["nvme"]=mnv
               l["ssd"]=msd
               l["cpu_freq"]=mcf
               l["ram_type"]=mrt
               l["gpu"]=mgp
               l["igpu"]=mig
               l["gpu_vram"]=mgr
               l["igpu_vram"]=mir
               l["hdd"]=mh
               l["max_ram"]=mmr
               l["cthreads"]=mct
               l["cbrand"]=mcb
               l["usb"]=mu
               l["video"]=mvv
               l["audio"]=ma
               l["ethernet"]=met
               l['battry_watt']=mbw
               l['thunderbolt']=mth
               l['charger_port']=mch
               l['resolution']=mre
               l["screen_size"]=mss
               l["touchscreen"]=mto
               l["dp_type"]=mdt
               l["panel"]=mpa
               l["wifi_gen"]=mwi
               l["dvd"]=mdv
               l["bluetooth"]=mbl
               l["numpad"]=mnp
               l["webcam"]=mwe
               l["mic"]=mic
               l["keyboard"]=mk
               l["sodimm"]=mso
               l["card_reader"]=mca
               l["led_keyb"]=mle
               print(json.dumps(l))
               def write_json(new_data, filename=jsof):
                 with open(filename,'r+') as file:
                # First we load existing data into a dict.
                    file_data = json.load(file)
        # Join new_data with file_data inside emp_details
                    file_data["laptop"].append(new_data)
        # Sets file's current position at offset.
                    file.seek(0)
        # convert back to json.
                    json.dump(file_data, file, indent = 4)
               write_json(l)
               newWindow.destroy()
           sub_btn=tk.Button(top,text="submit",command=submit)
           sub_btn.pack()
           brand=tk.Label(left_pane,text="brand")
           brand.pack(fill = tk.BOTH, expand = True)
           model=tk.Label(left_pane,text="model")
           model.pack(fill = tk.BOTH, expand = True)
           series=tk.Label(left_pane,text="series")
           series.pack(fill = tk.BOTH, expand = True)
           cmodel=tk.Label(left_pane,text="cpu model")
           cmodel.pack(fill = tk.BOTH, expand = True)
           ccore=tk.Label(left_pane,text="cpu core")
           ccore.pack(fill = tk.BOTH, expand = True)
           cbrand=tk.Label(left_pane,text="cpu brand")
           cthread=tk.Label(left_pane,text="cpu thread")
           cthread.pack(fill = tk.BOTH, expand = True)
           cfreq=tk.Label(left_pane,text="cpu Frequency")
           cfreq.pack(fill = tk.BOTH, expand = True)
           ssize=tk.Label(left_pane,text="screen size")
           ssize.pack(fill = tk.BOTH, expand = True)
           touchscreen=tk.Label(left_pane,text="touchscreen")
           touchscreen.pack(fill = tk.BOTH, expand = True)
           dtype=tk.Label(left_pane,text="display type")
           dtype.pack(fill = tk.BOTH, expand = True)
           resolution=tk.Label(left_pane,text="resolution")
           resolution.pack(fill = tk.BOTH, expand = True)
           panel=tk.Label(left_pane,text="panel")
           panel.pack(fill = tk.BOTH, expand = True)
           igpu=tk.Label(left_pane,text="igpu")
           igpu.pack(fill = tk.BOTH, expand = True)
           gpu=tk.Label(left_pane,text="gpu")
           gpu.pack(fill = tk.BOTH, expand = True)
           gvram=tk.Label(left_pane,text="gpu vram")
           gvram.pack(fill = tk.BOTH, expand = True)
           ivram=tk.Label(left_pane,text="igpu vram")
           ivram.pack(fill = tk.BOTH, expand = True)
           sodimm=tk.Label(left_pane,text="sodimm")
           sodimm.pack(fill = tk.BOTH, expand = True)
           ram_slots=tk.Label(left_pane,text="ram_slots")
           ram_slots.pack(fill = tk.BOTH, expand = True)
           maxram=tk.Label(left_pane,text="maxram")
           maxram.pack(fill = tk.BOTH, expand = True)
           ram=tk.Label(left_pane,text="ram")
           ram.pack(fill = tk.BOTH, expand = True)
           ramt=tk.Label(left_pane,text="ram type (ddr)")
           ramt.pack(fill = tk.BOTH, expand = True)
           ssd=tk.Label(left_pane,text="ssd")
           ssd.pack(fill = tk.BOTH, expand = True)
           nvme=tk.Label(left_pane,text="nvme")
           nvme.pack(fill = tk.BOTH, expand = True)
           hdd=tk.Label(left_pane,text="hdd")
           hdd.pack(fill = tk.BOTH, expand = True)
           dvd=tk.Label(left_pane,text="dvd")
           dvd.pack(fill = tk.BOTH, expand = True)
           bluetooth=tk.Label(left_pane,text="bluetooth")
           bluetooth.pack(fill = tk.BOTH, expand = True)
           wifigen=tk.Label(left_pane,text="wifi gen")
           wifigen.pack(fill = tk.BOTH, expand = True)
           webcam=tk.Label(left_pane,text="webcam")
           webcam.pack(fill = tk.BOTH, expand = True)
           mic=tk.Label(left_pane,text="mic")
           mic.pack(fill = tk.BOTH, expand = True)
           ledkey=tk.Label(left_pane,text="backlit keyboard")
           ledkey.pack(fill = tk.BOTH, expand = True)
           keyboard=tk.Label(left_pane,text="keyboard")
           keyboard.pack(fill = tk.BOTH, expand = True)
           numpad=tk.Label(left_pane,text="numpad included")
           numpad.pack(fill = tk.BOTH, expand = True)
           cardre=tk.Label(left_pane,text="card reader")
           cardre.pack(fill = tk.BOTH, expand = True)
           video=tk.Label(left_pane,text="video ports")
           video.pack(fill = tk.BOTH, expand = True)
           usb=tk.Label(left_pane,text="usb ports")
           usb.pack(fill = tk.BOTH, expand = True)
           charger=tk.Label(left_pane,text="charger port")
           charger.pack(fill = tk.BOTH, expand = True)
           audio=tk.Label(left_pane,text="audio ports")
           audio.pack(fill = tk.BOTH, expand = True)
           battrywa=tk.Label(left_pane,text="battry watts")
           battrywa.pack(fill = tk.BOTH, expand = True)
           thunderbolt=tk.Label(left_pane,text="thunderbolt")
           thunderbolt.pack(fill = tk.BOTH, expand = True)
           ethernet=tk.Label(left_pane,text="ethernet ports")
           ethernet.pack(fill = tk.BOTH, expand = True)


           brandv=tk.StringVar()
           modelv=tk.StringVar()
           seriesv=tk.StringVar()
           cmodelv=tk.StringVar()
           ccorev=tk.StringVar()
           cbrandv=tk.StringVar()
           cthreadv=tk.StringVar()
           cfreqv=tk.StringVar()
           ssizev=tk.StringVar()
           touchscreenv=tk.StringVar()
           dtypev=tk.StringVar()
           resolutionv=tk.StringVar()
           panelv=tk.StringVar()
           igpuv=tk.StringVar()
           gpuv=tk.StringVar()
           gvramv=tk.StringVar()
           ivramv=tk.StringVar()
           sodimmv=tk.StringVar()
           ram_slotsv=tk.StringVar()
           maxramv=tk.StringVar()
           ramv=tk.StringVar()
           ramtv=tk.StringVar()
           ssdv=tk.StringVar()
           nvmev=tk.StringVar()
           hddv=tk.StringVar()
           dvdv=tk.StringVar()
           bluetoothv=tk.StringVar()
           wifigenv=tk.StringVar()
           webcamv=tk.StringVar()
           micv=tk.StringVar()
           ledkeyv=tk.StringVar()
           keyboardv=tk.StringVar()
           numpadv=tk.StringVar()
           cardrev=tk.StringVar()
           videov=tk.StringVar()
           usbv=tk.StringVar()
           chargerv=tk.StringVar()
           audiov=tk.StringVar()
           battrywav=tk.StringVar()
           thunderboltv=tk.StringVar()
           ethernetv=tk.StringVar()


           brande=tk.Entry(right_pane,textvariable=brandv)
           brande.pack(fill = tk.BOTH, expand = True)
           modele=tk.Entry(right_pane,textvariable=modelv)
           modele.pack(fill = tk.BOTH, expand = True)
           seriese=tk.Entry(right_pane,textvariable=seriesv)
           seriese.pack(fill = tk.BOTH, expand = True)
           cmodele=tk.Entry(right_pane,textvariable=cmodelv)
           cmodele.pack(fill = tk.BOTH, expand = True)
           ccoree=tk.Entry(right_pane,textvariable=ccorev)
           ccoree.pack(fill = tk.BOTH, expand = True)
           cbrande=tk.Entry(right_pane,textvariable=cbrandv)
           cbrande.pack(fill = tk.BOTH, expand = True)
           cthreade=tk.Entry(right_pane,textvariable=cthreadv)
           cthreade.pack(fill = tk.BOTH, expand = True)
           cfreqe=tk.Entry(right_pane,textvariable=cfreqv)
           cfreqe.pack(fill = tk.BOTH, expand = True)
           ssizee=tk.Entry(right_pane,textvariable=ssizev)
           ssizee.pack(fill = tk.BOTH, expand = True)
           touchscreene=tk.Entry(right_pane,textvariable=touchscreenv)
           touchscreene.pack(fill = tk.BOTH, expand = True)
           dtypee=tk.Entry(right_pane,textvariable=dtypev)
           dtypee.pack(fill = tk.BOTH, expand = True)
           resolutione=tk.Entry(right_pane,textvariable=resolutionv)
           resolutione.pack(fill = tk.BOTH, expand = True)
           panele=tk.Entry(right_pane,textvariable=panelv)
           panele.pack(fill = tk.BOTH, expand = True)
           igpue=tk.Entry(right_pane,textvariable=igpuv)
           igpue.pack(fill = tk.BOTH, expand = True)
           gpue=tk.Entry(right_pane,textvariable=gpuv)
           gpue.pack(fill = tk.BOTH, expand = True)
           gvrame=tk.Entry(right_pane,textvariable=gvramv)
           gvrame.pack(fill = tk.BOTH, expand = True)
           ivrame=tk.Entry(right_pane,textvariable=ivramv)
           ivrame.pack(fill = tk.BOTH, expand = True)
           sodimme=tk.Entry(right_pane,textvariable=sodimmv)
           sodimme.pack(fill = tk.BOTH, expand = True)
           ram_slotse=tk.Entry(right_pane,textvariable=ram_slotsv)
           ram_slotse.pack(fill = tk.BOTH, expand = True)
           maxrame=tk.Entry(right_pane,textvariable=maxramv)
           maxrame.pack(fill = tk.BOTH, expand = True)
           rame=tk.Entry(right_pane,textvariable=ramv)
           rame.pack(fill = tk.BOTH, expand = True)
           ramte=tk.Entry(right_pane,textvariable=ramtv)
           ramte.pack(fill = tk.BOTH, expand = True)
           ssde=tk.Entry(right_pane,textvariable=ssdv)
           ssde.pack(fill = tk.BOTH, expand = True)
           nvmee=tk.Entry(right_pane,textvariable=nvmev)
           nvmee.pack(fill = tk.BOTH, expand = True)
           hdde=tk.Entry(right_pane,textvariable=hddv)
           hdde.pack(fill = tk.BOTH, expand = True)
           dvde=tk.Entry(right_pane,textvariable=dvdv)
           dvde.pack(fill = tk.BOTH, expand = True)
           bluetoothe=tk.Entry(right_pane,textvariable=bluetoothv)
           bluetoothe.pack(fill = tk.BOTH, expand = True)
           wifigene=tk.Entry(right_pane,textvariable=wifigenv)
           wifigene.pack(fill = tk.BOTH, expand = True)
           webcame=tk.Entry(right_pane,textvariable=webcamv)
           webcame.pack(fill = tk.BOTH, expand = True)
           mice=tk.Entry(right_pane,textvariable=micv)
           mice.pack(fill = tk.BOTH, expand = True)
           ledkeye=tk.Entry(right_pane,textvariable=ledkeyv)
           ledkeye.pack(fill = tk.BOTH, expand = True)
           keyboarde=tk.Entry(right_pane,textvariable=keyboardv)
           keyboarde.pack(fill = tk.BOTH, expand = True)
           numpade=tk.Entry(right_pane,textvariable=numpadv)
           numpade.pack(fill = tk.BOTH, expand = True)
           cardree=tk.Entry(right_pane,textvariable=cardrev)
           cardree.pack(fill = tk.BOTH, expand = True)
           videoe=tk.Entry(right_pane,textvariable=videov)
           videoe.pack(fill = tk.BOTH, expand = True)
           usbe=tk.Entry(right_pane,textvariable=usbv)
           usbe.pack(fill = tk.BOTH, expand = True)
           chargere=tk.Entry(right_pane,textvariable=chargerv)
           chargere.pack(fill = tk.BOTH, expand = True)
           audioe=tk.Entry(right_pane,textvariable=audiov)
           audioe.pack(fill = tk.BOTH, expand = True)
           battrywae=tk.Entry(right_pane,textvariable=battrywav)
           battrywae.pack(fill = tk.BOTH, expand = True)
           thunderbolte=tk.Entry(right_pane,textvariable=thunderboltv)
           thunderbolte.pack(fill = tk.BOTH, expand = True)
           ethernete=tk.Entry(right_pane,textvariable=ethernetv)
           ethernete.pack(fill = tk.BOTH, expand = True)
       elif selection == "networking":
           print(selection)
           drop.pack_forget()
           top = tk.Frame(newWindow, background="black", height=40)
           main = tk.PanedWindow(newWindow, background="black")

           top.pack(side="top", fill="x")
           main.pack(side="top", fill="both", expand=True)
           left_pane = tk.Frame(main, background="black", width=300)
           right_pane = tk.PanedWindow(main, background="black", width=300)
           main.add(left_pane)
           main.add(right_pane)
           left = tk.Label(top,text="networking")
           left.pack()
           def choose1():
               inp=pi.get()
               if inp == "patch_panel":
                   sub_btn.destroy()
                   co.destroy()

                   def submit():
                       # print(data)
                       newWindow.destroy()


                   btn=tk.Button(top,text="submit",command=submit)
                   btn.pack()

                   # brand
                   # model
                   # name
                   # fibre_port
                   # eth_ports


               if inp == "switch":
                   sub_btn.destroy()
                   co.destroy()


                   def submit():
                       sb=brandv.get()
                       sna=namev.get()
                       sm=modelv.get()
                       sne=net_man_typev.get()
                       sp=portspeedv.get()
                       se=ethernetv.get()
                       sf=fibree.get()
                       data='{"name":"' + sna + '","brand":"' + sb + '","model":"' + sm + '","eth_ports":"' + se + '","fibre_port":"' + sf + '","port_speed":"' + sp + '","net_man_type":"' + sne + '"}'
                       print(data)
                       newWindow.destroy()


                   btn=tk.Button(top,text="submit",command=submit)
                   btn.pack()

                   brand=tk.Label(left_pane,text="brand")
                   fibre=tk.Label(left_pane,text="fibre ports")
                   fibre.pack(fill = tk.BOTH, expand = True)
                   ethernet=tk.Label(left_pane,text="ethernet ports")
                   ethernet.pack(fill = tk.BOTH, expand = True)
                   brand.pack(fill = tk.BOTH, expand = True)
                   name=tk.Label(left_pane,text="name")
                   name.pack(fill = tk.BOTH, expand = True)
                   model=tk.Label(left_pane,text="model")
                   model.pack(fill = tk.BOTH, expand = True)
                   net_man_type=tk.Label(left_pane,text="Network Management Type")
                   net_man_type.pack(fill = tk.BOTH, expand = True)
                   portspeed=tk.Label(left_pane,text="port speed")
                   portspeed.pack(fill = tk.BOTH, expand = True)


                   brandv=tk.StringVar()
                   namev=tk.StringVar()
                   modelv=tk.StringVar()
                   net_man_typev=tk.StringVar()
                   portspeedv=tk.StringVar()
                   fibrev=tk.StringVar()
                   ethernetv=tk.StringVar()

                   brande=tk.Entry(right_pane,textvariable=brandv)
                   brande.pack(fill = tk.BOTH, expand = True)
                   fibree=tk.Entry(right_pane,textvariable=fibrev)
                   fibree.pack(fill = tk.BOTH, expand = True)
                   ethernete=tk.Entry(right_pane,textvariable=ethernetv)
                   ethernete.pack(fill = tk.BOTH, expand = True)
                   namee=tk.Entry(right_pane,textvariable=namev)
                   namee.pack(fill = tk.BOTH, expand = True)
                   modele=tk.Entry(right_pane,textvariable=modelv)
                   modele.pack(fill = tk.BOTH, expand = True)
                   net_man_typee=tk.Entry(right_pane,textvariable=net_man_typev)
                   net_man_typee.pack(fill = tk.BOTH, expand = True)
                   portspeede=tk.Entry(right_pane,textvariable=portspeedv)
                   portspeede.pack(fill = tk.BOTH, expand = True)
           sub_btn=tk.Button(top,text="submit",command=choose1)
           sub_btn.pack()

           pi=tk.StringVar()
           pi.set("choose one")

           co= tk.OptionMenu(right_pane, pi,"switch", "router","wifi_extender","patch_panel")
           co.pack()

    # choose caterogory
    menu= tk.StringVar()
    menu.set("Select Any Language")
    drop= tk.OptionMenu(newWindow, menu,"tools", "pc_parts","pc","laptop","networking","cables","books","monitors","adapters","games",command=callback)
    drop.pack()

tbutton1=tk.Button(toolbar, text="+",command=openNewWindow)
tbutton1.pack(side=tk.RIGHT)

# sidebar level 1
listtree = ttk.Treeview(left_pane)
listtree.insert('','0','item1',text="tools")
listtree.insert('','0','item2',text="pc_parts")
listtree.insert('','end','item3',text="pc")
listtree.insert('','end','item4',text="laptop")
listtree.insert('','0','item5',text="networking")
listtree.insert('','end','item6',text="cables")
listtree.insert('','end','item7',text="books")
listtree.insert('','end','item8',text="monitors")
listtree.insert('','end','item9',text="adapters")
listtree.insert('','end','item10',text="games")
# level 2 parts
listtree.insert('item2','end','ram',text="ram")
listtree.insert('item2','end','gpu',text='gpu')
listtree.insert('item2','end','case',text="case")
listtree.insert('item2','end','cpu',text="cpu")
listtree.insert('item2','end','cpu_cooler',text="cpu_cooler")
listtree.insert('item2','end','psu',text="psu")
listtree.insert('item2','end','storage',text="storage")
listtree.insert('item2','end','motherboard',text="motherboard")
# level 2 tools
# listbox.config(font="20")
listtree.insert('item1','end','skrew',text="skrew")
listtree.insert('item1','end','bolt',text='bolt')

def go(event):
    # cs = listbox.curselection()
    # do=listbox.get(cs)
    curItem = listtree.focus()
    cs=listtree.item(curItem)
    do=cs["text"]
    h=tk.Scrollbar(right_pane, orient='horizontal')
    h.pack(side=tk.BOTTOM, fill='x')
    if do == "gpu":
        f = open(jsof)
        data = json.load(f)
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("name","size","core_clock","brand","model","mem_type","output","base_brand","cuda","mem_clock","card_bus","hieght","width","length","power","watt"))
        treeview.heading("#1",text="name")
        treeview.heading("#2",text="size")
        treeview.heading("#3",text="core_clock")
        treeview.heading("#4",text="brand")
        treeview.heading("#5",text="model")
        treeview.heading("#6",text="mem_type")
        treeview.heading("#7",text="output")
        treeview.heading("#8",text="base_brand")
        treeview.heading("#9",text="cuda")
        treeview.heading("#10",text="mem_clock")
        treeview.heading("#11",text="card_bus")
        treeview.heading("#12",text="hieght")
        treeview.heading("#13",text="width")
        treeview.heading("#14",text="length")
        treeview.heading("#15",text="power")
        treeview.heading("#16",text="watt")
        h.config(command=treeview.xview)
        treeview.pack()
        for row in data["gpu"]:
            treeview.insert("","end",values=(row["name"],row["size"],row["core_clock"],row["brand"],row["model"],row["mem_type"],row["output"],row["base_brand"],row["cuda"],row["mem_clock"],row["card_bus"],row["hieght"],row["width"],row["length"],row["power"],row["watt"]))
    if do == "cpu":
        f = open(jsof)
        data = json.load(f)
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("name","core","thread","socket","model","base_freq","turbo-freq","igpu","brand","cache","unlocked","year"))
        treeview.heading("#1",text="name")
        treeview.heading("#2",text="core")
        treeview.heading("#3",text="thread")
        treeview.heading("#4",text="socket")
        treeview.heading("#5",text="model")
        treeview.heading("#6",text="base_freq")
        treeview.heading("#7",text="turbo-freq")
        treeview.heading("#8",text="igpu")
        treeview.heading("#9",text="brand")
        treeview.heading("#10",text="cache")
        treeview.heading("#11",text="unlocked")
        treeview.heading("#12",text="year")
        h.config(command=treeview.xview)
        treeview.pack()
        for row in data["cpu"]:
            treeview.insert("","end",values=(row["name"],row["core"],row["thread"],row["socket"],row["model"],row["base_freq"],row["turbo-freq"],row["igpu"],row["brand"],row["cache"],row["unlocked"],row["year"]))
    if do == "case":
        f = open(jsof)
        data = json.load(f)
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("name","model","mobo_supp","case_type","3drive_bays","2drive_bays","pcie","ports","gpu-l","gpu-h","brand","cpu-h","window","series","fan","psu-l"))
        treeview.heading("#1",text="name")
        treeview.heading("#2",text="model")
        treeview.heading("#3",text="mobo_supp")
        treeview.heading("#4",text="case_type")
        treeview.heading("#5",text="3drive_bays")
        treeview.heading("#6",text="2drive_bays")
        treeview.heading("#7",text="pcie")
        treeview.heading("#8",text="ports")
        treeview.heading("#9",text="gpu-l")
        treeview.heading("#10",text="gpu-h")
        treeview.heading("#11",text="brand")
        treeview.heading("#12",text="cpu-h")
        treeview.heading("#13",text="window")
        treeview.heading("#14",text="series")
        treeview.heading("#15",text="fan")
        treeview.heading("#16",text="psu-l")
        h.config(command=treeview.xview)
        treeview.pack()
        for row in data["case"]:
            treeview.insert("","end",values=(row["name"],row["model"],row["mobo_supp"],row["case_type"],row["3drive_bays"],row["2drive_bays"],row["pcie"],row["ports"],row["gpu-l"],row["gpu-h"],row["brand"],row["cpu-h"],row["window"],row["series"],row["fan"],row["psu-l"]))
    if do == "psu":
        f = open(jsof)
        data = json.load(f)
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("name","watt","rating","brand","model","modular","type","connectors","max_psu_l"))
        treeview.heading("#1",text="name")
        treeview.heading("#2",text="watt")
        treeview.heading("#3",text="rating")
        treeview.heading("#4",text="brand")
        treeview.heading("#5",text="model")
        treeview.heading("#6",text="modular")
        treeview.heading("#7",text="type")
        treeview.heading("#8",text="connectors")
        treeview.heading("#9",text="max_psu_l")
        h.config(command=treeview.xview)
        treeview.pack()
        for row in data["psu"]:
            treeview.insert("","end",values=(row["name"],row["watt"],row["rating"],row["brand"],row["model"],row["modular"],row["type"],row["connectors"],row["max_psu_l"]))
    if do == "storage":
        f = open(jsof)
        data = json.load(f)
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("name","brand","size","type","form","interface","internal","model","rpm","read","write"))
        treeview.heading("#1",text="name")
        treeview.heading("#2",text="brand")
        treeview.heading("#3",text="size")
        treeview.heading("#4",text="type")
        treeview.heading("#5",text="form")
        treeview.heading("#6",text="interface")
        treeview.heading("#7",text="internal")
        treeview.heading("#8",text="model")
        treeview.heading("#9",text="rpm")
        treeview.heading("#10",text="read")
        treeview.heading("#11",text="write")
        h.config(command=treeview.xview)
        treeview.pack()
        for row in data["storage"]:
            treeview.insert("","end",values=(row["name"],row["brand"],row["size"],row["type"],row["form"],row["interface"],row["internal"],row["model"],row["rpm"],row["read"],row["write"]))


    if do == "ram":
        f = open(jsof)
        data = json.load(f)
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("name","cap_total","cap_per","ddr","dimm","model","speed","brand","form"))
        treeview.heading("#1",text="name")
        treeview.heading("#2",text="cap_total")
        treeview.heading("#3",text="cap_per")
        treeview.heading("#4",text="ddr")
        treeview.heading("#5",text="dimm")
        treeview.heading("#6",text="model")
        treeview.heading("#7",text="speed")
        treeview.heading("#8",text="brand")
        treeview.heading("#9",text="form")
        h.config(command=treeview.xview)
        treeview.pack()
        for row in data["ram"]:
            treeview.insert("","end",values=(row["name"],row["cap_total"],row["cap_per"],row["ddr"],row["dimm"],row["model"],row["speed"],row["brand"],row["form"]))
    if do == "cables":
        f = open(jsof)
        data = json.load(f)
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("cable_gender","cp1","cp2","cp3","caterogory","length","amount"))
        treeview.heading("#1",text="cable_gender")
        treeview.heading("#2",text="cp1")
        treeview.heading("#3",text="cp2")
        treeview.heading("#4",text="cp3")
        treeview.heading("#5",text="caterogory")
        treeview.heading("#6",text="length")
        treeview.heading("#7",text="amount")
        h.config(command=treeview.xview)
        treeview.pack()
        f.close()
        for row in data["cable"]:
            treeview.insert("", "end", values=(row["cable_gender"], row["cp1"], row["cp2"], row["cp3"], row["caterogory"], row["length"], row["amount"]))
    if do == "laptop":
        f = open(jsof)
        data = json.load(f)
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("brand","model","cpu_core","series","cpu_model","ram_slots","ram","nvme","ssd","cpu_freq","ram_type","gpu","igpu","gpu_vram","igpu_vram","hdd","max_ram","cthreads","cbrand","usb","video","audio","ethernet","battry_watt","thunderbolt","charger_port","resolution","screen_size","touchscreen","dp_type","panel","wifi_gen","dvd","bluetooth","numpad","webcam","mic","keyboard","sodimm","card_reader","led_keyb"))
        treeview.heading("#1",text="brand")
        treeview.heading("#2",text="model")
        treeview.heading("#3",text="cpu_core")
        treeview.heading("#4",text="series")
        treeview.heading("#5",text="cpu_model")
        treeview.heading("#6",text="ram_slots")
        treeview.heading("#7",text="ram")
        treeview.heading("#8",text="nvme")
        treeview.heading("#9",text="ssd")
        treeview.heading("#10",text="cpu_freq")
        treeview.heading("#11",text="ram_type")
        treeview.heading("#12",text="gpu")
        treeview.heading("#13",text="igpu")
        treeview.heading("#14",text="gpu_vram")
        treeview.heading("#15",text="igpu_vram")
        treeview.heading("#16",text="hdd")
        treeview.heading("#17",text="max_ram")
        treeview.heading("#18",text="cthreads")
        treeview.heading("#19",text="cbrand")
        treeview.heading("#20",text="usb")
        treeview.heading("#21",text="video")
        treeview.heading("#22",text="audio")
        treeview.heading("#23",text="ethernet")
        treeview.heading("#24",text="battry_watt")
        treeview.heading("#25",text="thunderbolt")
        treeview.heading("#26",text="charger_port")
        treeview.heading("#27",text="resolution")
        treeview.heading("#28",text="screen_size")
        treeview.heading("#29",text="touchscreen")
        treeview.heading("#30",text="dp_type")
        treeview.heading("#31",text="panel")
        treeview.heading("#32",text="wifi_gen")
        treeview.heading("#33",text="dvd")
        treeview.heading("#34",text="bluetooth")
        treeview.heading("#35",text="numpad")
        treeview.heading("#36",text="webcam")
        treeview.heading("#37",text="mic")
        treeview.heading("#38",text="keyboard")
        treeview.heading("#39",text="sodimm")
        treeview.heading("#40",text="card_reader")
        treeview.heading("#41",text="led_keyb")
        h.config(command=treeview.xview)
        treeview.pack()
        for row in data["laptop"]:
            treeview.insert("","end",values=(row["brand"],row["model"],row["cpu_core"],row["series"],row["cpu_model"],row["ram_slots"],row["ram"],row["nvme"],row["ssd"],row["cpu_freq"],row["ram_type"],row["gpu"],row["igpu"],row["gpu_vram"],row["igpu_vram"],row["hdd"],row["max_ram"],row["cthreads"],row["cbrand"],row["usb"],row["video"],row["audio"],row["ethernet"],row["battry_watt"],row["thunderbolt"],row["charger_port"],row["resolution"],row["screen_size"],row["touchscreen"],row["dp_type"],row["panel"],row["wifi_gen"],row["dvd"],row["bluetooth"],row["numpad"],row["webcam"],row["mic"],row["keyboard"],row["sodimm"],row["card_reader"],row["led_keyb"]))
    if do == "monitors":
        f = open(jsof)
        data = json.load(f)
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("brand","model","screen_size","connecters","video","usb","vesa","resolution","refresh_rate","widescreen","glare_screen","panel","led_backlight","display_type","constrast_ratio","aspect_ratio","response_time","adaptive_sync_tech","input_video"))
        treeview.heading("#1",text="brand")
        treeview.heading("#2",text="model")
        treeview.heading("#3",text="screen_size")
        treeview.heading("#4",text="connecters")
        treeview.heading("#5",text="video")
        treeview.heading("#6",text="usb")
        treeview.heading("#7",text="vesa")
        treeview.heading("#8",text="resolution")
        treeview.heading("#9",text="refresh_rate")
        treeview.heading("#10",text="widescreen")
        treeview.heading("#11",text="glare_screen")
        treeview.heading("#12",text="panel")
        treeview.heading("#13",text="led_backlight")
        treeview.heading("#14",text="display_type")
        treeview.heading("#15",text="constrast_ratio")
        treeview.heading("#16",text="aspect_ratio")
        treeview.heading("#17",text="response_time")
        treeview.heading("#18",text="adaptive_sync_tech")
        treeview.heading("#19",text="input_video")
        h.config(command=treeview.xview)
        treeview.pack()
        for row in data["monitor"]:
            treeview.insert("","end",values=(row["brand"],row["model"],row["screen_size"],row["connecters"],row["video"],row["usb"],row["vesa"],row["resolution"],row["refresh_rate"],row["widescreen"],row["glare_screen"],row["panel"],row["led_backlight"],row["display_type"],row["constrast_ratio"],row["aspect_ratio"],row["response_time"],row["adaptive_sync_tech"],row["input_video"]))
    if do == "adapters":
        f = open(jsof)
        data = json.load(f)
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("port1","ports2","port_gender1","port_gender2","caterogory","length"))
        treeview.heading("#1",text="port1")
        treeview.heading("#2",text="ports2")
        treeview.heading("#3",text="port_gender1")
        treeview.heading("#4",text="port_gender2")
        treeview.heading("#5",text="caterogory")
        treeview.heading("#6",text="length")
        h.config(command=treeview.xview)
        treeview.pack()
        for row in data["adapter"]:
            treeview.insert("","end",values=(row["port1"],row["ports2"],row["port_gender1"],row["port_gender2"],row["caterogory"],row["length"]))
        f.close
    if do == "pc":
        f = open(jsof)
        data = json.load(f)
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("cpu_model","cpu_core","igpu","ram","ram_slots","ddr","sata","max_ram","nvme","csocket","cthread","gpu_model","usb_ports","cpu_brand","cpu_chipset","gbrand","pcie_gen","cpu_clock","vram","ecc","display_ports","other_ports","hdmi_ports","serial","gmem_type","pcie16","amount"))
        treeview.heading("#1",text="cpu_model")
        treeview.heading("#2",text="cpu_core")
        treeview.heading("#3",text="igpu")
        treeview.heading("#4",text="ram")
        treeview.heading("#5",text="ram_slots")
        treeview.heading("#6",text="ddr")
        treeview.heading("#7",text="sata")
        treeview.heading("#8",text="max_ram")
        treeview.heading("#9",text="nvme")
        treeview.heading("#10",text="csocket")
        treeview.heading("#11",text="cthread")
        treeview.heading("#12",text="gpu_model")
        treeview.heading("#13",text="usb_ports")
        treeview.heading("#14",text="cpu_brand")
        treeview.heading("#15",text="cpu_chipset")
        treeview.heading("#16",text="gbrand")
        treeview.heading("#17",text="pcie_gen")
        treeview.heading("#18",text="cpu_clock")
        treeview.heading("#19",text="vram")
        treeview.heading("#19",text="ecc")
        treeview.heading("#20",text="display_ports")
        treeview.heading("#21",text="other_ports")
        treeview.heading("#22",text="hdmi_ports")
        treeview.heading("#23",text="serial")
        treeview.heading("#24",text="gmem_type")
        treeview.heading("#25",text="pcie16")
        treeview.heading("#26",text="amount")
        h.config(command=treeview.xview)
        treeview.pack()
        for row in data["pc"]:
            treeview.insert("","end",values=(row["cpu_model"],row["cpu_core"],row["igpu"],row["ram"],row["ram_slots"],row["ddr"],row["sata"],row["max_ram"],row["nvme"],row["csocket"],row["cthread"],row["gpu_model"],row["usb_ports"],row["cpu_brand"],row["cpu_chipset"],row["gbrand"],row["pcie_gen"],row["cpu_clock"],row["vram"],row["ecc"],row["display_ports"],row["other_ports"],row["hdmi_ports"],row["serial"],row["gmem_type"],row["pcie16"],row["amount"]))
        f.close()
    if do == "games":
        # print(pd.read_json('games.json'))
        f = open(jsof)
        data = json.load(f)
        treeview=ttk.Treeview(right_pane,columns=("name","platform","studio","online"))
        treeview.heading("#1",text="name")
        treeview.heading("#2",text="platform")
        treeview.heading("#3",text="studio")
        treeview.heading("#4",text="online")
        treeview.pack()
        for row in data["game"]:
            treeview.insert("", "end", values=(row["name"], row["platform"], row["studio"], row["online"]))
        f.close()
    if do == "books":
        f = open(jsof)
        data = json.load(f)
        treeview=ttk.Treeview(right_pane,columns=("name","author","date","online"))
        treeview.heading("#1",text="name")
        treeview.heading("#2",text="author")
        treeview.heading("#3",text="date")
        treeview.heading("#4",text="online")
        treeview.pack()
        for row in data["book"]:
            treeview.insert("", "end", values=(row["name"], row["author"], row["date"], row["online"]))
        f.close()
listtree.bind('<Double-1>', go)
listtree.pack()
# catwin=tk.
window.mainloop()
# todo
"""
networking
tools

"""
