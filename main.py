import os
import sqlalchemy
import pandas
import numpy
import urllib
from sqlalchemy import create_engine



    
class Container:
    pass


class ContainerYardMap:
    def __init__(self,L=1,W=1,space_count=4,subspace_count=9,
                 container_count=9,space_stack_max=5,free_space=0.01,
                 ship_stations=5,clear_DB=False):
        
            
        self.L = L
        self.W = W
        self.space_count = space_count
        self.space_stack_max= space_stack_max
        self.subspace_count = subspace_count
        
        params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                    "SERVER=LAPTOP-4P9LLMN9;"
                                    "DATABASE=major;"
                                    "Trusted_Connection=yes;"
                                    )

        self.engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
        
        if clear_DB:
            with self.engine.connect() as e:
                e.execute("""
                          truncate table [major].[dbo].tb_ships
                          truncate table [major].[dbo].tb_container
                          truncate table [major].[dbo].tb_container_spaces
                          truncate table [major].[dbo].tb_subspace
                          truncate table [major].[dbo].tb_subspace_stack
                          
                          """)
    def remap(self):
        pass
    
    def NewShip(self,ship_id,container_drop_count,container_export_count,
                container_id=[],container_destination=[],container_start_date=[],
                container_destination_date=[]
                ):
        
        self.remap()     
        
        if container_drop_count == 0:
            print("no containers to be dropped")
        else:
            for cont in range(container_drop_count):
                pass
        if container_export_count==0:
            print("no containers to be exported")
        else:
            for cont in range(container_export_count):
                pass
        
            
    
    def get_optimal_location(self):
        pass
    
    
    def main(self):
        with self.engine.connect() as conn:
            data= conn.execute("select * from [major].[dbo].tb_ships").fetchall()
    
  
    

if __name__ == '__main__':


  T=ContainerYardMap()
  T.NewShip(ship_id=1231,container_drop_count=2,
            container_ids=[123,1211])
        

