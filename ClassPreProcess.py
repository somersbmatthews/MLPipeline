import pandas


class PreProcess:

    global xvalues
    global yvalues
 
    

    def ColumnSelectorForX(self):

        PreProcessed = pandas.read_csv('/Users/MAC/HRDiagram/hygdata_v3.csv')

        xcolumn = ['ci']

        xvalues = PreProcessed[xcolumn]
    
        return xvalues
        
   
    def ColumnSelectorForY(self):

        PreProcessed = pandas.read_csv('/Users/MAC/HRDiagram/hygdata_v3.csv')
        
        ycolumn = ['absmag']
        
        yvalues = PreProcessed[ycolumn]
        
        return yvalues


        
        






