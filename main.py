#!/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import json
import re
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
def delwin():
    result= messagebox.askquestion("askquestion", "Are you sure? this will delete it")
    print(result)
    if result == "yes":
        rowe=treeview.index(treeview.focus())
        print(rowe)
        with open(jsof,'r+') as file:
            file_data = json.load(file)
            del file_data[edin][rowe]
            with open(jsof, 'w') as outfile:
                json.dump(file_data, outfile)
            print(file_data)

tbutton3=tk.Button(toolbar,command=delwin, text="x")
tbutton3.pack( side = tk.RIGHT)

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,indent=0,separators=(',', ':'))
def editWin():
    editWin = tk.Toplevel(window)

    # sets the title of the
    # Toplevel widget
    editWin.title("New Window")

    # sets the geometry of toplevel
    editWin.geometry("200x200")
    editWin.configure(background="black")
    # Function to convert
    # res=str(ref).translate({ ord(c): None for c in "[]'" })
    # Grab record number
    selected = treeview.focus()
    # Grab record values
    values = treeview.item(selected, 'values')
    # Select Record
    add_frame = tk.Frame(editWin)
    add_frame.pack(pady=20)
    if edin == "laptop":
        brandl=tk.Label(add_frame,text="brand")
        brandl.grid(row=0,column=0)
        modell=tk.Label(add_frame,text="model")
        modell.grid(row=0,column=1)
        cpu_corel=tk.Label(add_frame,text="cpu core")
        cpu_corel.grid(row=0,column=2)
        seriesl=tk.Label(add_frame,text="series")
        seriesl.grid(row=0,column=3)
        cpu_modell=tk.Label(add_frame,text="cpu model")
        cpu_modell.grid(row=0,column=4)
        ram_slotsl=tk.Label(add_frame,text="ram slots")
        ram_slotsl.grid(row=0,column=5)
        raml=tk.Label(add_frame,text="ram")
        raml.grid(row=0,column=6)
        nvmel=tk.Label(add_frame,text="nvme")
        nvmel.grid(row=0,column=7)
        ssdl=tk.Label(add_frame,text="ssd")
        ssdl.grid(row=0,column=8)
        cpu_freql=tk.Label(add_frame,text="cpu freq")
        cpu_freql.grid(row=0,column=9)
        ram_typel=tk.Label(add_frame,text="ram type")
        ram_typel.grid(row=0,column=10)
        gpul=tk.Label(add_frame,text="gpu")
        gpul.grid(row=2,column=0)
        igpul=tk.Label(add_frame,text="igpu")
        igpul.grid(row=2,column=1)
        gpu_vraml=tk.Label(add_frame,text="gpu vram")
        gpu_vraml.grid(row=2,column=2)
        igpu_vraml=tk.Label(add_frame,text="igpu vram")
        igpu_vraml.grid(row=2,column=3)
        hddl=tk.Label(add_frame,text="hdd")
        hddl.grid(row=2,column=4)
        max_raml=tk.Label(add_frame,text="max ram")
        max_raml.grid(row=2,column=5)
        cthreadl=tk.Label(add_frame,text="cthread")
        cthreadl.grid(row=2,column=6)
        cbrandl=tk.Label(add_frame,text="cbrand")
        cbrandl.grid(row=2,column=7)
        usbl=tk.Label(add_frame,text="usb")
        usbl.grid(row=2,column=8)
        videol=tk.Label(add_frame,text="video")
        videol.grid(row=2,column=9)
        audiol=tk.Label(add_frame,text="audio")
        audiol.grid(row=2,column=10)
        ethernetl=tk.Label(add_frame,text="ethernet")
        ethernetl.grid(row=4,column=0)
        battry_wattl=tk.Label(add_frame,text="battry watt")
        battry_wattl.grid(row=4,column=1)
        thunderboltl=tk.Label(add_frame,text="thunderbolt")
        thunderboltl.grid(row=4,column=2)
        charger_portl=tk.Label(add_frame,text="charger port")
        charger_portl.grid(row=4,column=3)
        resolutionl=tk.Label(add_frame,text="resolution")
        resolutionl.grid(row=4,column=4)
        screen_sizel=tk.Label(add_frame,text="screen size")
        screen_sizel.grid(row=4,column=5)
        touchscreenl=tk.Label(add_frame,text="touchscreen")
        touchscreenl.grid(row=4,column=6)
        dp_typel=tk.Label(add_frame,text="dp type")
        dp_typel.grid(row=4,column=7)
        panell=tk.Label(add_frame,text="panel")
        panell.grid(row=4,column=8)
        wifi_genl=tk.Label(add_frame,text="wifi gen")
        wifi_genl.grid(row=4,column=9)
        dvdl=tk.Label(add_frame,text="dvd")
        dvdl.grid(row=4,column=10)
        bluetoothl=tk.Label(add_frame,text="bluetooth")
        bluetoothl.grid(row=6,column=0)
        numpadl=tk.Label(add_frame,text="numpad")
        numpadl.grid(row=6,column=1)
        webcaml=tk.Label(add_frame,text="webcam")
        webcaml.grid(row=6,column=2)
        micl=tk.Label(add_frame,text="mic")
        micl.grid(row=6,column=3)
        keyboardl=tk.Label(add_frame,text="keyboard")
        keyboardl.grid(row=6,column=4)
        sodimml=tk.Label(add_frame,text="sodimm")
        sodimml.grid(row=6,column=5)
        card_readerl=tk.Label(add_frame,text="card reader")
        card_readerl.grid(row=6,column=6)
        led_keybl=tk.Label(add_frame,text="led keyb")
        led_keybl.grid(row=6,column=7)

        brand_box=tk.Entry(add_frame)
        brand_box.grid(row=1,column=0)
        model_box=tk.Entry(add_frame)
        model_box.grid(row=1,column=1)
        cpu_core_box=tk.Entry(add_frame)
        cpu_core_box.grid(row=1,column=2)
        series_box=tk.Entry(add_frame)
        series_box.grid(row=1,column=3)
        cpu_model_box=tk.Entry(add_frame)
        cpu_model_box.grid(row=1,column=4)
        ram_slots_box=tk.Entry(add_frame)
        ram_slots_box.grid(row=1,column=5)
        ram_box=tk.Entry(add_frame)
        ram_box.grid(row=1,column=6)
        nvme_box=tk.Entry(add_frame)
        nvme_box.grid(row=1,column=7)
        ssd_box=tk.Entry(add_frame)
        ssd_box.grid(row=1,column=8)
        cpu_freq_box=tk.Entry(add_frame)
        cpu_freq_box.grid(row=1,column=9)
        ram_type_box=tk.Entry(add_frame)
        ram_type_box.grid(row=1,column=10)
        gpu_box=tk.Entry(add_frame)
        gpu_box.grid(row=3,column=0)
        igpu_box=tk.Entry(add_frame)
        igpu_box.grid(row=3,column=1)
        gpu_vram_box=tk.Entry(add_frame)
        gpu_vram_box.grid(row=3,column=2)
        igpu_vram_box=tk.Entry(add_frame)
        igpu_vram_box.grid(row=3,column=3)
        hdd_box=tk.Entry(add_frame)
        hdd_box.grid(row=3,column=4)
        max_ram_box=tk.Entry(add_frame)
        max_ram_box.grid(row=3,column=5)
        cthread_box=tk.Entry(add_frame)
        cthread_box.grid(row=3,column=6)
        cbrand_box=tk.Entry(add_frame)
        cbrand_box.grid(row=3,column=7)
        usb_box=tk.Entry(add_frame)
        usb_box.grid(row=3,column=8)
        video_box=tk.Entry(add_frame)
        video_box.grid(row=3,column=9)
        audio_box=tk.Entry(add_frame)
        audio_box.grid(row=3,column=10)
        ethernet_box=tk.Entry(add_frame)
        ethernet_box.grid(row=5,column=0)
        battry_watt_box=tk.Entry(add_frame)
        battry_watt_box.grid(row=5,column=1)
        thunderbolt_box=tk.Entry(add_frame)
        thunderbolt_box.grid(row=5,column=2)
        charger_port_box=tk.Entry(add_frame)
        charger_port_box.grid(row=5,column=3)
        resolution_box=tk.Entry(add_frame)
        resolution_box.grid(row=5,column=4)
        screen_size_box=tk.Entry(add_frame)
        screen_size_box.grid(row=5,column=5)
        touchscreen_box=tk.Entry(add_frame)
        touchscreen_box.grid(row=5,column=6)
        dp_type_box=tk.Entry(add_frame)
        dp_type_box.grid(row=5,column=7)
        panel_box=tk.Entry(add_frame)
        panel_box.grid(row=5,column=8)
        wifi_gen_box=tk.Entry(add_frame)
        wifi_gen_box.grid(row=5,column=9)
        dvd_box=tk.Entry(add_frame)
        dvd_box.grid(row=5,column=10)
        bluetooth_box=tk.Entry(add_frame)
        bluetooth_box.grid(row=7,column=0)
        numpad_box=tk.Entry(add_frame)
        numpad_box.grid(row=7,column=1)
        webcam_box=tk.Entry(add_frame)
        webcam_box.grid(row=7,column=2)
        mic_box=tk.Entry(add_frame)
        mic_box.grid(row=7,column=3)
        keyboard_box=tk.Entry(add_frame)
        keyboard_box.grid(row=7,column=4)
        sodimm_box=tk.Entry(add_frame)
        sodimm_box.grid(row=7,column=5)
        card_reader_box=tk.Entry(add_frame)
        card_reader_box.grid(row=7,column=6)
        led_keyb_box=tk.Entry(add_frame)
        led_keyb_box.grid(row=7,column=7)


        brand_box.insert(0,values[0])
        model_box.insert(0,values[1])
        cpu_core_box.insert(0,values[2])
        series_box.insert(0,values[3])
        cpu_model_box.insert(0,values[4])
        ram_slots_box.insert(0,values[5])
        ram_box.insert(0,values[6])
        nvme_box.insert(0,values[7])
        ssd_box.insert(0,values[8])
        cpu_freq_box.insert(0,values[9])
        ram_type_box.insert(0,values[10])
        gpu_box.insert(0,values[11])
        igpu_box.insert(0,values[12])
        gpu_vram_box.insert(0,values[13])
        igpu_vram_box.insert(0,values[14])
        hdd_box.insert(0,values[15])
        max_ram_box.insert(0,values[16])
        cthread_box.insert(0,values[17])
        cbrand_box.insert(0,values[18])
        usb_box.insert(0,values[19])
        video_box.insert(0,values[20])
        audio_box.insert(0,values[21])
        ethernet_box.insert(0,values[22])
        battry_watt_box.insert(0,values[23])
        thunderbolt_box.insert(0,values[24])
        charger_port_box.insert(0,values[25])
        resolution_box.insert(0,values[26])
        screen_size_box.insert(0,values[27])
        touchscreen_box.insert(0,values[28])
        dp_type_box.insert(0,values[29])
        panel_box.insert(0,values[30])
        wifi_gen_box.insert(0,values[31])
        dvd_box.insert(0,values[32])
        bluetooth_box.insert(0,values[33])
        numpad_box.insert(0,values[34])
        webcam_box.insert(0,values[35])
        mic_box.insert(0,values[36])
        keyboard_box.insert(0,values[37])
        sodimm_box.insert(0,values[38])
        card_reader_box.insert(0,values[39])
        led_keyb_box.insert(0,values[40])
    if edin == "pc":
        cpu_modell=tk.Label(add_frame,text="cpu_model")
        cpu_modell.grid(row=0,column=0)
        cpu_corel=tk.Label(add_frame,text="cpu_core")
        cpu_corel.grid(row=0,column=1)
        igpul=tk.Label(add_frame,text="igpu")
        igpul.grid(row=0,column=2)
        raml=tk.Label(add_frame,text="ram")
        raml.grid(row=0,column=3)
        ram_slotsl=tk.Label(add_frame,text="ram slots")
        ram_slotsl.grid(row=0,column=4)
        ddrl=tk.Label(add_frame,text="ddr")
        ddrl.grid(row=0,column=5)
        satal=tk.Label(add_frame,text="sata")
        satal.grid(row=0,column=6)
        max_raml=tk.Label(add_frame,text="max ram")
        max_raml.grid(row=0,column=7)
        nvmel=tk.Label(add_frame,text="nvme")
        nvmel.grid(row=0,column=8)
        csocketl=tk.Label(add_frame,text="csocket")
        csocketl.grid(row=0,column=9)
        cthreadl=tk.Label(add_frame,text="cthread")
        cthreadl.grid(row=0,column=10)
        gpu_modell=tk.Label(add_frame,text="gpu model")
        gpu_modell.grid(row=2,column=0)
        usb_portsl=tk.Label(add_frame,text="usb ports")
        usb_portsl.grid(row=2,column=1)
        cpu_brandl=tk.Label(add_frame,text="cpu brand")
        cpu_brandl.grid(row=2,column=2)
        cpu_chipsetl=tk.Label(add_frame,text="cpu chipset")
        cpu_chipsetl.grid(row=2,column=3)
        gbrandl=tk.Label(add_frame,text="gbrand")
        gbrandl.grid(row=2,column=4)
        pcie_genl=tk.Label(add_frame,text="pcie gen")
        pcie_genl.grid(row=2,column=5)
        cpu_clockl=tk.Label(add_frame,text="cpu clock")
        cpu_clockl.grid(row=2,column=6)
        vraml=tk.Label(add_frame,text="vram")
        vraml.grid(row=2,column=7)
        eccl=tk.Label(add_frame,text="ecc")
        eccl.grid(row=2,column=8)
        display_portsl=tk.Label(add_frame,text="display_ports")
        display_portsl.grid(row=2,column=9)
        other_portsl=tk.Label(add_frame,text="other ports")
        other_portsl.grid(row=2,column=10)
        hdmi_portsl=tk.Label(add_frame,text="hdmi ports")
        hdmi_portsl.grid(row=4,column=0)
        seriall=tk.Label(add_frame,text="serial")
        seriall.grid(row=4,column=1)
        gmem_typel=tk.Label(add_frame,text="gmem type")
        gmem_typel.grid(row=4,column=2)
        pcie16l=tk.Label(add_frame,text="pcie16")
        pcie16l.grid(row=4,column=3)
        amountl=tk.Label(add_frame,text="amount")
        amountl.grid(row=4,column=4)

        cpu_model_box=tk.Entry(add_frame)
        cpu_model_box.grid(row=1,column=0)
        cpu_core_box=tk.Entry(add_frame)
        cpu_core_box.grid(row=1,column=1)
        igpu_box=tk.Entry(add_frame)
        igpu_box.grid(row=1,column=2)
        ram_box=tk.Entry(add_frame)
        ram_box.grid(row=1,column=3)
        ram_slots_box=tk.Entry(add_frame)
        ram_slots_box.grid(row=1,column=4)
        ddr_box=tk.Entry(add_frame)
        ddr_box.grid(row=1,column=5)
        sata_box=tk.Entry(add_frame)
        sata_box.grid(row=1,column=6)
        max_ram_box=tk.Entry(add_frame)
        max_ram_box.grid(row=1,column=7)
        nvme_box=tk.Entry(add_frame)
        nvme_box.grid(row=1,column=8)
        csocket_box=tk.Entry(add_frame)
        csocket_box.grid(row=1,column=9)
        cthread_box=tk.Entry(add_frame)
        cthread_box.grid(row=1,column=10)
        gpu_model_box=tk.Entry(add_frame)
        gpu_model_box.grid(row=3,column=0)
        usb_ports_box=tk.Entry(add_frame)
        usb_ports_box.grid(row=3,column=1)
        cpu_brand_box=tk.Entry(add_frame)
        cpu_brand_box.grid(row=3,column=2)
        cpu_chipset_box=tk.Entry(add_frame)
        cpu_chipset_box.grid(row=3,column=3)
        gbrand_box=tk.Entry(add_frame)
        gbrand_box.grid(row=3,column=4)
        pcie_gen_box=tk.Entry(add_frame)
        pcie_gen_box.grid(row=3,column=5)
        cpu_clock_box=tk.Entry(add_frame)
        cpu_clock_box.grid(row=3,column=6)
        vram_box=tk.Entry(add_frame)
        vram_box.grid(row=3,column=7)
        ecc_box=tk.Entry(add_frame)
        ecc_box.grid(row=3,column=8)
        display_ports_box=tk.Entry(add_frame)
        display_ports_box.grid(row=3,column=9)
        other_ports_box=tk.Entry(add_frame)
        other_ports_box.grid(row=3,column=10)
        hdmi_ports_box=tk.Entry(add_frame)
        hdmi_ports_box.grid(row=5,column=0)
        serial_box=tk.Entry(add_frame)
        serial_box.grid(row=5,column=1)
        gmem_type_box=tk.Entry(add_frame)
        gmem_type_box.grid(row=5,column=2)
        pcie16_box=tk.Entry(add_frame)
        pcie16_box.grid(row=5,column=3)
        amount_box=tk.Entry(add_frame)
        amount_box.grid(row=5,column=4)

        cpu_model_box.insert(0,values[0])
        cpu_core_box.insert(0,values[1])
        igpu_box.insert(0,values[2])
        ram_box.insert(0,values[3])
        ram_slots_box.insert(0,values[4])
        ddr_box.insert(0,values[5])
        sata_box.insert(0,values[6])
        max_ram_box.insert(0,values[7])
        nvme_box.insert(0,values[8])
        csocket_box.insert(0,values[9])
        cthread_box.insert(0,values[10])
        gpu_model_box.insert(0,values[11])
        usb_ports_box.insert(0,values[12])
        cpu_brand_box.insert(0,values[13])
        cpu_chipset_box.insert(0,values[14])
        gbrand_box.insert(0,values[15])
        pcie_gen_box.insert(0,values[16])
        cpu_clock_box.insert(0,values[17])
        vram_box.insert(0,values[18])
        ecc_box.insert(0,values[19])
        display_ports_box.insert(0,values[20])
        other_ports_box.insert(0,values[21])
        hdmi_ports_box.insert(0,values[22])
        serial_box.insert(0,values[23])
        gmem_type_box.insert(0,values[24])
        pcie16_box.insert(0,values[25])
        amount_box.insert(0,values[26])
    if edin == "motherboard":
        namel=tk.Label(add_frame,text="name")
        namel.grid(row=0,column=0)
        modell=tk.Label(add_frame,text="model")
        modell.grid(row=0,column=1)
        cpu_socketl=tk.Label(add_frame,text="cpu socket")
        cpu_socketl.grid(row=0,column=2)
        chipsetl=tk.Label(add_frame,text="chipset")
        chipsetl.grid(row=0,column=3)
        satal=tk.Label(add_frame,text="sata")
        satal.grid(row=0,column=4)
        ddrl=tk.Label(add_frame,text="ddr")
        ddrl.grid(row=0,column=5)
        usbcl=tk.Label(add_frame,text="usbc")
        usbcl.grid(row=0,column=6)
        usbl=tk.Label(add_frame,text="usb")
        usbl.grid(row=0,column=7)
        portsl=tk.Label(add_frame,text="ports")
        portsl.grid(row=0,column=8)
        form_factorl=tk.Label(add_frame,text="form factor")
        form_factorl.grid(row=0,column=9)
        brandl=tk.Label(add_frame,text="brand")
        brandl.grid(row=0,column=10)
        max_raml=tk.Label(add_frame,text="max ram")
        max_raml.grid(row=2,column=0)
        seriesl=tk.Label(add_frame,text="series")
        seriesl.grid(row=2,column=1)
        motherboard_portsl=tk.Label(add_frame,text="motherboard ports")
        motherboard_portsl.grid(row=2,column=2)
        sodimml=tk.Label(add_frame,text="sodimm")
        sodimml.grid(row=2,column=3)
        pcie16l=tk.Label(add_frame,text="pcie16")
        pcie16l.grid(row=2,column=4)
        ram_slotsl=tk.Label(add_frame,text="ram slots")
        ram_slotsl.grid(row=2,column=5)
        nvmel=tk.Label(add_frame,text="nvme")
        nvmel.grid(row=2,column=6)
        pcie_genl=tk.Label(add_frame,text="pcie gen")
        pcie_genl.grid(row=2,column=7)
        ethernetl=tk.Label(add_frame,text="ethernet")
        ethernetl.grid(row=2,column=8)
        nvme_pciel=tk.Label(add_frame,text="nvme pcie")
        nvme_pciel.grid(row=2,column=9)
        wifil=tk.Label(add_frame,text="wifi")
        wifil.grid(row=2,column=10)
        bluetoothl=tk.Label(add_frame,text="bluetooth")
        bluetoothl.grid(row=4,column=0)
        sata_speedl=tk.Label(add_frame,text="")
        sata_speedl.grid(row=4,column=1)
        vrml=tk.Label(add_frame,text="vrm")
        vrml.grid(row=4,column=2)
        cpu_seriesl=tk.Label(add_frame,text="cpu series")
        cpu_seriesl.grid(row=4,column=3)
        graphicsl=tk.Label(add_frame,text="graphics")
        graphicsl.grid(row=4,column=4)
        iaudiol=tk.Label(add_frame,text="iaudio")
        iaudiol.grid(row=4,column=5)
        pciel=tk.Label(add_frame,text="pcie")
        pciel.grid(row=4,column=6)
        ioshieldl=tk.Label(add_frame,text="ioshield")
        ioshieldl.grid(row=4,column=7)


        name_box=tk.Entry(add_frame)
        name_box.grid(row=1,column=0)
        model_box=tk.Entry(add_frame)
        model_box.grid(row=1,column=1)
        cpu_socket_box=tk.Entry(add_frame)
        cpu_socket_box.grid(row=1,column=2)
        chipset_box=tk.Entry(add_frame)
        chipset_box.grid(row=1,column=3)
        sata_box=tk.Entry(add_frame)
        sata_box.grid(row=1,column=4)
        ddr_box=tk.Entry(add_frame)
        ddr_box.grid(row=1,column=5)
        usbc_box=tk.Entry(add_frame)
        usbc_box.grid(row=1,column=6)
        usb_box=tk.Entry(add_frame)
        usb_box.grid(row=1,column=7)
        ports_box=tk.Entry(add_frame)
        ports_box.grid(row=1,column=8)
        form_factor_box=tk.Entry(add_frame)
        form_factor_box.grid(row=1,column=9)
        brand_box=tk.Entry(add_frame)
        brand_box.grid(row=1,column=10)
        max_ram_box=tk.Entry(add_frame)
        max_ram_box.grid(row=3,column=0)
        series_box=tk.Entry(add_frame)
        series_box.grid(row=3,column=1)
        motherboard_ports_box=tk.Entry(add_frame)
        motherboard_ports_box.grid(row=3,column=2)
        sodimm_box=tk.Entry(add_frame)
        sodimm_box.grid(row=3,column=3)
        pcie16_box=tk.Entry(add_frame)
        pcie16_box.grid(row=3,column=4)
        ram_slots_box=tk.Entry(add_frame)
        ram_slots_box.grid(row=3,column=5)
        nvme_box=tk.Entry(add_frame)
        nvme_box.grid(row=3,column=6)
        pcie_gen_box=tk.Entry(add_frame)
        pcie_gen_box.grid(row=3,column=7)
        ethernet_box=tk.Entry(add_frame)
        ethernet_box.grid(row=3,column=8)
        nvme_pcie_box=tk.Entry(add_frame)
        nvme_pcie_box.grid(row=3,column=9)
        wifi_box=tk.Entry(add_frame)
        wifi_box.grid(row=3,column=10)
        bluetooth_box=tk.Entry(add_frame)
        bluetooth_box.grid(row=5,column=0)
        sata_speed_box=tk.Entry(add_frame)
        sata_speed_box.grid(row=5,column=1)
        vrm_box=tk.Entry(add_frame)
        vrm_box.grid(row=5,column=2)
        cpu_series_box=tk.Entry(add_frame)
        cpu_series_box.grid(row=5,column=3)
        graphics_box=tk.Entry(add_frame)
        graphics_box.grid(row=5,column=4)
        iaudio_box=tk.Entry(add_frame)
        iaudio_box.grid(row=5,column=5)
        pcie_box=tk.Entry(add_frame)
        pcie_box.grid(row=5,column=6)
        ioshield_box=tk.Entry(add_frame)
        ioshield_box.grid(row=5,column=7)


        name_box.insert(0,values[0])
        model_box.insert(0,values[1])
        cpu_socket_box.insert(0,values[2])
        chipset_box.insert(0,values[3])
        sata_box.insert(0,values[4])
        ddr_box.insert(0,values[5])
        usbc_box.insert(0,values[6])
        usb_box.insert(0,values[7])
        ports_box.insert(0,values[8])
        form_factor_box.insert(0,values[9])
        brand_box.insert(0,values[10])
        max_ram_box.insert(0,values[11])
        series_box.insert(0,values[12])
        motherboard_ports_box.insert(0,values[13])
        sodimm_box.insert(0,values[14])
        pcie16_box.insert(0,values[15])
        ram_slots_box.insert(0,values[16])
        nvme_box.insert(0,values[17])
        pcie_gen_box.insert(0,values[18])
        ethernet_box.insert(0,values[19])
        nvme_pcie_box.insert(0,values[20])
        wifi_box.insert(0,values[21])
        bluetooth_box.insert(0,values[22])
        sata_speed_box.insert(0,values[23])
        vrm_box.insert(0,values[24])
        cpu_series_box.insert(0,values[25])
        graphics_box.insert(0,values[26])
        iaudio_box.insert(0,values[27])
        pcie_box.insert(0,values[28])
        ioshield_box.insert(0,values[29])
    if edin == "cable":
        cable_gender=tk.Label(add_frame,text="cable gender")
        cable_gender.grid(row=0,column=0)
        cp1=tk.Label(add_frame,text="cp1")
        cp1.grid(row=0,column=1)
        cp2=tk.Label(add_frame,text="cp2")
        cp2.grid(row=0,column=2)
        cp3=tk.Label(add_frame,text="cp3")
        cp3.grid(row=0,column=3)
        caterogory=tk.Label(add_frame,text="caterogory")
        caterogory.grid(row=0,column=4)
        length=tk.Label(add_frame,text="length")
        length.grid(row=0,column=5)
        amount=tk.Label(add_frame,text="amount")
        amount.grid(row=0,column=6)

        cable_gender_box=tk.Entry(add_frame)
        cable_gender_box.grid(row=1,column=0)
        cp1_box=tk.Entry(add_frame)
        cp1_box.grid(row=1,column=1)
        cp2_box=tk.Entry(add_frame)
        cp2_box.grid(row=1,column=2)
        cp3_box=tk.Entry(add_frame)
        cp3_box.grid(row=1,column=3)
        caterogory_box=tk.Entry(add_frame)
        caterogory_box.grid(row=1,column=4)
        length_box=tk.Entry(add_frame)
        length_box.grid(row=1,column=5)
        amount_box=tk.Entry(add_frame)
        amount_box.grid(row=1,column=6)


        cable_gender_box.insert(0,values[0])
        cp1_box.insert(0,values[1])
        cp2_box.insert(0,values[2])
        cp3_box.insert(0,values[3])
        caterogory_box.insert(0,values[4])
        length_box.insert(0,values[5])
        amount_box.insert(0,values[6])
    if edin == "monitor":
        brand=tk.Label(add_frame,text="brand")
        brand.grid(row=0,column=0)
        model=tk.Label(add_frame,text="model")
        model.grid(row=0,column=1)
        screen_size=tk.Label(add_frame,text="screen size")
        screen_size.grid(row=0,column=2)
        connecters=tk.Label(add_frame,text="connecters")
        connecters.grid(row=0,column=3)
        video=tk.Label(add_frame,text="video")
        video.grid(row=0,column=4)
        usb=tk.Label(add_frame,text="usb")
        usb.grid(row=0,column=5)
        vesa=tk.Label(add_frame,text="vesa")
        vesa.grid(row=0,column=6)
        resolution=tk.Label(add_frame,text="resolution")
        resolution.grid(row=0,column=7)
        refresh_rate=tk.Label(add_frame,text="refresh rate")
        refresh_rate.grid(row=0,column=8)
        widescreen=tk.Label(add_frame,text="widescreen")
        widescreen.grid(row=0,column=9)
        glare_screen=tk.Label(add_frame,text="glare screen")
        glare_screen.grid(row=0,column=10)
        panel=tk.Label(add_frame,text="panel")
        panel.grid(row=2,column=0)
        led_backlight=tk.Label(add_frame,text="led backlight")
        led_backlight.grid(row=2,column=1)
        display_type=tk.Label(add_frame,text="display type")
        display_type.grid(row=2,column=2)
        constrast_ratio=tk.Label(add_frame,text="constrast ratio")
        constrast_ratio.grid(row=2,column=3)
        aspect_ratio=tk.Label(add_frame,text="aspect ratio")
        aspect_ratio.grid(row=2,column=4)
        response_time=tk.Label(add_frame,text="response time")
        response_time.grid(row=2,column=5)
        adaptive_sync_tech=tk.Label(add_frame,text="adaptive_sync_tech")
        adaptive_sync_tech.grid(row=2,column=6)
        input_video=tk.Label(add_frame,text="input video")
        input_video.grid(row=2,column=7)


        brand_box=tk.Entry(add_frame)
        brand_box.grid(row=1,column=0)
        model_box=tk.Entry(add_frame)
        model_box.grid(row=1,column=1)
        screen_size_box=tk.Entry(add_frame)
        screen_size_box.grid(row=1,column=2)
        connecters_box=tk.Entry(add_frame)
        connecters_box.grid(row=1,column=3)
        video_box=tk.Entry(add_frame)
        video_box.grid(row=1,column=4)
        usb_box=tk.Entry(add_frame)
        usb_box.grid(row=1,column=5)
        vesa_box=tk.Entry(add_frame)
        vesa_box.grid(row=1,column=6)
        resolution_box=tk.Entry(add_frame)
        resolution_box.grid(row=1,column=7)
        refresh_rate_box=tk.Entry(add_frame)
        refresh_rate_box.grid(row=1,column=8)
        widescreen_box=tk.Entry(add_frame)
        widescreen_box.grid(row=1,column=9)
        glare_screen_box=tk.Entry(add_frame)
        glare_screen_box.grid(row=1,column=10)
        panel_box=tk.Entry(add_frame)
        panel_box.grid(row=3,column=0)
        led_backlight_box=tk.Entry(add_frame)
        led_backlight_box.grid(row=3,column=1)
        display_type_box=tk.Entry(add_frame)
        display_type_box.grid(row=3,column=2)
        constrast_ratio_box=tk.Entry(add_frame)
        constrast_ratio_box.grid(row=3,column=3)
        aspect_ratio_box=tk.Entry(add_frame)
        aspect_ratio_box.grid(row=3,column=4)
        response_time_box=tk.Entry(add_frame)
        response_time_box.grid(row=3,column=5)
        adaptive_sync_tech_box=tk.Entry(add_frame)
        adaptive_sync_tech_box.grid(row=3,column=6)
        input_video_box=tk.Entry(add_frame)
        input_video_box.grid(row=3,column=7)

        brand_box.insert(0,values[0])
        model_box.insert(0,values[1])
        screen_size_box.insert(0,values[2])
        connecters_box.insert(0,values[3])
        video_box.insert(0,values[4])
        usb_box.insert(0,values[5])
        vesa_box.insert(0,values[6])
        resolution_box.insert(0,values[7])
        refresh_rate_box.insert(0,values[8])
        widescreen_box.insert(0,values[9])
        glare_screen_box.insert(0,values[10])
        panel_box.insert(0,values[11])
        led_backlight_box.insert(0,values[12])
        display_type_box.insert(0,values[13])
        constrast_ratio_box.insert(0,values[14])
        aspect_ratio_box.insert(0,values[15])
        response_time_box.insert(0,values[16])
        adaptive_sync_tech_box.insert(0,values[17])
        input_video_box.insert(0,values[18])
    if edin == "adapter":
        port1=tk.Label(add_frame,text="port1")
        port1.grid(row=0,column=0)
        ports2=tk.Label(add_frame,text="port2")
        ports2.grid(row=0,column=1)
        port_gender1=tk.Label(add_frame,text="port gender1")
        port_gender1.grid(row=0,column=2)
        port_gender2=tk.Label(add_frame,text="port gender2")
        port_gender2.grid(row=0,column=3)
        caterogory=tk.Label(add_frame,text="caterogory")
        caterogory.grid(row=0,column=4)
        length=tk.Label(add_frame,text="length")
        length.grid(row=0,column=5)


        port1_box=tk.Entry(add_frame)
        port1_box.grid(row=1,column=0)
        ports2_box=tk.Entry(add_frame)
        ports2_box.grid(row=1,column=1)
        port_gender1_box=tk.Entry(add_frame)
        port_gender1_box.grid(row=1,column=2)
        port_gender2_box=tk.Entry(add_frame)
        port_gender2_box.grid(row=1,column=3)
        caterogory_box=tk.Entry(add_frame)
        caterogory_box.grid(row=1,column=4)
        length_box=tk.Entry(add_frame)
        length_box.grid(row=1,column=5)


        port1_box.insert(0,values[0])
        ports2_box.insert(0,values[1])
        port_gender1_box.insert(0,values[2])
        port_gender2_box.insert(0,values[3])
        caterogory_box.insert(0,values[4])
        length_box.insert(0,values[5])
    if edin == "case":
        name=tk.Label(add_frame,text="name")
        name.grid(row=0,column=0)
        model=tk.Label(add_frame,text="model")
        model.grid(row=0,column=1)
        mobo_supp=tk.Label(add_frame,text="mobo supp")
        mobo_supp.grid(row=0,column=2)
        case_type=tk.Label(add_frame,text="case type")
        case_type.grid(row=0,column=3)
        tdrive_bays=tk.Label(add_frame,text="3.5 drivebays")
        tdrive_bays.grid(row=0,column=4)
        sdrive_bays=tk.Label(add_frame,text="2.5 drivebays")
        sdrive_bays.grid(row=0,column=5)
        pcie=tk.Label(add_frame,text="pcie")
        pcie.grid(row=0,column=6)
        ports=tk.Label(add_frame,text="ports")
        ports.grid(row=0,column=7)
        gpul=tk.Label(add_frame,text="gpu length")
        gpul.grid(row=0,column=8)
        gpuh=tk.Label(add_frame,text="gpu height")
        gpuh.grid(row=0,column=9)
        brand=tk.Label(add_frame,text="brand")
        brand.grid(row=0,column=10)
        cpuh=tk.Label(add_frame,text="cpu height")
        cpuh.grid(row=2,column=0)
        windoww=tk.Label(add_frame,text="window")
        windoww.grid(row=2,column=1)
        series=tk.Label(add_frame,text="series")
        series.grid(row=2,column=2)
        fan=tk.Label(add_frame,text="fans")
        fan.grid(row=2,column=3)
        psul=tk.Label(add_frame,text="psu length")
        psul.grid(row=2,column=4)



        name_box=tk.Entry(add_frame)
        name_box.grid(row=1,column=0)
        model_box=tk.Entry(add_frame)
        model_box.grid(row=1,column=1)
        mobo_supp_box=tk.Entry(add_frame)
        mobo_supp_box.grid(row=1,column=2)
        case_type_box=tk.Entry(add_frame)
        case_type_box.grid(row=1,column=3)
        tdrive_bays_box=tk.Entry(add_frame)
        tdrive_bays_box.grid(row=1,column=4)
        sdrive_bays_box=tk.Entry(add_frame)
        sdrive_bays_box.grid(row=1,column=5)
        pcie_box=tk.Entry(add_frame)
        pcie_box.grid(row=1,column=6)
        ports_box=tk.Entry(add_frame)
        ports_box.grid(row=1,column=7)
        gpul_box=tk.Entry(add_frame)
        gpul_box.grid(row=1,column=8)
        gpuh_box=tk.Entry(add_frame)
        gpuh_box.grid(row=1,column=9)
        brand_box=tk.Entry(add_frame)
        brand_box.grid(row=1,column=10)
        cpuh_box=tk.Entry(add_frame)
        cpuh_box.grid(row=3,column=0)
        window_box=tk.Entry(add_frame)
        window_box.grid(row=3,column=1)
        series_box=tk.Entry(add_frame)
        series_box.grid(row=3,column=2)
        fan_box=tk.Entry(add_frame)
        fan_box.grid(row=3,column=3)
        psul_box=tk.Entry(add_frame)
        psul_box.grid(row=3,column=4)


        name_box.insert(0,values[0])
        model_box.insert(0,values[1])
        mobo_supp_box.insert(0,values[2])
        case_type_box.insert(0,values[3])
        tdrive_bays_box.insert(0,values[4])
        sdrive_bays_box.insert(0,values[5])
        pcie_box.insert(0,values[6])
        ports_box.insert(0,values[7])
        gpul_box.insert(0,values[8])
        gpuh_box.insert(0,values[9])
        brand_box.insert(0,values[10])
        cpuh_box.insert(0,values[11])
        window_box.insert(0,values[12])
        series_box.insert(0,values[13])
        fan_box.insert(0,values[14])
        psul_box.insert(0,values[15])
    if edin == "cpu":
        name=tk.Label(add_frame,text="name")
        name.grid(row=0,column=0)
        core=tk.Label(add_frame,text="core")
        core.grid(row=0,column=1)
        thread=tk.Label(add_frame,text="thread")
        thread.grid(row=0,column=2)
        socket=tk.Label(add_frame,text="socket")
        socket.grid(row=0,column=3)
        model=tk.Label(add_frame,text="model")
        model.grid(row=0,column=4)
        base_freq=tk.Label(add_frame,text="base freq")
        base_freq.grid(row=0,column=5)
        turbo_freq=tk.Label(add_frame,text="turbo freq")
        turbo_freq.grid(row=0,column=6)
        igpu=tk.Label(add_frame,text="igpu")
        igpu.grid(row=0,column=7)
        brand=tk.Label(add_frame,text="brand")
        brand.grid(row=0,column=8)
        cache=tk.Label(add_frame,text="cache")
        cache.grid(row=0,column=9)
        unlocked=tk.Label(add_frame,text="unlocked")
        unlocked.grid(row=0,column=10)
        year=tk.Label(add_frame,text="year")
        year.grid(row=0,column=11)


        name_box=tk.Entry(add_frame)
        name_box.grid(row=1,column=0)
        core_box=tk.Entry(add_frame)
        core_box.grid(row=1,column=1)
        thread_box=tk.Entry(add_frame)
        thread_box.grid(row=1,column=2)
        socket_box=tk.Entry(add_frame)
        socket_box.grid(row=1,column=3)
        model_box=tk.Entry(add_frame)
        model_box.grid(row=1,column=4)
        base_freq_box=tk.Entry(add_frame)
        base_freq_box.grid(row=1,column=5)
        turbo_freq_box=tk.Entry(add_frame)
        turbo_freq_box.grid(row=1,column=6)
        igpu_box=tk.Entry(add_frame)
        igpu_box.grid(row=1,column=7)
        brand_box=tk.Entry(add_frame)
        brand_box.grid(row=1,column=8)
        cache_box=tk.Entry(add_frame)
        cache_box.grid(row=1,column=9)
        unlocked_box=tk.Entry(add_frame)
        unlocked_box.grid(row=1,column=10)
        year_box=tk.Entry(add_frame)
        year_box.grid(row=1,column=11)



        name_box.insert(0,values[0])
        core_box.insert(0,values[1])
        thread_box.insert(0,values[2])
        socket_box.insert(0,values[3])
        model_box.insert(0,values[4])
        base_freq_box.insert(0,values[5])
        turbo_freq_box.insert(0,values[6])
        igpu_box.insert(0,values[7])
        brand_box.insert(0,values[8])
        cache_box.insert(0,values[9])
        unlocked_box.insert(0,values[10])
        year_box.insert(0,values[11])
    if edin == "gpu":
        namel=tk.Label(add_frame,text="name")
        namel.grid(row=0,column=0)
        sizel=tk.Label(add_frame,text="size")
        sizel.grid(row=0,column=1)
        core_clockl=tk.Label(add_frame,text="core clock")
        core_clockl.grid(row=0,column=2)
        brandl=tk.Label(add_frame,text="brand")
        brandl.grid(row=0,column=3)
        modell=tk.Label(add_frame,text="model")
        modell.grid(row=0,column=4)
        mem_typel=tk.Label(add_frame,text="mem type")
        mem_typel.grid(row=0,column=5)
        base_brandl=tk.Label(add_frame,text="base brand")
        base_brandl.grid(row=0,column=6)
        cudal=tk.Label(add_frame,text="cuda")
        cudal.grid(row=0,column=7)
        mem_clockl=tk.Label(add_frame,text="mem clock")
        mem_clockl.grid(row=0,column=8)
        outputl=tk.Label(add_frame,text="output")
        outputl.grid(row=0,column=9)
        card_busl=tk.Label(add_frame,text="card bus")
        card_busl.grid(row=0,column=10)
        hieghtl=tk.Label(add_frame,text="height")
        hieghtl.grid(row=2,column=0)
        widthl=tk.Label(add_frame,text="width")
        widthl.grid(row=2,column=1)
        lengthl=tk.Label(add_frame,text="length")
        lengthl.grid(row=2,column=2)
        powerl=tk.Label(add_frame,text="power")
        powerl.grid(row=2,column=3)
        wattl=tk.Label(add_frame,text="watt")
        wattl.grid(row=2,column=4)

        name_box=tk.Entry(add_frame)
        name_box.grid(row=1,column=0)
        size_box=tk.Entry(add_frame)
        size_box.grid(row=1,column=1)
        core_clock_box=tk.Entry(add_frame)
        core_clock_box.grid(row=1,column=2)
        brand_box=tk.Entry(add_frame)
        brand_box.grid(row=1,column=3)
        model_box=tk.Entry(add_frame)
        model_box.grid(row=1,column=4)
        mem_type_box=tk.Entry(add_frame)
        mem_type_box.grid(row=1,column=5)
        output_box=tk.Entry(add_frame)
        output_box.grid(row=1,column=6)
        base_brand_box=tk.Entry(add_frame)
        base_brand_box.grid(row=1,column=7)
        cuda_box=tk.Entry(add_frame)
        cuda_box.grid(row=1,column=8)
        mem_clock_box=tk.Entry(add_frame)
        mem_clock_box.grid(row=1,column=9)
        card_bus_box=tk.Entry(add_frame)
        card_bus_box.grid(row=1,column=10)
        hieght_box=tk.Entry(add_frame)
        hieght_box.grid(row=3,column=0)
        width_box=tk.Entry(add_frame)
        width_box.grid(row=3,column=1)
        length_box=tk.Entry(add_frame)
        length_box.grid(row=3,column=2)
        power_box=tk.Entry(add_frame)
        power_box.grid(row=3,column=3)
        watt_box=tk.Entry(add_frame)
        watt_box.grid(row=3,column=4)


        name_box.insert(0,values[0])
        size_box.insert(0,values[1])
        core_clock_box.insert(0,values[2])
        brand_box.insert(0,values[3])
        model_box.insert(0,values[4])
        mem_type_box.insert(0,values[5])
        base_brand_box.insert(0,values[6])
        cuda_box.insert(0,values[7])
        mem_clock_box.insert(0,values[8])
        output_box.insert(0,values[9])
        card_bus_box.insert(0,values[10])
        hieght_box.insert(0,values[11])
        width_box.insert(0,values[12])
        length_box.insert(0,values[13])
        power_box.insert(0,values[14])
        watt_box.insert(0,values[15])

    if edin == "game":
        namel=tk.Label(add_frame,text="name")
        namel.grid(row=0,column=0)
        platforml=tk.Label(add_frame,text="platform")
        platforml.grid(row=0,column=1)
        studiol=tk.Label(add_frame,text="studio")
        studiol.grid(row=0,column=2)
        onlinel=tk.Label(add_frame,text="online")
        onlinel.grid(row=0,column=3)

        name_box=tk.Entry(add_frame)
        name_box.grid(row=1, column=0)
        platform_box=tk.Entry(add_frame)
        platform_box.grid(row=1, column=1)
        studio_box=tk.Entry(add_frame)
        studio_box.grid(row=1, column=2)
        online_box=tk.Entry(add_frame)
        online_box.grid(row=1, column=3)
        name_box.insert(0,values[0])
        platform_box.insert(0,values[1])
        studio_box.insert(0,values[2])
        online_box.insert(0,values[3])

    if edin == "psu":
        namel=tk.Label(add_frame,text="name")
        namel.grid(row=0,column=0)
        wattl=tk.Label(add_frame,text="watt")
        wattl.grid(row=0,column=1)
        ratingl=tk.Label(add_frame,text="rating")
        ratingl.grid(row=0,column=2)
        brandl=tk.Label(add_frame,text="brand")
        brandl.grid(row=0,column=3)
        modell=tk.Label(add_frame,text="model")
        modell.grid(row=0,column=4)
        moduarl=tk.Label(add_frame,text="moduar")
        moduarl.grid(row=0,column=5)
        typel=tk.Label(add_frame,text="type")
        typel.grid(row=0,column=6)
        connectersl=tk.Label(add_frame,text="connecters")
        connectersl.grid(row=0,column=7)
        max_psu_ll=tk.Label(add_frame,text="max_psu_l")
        max_psu_ll.grid(row=0,column=8)

        name_box=tk.Entry(add_frame)
        name_box.grid(row=1,column=0)
        watt_box=tk.Entry(add_frame)
        watt_box.grid(row=1,column=1)
        rating_box=tk.Entry(add_frame)
        rating_box.grid(row=1,column=2)
        brand_box=tk.Entry(add_frame)
        brand_box.grid(row=1,column=3)
        model_box=tk.Entry(add_frame)
        model_box.grid(row=1,column=4)
        moduar_box=tk.Entry(add_frame)
        moduar_box.grid(row=1,column=5)
        type_box=tk.Entry(add_frame)
        type_box.grid(row=1,column=6)
        connecters_box=tk.Entry(add_frame)
        connecters_box.grid(row=1,column=7)
        max_psu_l_box=tk.Entry(add_frame)
        max_psu_l_box.grid(row=1,column=8)

        name_box.insert(0,values[0])
        watt_box.insert(0,values[1])
        rating_box.insert(0,values[2])
        brand_box.insert(0,values[3])
        model_box.insert(0,values[4])
        moduar_box.insert(0,values[5])
        type_box.insert(0,values[6])
        connecters_box.insert(0,values[7])
        max_psu_l_box.insert(0,values[8])

    if edin == "ram":
        namel=tk.Label(add_frame,text="name")
        namel.grid(row=0,column=0)
        cap_totall=tk.Label(add_frame,text="cap_total")
        cap_totall.grid(row=0,column=1)
        cap_perl=tk.Label(add_frame,text="cap_per")
        cap_perl.grid(row=0,column=2)
        ddrl=tk.Label(add_frame,text="ddr")
        ddrl.grid(row=0,column=3)
        dimml=tk.Label(add_frame,text="dimm")
        dimml.grid(row=0,column=4)
        modell=tk.Label(add_frame,text="model")
        modell.grid(row=0,column=5)
        speedl=tk.Label(add_frame,text="speed")
        speedl.grid(row=0,column=6)
        brandl=tk.Label(add_frame,text="brand")
        brandl.grid(row=0,column=7)
        forml=tk.Label(add_frame,text="form")
        forml.grid(row=0,column=8)

        name_box=tk.Entry(add_frame)
        name_box.grid(row=1,column=0)
        cap_total_box=tk.Entry(add_frame)
        cap_total_box.grid(row=1,column=1)
        cap_per_box=tk.Entry(add_frame)
        cap_per_box.grid(row=1,column=2)
        ddr_box=tk.Entry(add_frame)
        ddr_box.grid(row=1,column=3)
        dimm_box=tk.Entry(add_frame)
        dimm_box.grid(row=1,column=4)
        model_box=tk.Entry(add_frame)
        model_box.grid(row=1,column=5)
        speed_box=tk.Entry(add_frame)
        speed_box.grid(row=1,column=6)
        brand_box=tk.Entry(add_frame)
        brand_box.grid(row=1,column=7)
        form_box=tk.Entry(add_frame)
        form_box.grid(row=1,column=8)

        name_box.insert(0,values[0])
        cap_total_box.insert(0,values[1])
        cap_per_box.insert(0,values[2])
        ddr_box.insert(0,values[3])
        dimm_box.insert(0,values[4])
        model_box.insert(0,values[5])
        speed_box.insert(0,values[6])
        brand_box.insert(0,values[7])
        form_box.insert(0,values[8])
    if edin == "storage":
        namel=tk.Label(add_frame,text="name")
        namel.grid(row=0,column=0)
        brandl=tk.Label(add_frame,text="brand")
        brandl.grid(row=0,column=1)
        sizel=tk.Label(add_frame,text="size")
        sizel.grid(row=0,column=2)
        typel=tk.Label(add_frame,text="type")
        typel.grid(row=0,column=3)
        forml=tk.Label(add_frame,text="form")
        forml.grid(row=0,column=4)
        interfacel=tk.Label(add_frame,text="interface")
        interfacel.grid(row=0,column=5)
        internall=tk.Label(add_frame,text="internal")
        internall.grid(row=0,column=6)
        modell=tk.Label(add_frame,text="model")
        modell.grid(row=0,column=7)
        rpml=tk.Label(add_frame,text="rpm")
        rpml.grid(row=0,column=8)
        readl=tk.Label(add_frame,text="read")
        readl.grid(row=0,column=9)
        writel=tk.Label(add_frame,text="write")
        writel.grid(row=0,column=10)


        name_box=tk.Entry(add_frame)
        name_box.grid(row=1,column=0)
        brand_box=tk.Entry(add_frame)
        brand_box.grid(row=1,column=1)
        size_box=tk.Entry(add_frame)
        size_box.grid(row=1,column=2)
        type_box=tk.Entry(add_frame)
        type_box.grid(row=1,column=3)
        form_box=tk.Entry(add_frame)
        form_box.grid(row=1,column=4)
        interface_box=tk.Entry(add_frame)
        interface_box.grid(row=1,column=5)
        internal_box=tk.Entry(add_frame)
        internal_box.grid(row=1,column=6)
        model_box=tk.Entry(add_frame)
        model_box.grid(row=1,column=7)
        rpm_box=tk.Entry(add_frame)
        rpm_box.grid(row=1,column=8)
        read_box=tk.Entry(add_frame)
        read_box.grid(row=1,column=9)
        write_box=tk.Entry(add_frame)
        write_box.grid(row=1,column=10)


        name_box.insert(0,values[0])
        brand_box.insert(0,values[1])
        size_box.insert(0,values[2])
        type_box.insert(0,values[3])
        form_box.insert(0,values[4])
        interface_box.insert(0,values[5])
        internal_box.insert(0,values[6])
        model_box.insert(0,values[7])
        rpm_box.insert(0,values[8])
        read_box.insert(0,values[9])
        write_box.insert(0,values[10])

    if edin == "book":
        namel=tk.Label(add_frame,text="name")
        namel.grid(row=0, column=0)
        authorl=tk.Label(add_frame,text="author")
        authorl.grid(row=0, column=1)
        datel=tk.Label(add_frame,text="date")
        datel.grid(row=0, column=2)
        onlinel=tk.Label(add_frame,text="online")
        onlinel.grid(row=0, column=3)

        name_box=tk.Entry(add_frame)
        name_box.grid(row=1, column=0)
        author_box=tk.Entry(add_frame)
        author_box.grid(row=1, column=1)
        date_box=tk.Entry(add_frame)
        date_box.grid(row=1, column=2)
        online_box=tk.Entry(add_frame)
        online_box.grid(row=1, column=3)
        name_box.insert(0,values[0])
        author_box.insert(0,values[1])
        date_box.insert(0,values[2])
        online_box.insert(0,values[3])

    def update_record():
        selected=treeview.focus()
        rowr=treeview.index(selected)
        if edin == "pc":
            treeview.item(selected,text="",values=(cpu_model_box.get(),cpu_core_box.get(),igpu_box.get(),ram_box.get(),ram_slots_box.get(),ddr_box.get(),sata_box.get(),max_ram_box.get(),nvme_box.get(),csocket_box.get(),cthread_box.get(),gpu_model_box.get(),usb_ports_box.get(),cpu_brand_box.get(),cpu_chipset_box.get(),gbrand_box.get(),pcie_gen_box.get(),cpu_clock_box.get(),vram_box.get(),ecc_box.get(),display_ports_box.get(),other_ports_box.get(),hdmi_ports_box.get(),serial_box.get(),gmem_type_box.get(),pcie16_box.get(),amount_box.get()))
            row = treeview.item(selected)["values"]
            print(row[0])
            with open(jsof,'r+') as file:
                    # First we load existing data into a dict.
                file_data = json.load(file)
                file_data['pc'][rowr]['cpu_model'] = row[0]
                file_data['pc'][rowr]['cpu_core'] = row[0]
                file_data['pc'][rowr]['igpu'] = row[0]
                file_data['pc'][rowr]['ram'] = row[0]
                file_data['pc'][rowr]['ram_slots'] = row[0]
                file_data['pc'][rowr]['ddr'] = row[0]
                file_data['pc'][rowr]['sata'] = row[0]
                file_data['pc'][rowr]['max_ram'] = row[0]
                file_data['pc'][rowr]['nvme'] = row[0]
                file_data['pc'][rowr]['csocket'] = row[0]
                file_data['pc'][rowr]['cthread'] = row[0]
                file_data['pc'][rowr]['gpu_model'] = row[0]
                file_data['pc'][rowr]['usb_ports'] = row[0]
                file_data['pc'][rowr]['cpu_brand'] = row[0]
                file_data['pc'][rowr]['cpu_chipset'] = row[0]
                file_data['pc'][rowr]['gbrand'] = row[0]
                file_data['pc'][rowr]['pcie_gen'] = row[0]
                file_data['pc'][rowr]['cpu_clock'] = row[0]
                file_data['pc'][rowr]['vram'] = row[0]
                file_data['pc'][rowr]['ecc'] = row[0]
                file_data['pc'][rowr]['display_ports'] = row[0]
                file_data['pc'][rowr]['other_ports'] = row[0]
                file_data['pc'][rowr]['hdmi_ports'] = row[0]
                file_data['pc'][rowr]['serial'] = row[0]
                file_data['pc'][rowr]['gmem_type'] = row[0]
                file_data['pc'][rowr]['pcie16'] = row[0]
                file_data['pc'][rowr]['amount'] = row[0]


                file.seek(0)
                print("game")
                # convert back to json.
                print(json.dumps(file_data))
                # json.dump(file_data, file)
                with open(jsof, 'w') as outfile:
                    json.dump(file_data, outfile)
        if edin == "laptop":
            treeview.item(selected,text="",values=(brand_box.get(),model_box.get(),cpu_core_box.get(),series_box.get(),cpu_model_box.get(),ram_slots_box.get(),ram_box.get(),nvme_box.get(),ssd_box.get(),cpu_freq_box.get(),ram_type_box.get(),gpu_box.get(),igpu_box.get(),gpu_vram_box.get(),igpu_vram_box.get(),hdd_box.get(),max_ram_box.get(),cthread_box.get(),cbrand_box.get(),usb_box.get(),video_box.get(),audio_box.get(),ethernet_box.get(),battry_watt_box.get(),thunderbolt_box.get(),charger_port_box.get(),resolution_box.get(),screen_size_box.get(),touchscreen_box.get(),dp_type_box.get(),panel_box.get(),wifi_gen_box.get(),dvd_box.get(),bluetooth_box.get(),numpad_box.get(),webcam_box.get(),mic_box.get(),keyboard_box.get(),sodimm_box.get(),card_reader_box.get(),led_keyb_box.get()))
            row = treeview.item(selected)["values"]
            print(row[0])
            with open(jsof,'r+') as file:
                    # First we load existing data into a dict.
                file_data = json.load(file)
                file_data['laptop'][rowr]['brand'] = row[0]
                file_data['laptop'][rowr]['model'] = row[1]
                file_data['laptop'][rowr]['cpu_core'] = row[2]
                file_data['laptop'][rowr]['series'] = row[3]
                file_data['laptop'][rowr]['cpu_model'] = row[4]
                file_data['laptop'][rowr]['ram_slots'] = row[5]
                file_data['laptop'][rowr]['ram'] = row[6]
                file_data['laptop'][rowr]['nvme'] = row[7]
                file_data['laptop'][rowr]['ssd'] = row[8]
                file_data['laptop'][rowr]['cpu_freq'] = row[9]
                file_data['laptop'][rowr]['ram_type'] = row[10]
                file_data['laptop'][rowr]['gpu'] = row[11]
                file_data['laptop'][rowr]['igpu'] = row[12]
                file_data['laptop'][rowr]['gpu_vram'] = row[13]
                file_data['laptop'][rowr]['igpu_vram'] = row[14]
                file_data['laptop'][rowr]['hdd'] = row[15]
                file_data['laptop'][rowr]['max_ram'] = row[16]
                file_data['laptop'][rowr]['cthread'] = row[17]
                file_data['laptop'][rowr]['cbrand'] = row[18]
                file_data['laptop'][rowr]['usb'] = row[19]
                file_data['laptop'][rowr]['video'] = row[20]
                file_data['laptop'][rowr]['audio'] = row[21]
                file_data['laptop'][rowr]['ethernet'] = row[22]
                file_data['laptop'][rowr]['battry_watt'] = row[23]
                file_data['laptop'][rowr]['thunderbolt'] = row[24]
                file_data['laptop'][rowr]['charger_port'] = row[25]
                file_data['laptop'][rowr]['resolution'] = row[26]
                file_data['laptop'][rowr]['screen_size'] = row[27]
                file_data['laptop'][rowr]['touchscreen'] = row[28]
                file_data['laptop'][rowr]['dp_type'] = row[29]
                file_data['laptop'][rowr]['panel'] = row[30]
                file_data['laptop'][rowr]['wifi_gen'] = row[31]
                file_data['laptop'][rowr]['dvd'] = row[32]
                file_data['laptop'][rowr]['bluetooth'] = row[33]
                file_data['laptop'][rowr]['numpad'] = row[34]
                file_data['laptop'][rowr]['webcam'] = row[35]
                file_data['laptop'][rowr]['mic'] = row[36]
                file_data['laptop'][rowr]['keyboard'] = row[37]
                file_data['laptop'][rowr]['sodimm'] = row[38]
                file_data['laptop'][rowr]['card_reader'] = row[39]
                file_data['laptop'][rowr]['led_keyb'] = row[40]

                file.seek(0)
                print("game")
                # convert back to json.
                print(json.dumps(file_data))
                # json.dump(file_data, file)
                with open(jsof, 'w') as outfile:
                    json.dump(file_data, outfile)
        if edin == "storage":
            treeview.item(selected,text="",values=(name_box.get(),brand_box.get(),size_box.get(),type_box.get(),form_box.get(),interface_box.get(),internal_box.get(),model_box.get(),rpm_box.get(),read_box.get(),write_box.get()))
            row = treeview.item(selected)["values"]
            print(row[0])
            with open(jsof,'r+') as file:
                    # First we load existing data into a dict.
                file_data = json.load(file)
                file_data['storage'][rowr]['name'] = row[0]
                file_data['storage'][rowr]['brand'] = row[1]
                file_data['storage'][rowr]['size'] = row[2]
                file_data['storage'][rowr]['type'] = row[3]
                file_data['storage'][rowr]['form'] = row[4]
                file_data['storage'][rowr]['interface'] = row[5]
                file_data['storage'][rowr]['internal'] = row[6]
                file_data['storage'][rowr]['model'] = row[7]
                file_data['storage'][rowr]['rpm'] = row[8]
                file_data['storage'][rowr]['read'] = row[9]
                file_data['storage'][rowr]['write'] = row[10]

                file.seek(0)
                print("game")
                # convert back to json.
                print(json.dumps(file_data))
                # json.dump(file_data, file)
                with open(jsof, 'w') as outfile:
                    json.dump(file_data, outfile)
        if edin == "ram":
            treeview.item(selected,text="",values=(name_box.get(),cap_total_box.get(),cap_per_box.get(),ddr_box.get(),dimm_box.get(),model_box.get(),speed_box.get(),brand_box.get(),form_box.get()))
            row = treeview.item(selected)["values"]
            print(row[0])
            with open(jsof,'r+') as file:
                    # First we load existing data into a dict.
                file_data = json.load(file)
                file_data['ram'][rowr]['name'] = row[0]
                file_data['ram'][rowr]['cap_total'] = row[1]
                file_data['ram'][rowr]['cap_per'] = row[2]
                file_data['ram'][rowr]['ddr'] = row[3]
                file_data['ram'][rowr]['dimm'] = row[4]
                file_data['ram'][rowr]['model'] = row[5]
                file_data['ram'][rowr]['speed'] = row[6]
                file_data['ram'][rowr]['brand'] = row[7]
                file_data['ram'][rowr]['form'] = row[8]


                file.seek(0)
                print("game")
                # convert back to json.
                print(json.dumps(file_data))
                # json.dump(file_data, file)
                with open(jsof, 'w') as outfile:
                    json.dump(file_data, outfile)
        if edin == "psu":
            treeview.item(selected,text="",values=(name_box.get(),watt_box.get(),rating_box.get(),brand_box.get(),model_box.get(),moduar_box.get(),type_box.get(),connecters_box.get(),max_psu_l_box.get()))
            row = treeview.item(selected)["values"]
            print(row[0])
            with open(jsof,'r+') as file:
                    # First we load existing data into a dict.
                file_data = json.load(file)
                file_data['psu'][rowr]['name'] = row[0]
                file_data['psu'][rowr]['watt'] = row[1]
                file_data['psu'][rowr]['rating'] = row[2]
                file_data['psu'][rowr]['brand'] = row[3]
                file_data['psu'][rowr]['model'] = row[4]
                file_data['psu'][rowr]['moduar'] = row[5]
                file_data['psu'][rowr]['type'] = row[6]
                file_data['psu'][rowr]['connecters'] = row[7]
                file_data['psu'][rowr]['max_psu_l'] = row[8]

                file.seek(0)
                print("game")
                # convert back to json.
                print(json.dumps(file_data))
                # json.dump(file_data, file)
                with open(jsof, 'w') as outfile:
                    json.dump(file_data, outfile)
        if edin == "motherboard":
            treeview.item(selected,text="",values=(name_box.get(),model_box.get(),cpu_socket_box.get(),chipset_box.get(),sata_box.get(),ddr_box.get(),usbc_box.get(),usb_box.get(),ports_box.get(),form_factor_box.get(),brand_box.get(),max_ram_box.get(),series_box.get(),motherboard_ports_box.get(),sodimm_box.get(),pcie16_box.get(),ram_slots_box.get(),nvme_box.get(),pcie_gen_box.get(),ethernet_box.get(),nvme_pcie_box.get(),wifi_box.get(),bluetooth_box.get(),sata_speed_box.get(),vrm_box.get(),cpu_series_box.get(),graphics_box.get(),iaudio_box.get(),pcie_box.get(),ioshield_box.get()))
            row = treeview.item(selected)["values"]
            print(row[0])
            with open(jsof,'r+') as file:
                    # First we load existing data into a dict.
                file_data = json.load(file)
                file_data['motherboard'][rowr]['name'] = row[0]
                file_data['motherboard'][rowr]['model'] = row[1]
                file_data['motherboard'][rowr]['cpu_socket'] = row[2]
                file_data['motherboard'][rowr]['chipset'] = row[3]
                file_data['motherboard'][rowr]['sata'] = row[4]
                file_data['motherboard'][rowr]['ddr'] = row[5]
                file_data['motherboard'][rowr]['usbc'] = row[6]
                file_data['motherboard'][rowr]['usb'] = row[7]
                file_data['motherboard'][rowr]['ports'] = row[8]
                file_data['motherboard'][rowr]['form_factor'] = row[9]
                file_data['motherboard'][rowr]['brand'] = row[10]
                file_data['motherboard'][rowr]['max_ram'] = row[11]
                file_data['motherboard'][rowr]['series'] = row[12]
                file_data['motherboard'][rowr]['motherboard_ports'] = row[13]
                file_data['motherboard'][rowr]['sodimm'] = row[14]
                file_data['motherboard'][rowr]['pcie16'] = row[15]
                file_data['motherboard'][rowr]['ram_slots'] = row[16]
                file_data['motherboard'][rowr]['nvme'] = row[17]
                file_data['motherboard'][rowr]['pcie_gen'] = row[18]
                file_data['motherboard'][rowr]['ethernet'] = row[19]
                file_data['motherboard'][rowr]['nvme_pcie'] = row[20]
                file_data['motherboard'][rowr]['wifi'] = row[21]
                file_data['motherboard'][rowr]['bluetooth'] = row[22]
                file_data['motherboard'][rowr]['sata_speed'] = row[23]
                file_data['motherboard'][rowr]['vrm'] = row[24]
                file_data['motherboard'][rowr]['cpu_series'] = row[25]
                file_data['motherboard'][rowr]['graphics'] = row[26]
                file_data['motherboard'][rowr]['iaudio'] = row[27]
                file_data['motherboard'][rowr]['pcie'] = row[28]
                file_data['motherboard'][rowr]['ioshield'] = row[29]

                    # Sets file's current position at offset.
                file.seek(0)
                print("game")
                # convert back to json.
                print(json.dumps(file_data))
                # json.dump(file_data, file)
                with open(jsof, 'w') as outfile:
                    json.dump(file_data, outfile)
        if edin == "adapter":
            treeview.item(selected,text="",values=(port1_box.get(),ports2_box.get(),port_gender1_box.get(),port_gender2_box,caterogory_box.get(),length_box.get()))
            row = treeview.item(selected)["values"]
            print(row[0])
            with open(jsof,'r+') as file:
                    # First we load existing data into a dict.
                file_data = json.load(file)
                file_data['adapter'][rowr]['port1'] = row[0]
                file_data['adapter'][rowr]['ports2'] = row[1]
                file_data['adapter'][rowr]['port_gender1'] = row[2]
                file_data['adapter'][rowr]['port_gender2'] = row[3]
                file_data['adapter'][rowr]['caterogory'] = row[4]
                file_data['adapter'][rowr]['length'] = row[5]

                    # Sets file's current position at offset.
                file.seek(0)
                print("game")
                # convert back to json.
                print(json.dumps(file_data))
                # json.dump(file_data, file)
                with open(jsof, 'w') as outfile:
                    json.dump(file_data, outfile)
        if edin == "monitor":
            treeview.item(selected,text="",values=(brand_box.get(),model_box.get(),screen_size_box.get(),connecters_box.get(),video_box.get(),usb_box.get(),vesa_box.get(),resolution_box.get(),refresh_rate_box.get(),widescreen_box.get(),glare_screen_box.get(),panel_box.get(),led_backlight_box.get(),display_type_box.get(),constrast_ratio_box.get(),aspect_ratio_box.get(),response_time_box.get(),adaptive_sync_tech_box.get(),input_video_box.get()))
            row = treeview.item(selected)["values"]
            print(row[0])
            with open(jsof,'r+') as file:
                    # First we load existing data into a dict.
                file_data = json.load(file)
                file_data['monitor'][rowr]['brand'] = row[0]
                file_data['monitor'][rowr]['model'] = row[1]
                file_data['monitor'][rowr]['screen_size'] = row[2]
                file_data['monitor'][rowr]['connecters'] = row[3]
                file_data['monitor'][rowr]['video'] = row[4]
                file_data['monitor'][rowr]['usb'] = row[5]
                file_data['monitor'][rowr]['vesa'] = row[6]
                file_data['monitor'][rowr]['resolution'] = row[7]
                file_data['monitor'][rowr]['refresh_rate'] = row[8]
                file_data['monitor'][rowr]['widescreen'] = row[9]
                file_data['monitor'][rowr]['glare_screen'] = row[10]
                file_data['monitor'][rowr]['panel'] = row[0]
                file_data['monitor'][rowr]['led_backlight'] = row[11]
                file_data['monitor'][rowr]['display_type'] = row[12]
                file_data['monitor'][rowr]['constrast_ratio'] = row[13]
                file_data['monitor'][rowr]['aspect_ratio'] = row[14]
                file_data['monitor'][rowr]['response_time'] = row[15]
                file_data['monitor'][rowr]['adaptive_sync_tech'] = row[16]
                file_data['monitor'][rowr]['input_video'] = row[17]


                    # Sets file's current position at offset.
                file.seek(0)
                print("game")
                # convert back to json.
                print(json.dumps(file_data))
                # json.dump(file_data, file)
                with open(jsof, 'w') as outfile:
                    json.dump(file_data, outfile)
        if edin == "case":
            treeview.item(selected,text="",values=(name_box.get(),model_box.get(),mobo_supp_box.get(),case_type_box.get(),tdrive_bays_box.get(),sdrive_bays_box.get(),pcie_box.get(),ports_box.get(),gpul_box.get(),gpuh_box.get(),brand_box.get(),cpuh_box.get(),window_box.get(),series_box.get(),fan_box.get(),psul_box.get()))
            row = treeview.item(selected)["values"]
            print(row[0])
            with open(jsof,'r+') as file:
                    # First we load existing data into a dict.
                file_data = json.load(file)
                file_data['case'][rowr]['name'] = row[0]
                file_data['case'][rowr]['model'] = row[1]
                file_data['case'][rowr]['mobo_supp'] = row[2]
                file_data['case'][rowr]['case_type'] = row[3]
                file_data['case'][rowr]['3drive_bays'] = row[4]
                file_data['case'][rowr]['2drive_bays'] = row[5]
                file_data['case'][rowr]['pcie'] = row[6]
                file_data['case'][rowr]['ports'] = row[7]
                file_data['case'][rowr]['gpu-l'] = row[8]
                file_data['case'][rowr]['gpu-h'] = row[9]
                file_data['case'][rowr]['brand'] = row[10]
                file_data['case'][rowr]['cpu-h'] = row[11]
                file_data['case'][rowr]['window'] = row[12]
                file_data['case'][rowr]['series'] = row[13]
                file_data['case'][rowr]['fan'] = row[14]
                file_data['case'][rowr]['psu-l'] = row[15]

                    # Sets file's current position at offset.
                file.seek(0)
                print("game")
                # convert back to json.
                print(json.dumps(file_data))
                # json.dump(file_data, file)
                with open(jsof, 'w') as outfile:
                    json.dump(file_data, outfile)
        if edin == "cable":
            treeview.item(selected,text="",values=(cable_gender_box.get(),cp1_box.get(),cp2_box.get(),cp3_box.get(),caterogory_box.get(),length_box.get(),amount_box.get()))
            row = treeview.item(selected)["values"]
            print(row[0])
            with open(jsof,'r+') as file:
                    # First we load existing data into a dict.
                file_data = json.load(file)
                file_data['cable'][rowr]['cable_gender'] = row[0]
                file_data['cable'][rowr]['cp1'] = row[1]
                file_data['cable'][rowr]['cp2'] = row[2]
                file_data['cable'][rowr]['cp3'] = row[3]
                file_data['cable'][rowr]['caterogory'] = row[4]
                file_data['cable'][rowr]['length'] = row[5]
                file_data['cable'][rowr]['amount'] = row[6]

                    # Sets file's current position at offset.
                file.seek(0)
                print("game")
                # convert back to json.
                print(json.dumps(file_data))
                # json.dump(file_data, file)
                with open(jsof, 'w') as outfile:
                    json.dump(file_data, outfile)
        if edin == "cpu":
            treeview.item(selected,text="",values=(name_box.get(),core_box.get(),thread_box.get(),socket_box.get(),model_box.get(),base_freq_box.get(),turbo_freq_box.get(),igpu_box.get(),brand_box.get(),cache_box.get(),unlocked_box.get(),year_box.get()))
            row = treeview.item(selected)["values"]
            print(row[0])
            with open(jsof,'r+') as file:
                    # First we load existing data into a dict.
                file_data = json.load(file)
                file_data['cpu'][rowr]['name'] = row[0]
                file_data['cpu'][rowr]['core'] = row[1]
                file_data['cpu'][rowr]['thread'] = row[2]
                file_data['cpu'][rowr]['socket'] = row[3]
                file_data['cpu'][rowr]['model'] = row[4]
                file_data['cpu'][rowr]['base_freq'] = row[5]
                file_data['cpu'][rowr]['turbo_freq'] = row[6]
                file_data['cpu'][rowr]['igpu'] = row[7]
                file_data['cpu'][rowr]['brand'] = row[8]
                file_data['cpu'][rowr]['cache'] = row[9]
                file_data['cpu'][rowr]['unlocked'] = row[10]
                file_data['cpu'][rowr]['year'] = row[11]

                    # Sets file's current position at offset.
                file.seek(0)
                print("game")
                # convert back to json.
                print(json.dumps(file_data))
                # json.dump(file_data, file)
                with open(jsof, 'w') as outfile:
                    json.dump(file_data, outfile)
        if edin == "gpu":
            treeview.item(selected, text="", values=(name_box.get(),size_box.get(),core_clock_box.get(),brand_box.get(),model_box.get(),mem_type_box.get(),output_box.get(),base_brand_box.get(),cuda_box.get(),mem_clock_box.get(),card_bus_box.get(),hieght_box.get(),width_box.get(),length_box.get(),power_box.get(),watt_box.get()))
            row = treeview.item(selected)["values"]
            print(row[0])
            with open(jsof,'r+') as file:
                    # First we load existing data into a dict.
                file_data = json.load(file)
                file_data['gpu'][rowr]['name'] = row[0]
                file_data['gpu'][rowr]['size'] = row[1]
                file_data['gpu'][rowr]['core_clock'] = row[2]
                file_data['gpu'][rowr]['brand'] = row[3]
                file_data['gpu'][rowr]['model'] = row[4]
                file_data['gpu'][rowr]['mem_type'] = row[5]
                file_data['gpu'][rowr]['output'] = row[6]
                file_data['gpu'][rowr]['base_brand'] = row[7]
                file_data['gpu'][rowr]['cuda'] = row[8]
                file_data['gpu'][rowr]['mem_clock'] = row[9]
                file_data['gpu'][rowr]['card_bus'] = row[10]
                file_data['gpu'][rowr]['hieght'] = row[11]
                file_data['gpu'][rowr]['width'] = row[12]
                file_data['gpu'][rowr]['length'] = row[13]
                file_data['gpu'][rowr]['power'] = row[14]
                file_data['gpu'][rowr]['watt'] = row[15]

                    # Sets file's current position at offset.
                file.seek(0)
                print("game")
                # convert back to json.
                print(json.dumps(file_data))
                # json.dump(file_data, file)
                with open(jsof, 'w') as outfile:
                    json.dump(file_data, outfile)
        if edin == "game":
            treeview.item(selected, text="", values=(name_box.get(),platform_box.get(),studio_box.get(),online_box.get()))
            row = treeview.item(selected)["values"]
            print(row[0])
            with open(jsof,'r+') as file:
                    # First we load existing data into a dict.
                file_data = json.load(file)
                file_data['game'][rowr]['name'] = row[0]
                file_data['game'][rowr]['platform'] = row[1]
                file_data['game'][rowr]['studio'] = row[2]
                file_data['game'][rowr]['online'] = row[3]

                    # Sets file's current position at offset.
                file.seek(0)
                print("game")
                # convert back to json.
                print(json.dumps(file_data))
                # json.dump(file_data, file)
                with open(jsof, 'w') as outfile:
                    json.dump(file_data, outfile)
        if edin == "books":
            treeview.item(selected, text="", values=(name_box.get(),author_box.get(),date_box.get(),online_box.get()))
            row = treeview.item(selected)["values"]
            print(row[0])
            with open(jsof,'r+') as file:
                    # First we load existing data into a dict.
                file_data = json.load(file)
                file_data['book'][rowr]['name'] = row[0]
                file_data['book'][rowr]['author'] = row[1]
                file_data['book'][rowr]['date'] = row[2]
                file_data['book'][rowr]['online'] = row[3]

                    # Sets file's current position at offset.
                file.seek(0)
                print("game")
                # convert back to json.
                print(json.dumps(file_data))
                # json.dump(file_data, file)
                with open(jsof, 'w') as outfile:
                    json.dump(file_data, outfile)
        editWin.destroy()

    update_button = tk.Button(add_frame, text="Save Record", command=update_record)
    update_button.grid()

tbutton2=tk.Button(toolbar, text="edit",command=editWin)
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
                       d={}
                       d["name"]=cn
                       d["brand"]=cb
                       d["model"]=cm
                       d["max_cpu_height"]=cv
                       d["rpm"]=cr
                       d["fansize"]=cf
                       d["fan_mount"]=cp
                       d["color"]=co
                       def write_json(new_data, filename=jsof):
                        with open(filename,'r+') as file:
                            file_data = json.load(file)
                            file_data["cpu_cooler"].append(new_data)
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
                       d = {}
                       d["name"]=mna
                       d["model"]=mmd
                       d["cpu_socket"]=mcp
                       d["chipset"]=mch
                       d["sata"]=msa
                       d["ddr"]=md
                       d["usbc"]=muc
                       d["usb"]=muv
                       d["ports"]=mpo
                       d["form_factor"]=mf
                       d["brand"]=mbr
                       d["max_ram"]=mm
                       d["series"]=mse
                       d["motherboard_ports"]=mmo
                       d["sodimm"]=mso
                       d["pcie16"]=mps
                       d["ram_slots"]=mr
                       d["nvme"]=mav
                       d["pcie_gen"]=mpg
                       d["ethernet"]=me
                       d["nvme_pcie"]=mnv
                       d["wifi"]=mw
                       d["bluetooth"]=mbl
                       d["sata_speed"]=msp
                       d["vrm"]=mv
                       d["cpu_series"]=mcps
                       d["graphics"]=mgr
                       d["iaudio"]=mia
                       d["pcie"]=mpv
                       d["ioshield"]=mis
                       def write_json(new_data, filename=jsof):
                        with open(filename,'r+') as file:
                            file_data = json.load(file)
                            file_data["motherboard"].append(new_data)
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
                       d['turbo_freq']=pbt
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
 # def update_record():
 #     # Grab record number
 #     selected = listtree.focus()
 #    # Save new data

 #    for entry in headers:
 #        listtree.item(selected, text="", values=(entry_box.get()))
 #        entry_box = tk.Entry(right_pane)
 #        entry_box.delete(0,tk.END)
    # Clear entry boxes
