from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.support.ui import Select



def entrando(username_info,password_info):
  global driver
  driver = webdriver.Chrome(r"./chromedriver") 
  
  
  url = 'https://stevegriggsdesign.com/portal/admin/leads'
  driver.get(url)
  driver.maximize_window()

  correo=driver.find_element_by_xpath('//input[@type="email"]')

  contrasena=driver.find_element_by_xpath('//input[@type="password"]')

  correo.send_keys(username_info)
  contrasena.send_keys(password_info)
  
  driver.find_element_by_xpath('//button[@type="submit"]').click()
  

def reporte(): 


  time.sleep(5)
  todos=Select(driver.find_element_by_xpath('//select[@name="table-leads_length"]'))
  todos.select_by_visible_text('All')
    
  time.sleep(3)
    
  name_leads=driver.find_elements_by_xpath('//a[contains(@href, "leads")]')
  
    
    
  leads=[]
  for n in name_leads:
      na=n.get_attribute('href')
      leads.append(na)
    
    
  s = set()
  any(x in s or s.add(x) for x in leads)
  s = set()
  
  
  duplicates = set(x for x in leads if x in s or s.add(x))
  
  
  
    
  todos_los_frames=[]
  todos_los_frames3=[]
    
  for d in duplicates:
      driver.get(d)
    
    
      time.sleep(4)
      
      des=''
      try:
          description_leads3=driver.find_element_by_xpath('//div[@class="lead-view"]')
            
          iso=description_leads3.text
            
          iso2=iso.split('\n')
          des=[]
          for i in iso2:      
              if '*' in i:
                  des.append(i)
                
      except:
          des='na'
            
       
            
      name_l=''
      try:
          name_leads=driver.find_element_by_xpath('//p[@class="bold font-medium-xs lead-name"]')
          name_l=(name_leads.text)
      except:
          name_l='no name'
            
      try:
          driver.find_element_by_xpath('//a[@aria-controls="lead_notes"]').click()
          time.sleep(3)
      except:
          pass  
        # casilla email leads
      email_l_row=('')
      try:
          email_leads=driver.find_element_by_xpath('//div[contains(text(), "Sent email")]')
            
    
            
          if email_leads:
              email_l_row=('complete')
          else:
              email_l_row=('')
      except:
          email_l_row=('')
            
      call_l_row=('')
      try:
          call_leads=driver.find_element_by_xpath('//div[contains(text(), "initial call")]')
            
          if call_leads:
              call_l_row=('complete')
          else:
              call_l_row=('')
                
      except:
          call_l_row=('')
            
                
      steve_l_row=('') 
      try:
          steve_leads=driver.find_element_by_xpath('//div[contains(text(), "Site visit")]')
            
          if steve_leads:
              steve_l_row=('complete')
          else:
              steve_l_row=('')
      except:
          steve_l_row=('')
            
      note_l=''
      try:
          description_leads4=driver.find_elements_by_xpath('//div[@data-note-description]')
           
            
          for ino in description_leads4:
              note_l=(ino.text)
        
      except:
          note_l=('Na')
        
        
        #proposal leads
        
      try:
          
          driver.find_element_by_xpath('//a[@aria-controls="tab_proposals_leads"]').click()
          time.sleep(4)
      except:
          pass
        
      proposal_l=''
      try:
          proposal_sent=driver.find_element_by_xpath('//span[contains(text(), "Sent")]')
          if proposal_sent:
              proposal_l='sent'
          else: 
              proposal_l='no sent'
                
      except:
          proposal_l='no sent'
         
            
         
      joined_des = "\n".join(des)
        
      df1 = pd.DataFrame({'leads name':[name_l]})
      df2 = pd.DataFrame({'Description':[joined_des]})
      df3 = pd.DataFrame({'email':[email_l_row]})
      df4 = pd.DataFrame({'call':[call_l_row]})
      df5 = pd.DataFrame({'visit':[steve_l_row]})
      df6 = pd.DataFrame({'proposal':[proposal_l]})
      df7 = pd.DataFrame({'notes':[note_l]})
    
    
    
            
            
      tru=pd.concat([df1,df2,df3,df4,df5,df6,df7], axis=1)
            
         
            
      todos_los_frames.append(tru)    
        
        
        
        
    
        
    #################################################################################################################
    #projectos    
        
        
        
    # on boarding
  driver.get('https://stevegriggsdesign.com/portal/admin/projects')
  time.sleep(2)
    
          
  todos=Select(driver.find_element_by_xpath('//select[@name="DataTables_Table_0_length"]'))
  todos.select_by_visible_text('All')
  time.sleep(3)
   
  name_projects=driver.find_elements_by_xpath('//a[contains(@href, "view")]')
    
  time.sleep(3)
  nasa=[]
  for nv in name_projects:
      nasaa=nv.get_attribute('href')
      nasa.append(nasaa)
        
    
    
  s = set()
  any(x in s or s.add(x) for x in nasa)
  s = set()
  
  
  
  duplicates2 = set(x for x in nasa if x in s or s.add(x))
    
    
  todos_los_frames2=[]
  for na in duplicates2:
      driver.get(na)
      time.sleep(3)
        
      descri_p=''
      try:
          description_pro=driver.find_element_by_xpath('//div[@class="tc-content project-overview-description"]')
            
          descri_p=description_pro.text.replace('DESCRIPTION','')
            
               
      except:
          descri_p=('Na')
        
      dfp0 = pd.DataFrame({'Description':[descri_p]})
    
    
        
      try:
          driver.find_element_by_xpath('//li[@class="project_tab_project_milestones"]').click()
          name_proj=driver.title
          time.sleep(3)
      except:
          pass
        
      dfp1 = pd.DataFrame({'project name':[name_proj]})
        
      try:
          driver.find_element_by_xpath('//input[@type="checkbox"]').click()
      except:
          pass
      time.sleep(3)
        
        
      task_c=[]
      try:
          onbo=driver.find_elements_by_xpath('//div/ul/li/div/div/div[2]/a[@class="task_milestone pull-left mbot5 mtop5 text-muted line-throught"]')
          for o in onbo:
              task_c.append(o.text)
      except:
          pass
          
        
          
      if '1. Send Design Proposal' in task_c:
          proposal_onb='complete'
      else:
          proposal_onb=''
      if '2. Send Thank you/Onboarding email to client' in task_c or '3. Get Information from Client'in task_c or '2. Send Onboarding email to client' in task_c:
          email_onb='complete'
      else:
          email_onb=''
                 
      if '3. Send Invoice' in task_c or '2. Send Invoice' in task_c:
          invoice_onb='complete'
      else:
                                  
          invoice_onb=''
        
        
      dfp2 = pd.DataFrame({'send proposal':[proposal_onb]})
      dfp3 = pd.DataFrame({'send email':[email_onb]})
      dfp4 = pd.DataFrame({'inovice':[invoice_onb]})
      
   
    
    
             
      try:
          driver.find_element_by_xpath('//input[@type="checkbox"]').click()
      except:
          pass
      time.sleep(3)
      
      send_desing_notes=''
      try:
          time.sleep(2)
          driver.find_element_by_xpath('//a[contains(text(), "1. Send Design Proposal")]').click()
          time.sleep(3)
          try:
              description_pro=driver.find_elements_by_xpath('//div[@data-task-attachment-id="0"]')
              send_desing_note=[]
              
                
              for i in description_pro:
                  send_desing_note.append(i.text)
              try:
                  send_desing_notes = "\n".join(send_desing_note)
              except:
                  send_desing_notes=i.text
                
          except:
              send_desing_notes=('Na')
            
          try:     
              aa=driver.find_elements_by_xpath('//button[@class="close"]')[5]
              aa.click()
         
          except:
              pass
      except:
          send_desing_notes=('')
            
      dfp5 = pd.DataFrame({'proposal notes':[send_desing_notes]})
         
        
      try:
          time.sleep(2)
          driver.find_element_by_xpath('//a[contains(text(), "2. Send Thank you/Onboarding email to client")]').click()
          time.sleep(3)
      except:
          pass
          try:
              time.sleep(2)
              driver.find_element_by_xpath('//a[contains(text(), "3. Get Information from Client")]').click()
              time.sleep(3)
          except:
              pass
              try:
                   time.sleep(2)
                   driver.find_element_by_xpath('//a[contains(text(), "2. Send Onboarding email to client")]').click()
                   time.sleep(3)
              except:
                  pass
      
      send_desing_notes2=''
      try:
          description_pro=driver.find_elements_by_xpath('//div[@data-task-attachment-id="0"]')
          send_desing_note2=[]
          
          for i in description_pro:
              send_desing_note2.append(i)
              try:
                  send_desing_notes2 = "\n".join(send_desing_note2)
              except:
                  send_desing_notes2=i.text
                    
                
          try:     
              aa=driver.find_elements_by_xpath('//button[@class="close"]')[5]
              aa.click()
         
          except:
              pass
                    
      except:
             send_desing_notes2=''
                
      dfp6 = pd.DataFrame({'email notes':[send_desing_notes2]})
           
      send_desing_note3=''  
      try:
          time.sleep(2)
          driver.find_element_by_xpath('//a[contains(text(), "3. Send Invoice")]').click()
          time.sleep(3)
          try:
              description_pro=driver.find_elements_by_xpath('//div[@data-task-attachment-id="0"]')
              send_desing_note3=[]
              for i in description_pro:
                  send_desing_note3.append(i)
              try:
                  send_desing_notes3 = "\n".join(send_desing_note3)
              except:
                  send_desing_notes3=i.text
          except:
              send_desing_notes3=('Na')
            
          try:
              aa=driver.find_elements_by_xpath('//button[@class="close"]')[5]
              aa.click()
         
          except:
              pass
      except:
          send_desing_notes3=''
           
    
      dfp7 = pd.DataFrame({'inovice notes':[send_desing_notes3]})    
        
        
            
      tru2=pd.concat([dfp1,dfp0,dfp2,dfp3,dfp4,dfp5,dfp6,dfp7], axis=1)
            
         
            
      todos_los_frames2.append(tru2)    
            
        
    ###########################################################################################################################################    
        
       # desing table
                
      if '1. Site Visit' in task_c:
          visit_ond='complete'
      else:
          visit_ond=''
      if '2. Get plot plan or survey' in task_c:
          survey_ond='complete'
      else:
          survey_ond=''
                    
      if '3. Design' in task_c:
          desing_ond='complete'
      else:
                                  
          desing_ond=''
      if "4. Client's Approval" in task_c:
          client_ond='complete'
      else:
                                  
          client_ond=''
            
      if '5. Request Permits' in task_c:
          permit_ond='complete'
      else:
                                  
          permit_ond=''
           
        
      dfd1 = pd.DataFrame({'site visit':[visit_ond]})
      dfd2 = pd.DataFrame({'survey':[survey_ond]})
      dfd3 = pd.DataFrame({'desing':[desing_ond]})
      dfd4 = pd.DataFrame({'Client Approval':[client_ond]})
      dfd5 = pd.DataFrame({'permits':[permit_ond]})
    
      send_desing_notes4=''
      try:
          time.sleep(2)
          driver.find_element_by_xpath('//a[contains(text(), "1. Site Visit")]').click()
          time.sleep(3)
          try:
              description_pro=driver.find_elements_by_xpath('//div[@data-task-attachment-id="0"]')
              send_desing_note4=[]
              for i in description_pro:
                  send_desing_note4.append(i)
              try:
                  send_desing_notes4 = "\n".join(send_desing_note3)
              except:
                  send_desing_notes4=i.text
          except:
              send_desing_notes4=('Na')
            
          try:
              aa=driver.find_elements_by_xpath('//button[@class="close"]')[5]
              aa.click()
         
          except:
              pass
      except:
          send_desing_notes4=''
           
    
      dfd6 = pd.DataFrame({'note visit':[send_desing_notes4]})    
        
      send_desing_notes5=''
      try:
          time.sleep(2)
          driver.find_element_by_xpath('//a[contains(text(), "2. Get plot plan or survey")]').click()
          time.sleep(3)
          try:
              description_pro=driver.find_elements_by_xpath('//div[@data-task-attachment-id="0"]')
              send_desing_note5=[]
              for i in description_pro:
                  send_desing_note5.append(i)
              try:
                  send_desing_notes5 = "\n".join(send_desing_note3)
              except:
                  send_desing_notes5=i.text
          except:
              send_desing_notes5=('Na')
            
          try:
              aa=driver.find_elements_by_xpath('//button[@class="close"]')[5]
              aa.click()
         
          except:
              pass
      except:
          send_desing_notes5=''
           
    
      dfd6 = pd.DataFrame({'Note survey':[send_desing_notes5]})    
        
      send_desing_notes6=''
      try:
          time.sleep(2)
          driver.find_element_by_xpath('//a[contains(text(), "3. Design")]').click()
          time.sleep(3)
          try:
              description_pro=driver.find_elements_by_xpath('//div[@data-task-attachment-id="0"]')
              send_desing_note6=[]
              for i in description_pro:
                  send_desing_note6.append(i)
              try:
                  send_desing_notes6 = "\n".join(send_desing_note3)
              except:
                  send_desing_notes6=i.text
          except:
              send_desing_notes6=('Na')
            
          try:
              aa=driver.find_elements_by_xpath('//button[@class="close"]')[5]
              aa.click()
         
          except:
              pass
      except:
          send_desing_notes6=''
           
    
      dfd6 = pd.DataFrame({'Note Desing':[send_desing_notes6]})    
        
      send_desing_notes7=''
      try:
          time.sleep(2)
          driver.find_element_by_xpath('//a[contains(text(), "Approval")]').click()
          time.sleep(3)
          try:
              description_pro=driver.find_elements_by_xpath('//div[@data-task-attachment-id="0"]')
              send_desing_note7=[]
              for i in description_pro:
                  send_desing_note7.append(i)
              try:
                  send_desing_notes7 = "\n".join(send_desing_note3)
              except:
                  send_desing_notes7=i.text
          except:
              send_desing_notes7=('Na')
            
          try:
              aa=driver.find_elements_by_xpath('//button[@class="close"]')[5]
              aa.click()
         
          except:
              pass
      except:
          send_desing_notes7=''
           
    
      dfd7 = pd.DataFrame({'Note Approval':[send_desing_notes7]})    
        
      send_desing_notes8=''
      try:
          time.sleep(2)
          driver.find_element_by_xpath('//a[contains(text(), "5. Request Permits")]').click()
          time.sleep(3)
          try:
              description_pro=driver.find_elements_by_xpath('//div[@data-task-attachment-id="0"]')
              send_desing_note8=[]
              for i in description_pro:
                  send_desing_note8.append(i)
              try:
                  send_desing_notes8 = "\n".join(send_desing_note3)
              except:
                  send_desing_notes8=i.text
          except:
              send_desing_notes8=('Na')
            
          try:
              aa=driver.find_elements_by_xpath('//button[@class="close"]')[5]
              aa.click()
        
          except:
              pass
      except:
          send_desing_notes8=''
           
    
      dfd8 = pd.DataFrame({'Note Permits':[send_desing_notes8]})    
       
      tru3=pd.concat([dfp1,dfp0,dfd1,dfd2,dfd3,dfd4,dfd5,dfd6,dfd7,dfd8], axis=1)
            
            
      todos_los_frames3.append(tru3)    
        
    
  driver.get('https://stevegriggsdesign.com/portal/admin/invoices')
    
  time.sleep(3)
    
    
  d=driver.find_elements_by_xpath('//tr/td[6]')
    
  namesp=[]
  for i in d:
      namesp.append(i.text)
    
    
  da=driver.find_elements_by_xpath('//tr/td[9]')
  
  
    
  pagos=[]
  for i in da:
      pagos.append(i.text)
  
  
 
  ds=driver.find_elements_by_xpath('//tr/td[8]')
    
  fechas=[]
  for i in ds:
      fechas.append(i.text)
    
    
    
     
  list_tuples = list(zip(namesp, pagos,fechas))  
      
    
  print(list_tuples)  
      
     
  dframe = pd.DataFrame(list_tuples, columns=['leads name', 'pagos','fechas'])  
    
    
    
    
  newdf = dframe.loc[(dframe.pagos == "PAID") ]
    
    
    
        
  leadsdata=pd.concat(todos_los_frames)
      
    
    
    
  projedata=pd.concat(todos_los_frames2)
    
  projedata2=pd.concat(todos_los_frames3)
    
    
    
    ################################leads########################################     
    
  sololeads=leadsdata.loc[(leadsdata.proposal == "no sent") ]
    
    #############################################################################
    
    
    ############################# on bording ####################################
    
  lead_con_proposal=leadsdata.loc[(leadsdata.proposal == "sent") ]
    
  
    
  data={'project name':lead_con_proposal['leads name'],
            'Description':'new project',
            'send proposal':'', 'send email':'', 'inovice':'',
           'proposal notes':'', 'email notes':'', 'inovice notes':''}
    
  pasando_leads_to_projec=pd.DataFrame(data)  
    
    #los sent + los que no tienen 3 checks
    
  cols = projedata.columns[projedata.columns.isin(['send email','send proposal', 'inovice'])]
  leads_to_onbording2=(projedata[(projedata[cols] == 'complete').all(1)])  
  
  
  newdf = dframe.loc[(dframe.pagos == "PAID") ]
  lista_pagos=list(newdf['leads name'].values)
  
  
  onbording_to_desing=leads_to_onbording2.loc[leads_to_onbording2['project name'].isin(lista_pagos)]
  
  
  project_sin_3_checks=projedata[~projedata.apply(tuple,1).isin(onbording_to_desing.apply(tuple,1))]
    
    
  onbording_table=pd.concat([project_sin_3_checks,pasando_leads_to_projec])
 

  
    ####################################### desing #######################################
    
    
  cols2 = projedata2.columns[projedata2.columns.isin(['site visit','survey', 'desing', 'Client Approval','permits'])]
  onbording_to_desing2=(projedata2[(projedata2[cols2] == 'complete').all(1)])  
  desing_sin_checks=projedata2[~projedata2.apply(tuple,1).isin(onbording_to_desing2.apply(tuple,1))]
    
    
    ######################################## execute ####################################
    
  
  import datetime

  now=datetime.datetime.now()  
  
  naa=now.strftime("%Y-%m-%d %H:%M")
  
  datv=str(naa).replace(' ','-').split('.')[0]
  
 
  
  dfo=datv.replace(':','')
 
  
  
    
    
  writer = pd.ExcelWriter('reportprojects-{}.xlsx'.format(dfo), engine='xlsxwriter')
  
    
    
  sololeads.to_excel(writer, sheet_name='leads',index=False)
  onbording_table.to_excel(writer, sheet_name='onbording',index=False)
  desing_sin_checks.to_excel(writer, sheet_name='desing',index=False)
    
    
  workbook  = writer.book
  worksheet = writer.sheets['leads']
    # Add a header format.
  header_format = workbook.add_format({
      'bold': True,
      'fg_color': '#ffcccc',
      'border': 1})
  for col_num, value in enumerate(sololeads.columns.values):
      worksheet.write(0, col_num, value, header_format)
    
      column_len = sololeads[value].astype(str).str.len().max()
      # Setting the length if the column header is larger
      # than the max column value length
      column_len = max(column_len, len(value)) + 3
      print(column_len)
        # set the column length
      worksheet.set_column(col_num, col_num, column_len)
        
    
  workbook  = writer.book
  worksheet = writer.sheets['onbording']
  # Add a header format.
  header_format = workbook.add_format({
      'bold': True,
      'fg_color': '#ffcccc',
      'border': 1})
  for col_num, value in enumerate(onbording_table.columns.values):
      worksheet.write(0, col_num, value, header_format)
   
      column_len = onbording_table[value].astype(str).str.len().max()
      # Setting the length if the column header is larger
      # than the max column value length
      column_len = max(column_len, len(value)) + 3
      print(column_len)
      # set the column length
      worksheet.set_column(col_num, col_num, column_len)
    
  workbook  = writer.book
  worksheet = writer.sheets['desing']
    # Add a header format.
  header_format = workbook.add_format({
      'bold': True,
      'fg_color': '#ffcccc',
      'border': 1})
  for col_num, value in enumerate(desing_sin_checks.columns.values):
      worksheet.write(0, col_num, value, header_format)
   
      column_len = desing_sin_checks[value].astype(str).str.len().max()
      # Setting the length if the column header is larger
      # than the max column value length
      column_len = max(column_len, len(value)) + 3
      print(column_len)
       # set the column length
      worksheet.set_column(col_num, col_num, column_len)
    
    
    
    
    
  writer.save()
    
  
  
  
  
  
  
    
  driver.close()