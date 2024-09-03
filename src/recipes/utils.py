from io import BytesIO 
import base64
import matplotlib.pyplot as plt

def get_graph():
   # tricky and copied from CF directions
   buffer = BytesIO()                   #create a BytesIO buffer for the image         
   plt.savefig(buffer, format='png')    #create a plot with a bytesIO object as a file-like object. Set format to png
   buffer.seek(0)                       #set cursor to the beginning of the stream
   image_png=buffer.getvalue()          #retrieve the content of the file
   graph=base64.b64encode(image_png)    #encode the bytes-like object
   graph=graph.decode('utf-8')          #decode to get the string as output
   buffer.close()                       #free up the memory of buffer
   return graph                         #return the image/graph


def get_chart(chart_type, data, **kwargs):
   #switch plot backend to AGG (Anti-Grain Geometry) - to write to file
   #AGG is preferred solution to write PNG files
   plt.switch_backend('AGG')
   #specify figure size
   fig=plt.figure(figsize=(6,3))

   #select chart_type based on user input from the form
   if chart_type == '#1':
       #plot bar chart between date on x-axis and quantity on y-axis
       plt.bar(data['cooking_time'], data['difficulty'])

   elif chart_type == '#2':
       #generate pie chart based on the cooking_time
       #The recipe titles are sent from the view as labels
       labels=kwargs.get('labels')
       plt.pie(data['cooking_time'], labels=labels)

   elif chart_type == '#3':
       #plot line chart based on date on x-axis and price on y-axis
       plt.plot(data['date_created'], data['cooking_time'])
   else:
       print ('unknown chart type')

   #specify layout details
   plt.tight_layout()
   #render the graph to file
   chart =get_graph() 
   return chart       