# Select Record
edin = "le"
heal = "ad"
def select_record():
    # Clear entry boxes
    # Grab record number
    selected = treeview.focus()
    # Grab record values
    # values = listtree.item(selected, 'values')
    global heal
    heal=treeview.item(selected, 'values')
print(heal)
def clicker(e):
    select_record()
headers="l"
def go(event):
    # cs = listbox.curselection()
    # do=listbox.get(cs)
    global treeview
    global edin
    global headers
    def hidse():
        for widget in right_pane.winfo_children():
            widget.pack_forget()
    curItem = listtree.focus()
    cs=listtree.item(curItem)
    do=cs["text"]
    h=tk.Scrollbar(right_pane, orient='horizontal')
    h.pack(side=tk.BOTTOM, fill='x')
    if do == "gpu":
        hidse()
        f = open(jsof)
        data = json.load(f)
        edin="gpu"
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("name","size","core_clock","brand","model","mem_type","output","base_brand","cuda","mem_clock","card_bus","hieght","width","length","power","watt"))
        headers=["name","size","core_clock","brand","model","mem_type","output","base_brand","cuda","mem_clock","card_bus","hieght","width","length","power","watt"]
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
        h.pack(side=tk.BOTTOM, fill='x')
        h.config(command=treeview.xview)
        treeview.pack()
        f.close()
        for row in data["gpu"]:
            treeview.insert("","end",values=(row["name"],row["size"],row["core_clock"],row["brand"],row["model"],row["mem_type"],row["output"],row["base_brand"],row["cuda"],row["mem_clock"],row["card_bus"],row["hieght"],row["width"],row["length"],row["power"],row["watt"]))
    if do == "cpu":
        hidse()
        f = open(jsof)
        data = json.load(f)
        edin="cpu"
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("name","core","thread","socket","model","base_freq","turbo_freq","igpu","brand","cache","unlocked","year"))
        headers=["name","core","thread","socket","model","base_freq","turbo_freq","igpu","brand","cache","unlocked","year"]
        treeview.heading("#1",text="name")
        treeview.heading("#2",text="core")
        treeview.heading("#3",text="thread")
        treeview.heading("#4",text="socket")
        treeview.heading("#5",text="model")
        treeview.heading("#6",text="base_freq")
        treeview.heading("#7",text="turbo_freq")
        treeview.heading("#8",text="igpu")
        treeview.heading("#9",text="brand")
        treeview.heading("#10",text="cache")
        treeview.heading("#11",text="unlocked")
        treeview.heading("#12",text="year")
        h.pack(side=tk.BOTTOM, fill='x')
        h.config(command=treeview.xview)
        treeview.pack()
        f.close()
        for row in data["cpu"]:
            treeview.insert("","end",values=(row["name"],row["core"],row["thread"],row["socket"],row["model"],row["base_freq"],row["turbo_freq"],row["igpu"],row["brand"],row["cache"],row["unlocked"],row["year"]))
    if do == "case":
        hidse()
        f = open(jsof)
        data = json.load(f)
        edin="case"
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("name","model","mobo_supp","case_type","3drive_bays","2drive_bays","pcie","ports","gpu-l","gpu-h","brand","cpu-h","window","series","fan","psu-l"))
        headers=["name","model","mobo_supp","case_type","3drive_bays","2drive_bays","pcie","ports","gpu-l","gpu-h","brand","cpu-h","window","series","fan","psu-l"]
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
        h.pack(side=tk.BOTTOM, fill='x')
        h.config(command=treeview.xview)
        treeview.pack()
        f.close()
        for row in data["case"]:
            treeview.insert("","end",values=(row["name"],row["model"],row["mobo_supp"],row["case_type"],row["3drive_bays"],row["2drive_bays"],row["pcie"],row["ports"],row["gpu-l"],row["gpu-h"],row["brand"],row["cpu-h"],row["window"],row["series"],row["fan"],row["psu-l"]))
    if do == "psu":
        hidse()
        f = open(jsof)
        data = json.load(f)
        edin="psu"
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("name","watt","rating","brand","model","modular","type","connectors","max_psu_l"))
        headers=["name","watt","rating","brand","model","modular","type","connectors","max_psu_l"]
        treeview.heading("#1",text="name")
        treeview.heading("#2",text="watt")
        treeview.heading("#3",text="rating")
        treeview.heading("#4",text="brand")
        treeview.heading("#5",text="model")
        treeview.heading("#6",text="modular")
        treeview.heading("#7",text="type")
        treeview.heading("#8",text="connectors")
        treeview.heading("#9",text="max_psu_l")
        h.pack(side=tk.BOTTOM, fill='x')
        h.config(command=treeview.xview)
        treeview.pack()
        f.close()
        for row in data["psu"]:
            treeview.insert("","end",values=(row["name"],row["watt"],row["rating"],row["brand"],row["model"],row["modular"],row["type"],row["connectors"],row["max_psu_l"]))
    if do == "storage":
        hidse()
        f = open(jsof)
        data = json.load(f)
        edin="storage"
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("name","brand","size","type","form","interface","internal","model","rpm","read","write"))
        headers=["name","brand","size","type","form","interface","internal","model","rpm","read","write"]
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
        h.pack(side=tk.BOTTOM, fill='x')
        h.config(command=treeview.xview)
        treeview.pack()
        f.close()
        for row in data["storage"]:
            treeview.insert("","end",values=(row["name"],row["brand"],row["size"],row["type"],row["form"],row["interface"],row["internal"],row["model"],row["rpm"],row["read"],row["write"]))


    if do == "ram":
        hidse()
        f = open(jsof)
        data = json.load(f)
        edin="ram"
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("name","cap_total","cap_per","ddr","dimm","model","speed","brand","form"))
        headers=["name","cap_total","cap_per","ddr","dimm","model","speed","brand","form"]
        treeview.heading("#1",text="name")
        treeview.heading("#2",text="cap_total")
        treeview.heading("#3",text="cap_per")
        treeview.heading("#4",text="ddr")
        treeview.heading("#5",text="dimm")
        treeview.heading("#6",text="model")
        treeview.heading("#7",text="speed")
        treeview.heading("#8",text="brand")
        treeview.heading("#9",text="form")
        h.pack(side=tk.BOTTOM, fill='x')
        h.config(command=treeview.xview)
        treeview.pack()
        f.close()
        for row in data["ram"]:
            treeview.insert("","end",values=(row["name"],row["cap_total"],row["cap_per"],row["ddr"],row["dimm"],row["model"],row["speed"],row["brand"],row["form"]))
    if do == "cables":
        hidse()
        f = open(jsof)
        data = json.load(f)
        edin="cable"
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("cable_gender","cp1","cp2","cp3","caterogory","length","amount"))
        headers=["cable_gender","cp1","cp2","cp3","caterogory","length","amount"]
        treeview.heading("#1",text="cable_gender")
        treeview.heading("#2",text="cp1")
        treeview.heading("#3",text="cp2")
        treeview.heading("#4",text="cp3")
        treeview.heading("#5",text="caterogory")
        treeview.heading("#6",text="length")
        treeview.heading("#7",text="amount")
        h.pack(side=tk.BOTTOM, fill='x')
        h.config(command=treeview.xview)
        treeview.pack()
        f.close()
        for row in data["cable"]:
            treeview.insert("", "end", values=(row["cable_gender"], row["cp1"], row["cp2"], row["cp3"], row["caterogory"], row["length"], row["amount"]))
    if do == "motherboard":
        hidse()
        f = open(jsof)
        data = json.load(f)
        edin="motherboard"
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("name","model","cpu_socket","chipset","sata","ddr","usbc","usb","ports","form_factor","brand","max_ram","series","motherboard_ports","sodimm","pcie16","ram_slots","nvme","pcie_gen","ethernet","nvme_pcie","wifi","bluetooth","sata_speed","vrm","cpu_series","graphics","iaudio","pcie","ioshield"))
        headers=["name","model","cpu_socket","chipset","sata","ddr","usbc","usb","ports","form_factor","brand","max_ram","series","motherboard_ports","sodimm","pcie16","ram_slots","nvme","pcie_gen","ethernet","nvme_pcie","wifi","bluetooth","sata_speed","vrm","cpu_series","graphics","iaudio","pcie","ioshield"]
        treeview.heading("#1",text="name")
        treeview.heading("#2",text="model")
        treeview.heading("#3",text="cpu_socket")
        treeview.heading("#4",text="chipset")
        treeview.heading("#5",text="sata")
        treeview.heading("#6",text="ddr")
        treeview.heading("#7",text="usbc")
        treeview.heading("#8",text="usb")
        treeview.heading("#9",text="ports")
        treeview.heading("#10",text="form_factor")
        treeview.heading("#11",text="brand")
        treeview.heading("#12",text="max_ram")
        treeview.heading("#13",text="series")
        treeview.heading("#14",text="motherboard_ports")
        treeview.heading("#15",text="sodimm")
        treeview.heading("#16",text="pcie16")
        treeview.heading("#17",text="ram_slots")
        treeview.heading("#18",text="nvme")
        treeview.heading("#19",text="pcie_gen")
        treeview.heading("#20",text="ethernet")
        treeview.heading("#21",text="nvme_pcie")
        treeview.heading("#22",text="wifi")
        treeview.heading("#23",text="bluetooth")
        treeview.heading("#24",text="sata_speed")
        treeview.heading("#25",text="vrm")
        treeview.heading("#26",text="cpu_series")
        treeview.heading("#27",text="graphics")
        treeview.heading("#28",text="iaudio")
        treeview.heading("#29",text="pcie")
        treeview.heading("#30",text="ioshield")
        h.pack(side=tk.BOTTOM, fill='x')
        h.config(command=treeview.xview)
        treeview.pack()
        f.close()
        for row in data["motherboard"]:
            treeview.insert("","end",values=(row["name"],row["model"],row["cpu_socket"],row["chipset"],row["sata"],row["ddr"],row["usbc"],row["usb"],row["ports"],row["form_factor"],row["brand"],row["max_ram"],row["series"],row["motherboard_ports"],row["sodimm"],row["pcie16"],row["ram_slots"],row["nvme"],row["pcie_gen"],row["ethernet"],row["nvme_pcie"],row["wifi"],row["bluetooth"],row["sata_speed"],row["vrm"],row["cpu_series"],row["graphics"],row["iaudio"],row["pcie"],row["ioshield"]))

    if do == "laptop":
        hidse()
        f = open(jsof)
        data = json.load(f)
        edin="laptop"
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("brand","model","cpu_core","series","cpu_model","ram_slots","ram","nvme","ssd","cpu_freq","ram_type","gpu","igpu","gpu_vram","igpu_vram","hdd","max_ram","cthreads","cbrand","usb","video","audio","ethernet","battry_watt","thunderbolt","charger_port","resolution","screen_size","touchscreen","dp_type","panel","wifi_gen","dvd","bluetooth","numpad","webcam","mic","keyboard","sodimm","card_reader","led_keyb"))
        headers=["brand","model","cpu_core","series","cpu_model","ram_slots","ram","nvme","ssd","cpu_freq","ram_type","gpu","igpu","gpu_vram","igpu_vram","hdd","max_ram","cthreads","cbrand","usb","video","audio","ethernet","battry_watt","thunderbolt","charger_port","resolution","screen_size","touchscreen","dp_type","panel","wifi_gen","dvd","bluetooth","numpad","webcam","mic","keyboard","sodimm","card_reader","led_keyb"]
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
        h.pack(side=tk.BOTTOM, fill='x')
        h.config(command=treeview.xview)
        treeview.pack()
        f.close()
        for row in data["laptop"]:
            treeview.insert("","end",values=(row["brand"],row["model"],row["cpu_core"],row["series"],row["cpu_model"],row["ram_slots"],row["ram"],row["nvme"],row["ssd"],row["cpu_freq"],row["ram_type"],row["gpu"],row["igpu"],row["gpu_vram"],row["igpu_vram"],row["hdd"],row["max_ram"],row["cthreads"],row["cbrand"],row["usb"],row["video"],row["audio"],row["ethernet"],row["battry_watt"],row["thunderbolt"],row["charger_port"],row["resolution"],row["screen_size"],row["touchscreen"],row["dp_type"],row["panel"],row["wifi_gen"],row["dvd"],row["bluetooth"],row["numpad"],row["webcam"],row["mic"],row["keyboard"],row["sodimm"],row["card_reader"],row["led_keyb"]))
    if do == "monitors":
        hidse()
        f = open(jsof)
        data = json.load(f)
        edin="monitor"
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("brand","model","screen_size","connecters","video","usb","vesa","resolution","refresh_rate","widescreen","glare_screen","panel","led_backlight","display_type","constrast_ratio","aspect_ratio","response_time","adaptive_sync_tech","input_video"))
        headers=["brand","model","screen_size","connecters","video","usb","vesa","resolution","refresh_rate","widescreen","glare_screen","panel","led_backlight","display_type","constrast_ratio","aspect_ratio","response_time","adaptive_sync_tech","input_video"]
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
        h.pack(side=tk.BOTTOM, fill='x')
        h.config(command=treeview.xview)
        treeview.pack()
        f.close()
        for row in data["monitor"]:
            treeview.insert("","end",values=(row["brand"],row["model"],row["screen_size"],row["connecters"],row["video"],row["usb"],row["vesa"],row["resolution"],row["refresh_rate"],row["widescreen"],row["glare_screen"],row["panel"],row["led_backlight"],row["display_type"],row["constrast_ratio"],row["aspect_ratio"],row["response_time"],row["adaptive_sync_tech"],row["input_video"]))
    if do == "adapters":
        hidse()
        f = open(jsof)
        data = json.load(f)
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("port1","ports2","port_gender1","port_gender2","caterogory","length"))
        headers=["port1","ports2","port_gender1","port_gender2","caterogory","length"]
        edin="adapter"
        treeview.heading("#1",text="port1")
        treeview.heading("#2",text="ports2")
        treeview.heading("#3",text="port_gender1")
        treeview.heading("#4",text="port_gender2")
        treeview.heading("#5",text="caterogory")
        treeview.heading("#6",text="length")
        h.pack(side=tk.BOTTOM, fill='x')
        h.config(command=treeview.xview)
        treeview.pack()
        f.close()
        for row in data["adapter"]:
            treeview.insert("","end",values=(row["port1"],row["ports2"],row["port_gender1"],row["port_gender2"],row["caterogory"],row["length"]))
        f.close
    if do == "pc":
        hidse()
        f = open(jsof)
        data = json.load(f)
        edin="pc"
        treeview=ttk.Treeview(right_pane,xscrollcommand=h.set,columns=("cpu_model","cpu_core","igpu","ram","ram_slots","ddr","sata","max_ram","nvme","csocket","cthread","gpu_model","usb_ports","cpu_brand","cpu_chipset","gbrand","pcie_gen","cpu_clock","vram","ecc","display_ports","other_ports","hdmi_ports","serial","gmem_type","pcie16","amount"))
        headers=["cpu_model","cpu_core","igpu","ram","ram_slots","ddr","sata","max_ram","nvme","csocket","cthread","gpu_model","usb_ports","cpu_brand","cpu_chipset","gbrand","pcie_gen","cpu_clock","vram","ecc","display_ports","other_ports","hdmi_ports","serial","gmem_type","pcie16","amount"]
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
        treeview.heading("#20",text="ecc")
        treeview.heading("#21",text="display_ports")
        treeview.heading("#22",text="other_ports")
        treeview.heading("#23",text="hdmi_ports")
        treeview.heading("#24",text="serial")
        treeview.heading("#25",text="gmem_type")
        treeview.heading("#26",text="pcie16")
        treeview.heading("#27",text="amount")
        h.pack(side=tk.BOTTOM, fill='x')
        h.config(command=treeview.xview)
        treeview.pack()
        f.close()
        for row in data["pc"]:
            treeview.insert("","end",values=(row["cpu_model"],row["cpu_core"],row["igpu"],row["ram"],row["ram_slots"],row["ddr"],row["sata"],row["max_ram"],row["nvme"],row["csocket"],row["cthread"],row["gpu_model"],row["usb_ports"],row["cpu_brand"],row["cpu_chipset"],row["gbrand"],row["pcie_gen"],row["cpu_clock"],row["vram"],row["ecc"],row["display_ports"],row["other_ports"],row["hdmi_ports"],row["serial"],row["gmem_type"],row["pcie16"],row["amount"]))
        f.close()
    if do == "games":
        hidse()
        f = open(jsof)
        data = json.load(f)
        edin="game"
        treeview=ttk.Treeview(right_pane,columns=("name","platform","studio","online"))
        headers=["name","platform","studio","online"]
        treeview.heading("#1",text="name")
        treeview.heading("#2",text="platform")
        treeview.heading("#3",text="studio")
        treeview.heading("#4",text="online")
        h.pack(side=tk.BOTTOM, fill='x')
        h.config(command=treeview.xview)
        treeview.pack()
        f.close()
        for row in data["game"]:
            treeview.insert("", "end", values=(row["name"], row["platform"], row["studio"], row["online"]))
        f.close()
    if do == "books":
        hidse()
        f = open(jsof)
        data = json.load(f)
        treeview=ttk.Treeview(right_pane,columns=("name","author","date","online"))
        headers=["name","author","date","online"]
        edin="book"
        treeview.heading("#1",text="name")
        treeview.heading("#2",text="author")
        treeview.heading("#3",text="date")
        treeview.heading("#4",text="online")
        h.config(command=treeview.xview)
        h.pack(side=tk.BOTTOM, fill='x')
        treeview.pack(fill="both", expand=True)
        f.close()
        for row in data["book"]:
            treeview.insert("", "end", values=(row["name"], row["author"], row["date"], row["online"]))
        f.close()

    treeview.bind("<ButtonRelease-1>", clicker)
print(headers)
listtree.bind('<Double-1>', go)
listtree.pack()
# catwin=tk.
window.mainloop()
# todo
"""
networking
tools

"""
