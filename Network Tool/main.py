import tkinter as tk
import customtkinter as ctk
import socket

import banner_grabber  # banner_grabber(target, port)
import nmapscan  # scan(target)
import geoip  # get_loc(url, path, file)
import wifiscanner  # wifi(ip_add_range_entered)
import packet_sniff  # packet(count)

def display_output(output_text):
    output_window = ctk.CTkToplevel(app)
    output_window.title("Output")
    output_window.geometry("400x300")
    output_window.resizable(False, False)

    output_label = ctk.CTkLabel(output_window, text=output_text, font=("Arial", 12))
    output_label.pack(pady=20)

def scanmap():
    try:
        get = ctk.CTkInputDialog(text="Enter a domain or IP: ", title="Nmap Scan")
        target = get.get_input()
        output = nmapscan.scan(target)
        display_output(output)
    except Exception as e:
        display_output("Error: Please enter a valid domain or IP.")

def get_ban():
    try:
        get0 = ctk.CTkInputDialog(text="Enter a URL or IP: ", title="Banner Grabber")
        url = socket.gethostbyname(get0.get_input())
        get1 = ctk.CTkInputDialog(text="Enter a port: ", title="Banner Grabber")
        port = get1.get_input()
        output = banner_grabber.banner_grabber(url, int(port))
        display_output(output)
    except Exception as e:
        display_output("Error: Please enter a valid URL or IP and port.")

def get_loc():
    try:
        get = ctk.CTkInputDialog(text="Enter a URL: ", title="GeoIP")
        url = get.get_input()
        output = geoip.get_loc(url)
        display_output(output)
    except Exception as e:
        display_output("Error: Please enter a valid URL.")

def wifiscan():
    try:
        get = ctk.CTkInputDialog(text="Enter an IP range: ", title="Wifi Scanner")
        ip_range = get.get_input()
        output = wifiscanner.wifi(ip_range)
        display_output(output)
    except Exception as e:
        display_output("Error: Please enter a valid IP range.")

def sniff():
    try:
        get = ctk.CTkInputDialog(text="Enter the number of packets to sniff: ", title="Packet Sniffer")
        packet_count = int(get.get_input())
        output = packet_sniff.packet(packet_count)
        display_output(output)
    except Exception as e:
        display_output("Error: Please enter a valid number of packets.")

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("Night_Purple.json")

app = ctk.CTk()
app.geometry("720x720")
app.resizable(False, False)
app.title("Network Tool")

title = ctk.CTkLabel(app, text="Network Tool_Lab Work 12 ", font=("Century Gothic", 20))
title.place(x=350, y=100, anchor="center")

nmaps = ctk.CTkButton(app, text="Nmap Scan", command=scanmap)
nmaps.place(x=350, y=150, anchor="center")

ban = ctk.CTkButton(app, text="Banner Grabber", command=get_ban)
ban.place(x=350, y=200, anchor="center")

loc = ctk.CTkButton(app, text="GeoIP", command=get_loc)
loc.place(x=350, y=250, anchor="center")

wifi = ctk.CTkButton(app, text="Wifi Scanner", command=wifiscan)
wifi.place(x=350, y=300, anchor="center")

pack = ctk.CTkButton(app, text="Packet Sniffer", command=sniff)
pack.place(x=350, y=350, anchor="center")

quit = ctk.CTkButton(app, text="Quit", command=app.quit)
quit.place(x=350, y=400, anchor="center")

app.mainloop()
