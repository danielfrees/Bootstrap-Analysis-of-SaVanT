def make_dataframe(text_file):
    with open(text_file, "r") as f:
        all_lines = f.read()
    all_lines_as_blocks = all_lines.split('\n')
    row_names = all_lines_as_blocks[0].split(',')
    all_lines_new = []
    for dat in all_lines_as_blocks[1:]:
        all_lines_new.append(dat.split(','))

    all_lines_new.pop()

    d = {}
    for line in all_lines_new:
        d['%s'%line[0]]=line[1:]

    import pandas as pd
    df = pd.DataFrame(data=d, index=row_names[1:])
    return df


import sys, getopt

def main():
    inputfile = ''
    outputfile = ''

    if (len(sys.argv) < 2):
        print('usage: heatmap_conversion.py -i <inputfile>')
        exit(0)

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:o",["ifile=","ofile="])
    except getopt.GetoptError as err:
        print(err)  # will print something like "option -a not recognized"
        print('usage: heatmap_conversion.py -i <inputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if(opt == '-h'):
            print('usage: heatmap_conversion.py -i <inputfile>')
            print('Takes in TEXT file for data and returns a pickled dataframe')
            print('Use pickle.load to load dataframe')
            sys.exit()
        elif(opt in ("-i", "--ifile")):
            inputfile=arg

    print ('Input file is %s' % inputfile)
    #print ('Output file is {}'.format(outputfile))
    df = make_dataframe(inputfile)
    import pickle
    df.to_pickle("./{}.pkl".format(inputfile))

if __name__ == "__main__":
    main()


# In[74]:




# In[75]:


#make_dataframe("SaVanT_MatrixSignatureVisualization_HeatmapData_202102121610242081.txt")


# In[ ]:


#with open("SaVanT_MatrixSignatureVisualization_HeatmapData_202102121610242081.txt", "r") as f:
  #  all_lines = f.read()


# In[2]:


#all_lines_as_blocks = all_lines.split('\n')


# In[5]:


#row_names = all_lines_as_blocks[0].split(',')


# In[82]:


#print(column_names)


# In[7]:


#all_lines = []
#for dat in all_lines_as_blocks[1:]:
   # all_lines.append(dat.split(','))


# In[9]:


#column_names = []
#for line in all_lines:
 #   column_names.append(line[0])


# In[38]:


#d = {}
#for line in all_lines[:21]:
#    d['%s'%line[0]]=line[1:]


# In[80]:


#print(len(column_names)-1)


# In[81]:


#print(len(d['Reversal reaction (leprosy)']))


# In[43]:


#import pandas as pd
#df = pd.DataFrame(data=d, index=row_names[1:])


# In[79]:


#df


# In[ ]:
