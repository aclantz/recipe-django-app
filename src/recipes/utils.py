from io import BytesIO 
import base64
import matplotlib.pyplot as plt

COLORS = {
    'background': '#faf9f6',      
    'text': '#3a3b3c',            
    'default': '#a3aa81',    
    'highlight': '#595f40'    
}

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


def get_chart(chart_type, data, highlight_recipe=None, **kwargs):
   plt.switch_backend('AGG')
   fig=plt.figure(figsize = (6,3))                                    #manage details of graphing

   ax = plt.gca()                                                     # Set background color for the plot area using the COLORS dictionary
   ax.set_facecolor(COLORS['background'])

   if chart_type == '#1':
      #Bar Chart
      colors = [COLORS['default'] if name != highlight_recipe['name'] else COLORS['highlight'] for name in data['name']]
      plt.bar(data['name'], data['cooking_time'], color=colors)
      plt.xlabel('Recipe Name', color=COLORS['text'])                 # X-axis label
      plt.ylabel('Cooking Time (minutes)', color=COLORS['text'])      # Y-axis label
      plt.title('Cooking Time by Recipe', color=COLORS['text'])

   elif chart_type == '#2':
      #Pie Chart
      colors = [COLORS['default'] if name != highlight_recipe['name'] else COLORS['highlight'] for name in data['name']]
      plt.pie(data['cooking_time'], labels=data['name'], colors=colors)
      plt.title('Distribution of Cooking Times', color=COLORS['text'])

   elif chart_type == '#3':
      #Line Chart
      plt.plot(data['name'], data['cooking_time'], color=COLORS['default'], marker='o')
      plt.plot(highlight_recipe['name'], highlight_recipe['cooking_time'], color=COLORS['highlight'], marker='o', markersize=10)
      plt.xlabel('Recipe Name', color=COLORS['text'])                 # X-axis label
      plt.ylabel('Cooking Time (minutes)', color=COLORS['text'])      # Y-axis label
      plt.title('Cooking Time by Recipe', color=COLORS['text'])

   else:
       print ('unknown chart type')
  
   ax.tick_params(axis='x', colors=COLORS['text'])                    # Set color for tick labels
   ax.tick_params(axis='y', colors=COLORS['text'])
   plt.tight_layout()                                                 #specify layout details
   chart = get_graph()                                                #render the graph to file
   return chart       