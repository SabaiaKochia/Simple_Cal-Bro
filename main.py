#   Saba Kochadze
#   Feb 29, 2024
#   Nutrients Tracker
import tkinter
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#Basic Macro Tracks
#   Protein = 4 Cal / gram
#   Lipds i.e. fat's = 9 Cal / gram
#   CarboHydrate's = 4 Cal / gram
#   According to google: Maintenance Calories = 15 * Body Weight ( 15 calories per pound of weight )

def calculate_cal():

    protein = int(protein_in.get())
    fat = int(fat_in.get())
    carbs = int(carb_in.get())
    weight = int(weight_in.get())

    total = (protein * 4) + (fat * 9) + (carbs * 4)
    maint = weight * 15
    difference_cal = total - weight

    Label(window, text = 'TOTAL CALORIE INTAKE: ' + str(total) + '\nMAINTENANCE CALORIES: ' + str(maint) + '\nDIFFERENCE: '+ str(difference_cal)).grid(row = 6, column = 0)

    sec_window  = Tk()

    sec_window.title("PIE-GRAPH")
    sec_window.geometry()

    #   Create Pie Graph of the data from above

    frame_chart = tkinter.Frame(sec_window)
    frame_chart.pack()

    nutrition_list = ['PROTEIN', 'FAT', 'CARBS']
    nutrition_value = [float(protein), float(fat), float(carbs)]

    fig = Figure()
    ax = fig.add_subplot(111)

    ax.pie(nutrition_value, radius=1, labels= nutrition_list, autopct='%0.2f%%', shadow= True)

    Label(sec_window, text = '--- ROTEIN: '+ str(protein * 4) + ' CAL ---''\n--- FAT\'S: '+str(fat * 9) +' CAL ---''\n--- CARB\'S: ' + str(carbs * 4) + ' CAL --- ''\n--- TOTAL CALORIES: '  + str(total) + ' CAL ---').pack()

    chart1 = FigureCanvasTkAgg(fig, frame_chart)
    chart1.get_tk_widget().pack()

    sec_window.mainloop()




window = Tk()

window.title("Cal-Bro")
window.geometry()

Label(window, text="--- ! MAKE SOME GAINS ! ---").grid(row=0, column = 1)

Label(window, text = 'PROTEIN (gr)').grid(row=1)
Label(window, text = 'FAT (gr)').grid(row=2)
Label(window, text = 'CARBS (gr)').grid(row=3)
Label(window, text = 'WEIGHT (lb)').grid(row=4)

protein_in = Entry(window)
protein_in.grid(row=1, column = 1)

fat_in = Entry(window)
fat_in.grid(row=2, column = 1)

carb_in = Entry(window)
carb_in.grid(row=3, column = 1)

weight_in = Entry(window)
weight_in.grid(row=4, column = 1)

Button(window, text = 'CALCULATE', command= calculate_cal).grid(row=5, column = 0)


Button(window, text = 'EXIT', command= window.quit).grid(row=6,column=2)

for row in range(7):
    window.grid_rowconfigure(row, weight=1)
for col in range(7):
    window.grid_columnconfigure(col, weight=1)
#   Displays the window
window.mainloop()


